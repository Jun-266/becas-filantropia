from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app_becas.models import File, Scholarship, Candidate
from app_becas.forms.upload_file_form import UploadFileForm

main_dir = '../templates/report_management/'


@login_required
def home(request):
    files = File.objects.all()
    return render(request, main_dir + 'home_reports.html', {
        'files': files
    })


@login_required
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


@login_required
def delete_report(request, file_id):
    a_file = get_object_or_404(File, pk=file_id)
    if request.method == 'POST':
        a_file.delete()
        return redirect('reports')


def render_list_of_candidates(request):
    scholarships = Scholarship.objects.all()
    return render(request, main_dir + 'list_of_candidates.html', {
        'scholarships': scholarships
    })


def generate_list_of_candidates(request):
    scholarship_id = request.POST['scholarship_id']
    scholarship = get_object_or_404(Scholarship, pk=scholarship_id)
    candidates = Candidate.objects.filter(requested_scholarship=scholarship_id)
    if request.method == 'POST':
        template = get_template('report_management/template_report_list_of_candidates.html')
        context = {'scholarship': scholarship, 'candidates': candidates}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
