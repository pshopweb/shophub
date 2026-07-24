# -*- coding: utf-8 -*-
"""Seed data generator for PShop demo catalog (run once; output committed to assets/data)."""
import json, random, os, hashlib
random.seed(7)
ROOT = "/home/user/PShop"
D = os.path.join(ROOT, "assets", "data")
os.makedirs(D, exist_ok=True)

categories = [
    ("c1","Electronics","electronics","Phones, laptops, audio & smart gear","#2563eb"),
    ("c2","Fashion","fashion","Clothing, footwear & accessories","#db2777"),
    ("c3","Home & Kitchen","home-kitchen","Appliances, cookware & decor","#f59e0b"),
    ("c4","Beauty","beauty","Skincare, grooming & fragrance","#8b5cf6"),
    ("c5","Sports","sports","Fitness, outdoor & sportswear","#10b981"),
    ("c6","Grocery","grocery","Daily essentials & packaged food","#ef4444"),
    ("c7","Toys & Baby","toys-baby","Toys, games & baby care","#06b6d4"),
    ("c8","Books","books","Fiction, academics & stationery","#64748b"),
]

subs = {
 "c1":["Smartphones","Laptops","Headphones","Smart Watches","Cameras","Accessories"],
 "c2":["Men's Wear","Women's Wear","Footwear","Watches","Bags","Jewellery"],
 "c3":["Cookware","Appliances","Furniture","Decor","Storage","Bedding"],
 "c4":["Skincare","Haircare","Makeup","Fragrance","Grooming","Wellness"],
 "c5":["Fitness","Cricket","Cycling","Footwear","Outdoor","Yoga"],
 "c6":["Staples","Snacks","Beverages","Dairy","Personal Care","Household"],
 "c7":["Action Figures","Board Games","Soft Toys","Baby Care","Learning","Outdoor Play"],
 "c8":["Fiction","Non-Fiction","Academics","Comics","Stationery","Exam Prep"],
}
brands = {
 "c1":["Nexon","Volta","AuraTech","Kiro","Zenix","Pulsewave"],
 "c2":["Urbanix","Métro","Denimo","Stridewell","Lumea","Craftline"],
 "c3":["HomeNest","Chefline","CasaVia","Ironhaus","Bloomly","Nordika"],
 "c4":["Glowen","Botanika","Purelis","Aromé","Sheen","Vitalya"],
 "c5":["Kinetiq","Strider","Peakform","Vantage","Rallye","Zenflow"],
 "c6":["Farmly","DailyGood","Harvestly","Nutrio","Pantrix","Freshkart"],
 "c7":["Playnest","Brickly","Cuddlo","Tinybean","Brainy","Zoomies"],
 "c8":["Inkwell","PagePress","Scholarix","Panelverse","Notely","RankUp"],
}
adj = ["Pro","Max","Ultra","Lite","Air","Edge","Prime","Neo","Core","Plus"]
nouns = {
 "Smartphones":["5G Smartphone","Camera Phone","Gaming Phone"],
 "Laptops":["Thin & Light Laptop","Creator Laptop","Gaming Laptop"],
 "Headphones":["ANC Headphones","Wireless Earbuds","Studio Headset"],
 "Smart Watches":["AMOLED Smartwatch","Fitness Band","GPS Watch"],
 "Cameras":["Mirrorless Camera","Action Camera","Vlogging Kit"],
 "Accessories":["Fast Charger","Power Bank","USB-C Hub"],
 "Men's Wear":["Cotton Shirt","Slim Fit Jeans","Hoodie"],
 "Women's Wear":["Rayon Kurta","Floral Dress","Knit Sweater"],
 "Footwear":["Running Shoes","Casual Sneakers","Leather Loafers"],
 "Watches":["Chronograph Watch","Minimal Watch","Diver Watch"],
 "Bags":["Laptop Backpack","Tote Bag","Duffel Bag"],
 "Jewellery":["Silver Pendant","Gold Plated Hoops","Charm Bracelet"],
 "Cookware":["Triply Kadai","Nonstick Tawa","Pressure Cooker"],
 "Appliances":["Air Fryer","Mixer Grinder","Robot Vacuum"],
 "Furniture":["Study Table","Bookshelf","Recliner Chair"],
 "Decor":["Wall Clock","Table Lamp","Photo Frame Set"],
 "Storage":["Airtight Jar Set","Wardrobe Organizer","Shoe Rack"],
 "Bedding":["Cotton Bedsheet","Memory Pillow","Comforter"],
 "Skincare":["Vitamin C Serum","Gel Moisturizer","Sunscreen SPF50"],
 "Haircare":["Onion Hair Oil","Repair Shampoo","Scalp Serum"],
 "Makeup":["Matte Lipstick","Liquid Foundation","Kajal Pencil"],
 "Fragrance":["Eau De Parfum","Body Mist","Attar Roll-On"],
 "Grooming":["Beard Trimmer","Shaving Kit","Hair Dryer"],
 "Wellness":["Multivitamin","Protein Powder","Omega-3"],
 "Fitness":["Adjustable Dumbbell","Resistance Bands","Skipping Rope"],
 "Cricket":["English Willow Bat","Batting Gloves","Leather Ball"],
 "Cycling":["MTB Cycle","Cycling Helmet","Bike Light"],
 "Outdoor":["Camping Tent","Trekking Pole","Sleeping Bag"],
 "Yoga":["Anti-Skid Yoga Mat","Foam Roller","Yoga Block"],
 "Staples":["Basmati Rice 5kg","Toor Dal 1kg","Atta 10kg"],
 "Snacks":["Trail Mix","Dark Chocolate","Baked Chips"],
 "Beverages":["Green Tea","Cold Brew Coffee","Fruit Juice"],
 "Dairy":["Paneer 400g","Ghee 1L","Cheese Slices"],
 "Personal Care":["Body Wash","Toothpaste Pack","Handwash Refill"],
 "Household":["Detergent 4kg","Floor Cleaner","Dish Gel"],
 "Action Figures":["Robot Figure","Hero Figure","Dino Set"],
 "Board Games":["Strategy Board Game","Family Card Game","Puzzle 1000pc"],
 "Soft Toys":["Teddy Bear","Plush Bunny","Unicorn Plush"],
 "Baby Care":["Baby Diapers","Baby Lotion","Feeding Bottle"],
 "Learning":["STEM Kit","Alphabet Blocks","Magnetic Tiles"],
 "Outdoor Play":["Kids Cycle","Football Size 5","Badminton Set"],
 "Fiction":["Mystery Novel","Fantasy Saga","Short Stories"],
 "Non-Fiction":["Business Memoir","Habit Guide","History Book"],
 "Academics":["Physics Textbook","Maths Guide","Chemistry Lab Manual"],
 "Comics":["Graphic Novel","Manga Vol.1","Comic Bundle"],
 "Stationery":["Gel Pen Pack","A5 Notebook","Highlighter Set"],
 "Exam Prep":["Aptitude Book","Mock Test Series","Previous Papers"],
}
features_pool = ["1 Year Warranty","Free Delivery","7 Day Replacement","Cash on Delivery","Premium Build",
  "Eco Friendly Packaging","Made in India","Bestseller Pick","Top Rated","Limited Stock"]
colors = ["Midnight Black","Cloud White","Ocean Blue","Rose Gold","Forest Green","Graphite","Sand Beige"]


# Realistic INR MRP bands (min, max) per sub-category.
PRICE_BANDS = {
 "Smartphones":(8999,89999),"Laptops":(32999,159999),"Headphones":(999,34999),
 "Smart Watches":(1499,44999),"Cameras":(12999,189999),"Accessories":(299,4999),
 "Men's Wear":(499,4999),"Women's Wear":(599,5999),"Footwear":(899,12999),
 "Watches":(1299,24999),"Bags":(699,7999),"Jewellery":(499,29999),
 "Cookware":(499,7999),"Appliances":(1499,44999),"Furniture":(2499,39999),
 "Decor":(299,5999),"Storage":(299,4999),"Bedding":(599,7999),
 "Skincare":(199,3999),"Haircare":(149,2499),"Makeup":(199,3499),
 "Fragrance":(499,8999),"Grooming":(699,7999),"Wellness":(299,4999),
 "Fitness":(399,14999),"Cricket":(299,17999),"Cycling":(499,49999),
 "Outdoor":(699,14999),"Yoga":(299,4999),
 "Staples":(99,1499),"Snacks":(49,999),"Beverages":(99,1999),
 "Dairy":(49,899),"Personal Care":(79,999),"Household":(99,1299),
 "Action Figures":(299,4999),"Board Games":(399,3999),"Soft Toys":(199,2999),
 "Baby Care":(149,2999),"Learning":(399,5999),"Outdoor Play":(499,9999),
 "Fiction":(149,999),"Non-Fiction":(199,1299),"Academics":(299,2499),
 "Comics":(149,1999),"Stationery":(49,999),"Exam Prep":(199,1499),
}

products = []
pid = 0
for cid, cname, cslug, _, ccolor in categories:
    for sub in subs[cid]:
        for k in range(2):   # 8 cats * 6 subs * 2 = 96 products
            pid += 1
            brand = random.choice(brands[cid])
            base = random.choice(nouns[sub])
            name = f"{brand} {base} {random.choice(adj)}"
            # Price bands are per sub-category so every item stays believable.
            lo, hi = PRICE_BANDS.get(sub, (499, 2999))
            mrp = int(round(random.uniform(lo, hi) / 10) * 10)
            disc = random.choice([5,10,15,20,25,30,35,40,45,50,55,60])
            price = max(lo // 2, int(round(mrp * (100 - disc) / 100 / 10) * 10))
            disc = round((1 - price / mrp) * 100)
            rating = round(random.uniform(3.3,4.9),1)
            reviews = random.randint(12, 4200)
            stock = random.choice([0,3,7,14,25,48,90,150,240])
            slug = "-".join(name.lower().replace("&","and").replace("'","").split())
            imgbase = f"assets/img/products/p{pid:03d}"
            products.append({
                "id": f"P{pid:04d}",
                "sku": f"PS-{cslug[:3].upper()}-{pid:04d}",
                "name": name,
                "slug": slug,
                "brand": brand,
                "categoryId": cid,
                "category": cname,
                "categorySlug": cslug,
                "subCategory": sub,
                "price": price,
                "mrp": mrp,
                "discount": disc,
                "currency": "INR",
                "rating": rating,
                "ratingCount": reviews,
                "reviewCount": max(3, reviews // 9),
                "stock": stock,
                "inStock": stock > 0,
                "images": [f"{imgbase}-1.svg", f"{imgbase}-2.svg", f"{imgbase}-3.svg"],
                "thumb": f"{imgbase}-1.svg",
                "colors": random.sample(colors, k=3),
                "highlights": random.sample(features_pool, k=4),
                "description": (f"The {name} from {brand} is engineered for everyday performance in the {sub.lower()} "
                    f"range. Built with premium materials, tested for durability and backed by PShop's easy returns, "
                    f"it delivers dependable quality at a fair price."),
                "specs": {
                    "Brand": brand, "Model": f"{base.split()[0]}-{pid:03d}", "Category": cname,
                    "Sub Category": sub, "Warranty": random.choice(["6 Months","1 Year","2 Years"]),
                    "Country of Origin": "India", "Package Contents": f"1 x {base}",
                },
                "tags": random.sample(["featured","trending","bestseller","flash","new","recommended"], k=random.randint(1,3)),
                "deliveryDays": random.randint(1,7),
                "returnDays": random.choice([7,10,15,30]),
                "codAvailable": random.random() > 0.15,
                "createdAt": f"2026-0{random.randint(1,7)}-{random.randint(10,28)}T10:00:00Z",
                "sold": random.randint(20, 9000),
            })

# guarantee tag coverage
for t, n in [("featured",12),("trending",12),("bestseller",12),("flash",10),("recommended",14),("new",10)]:
    have = [p for p in products if t in p["tags"]]
    need = n - len(have)
    i = 0
    while need > 0 and i < len(products):
        if t not in products[i]["tags"]:
            products[i]["tags"].append(t); need -= 1
        i += 1

flash = [p for p in products if "flash" in p["tags"]]
for p in flash:
    p["flashPrice"] = int(round(p["price"]*0.82/10)*10)

cats_out = []
for cid, cname, cslug, desc, color in categories:
    cats_out.append({"id":cid,"name":cname,"slug":cslug,"description":desc,"color":color,
        "icon":f"assets/img/categories/{cslug}.svg","banner":f"assets/img/categories/{cslug}-banner.svg",
        "subCategories":subs[cid],"brands":brands[cid],
        "productCount":len([p for p in products if p["categoryId"]==cid])})

coupons = [
 {"code":"PSHOP10","type":"percent","value":10,"minOrder":999,"maxDiscount":300,"expiry":"2026-12-31","active":True,"description":"10% off on orders above ₹999"},
 {"code":"FLAT200","type":"flat","value":200,"minOrder":1499,"maxDiscount":200,"expiry":"2026-12-31","active":True,"description":"Flat ₹200 off above ₹1499"},
 {"code":"NEWUSER","type":"percent","value":15,"minOrder":499,"maxDiscount":500,"expiry":"2026-12-31","active":True,"description":"15% off for first order"},
 {"code":"FREESHIP","type":"shipping","value":0,"minOrder":0,"maxDiscount":79,"expiry":"2026-12-31","active":True,"description":"Free delivery on any order"},
 {"code":"BIGSAVE50","type":"percent","value":50,"minOrder":4999,"maxDiscount":1500,"expiry":"2026-10-31","active":True,"description":"50% off above ₹4999 (max ₹1500)"},
]

banners = [
 {"id":"b1","title":"Monsoon Mega Sale","subtitle":"Up to 60% off on Electronics","cta":"Shop Electronics","link":"pages/category.html?cat=electronics","image":"assets/img/banners/banner-1.svg","theme":"#1d4ed8"},
 {"id":"b2","title":"Fashion Fiesta","subtitle":"Trending styles from ₹299","cta":"Explore Fashion","link":"pages/category.html?cat=fashion","image":"assets/img/banners/banner-2.svg","theme":"#be185d"},
 {"id":"b3","title":"Home Upgrade Days","subtitle":"Appliances & cookware deals","cta":"Shop Home","link":"pages/category.html?cat=home-kitchen","image":"assets/img/banners/banner-3.svg","theme":"#b45309"},
 {"id":"b4","title":"Flash Sale Live","subtitle":"Extra 18% off — limited hours","cta":"Grab Now","link":"pages/shop.html?tag=flash","image":"assets/img/banners/banner-4.svg","theme":"#047857"},
]

reviewers = ["Aarav S.","Priya K.","Rohit M.","Sneha R.","Imran A.","Neha G.","Vikram J.","Divya P.","Karan T.","Meera N.","Anil B.","Fatima Z."]
rtitles = ["Great value for money","Exactly as described","Solid build quality","Good but could improve","Absolutely loved it","Delivery was quick","Worth every rupee","Decent for the price"]
rbodies = ["Using it for two weeks now and it works flawlessly. Packaging was neat and delivery was on time.",
 "Quality feels premium and matches the photos. Would recommend to anyone looking in this budget.",
 "Does the job well. Minor issues with finish but overall a satisfying purchase from PShop.",
 "Better than what I expected at this price point. Customer support was responsive too.",
 "Product is genuine and sealed. Been comparing for a month and this was the best deal.",
 "Good performance so far. Will update the review after a few months of usage."]
reviews = []
rid = 0
for p in random.sample(products, 60):
    for _ in range(random.randint(2,5)):
        rid += 1
        st = random.choice([5,5,5,4,4,4,3,2])
        reviews.append({"id":f"R{rid:04d}","productId":p["id"],"user":random.choice(reviewers),
          "rating":st,"title":random.choice(rtitles),"comment":random.choice(rbodies),
          "date":f"2026-0{random.randint(1,7)}-{random.randint(10,28)}","verified":random.random()>0.2,
          "helpful":random.randint(0,180),"status":"approved"})

faqs = [
 ("Orders","How do I place an order on PShop?","Add products to your cart, open the cart page, apply a coupon if you have one, then continue to checkout. Choose a delivery address, pick a payment method and confirm. You will receive an order ID instantly."),
 ("Orders","Can I cancel my order after placing it?","Yes. Orders can be cancelled free of charge any time before they are marked Shipped. Open Orders → Order Details → Cancel Order and select a reason."),
 ("Orders","How do I track my shipment?","Every order has a live timeline. Go to Orders → Track Order to see Placed, Packed, Shipped, Out for Delivery and Delivered stages with timestamps."),
 ("Payments","Which payment methods are supported?","We support Cash on Delivery, UPI (any UPI app), Razorpay cards/netbanking/wallets, and PShop wallet refunds."),
 ("Payments","When will I get my refund?","Refunds for prepaid orders are initiated within 24 hours of return pickup and reach your source account in 3–5 business days. COD refunds go to your bank account in 5–7 business days."),
 ("Payments","Is it safe to pay online?","Yes. Payments are processed by PCI-DSS compliant gateways. PShop never stores your full card number or UPI PIN."),
 ("Delivery","What are the delivery charges?","Delivery is free on orders above ₹499. Below that a flat ₹79 shipping fee applies. Express delivery costs ₹129."),
 ("Delivery","Do you deliver to my pincode?","We deliver to 19,000+ pincodes across India. Enter your pincode on any product page to check serviceability and the expected delivery date."),
 ("Returns","What is the return policy?","Most products carry a 7–30 day return window depending on category. The exact window is shown on the product page and in your order details."),
 ("Returns","How does replacement work?","Choose Replace Order from Order Details within the return window. A pickup is scheduled and the replacement ships once the original item is picked up."),
 ("Account","How do I reset my password?","Go to Login → Forgot Password, enter your registered email or mobile, verify the OTP and set a new password."),
 ("Account","How does OTP login work?","Enter your mobile number on the OTP Verification page. We send a 6-digit code valid for 5 minutes. Enter it to sign in without a password."),
 ("Account","How do I delete my account?","Open Settings → Danger Zone → Delete Account. This permanently removes your profile, addresses and cart. Order history is retained for legal compliance."),
 ("Products","Are the products genuine?","All products are sourced from brand-authorised sellers and pass a quality check before dispatch."),
 ("Products","How do I compare products?","Click the compare icon on any product card. You can compare up to 4 products side by side including price, rating, brand and specifications."),
]

json.dump(products, open(os.path.join(D,"products.json"),"w"), indent=1)
json.dump(cats_out, open(os.path.join(D,"categories.json"),"w"), indent=1)
json.dump(coupons, open(os.path.join(D,"coupons.json"),"w"), indent=1)
json.dump(banners, open(os.path.join(D,"banners.json"),"w"), indent=1)
json.dump(reviews, open(os.path.join(D,"reviews.json"),"w"), indent=1)
json.dump([{"category":c,"question":q,"answer":a} for c,q,a in faqs], open(os.path.join(D,"faqs.json"),"w"), indent=1)
print("products",len(products),"reviews",len(reviews),"cats",len(cats_out))
