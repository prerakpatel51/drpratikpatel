from django.http import HttpResponse
from django.shortcuts import render


SERVICES = [
    {
        "number": "01",
        "title": "Adult internal medicine",
        "description": "Comprehensive care for adults, with careful attention to symptoms, health history, medications, and the goals that matter to you.",
    },
    {
        "number": "02",
        "title": "Chronic condition management",
        "description": "Ongoing monitoring and practical treatment plans for diabetes, high blood pressure, and other long-term health concerns.",
    },
    {
        "number": "03",
        "title": "Preventive and wellness care",
        "description": "Routine evaluations, age-appropriate screenings, risk-factor review, and guidance designed to protect your long-term health.",
    },
    {
        "number": "04",
        "title": "Healthy weight-loss planning",
        "description": "Medically supervised support that considers nutrition, activity, health conditions, medications, and realistic, sustainable goals.",
    },
    {
        "number": "05",
        "title": "Healthy weight-gain planning",
        "description": "A clinical evaluation to identify barriers to healthy weight gain and create a structured plan for nutrition, strength, and follow-up.",
    },
    {
        "number": "06",
        "title": "Prescription treatment evaluation",
        "description": "An individualized consultation to discuss whether prescription therapy, including a GLP-1 medicine, is medically appropriate and safe for you.",
    },
]


def home(request):
    return render(request, "clinic/home.html", {"services": SERVICES})


def health(_request):
    return HttpResponse("healthy", content_type="text/plain")
