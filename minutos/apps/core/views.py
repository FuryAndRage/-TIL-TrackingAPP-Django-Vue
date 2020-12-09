from django.shortcuts import render

def frontpage(request):
    return render(request, 'frontpage.html')

def privacy_policy(request):
    return render(request, 'privacy.html')

def terms_of_service(request):
    return render(request, 'termsofservice.html')

def plans(request):
    return render(request, 'plans.html')