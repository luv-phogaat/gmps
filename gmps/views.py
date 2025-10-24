from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.template import loader
from .forms import ContactForm
from .models import ResultPdf, Image



def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {"home_page": "activeMenu"}
    # template = loader.get_template('gmps/index.html')
    return render(request, 'gmps/index.html', context)

def about(request):
    context = {"about_page": "activeMenu"}
    return render(request, 'gmps/about.html', context)

def admission(request):
    context = {"admission_page": "activeMenu"}
    return render(request, 'gmps/admission.html', context)

def career(request):
    context = {"career_page": "activeMenu"}
    return render(request, 'gmps/career.html', context)

def result(request):
    resultData = ResultPdf.objects.all()
    context = {"result_page": "activeMenu", "resultData": resultData}
    return render(request, 'gmps/result.html', context)

def gallery(request):
    images = Image.objects.all()
    context = {"gallery_page": "activeMenu", "images": images}
    return render(request, 'gmps/gallery.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        # print('Printing', request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # text = form.cleaned_data['']
            form = ContactForm()
    context = {"contact_page": "activeMenu"}
    return render(request, 'gmps/contactus.html', context)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

# def error_404(request, exception, template_name="404.html"):
#     response = render_to_response(template_name)
#     response.status_code = 404
#     return response

# def error_500(request, *args, **argv):
#     return render(request, '500.html', status=500)

def post(request):
    context = {"contact_page": "activeMenu"}
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        # text = form.cleaned_data['']
        form = ContactForm()
        return redirect('contact')
    return render(request, 'gmps/contactus.html', context)

