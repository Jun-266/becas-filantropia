from django.shortcuts import render, redirect
from app_becas.models import File
from app_becas.forms.upload_file_form import UploadFileForm

main_dir = '../templates/report_management/'


def home(request):
    files = File.objects.all()
    return render(request, main_dir + 'home_reports.html', {
        'files': files
    })


def upload_report(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reports')
    else:
        form = UploadFileForm()
    return render(request, main_dir + 'upload_report.html', {
        'form_for_file': form
    })


def external_reports(request):
    return render(request, main_dir + 'external_reports.html')


def generate_report(request):
    return render(request, main_dir + 'generate_report.html')
