from django.shortcuts import render

main_dir = '../templates/report_management/'


def home(request):
    return render(request, main_dir + 'home_reports.html')


def upload_report(request):
    return render(request, main_dir + 'upload_report.html')


def external_reports(request):
    return render(request, main_dir + 'external_reports.html')


def generate_report(request):
    return render(request, main_dir + 'generate_report.html')
