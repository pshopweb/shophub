# -*- coding: utf-8 -*-
"""Screenshot + console-error harness for visual QA. Dev-only helper."""
import sys, asyncio, json
from playwright.async_api import async_playwright

BASE = "http://localhost:8899/"

async def shot(pages, width=1366, height=900, full=True, outdir="/tmp/shots", theme="light", mobile=False):
    results = []
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        for name, path in pages:
            ctx = await b.new_context(
                viewport={"width": width, "height": height},
                device_scale_factor=1,
                is_mobile=mobile, has_touch=mobile,
                color_scheme=theme)
            pg = await ctx.new_page()
            errs = []
            pg.on("console", lambda m: errs.append(f"{m.type}: {m.text}") if m.type in ("error","warning") else None)
            pg.on("pageerror", lambda e: errs.append(f"pageerror: {e}"))
            try:
                await pg.goto(BASE + path, wait_until="networkidle", timeout=30000)
                await pg.wait_for_timeout(1400)
            except Exception as e:
                errs.append(f"nav: {e}")
            out = f"{outdir}/{name}.png"
            try:
                await pg.screenshot(path=out, full_page=full)
            except Exception as e:
                errs.append(f"shot: {e}")
            results.append({"page": name, "path": path, "errors": errs[:12]})
            await ctx.close()
        await b.close()
    return results

if __name__ == "__main__":
    import os
    args = json.loads(sys.argv[1])
    os.makedirs(args.get("outdir","/tmp/shots"), exist_ok=True)
    r = asyncio.run(shot(args["pages"], args.get("width",1366), args.get("height",900),
                         args.get("full",True), args.get("outdir","/tmp/shots"),
                         args.get("theme","light"), args.get("mobile",False)))
    for x in r:
        print(f"\n=== {x['page']} ({x['path']}) ===")
        if x["errors"]:
            for e in x["errors"]: print("  !", e[:220])
        else:
            print("   no console errors")
