from django.shortcuts import render
from .models import Profile
import pdfkit
from pdfkit.configuration import Configuration
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        summary = request.POST.get('summary')
        degree = request.POST.get('degree')
        university = request.POST.get('university')
        previous_experience = request.POST.get('previous_experience')
        skills = request.POST.get('skills')  # Expected as comma-separated string

        # Create a new Profile object and save it to the database
        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            address=address,
            summary=summary,
            degree=degree,
            university=university,
            previous_experience=previous_experience,
            skills=skills
        )
        profile.save()
    return render(request, 'pdf/accept.html')


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)

    # Convert comma-separated skills string to a list
    skill_list = [skill.strip() for skill in user_profile.skills.split(',') if skill.strip()]

    # Pass the list along with the user_profile to the template
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile, 'skills': skill_list})

    config = Configuration(wkhtmltopdf=r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, configuration=config, options={'page-size': 'A4', 'encoding': 'UTF-8'})
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response

from django.shortcuts import redirect
from django.views.decorators.http import require_POST

def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles': profiles})

@require_POST
def delete_profile(request, id):
    try:
        profile = Profile.objects.get(pk=id)
        profile.delete()
    except Profile.DoesNotExist:
        pass
    return redirect('list')

def view_resume_html(request, id):
    try:
        user_profile = Profile.objects.get(pk=id)
    except Profile.DoesNotExist:
        return redirect('list')

    skill_list = [skill.strip() for skill in user_profile.skills.split(',') if skill.strip()]
    return render(request, 'pdf/resume.html', {'user_profile': user_profile, 'skills': skill_list})
