# -*- coding: utf-8 -*-
"""
Builds the HTML shell for every PShop page.
Keeps <head>, loader, header/footer mounts and script wiring identical
across the site so pages only carry their own markup.
"""
import os
ROOT = "/home/user/PShop"

SHELL = '''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="author" content="PShop Retail India Pvt. Ltd.">
<meta name="theme-color" content="#2563eb">
<link rel="canonical" href="https://pshop.example/{canon}">
<!-- Open Graph / social -->
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="PShop">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{root}assets/img/banners/banner-1.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
{robots}<!-- Icons & manifest -->
<link rel="icon" href="{root}assets/img/icons/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/img/icons/favicon.svg">
<link rel="manifest" href="{root}manifest.webmanifest">
<!-- Fonts (async, non-blocking) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" media="print" onload="this.media='all'"
  href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@600;700;800&display=swap">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@600;700;800&display=swap"></noscript>
<!-- Styles -->
<link rel="stylesheet" href="{root}assets/css/main.css">
<link rel="stylesheet" href="{root}assets/css/pages/{css}.css">
{extrahead}<!-- Apply saved theme before first paint to avoid a flash -->
<script>
(function(){{try{{var t=JSON.parse(localStorage.getItem('pshop_theme')||'"auto"');
var d=t==='dark'||(t==='auto'&&matchMedia('(prefers-color-scheme:dark)').matches);
document.documentElement.dataset.theme=d?'dark':'light';}}catch(e){{}}}})();
</script>
{schema}</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>

<div class="page-loader" role="status" aria-label="Loading PShop"><div class="ring"></div></div>

<div id="site-header"></div>

<main id="main" class="{mainclass}">
{body}
</main>

<div id="site-footer"></div>
<div id="bottom-nav"></div>

<noscript>
  <div style="padding:1rem;background:#fee2e2;color:#991b1b;text-align:center">
    PShop needs JavaScript enabled to load products and manage your cart.
  </div>
</noscript>

<script type="module" src="{root}assets/js/pages/{js}.js"></script>
</body>
</html>
'''

def build(filename, *, title, desc, keywords, css, js, body,
          mainclass="", extrahead="", schema="", noindex=False, ogtype="website", folder="pages"):
    root = "../" if folder in ("pages", "admin") else ""
    canon = (folder + "/" if folder else "") + filename
    out = SHELL.format(
        title=title, desc=desc, keywords=keywords, css=css, js=js, body=body,
        mainclass=mainclass, extrahead=extrahead, schema=schema, root=root,
        canon=canon, ogtype=ogtype,
        robots='<meta name="robots" content="noindex,nofollow">\n' if noindex else '<meta name="robots" content="index,follow">\n'
    )
    path = os.path.join(ROOT, folder, filename) if folder else os.path.join(ROOT, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(out)
    return path
