from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app_becas.models import File, Scholarship, Candidate, Donation, Egress, SelectionCriteria, Donor
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


@login_required
def render_list_of_candidates(request):
    scholarships = Scholarship.objects.all()
    return render(request, main_dir + 'list_of_candidates.html', {
        'scholarships': scholarships
    })


@login_required
def scholarship_students_report(request):
    if request.method == 'GET':
        scholarships = Scholarship.objects.all()
        return render(request, main_dir + 'scholarship_students.html', {
            'scholarships': scholarships
        })
    elif request.method == 'POST':
        return redirect('reports')


@login_required
def scholarship_finantial_report(request):
    scholarships = Scholarship.objects.all()
    return render(request, main_dir + 'scholarship_finantial.html', {
        'scholarships': scholarships
    })


@login_required
def generate_list_of_candidates(request):
    if request.method == 'POST':
        scholarship_id = request.POST['scholarship_id']
        scholarship = get_object_or_404(Scholarship, pk=scholarship_id)
        candidates = Candidate.objects.filter(requested_scholarship=scholarship_id)

        if candidates.count() == 0:
            files = File.objects.all()
            return render(request, main_dir + 'home_reports.html', {
                'error_message': 'La beca seleccionada no tiene aspirantes.',
                'files': files
            })
        else:
            template = get_template('report_management/template_report_list_of_candidates.html')
            context = {'scholarship': scholarship, 'candidates': candidates}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response


@login_required
def generate_report_scholarship_students(request):
    if request.method == 'POST':
        scholarship_id = request.POST['scholarship_id']
        scholarship = get_object_or_404(Scholarship, pk=scholarship_id)
        candidates = Candidate.objects.filter(requested_scholarship=scholarship_id)

        if candidates.count() == 0:
            files = File.objects.all()
            return render(request, main_dir + 'home_reports.html', {
                'error_message': 'La beca seleccionada no tiene estudiantes becados.',
                'files': files
            })
        else:
            template = get_template('report_management/template_scholarship_students_report.html')
            context = {'scholarship': scholarship, 'candidates': candidates}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response


@login_required
def generate_scholarship_finantial_report(request):
    if request.method == 'POST':
        scholarship_id = request.POST['scholarship_id']
        scholarship = get_object_or_404(Scholarship, pk=scholarship_id)
        donations = Donation.objects.filter(scholarship_id=scholarship_id)
        egresses = Egress.objects.filter(scholarship_id=scholarship_id)
        selection_criteria = SelectionCriteria.objects.filter(scholarship_id=scholarship_id)
        donors = Donor.objects.filter(scholarships=scholarship_id)
        number_of_students = Candidate.objects.count()

        template = get_template('report_management/template_scholarship_finantial_report.html')
        context = {'scholarship': scholarship,
                   'donations': donations,
                   'number_of_students': number_of_students,
                   'egresses': egresses,
                   'criteria': selection_criteria,
                   'donors': donors
                   }
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
