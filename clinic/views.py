import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


SERVICES = [
    {
        "number": "01",
        "title": "Primary care",
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


FAQS = [
    {
        "question": "How do I find an internal medicine physician near Viera or Rockledge?",
        "answer": "Dr. Pratik Patel sees adult patients at 8041 Spyglass Hill Road, Suite 102, in Melbourne near Viera. The clinic also serves patients from Rockledge and surrounding Brevard County communities. Call (321) 255-4003 to ask about appointment availability.",
    },
    {
        "question": "What does an internal medicine physician treat?",
        "answer": "Internal medicine physicians specialize in adult health. Visits may address preventive care, new symptoms, medication concerns, and chronic conditions such as type 2 diabetes and high blood pressure. Care is based on each patient's medical history and needs.",
    },
    {
        "question": "Does Dr. Patel provide primary care for adults?",
        "answer": "Yes. Dr. Patel provides primary care and internal medicine for adults, including routine health evaluations, preventive guidance, chronic condition follow-up, medication review, and evaluation of new health concerns.",
    },
    {
        "question": "Does Dr. Patel offer medical weight-loss and healthy weight-gain care?",
        "answer": "Yes. Visits may address physician-guided weight loss, healthy weight gain, or weight maintenance. Recommendations begin with an individual medical evaluation and consider medical conditions, current medicines, nutrition, activity, sleep, and personal goals.",
    },
    {
        "question": "Can I request Ozempic or another GLP-1 medicine?",
        "answer": "You may discuss Ozempic or another GLP-1 medicine during a visit. A prescription is not guaranteed and depends on an appropriate diagnosis, medical evaluation, safety review, and individual eligibility. Ozempic is not FDA-approved as a weight-loss medication.",
    },
    {
        "question": "Do I need a referral to make an appointment?",
        "answer": "Referral requirements vary by insurance plan. Call the office before scheduling so the team can explain appointment requirements and help you determine whether your plan requires a referral.",
    },
    {
        "question": "What should I bring to my first appointment?",
        "answer": "Bring a photo ID, insurance information, a current medication and supplement list, relevant medical records, recent test results, and the names of other clinicians involved in your care. Call the office if you are unsure what is needed.",
    },
    {
        "question": "Is Dr. Patel accepting new patients?",
        "answer": "New-patient availability can change. Call the office at (321) 255-4003 for the most current scheduling information.",
    },
    {
        "question": "What should I do if I have a medical emergency?",
        "answer": "This clinic website is not monitored for emergencies. Call 911 or go to the nearest emergency department if you believe you are experiencing a medical emergency.",
    },
]


def home(request):
    faq_entities = [
        {
            "@type": "Question",
            "name": faq["question"],
            "acceptedAnswer": {"@type": "Answer", "text": faq["answer"]},
        }
        for faq in FAQS
    ]
    return render(
        request,
        "clinic/home.html",
        {
            "services": SERVICES,
            "faqs": FAQS,
            "faq_entities_json": json.dumps(faq_entities),
            "canonical_url": request.build_absolute_uri(request.path),
            "google_review_url": settings.GOOGLE_REVIEW_URL,
            "google_review_write_url": settings.GOOGLE_REVIEW_WRITE_URL,
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
