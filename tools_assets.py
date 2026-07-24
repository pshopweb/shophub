# -*- coding: utf-8 -*-
"""Generates all SVG art: product shots, category icons, banners, logo, avatars, payment marks."""
import json, os, random, math, hashlib
ROOT="/home/user/PShop"; A=os.path.join(ROOT,"assets","img")
for d in ["products","categories","brands","icons","banners","misc"]: os.makedirs(os.path.join(A,d),exist_ok=True)
P=json.load(open(os.path.join(ROOT,"assets/data/products.json")))
C=json.load(open(os.path.join(ROOT,"assets/data/categories.json")))

def X(t):
    """Escape text for safe XML embedding."""
    return str(t).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

def h(s,mod): return int(hashlib.md5(s.encode()).hexdigest(),16)%mod
PAL=[("#dbeafe","#1d4ed8"),("#fce7f3","#be185d"),("#fef3c7","#b45309"),("#ede9fe","#6d28d9"),
     ("#d1fae5","#047857"),("#fee2e2","#b91c1c"),("#cffafe","#0e7490"),("#e2e8f0","#334155"),
     ("#ffe4e6","#9f1239"),("#ecfccb","#4d7c0f")]

def shape(kind,c1,c2,i):
    """Vector silhouettes per sub-category family."""
    s=[]
    if kind=="phone":
        s.append(f'<rect x="160" y="70" width="180" height="360" rx="28" fill="{c2}"/>')
        s.append(f'<rect x="172" y="86" width="156" height="328" rx="20" fill="#fff" opacity=".92"/>')
        s.append(f'<circle cx="250" cy="404" r="9" fill="{c2}" opacity=".5"/>')
        s.append(f'<rect x="196" y="104" width="108" height="14" rx="7" fill="{c2}" opacity=".25"/>')
        s.append(f'<rect x="196" y="140" width="108" height="150" rx="10" fill="{c2}" opacity=".18"/>')
    elif kind=="laptop":
        s.append(f'<rect x="110" y="120" width="280" height="180" rx="14" fill="{c2}"/>')
        s.append(f'<rect x="124" y="134" width="252" height="152" rx="8" fill="#fff" opacity=".92"/>')
        s.append(f'<path d="M80 300h340l30 60H50z" fill="{c2}" opacity=".8"/>')
        s.append(f'<rect x="210" y="330" width="80" height="10" rx="5" fill="#fff" opacity=".7"/>')
    elif kind=="audio":
        s.append(f'<path d="M130 280v-30a120 120 0 0 1 240 0v30" stroke="{c2}" stroke-width="26" fill="none" stroke-linecap="round"/>')
        s.append(f'<rect x="96" y="266" width="70" height="120" rx="30" fill="{c2}"/>')
        s.append(f'<rect x="334" y="266" width="70" height="120" rx="30" fill="{c2}"/>')
        s.append(f'<rect x="110" y="288" width="42" height="76" rx="20" fill="#fff" opacity=".55"/>')
    elif kind=="watch":
        s.append(f'<rect x="205" y="60" width="90" height="110" rx="24" fill="{c2}" opacity=".85"/>')
        s.append(f'<rect x="205" y="330" width="90" height="110" rx="24" fill="{c2}" opacity=".85"/>')
        s.append(f'<rect x="160" y="150" width="180" height="200" rx="42" fill="{c2}"/>')
        s.append(f'<rect x="176" y="166" width="148" height="168" rx="32" fill="#fff" opacity=".93"/>')
        s.append(f'<circle cx="250" cy="250" r="46" fill="none" stroke="{c2}" stroke-width="9" opacity=".5"/>')
        s.append(f'<path d="M250 218v34l22 14" stroke="{c2}" stroke-width="9" fill="none" stroke-linecap="round"/>')
    elif kind=="camera":
        s.append(f'<rect x="90" y="150" width="320" height="210" rx="26" fill="{c2}"/>')
        s.append(f'<path d="M190 150l24-38h72l24 38z" fill="{c2}"/>')
        s.append(f'<circle cx="250" cy="255" r="72" fill="#fff" opacity=".9"/>')
        s.append(f'<circle cx="250" cy="255" r="44" fill="{c2}" opacity=".55"/>')
        s.append(f'<circle cx="350" cy="190" r="12" fill="#fff" opacity=".7"/>')
    elif kind=="shirt":
        s.append(f'<path d="M180 90l70 34 70-34 90 52-38 74-32-16v190H160V200l-32 16-38-74z" fill="{c2}"/>')
        s.append(f'<path d="M215 96c12 30 58 30 70 0" stroke="#fff" stroke-width="10" fill="none" opacity=".8"/>')
        s.append(f'<rect x="234" y="180" width="32" height="150" fill="#fff" opacity=".28"/>')
    elif kind=="shoe":
        s.append(f'<path d="M70 300c60-10 96-30 130-62 20-20 44-18 54 4 14 32 52 54 106 62 40 6 66 14 66 36 0 18-14 30-40 30H96c-18 0-34-12-34-32 0-20 4-34 8-38z" fill="{c2}"/>')
        s.append(f'<path d="M92 348h336" stroke="#fff" stroke-width="12" opacity=".55"/>')
        s.append(f'<path d="M212 258l40 30M244 226l42 32" stroke="#fff" stroke-width="10" opacity=".7" stroke-linecap="round"/>')
    elif kind=="bag":
        s.append(f'<path d="M120 180h260l26 240H94z" fill="{c2}"/>')
        s.append(f'<path d="M190 190v-34a60 60 0 0 1 120 0v34" stroke="{c2}" stroke-width="20" fill="none"/>')
        s.append(f'<rect x="220" y="250" width="60" height="46" rx="10" fill="#fff" opacity=".6"/>')
    elif kind=="pot":
        s.append(f'<path d="M110 210h280v110a90 90 0 0 1-90 90h-100a90 90 0 0 1-90-90z" fill="{c2}"/>')
        s.append(f'<rect x="86" y="186" width="328" height="30" rx="15" fill="{c2}" opacity=".75"/>')
        s.append(f'<rect x="380" y="228" width="90" height="22" rx="11" fill="{c2}" opacity=".85"/>')
        s.append(f'<path d="M160 260h180" stroke="#fff" stroke-width="12" opacity=".45"/>')
    elif kind=="appliance":
        s.append(f'<rect x="130" y="110" width="240" height="300" rx="34" fill="{c2}"/>')
        s.append(f'<rect x="156" y="146" width="188" height="150" rx="18" fill="#fff" opacity=".9"/>')
        s.append(f'<circle cx="250" cy="352" r="30" fill="#fff" opacity=".65"/>')
        s.append(f'<circle cx="250" cy="352" r="12" fill="{c2}" opacity=".6"/>')
    elif kind=="chair":
        s.append(f'<rect x="150" y="90" width="200" height="180" rx="30" fill="{c2}"/>')
        s.append(f'<rect x="120" y="270" width="260" height="60" rx="22" fill="{c2}" opacity=".85"/>')
        s.append(f'<rect x="146" y="330" width="24" height="90" rx="12" fill="{c2}"/>')
        s.append(f'<rect x="330" y="330" width="24" height="90" rx="12" fill="{c2}"/>')
    elif kind=="bottle":
        s.append(f'<rect x="214" y="70" width="72" height="60" rx="12" fill="{c2}" opacity=".8"/>')
        s.append(f'<path d="M186 150c0-24 28-20 28-40h72c0 20 28 16 28 40v230a40 40 0 0 1-40 40h-48a40 40 0 0 1-40-40z" fill="{c2}"/>')
        s.append(f'<rect x="204" y="230" width="92" height="90" rx="12" fill="#fff" opacity=".75"/>')
    elif kind=="tube":
        s.append(f'<path d="M200 120h100l24 250a56 56 0 0 1-56 62h-36a56 56 0 0 1-56-62z" fill="{c2}"/>')
        s.append(f'<rect x="212" y="70" width="76" height="52" rx="14" fill="{c2}" opacity=".8"/>')
        s.append(f'<rect x="196" y="250" width="108" height="70" rx="14" fill="#fff" opacity=".7"/>')
    elif kind=="dumbbell":
        s.append(f'<rect x="180" y="228" width="140" height="44" rx="14" fill="{c2}"/>')
        s.append(f'<rect x="104" y="180" width="66" height="140" rx="22" fill="{c2}"/>')
        s.append(f'<rect x="330" y="180" width="66" height="140" rx="22" fill="{c2}"/>')
        s.append(f'<rect x="66" y="206" width="40" height="88" rx="16" fill="{c2}" opacity=".8"/>')
        s.append(f'<rect x="394" y="206" width="40" height="88" rx="16" fill="{c2}" opacity=".8"/>')
    elif kind=="ball":
        s.append(f'<circle cx="250" cy="250" r="150" fill="{c2}"/>')
        s.append(f'<path d="M250 100c50 50 50 250 0 300M100 250h300" stroke="#fff" stroke-width="12" fill="none" opacity=".6"/>')
        s.append(f'<circle cx="250" cy="250" r="150" fill="none" stroke="#fff" stroke-width="8" opacity=".35"/>')
    elif kind=="box":
        s.append(f'<path d="M250 90l160 76v168l-160 76-160-76V166z" fill="{c2}"/>')
        s.append(f'<path d="M90 166l160 76 160-76M250 242v168" stroke="#fff" stroke-width="10" fill="none" opacity=".6"/>')
    elif kind=="teddy":
        s.append(f'<circle cx="170" cy="150" r="46" fill="{c2}"/><circle cx="330" cy="150" r="46" fill="{c2}"/>')
        s.append(f'<circle cx="250" cy="200" r="86" fill="{c2}"/>')
        s.append(f'<ellipse cx="250" cy="340" rx="104" ry="90" fill="{c2}"/>')
        s.append(f'<circle cx="222" cy="188" r="10" fill="#fff"/><circle cx="278" cy="188" r="10" fill="#fff"/>')
        s.append(f'<ellipse cx="250" cy="222" rx="26" ry="18" fill="#fff" opacity=".8"/>')
    elif kind=="book":
        s.append(f'<path d="M120 110h120c22 0 32 12 32 30v260c0-14-12-24-32-24H120z" fill="{c2}"/>')
        s.append(f'<path d="M380 110H260c-22 0-32 12-32 30v260c0-14 12-24 32-24h120z" fill="{c2}" opacity=".75"/>')
        s.append(f'<path d="M250 140v240" stroke="#fff" stroke-width="8" opacity=".7"/>')
        s.append(f'<path d="M150 180h80M150 220h80M280 180h80M280 220h80" stroke="#fff" stroke-width="9" opacity=".55" stroke-linecap="round"/>')
    else:
        s.append(f'<rect x="130" y="130" width="240" height="240" rx="40" fill="{c2}"/>')
        s.append(f'<circle cx="250" cy="250" r="70" fill="#fff" opacity=".8"/>')
    return "".join(s)

KIND={"Smartphones":"phone","Laptops":"laptop","Headphones":"audio","Smart Watches":"watch","Cameras":"camera",
"Accessories":"box","Men's Wear":"shirt","Women's Wear":"shirt","Footwear":"shoe","Watches":"watch","Bags":"bag",
"Jewellery":"box","Cookware":"pot","Appliances":"appliance","Furniture":"chair","Decor":"box","Storage":"box",
"Bedding":"box","Skincare":"tube","Haircare":"bottle","Makeup":"tube","Fragrance":"bottle","Grooming":"appliance",
"Wellness":"bottle","Fitness":"dumbbell","Cricket":"ball","Cycling":"ball","Outdoor":"box","Yoga":"box",
"Staples":"box","Snacks":"box","Beverages":"bottle","Dairy":"box","Personal Care":"bottle","Household":"bottle",
"Action Figures":"teddy","Board Games":"box","Soft Toys":"teddy","Baby Care":"bottle","Learning":"box",
"Outdoor Play":"ball","Fiction":"book","Non-Fiction":"book","Academics":"book","Comics":"book",
"Stationery":"book","Exam Prep":"book"}

def product_svg(p, idx):
    c1,c2 = PAL[h(p["id"]+str(idx),len(PAL))]
    k = KIND.get(p["subCategory"],"box")
    rot = [0,-8,7][idx-1]; sc=[1,0.92,1.06][idx-1]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500" role="img" aria-label="{X(p['name'])}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="#ffffff"/></linearGradient>
<filter id="s" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="{c2}" flood-opacity=".22"/></filter></defs>
<rect width="500" height="500" fill="url(#g)"/>
<circle cx="410" cy="92" r="70" fill="{c2}" opacity=".08"/><circle cx="80" cy="430" r="90" fill="{c2}" opacity=".07"/>
<g filter="url(#s)" transform="rotate({rot} 250 250) scale({sc}) translate({250-250*sc:.1f} {250-250*sc:.1f})">{shape(k,c1,c2,idx)}</g>
<text x="250" y="472" font-family="Inter,Segoe UI,sans-serif" font-size="19" font-weight="700" fill="{c2}" text-anchor="middle" opacity=".85">{X(p["brand"])}</text>
</svg>'''

for p in P:
    for i in (1,2,3):
        open(os.path.join(A,"products",f"{p['id'][1:].lstrip('0').rjust(3,'0')}"),"a").close() if False else None
        fn=p["images"][i-1].split("/")[-1]
        open(os.path.join(A,"products",fn),"w").write(product_svg(p,i))

CI={"electronics":"phone","fashion":"shirt","home-kitchen":"pot","beauty":"tube","sports":"dumbbell",
    "grocery":"box","toys-baby":"teddy","books":"book"}
for c in C:
    col=c["color"]
    open(os.path.join(A,"categories",f"{c['slug']}.svg"),"w").write(
f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="160" height="160" role="img" aria-label="{X(c['name'])}">
<defs><linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{col}" stop-opacity=".18"/><stop offset="1" stop-color="{col}" stop-opacity=".04"/></linearGradient></defs>
<rect width="500" height="500" rx="120" fill="url(#cg)"/>{shape(CI[c['slug']],"#fff",col,1)}</svg>''')
    open(os.path.join(A,"categories",f"{c['slug']}-banner.svg"),"w").write(
f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 400" width="1600" height="400" role="img" aria-label="{X(c['name'])} banner">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{col}"/><stop offset="1" stop-color="{col}" stop-opacity=".55"/></linearGradient></defs>
<rect width="1600" height="400" fill="url(#bg)"/><circle cx="1380" cy="80" r="180" fill="#fff" opacity=".1"/><circle cx="1180" cy="360" r="130" fill="#fff" opacity=".08"/>
<text x="70" y="190" font-family="Inter,Segoe UI,sans-serif" font-size="62" font-weight="800" fill="#fff">{X(c["name"])}</text>
<text x="72" y="248" font-family="Inter,Segoe UI,sans-serif" font-size="26" fill="#fff" opacity=".9">{X(c["description"])}</text></svg>''')

B=json.load(open(os.path.join(ROOT,"assets/data/banners.json")))
art=["phone","shirt","appliance","watch"]
for i,b in enumerate(B):
    t=b["theme"]
    open(os.path.join(A,"banners",f"banner-{i+1}.svg"),"w").write(
f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 620" width="1600" height="620" role="img" aria-label="{X(b['title'])}">
<defs><linearGradient id="hb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t}"/><stop offset="1" stop-color="#0f172a"/></linearGradient>
<filter id="bl"><feGaussianBlur stdDeviation="40"/></filter></defs>
<rect width="1600" height="620" fill="url(#hb)"/>
<circle cx="1250" cy="150" r="220" fill="#fff" opacity=".12" filter="url(#bl)"/>
<circle cx="230" cy="540" r="180" fill="#fff" opacity=".08" filter="url(#bl)"/>
<g transform="translate(1050 60) scale(0.95)" opacity=".95">{shape(art[i],"#fff","#ffffff",1)}</g>
<g opacity=".18"><path d="M0 500c260-90 520 60 800-20s540 40 800-30v170H0z" fill="#fff"/></g>
</svg>''')

# logo, favicon, avatar, payment marks, placeholder
open(os.path.join(A,"icons","logo.svg"),"w").write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 56" width="220" height="56" role="img" aria-label="PShop">
<defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2563eb"/><stop offset="1" stop-color="#7c3aed"/></linearGradient></defs>
<rect x="2" y="6" width="44" height="44" rx="14" fill="url(#lg)"/>
<path d="M16 38V18h9a6 6 0 0 1 0 12h-9" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<text x="58" y="38" font-family="Inter,Segoe UI,sans-serif" font-size="27" font-weight="800" fill="url(#lg)">PShop</text></svg>''')
open(os.path.join(A,"icons","favicon.svg"),"w").write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
<defs><linearGradient id="f" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2563eb"/><stop offset="1" stop-color="#7c3aed"/></linearGradient></defs>
<rect width="64" height="64" rx="18" fill="url(#f)"/>
<path d="M22 46V18h12a8 8 0 0 1 0 16h-12" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>''')
open(os.path.join(A,"misc","avatar.svg"),"w").write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
<rect width="200" height="200" rx="100" fill="#e0e7ff"/><circle cx="100" cy="78" r="36" fill="#6366f1"/>
<path d="M28 186c8-42 36-62 72-62s64 20 72 62z" fill="#6366f1"/></svg>''')
open(os.path.join(A,"misc","placeholder.svg"),"w").write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500">
<rect width="500" height="500" fill="#f1f5f9"/><rect x="140" y="160" width="220" height="170" rx="16" fill="#cbd5e1"/>
<circle cx="200" cy="212" r="22" fill="#94a3b8"/><path d="M150 320l70-72 52 50 40-34 38 56z" fill="#94a3b8"/></svg>''')
open(os.path.join(A,"misc","empty.svg"),"w").write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="400" height="300">
<rect width="400" height="300" fill="none"/><path d="M110 120h180l22 110H88z" fill="#e2e8f0"/><path d="M150 120V96a50 50 0 0 1 100 0v24" stroke="#cbd5e1" stroke-width="14" fill="none"/>
<circle cx="200" cy="176" r="26" fill="#cbd5e1"/><path d="M188 176h24" stroke="#fff" stroke-width="7" stroke-linecap="round"/></svg>''')
open(os.path.join(A,"misc","404.svg"),"w").write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 320" width="600" height="320">
<text x="300" y="200" font-family="Inter,Segoe UI,sans-serif" font-size="150" font-weight="900" fill="#2563eb" opacity=".2" text-anchor="middle">404</text>
<circle cx="300" cy="150" r="70" fill="none" stroke="#2563eb" stroke-width="12"/><path d="M350 200l50 50" stroke="#2563eb" stroke-width="16" stroke-linecap="round"/></svg>''')
pays={"upi":("#0f766e","UPI"),"razorpay":("#1e40af","Razorpay"),"cod":("#b45309","COD"),"visa":("#1a1f71","VISA"),"mastercard":("#eb001b","MC")}
for k,(col,label) in pays.items():
    open(os.path.join(A,"icons",f"pay-{k}.svg"),"w").write(
f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 48" width="120" height="48" role="img" aria-label="{label}">
<rect width="120" height="48" rx="10" fill="{col}" opacity=".12"/><rect x="1" y="1" width="118" height="46" rx="9" fill="none" stroke="{col}" stroke-opacity=".3"/>
<text x="60" y="31" font-family="Inter,Segoe UI,sans-serif" font-size="17" font-weight="800" fill="{col}" text-anchor="middle">{label}</text></svg>''')
print("assets written:", sum(len(os.listdir(os.path.join(A,d))) for d in ["products","categories","banners","icons","misc"]))
