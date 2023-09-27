from django.shortcuts import render

main_dir = '../templates/report-management/'


def home(request):
    return render(request, main_dir + 'home-reports.html')


def upload_report(request):
    return render(request, main_dir + 'upload-report.html')
