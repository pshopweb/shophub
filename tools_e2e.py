# -*- coding: utf-8 -*-
"""End-to-end interaction tests against the running dev server. Dev-only helper."""
import asyncio, sys
from playwright.async_api import async_playwright
BASE = "http://localhost:8899/"
results = []
def check(name, cond, extra=""):
    results.append((name, bool(cond), extra))
    print(("  PASS  " if cond else "  FAIL  ") + name + (f"  [{extra}]" if extra and not cond else ""))

async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        ctx = await b.new_context(viewport={"width":1366,"height":900})
        pg = await ctx.new_page()
        errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)

        # --- product page: add to cart ---
        await pg.goto(BASE+"pages/product-details.html?id=P0001", wait_until="networkidle")
        await pg.wait_for_timeout(800)
        title = await pg.text_content("#pd-title")
        check("product title renders", title and len(title)>4, title)
        await pg.click("#btn-add")
        await pg.wait_for_timeout(600)
        badge = await pg.text_content("[data-cart-count]")
        check("cart badge = 1 after add", badge=="1", f"got {badge!r}")
        toast_seen = await pg.locator(".toast").count()
        check("toast appears on add", toast_seen>0)

        # qty stepper
        await pg.click("[data-step='1']")
        val = await pg.input_value("#qty-input")
        check("qty stepper increments", val=="2", val)

        # pincode
        await pg.fill("#pincode","800001")
        await pg.click("#check-pin")
        await pg.wait_for_timeout(300)
        pin = await pg.text_content("#pin-result")
        check("pincode check responds", "Delivery to" in pin or "not deliver" in pin, pin)

        # wishlist toggle
        await pg.click("[data-wish]")
        await pg.wait_for_timeout(400)
        w = await pg.text_content("[data-wish-count]")
        check("wishlist badge = 1", w=="1", f"got {w!r}")

        # --- add a 2nd product from shop ---
        await pg.goto(BASE+"pages/shop.html", wait_until="networkidle")
        await pg.wait_for_timeout(900)
        cards = await pg.locator(".product-card").count()
        check("shop renders 12 cards", cards==12, f"got {cards}")
        btns = pg.locator("[data-add-cart]:not([disabled])")
        await btns.nth(0).click()
        await pg.wait_for_timeout(700)
        badge = await pg.text_content("[data-cart-count]")
        check("cart badge = 2 after 2nd add", badge=="2", f"got {badge!r}")

        # filter interaction
        await pg.locator("#f-brand input").nth(0).check()
        await pg.wait_for_timeout(900)
        cnt = await pg.text_content("#result-count")
        chips = await pg.locator("#active-chips .chip").count()
        check("brand filter applies + chip shows", chips>=1, f"chips={chips} count={cnt}")

        # sort
        await pg.select_option("#sort-sel","price-asc")
        await pg.wait_for_timeout(900)
        prices = await pg.locator(".pc-price .price").all_text_contents()
        nums=[int(p.replace("₹","").replace(",","")) for p in prices if p.strip()]
        check("sort price-asc is ordered", nums==sorted(nums), str(nums[:5]))

        # --- cart page ---
        await pg.goto(BASE+"pages/cart.html", wait_until="networkidle")
        await pg.wait_for_timeout(800)
        items = await pg.locator(".cart-item").count()
        check("cart shows 2 line items", items==2, f"got {items}")
        total_before = await pg.text_content(".sum-row.total span:last-child")

        # coupon apply
        await pg.fill("#coupon-code","PSHOP10")
        await pg.click("#coupon-form button")
        await pg.wait_for_timeout(800)
        applied = await pg.locator(".coupon-applied").count()
        total_after = await pg.text_content(".sum-row.total span:last-child")
        check("coupon PSHOP10 applies", applied==1)
        check("total changes after coupon", total_before!=total_after, f"{total_before} -> {total_after}")

        # qty change updates total
        await pg.locator("[data-qty][data-step='1']").nth(0).click()
        await pg.wait_for_timeout(700)
        t3 = await pg.text_content(".sum-row.total span:last-child")
        check("total updates on qty change", t3!=total_after, f"{total_after} -> {t3}")

        # remove item
        await pg.locator("[data-remove]").nth(0).click()
        await pg.wait_for_timeout(900)
        items2 = await pg.locator(".cart-item").count()
        check("remove deletes a line", items2==1, f"got {items2}")

        # --- wishlist page ---
        await pg.goto(BASE+"pages/wishlist.html", wait_until="networkidle")
        await pg.wait_for_timeout(900)
        wc = await pg.locator("#wish-grid .product-card").count()
        check("wishlist shows saved item", wc==1, f"got {wc}")

        # --- theme toggle persists ---
        await pg.click("[data-theme-toggle]")
        await pg.wait_for_timeout(400)
        th = await pg.get_attribute("html","data-theme")
        check("dark mode toggles", th=="dark", th)
        await pg.reload(wait_until="networkidle")
        await pg.wait_for_timeout(600)
        th2 = await pg.get_attribute("html","data-theme")
        check("dark mode persists on reload", th2=="dark", th2)
        await pg.click("[data-theme-toggle]")

        # --- search ---
        await pg.goto(BASE+"index.html", wait_until="networkidle")
        await pg.wait_for_timeout(700)
        await pg.fill("#q","laptop")
        await pg.wait_for_timeout(900)
        sug = await pg.locator("#suggest .suggest-item").count()
        check("search suggestions appear", sug>0, f"got {sug}")
        await pg.press("#q","Enter")
        await pg.wait_for_load_state("networkidle")
        await pg.wait_for_timeout(900)
        sr = await pg.locator(".product-card").count()
        check("search results render", sr>0, f"got {sr}")

        errs = [e for e in errs if "favicon" not in e.lower()]
        check("no JS errors during flow", len(errs)==0, "; ".join(errs[:3]))
        await b.close()

    print("\n" + "="*54)
    p=sum(1 for _,ok,_ in results if ok); t=len(results)
    print(f"  {p}/{t} passed")
    if p<t:
        print("  Failures:")
        for n,ok,x in results:
            if not ok: print(f"   - {n} {x}")
    return 0 if p==t else 1

sys.exit(asyncio.run(main()))
