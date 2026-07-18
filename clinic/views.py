from django.http import HttpResponse
from django.shortcuts import render


SERVICES = [
    {
        "number": "01",
        "title": "Adult primary care & internal medicine",
        "description": "Comprehensive medical care for adults, including evaluation of new symptoms, medication review, follow-up care, and coordination across your complete health picture.",
    },
    {
        "number": "02",
        "title": "Diabetes & blood pressure care",
        "description": "Ongoing monitoring and individualized treatment planning for type 2 diabetes, high blood pressure, and other chronic health conditions.",
    },
    {
        "number": "03",
        "title": "Preventive care & wellness visits",
        "description": "Routine adult health evaluations, age-appropriate screening guidance, risk-factor review, and practical steps to support long-term wellness.",
    },
    {
        "number": "04",
        "title": "Medical weight-loss support",
        "description": "Physician-guided weight-loss planning that considers nutrition, activity, sleep, medical conditions, current medicines, and sustainable goals.",
    },
    {
        "number": "05",
        "title": "Healthy weight-gain evaluation",
        "description": "A medical evaluation for difficulty gaining weight, followed by an individualized plan for nutrition, strength, underlying health needs, and follow-up.",
    },
    {
        "number": "06",
        "title": "GLP-1 & Ozempic consultation",
        "description": "A one-on-one evaluation to discuss whether a GLP-1 medicine or another prescription option is indicated, medically appropriate, and safe for you.",
    },
]


def home(request):
    return render(
        request,
        "clinic/home.html",
        {
            "services": SERVICES,
            "canonical_url": request.build_absolute_uri(request.path),
        },
    )


def health(_request):
    return HttpResponse("healthy", content_type="text/plain")


def robots(request):
    sitemap_url = request.build_absolute_uri("/sitemap.xml")
    body = f"User-agent: *\nAllow: /\nDisallow: /health/\nSitemap: {sitemap_url}\n"
    return HttpResponse(body, content_type="text/plain")


def sitemap(request):
    homepage_url = request.build_absolute_uri("/")
    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{homepage_url}</loc>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
'''
    return HttpResponse(body, content_type="application/xml")
