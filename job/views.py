from django.shortcuts import render
from .models import Job, Education, SkillCategory, Skill, Language, Blog, AboutMe, PersonalSkill
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def index(request):
    jobs = Job.objects.all().order_by('-id')
    edu = Education.objects.all()
    skill = Skill.objects.all()
    lang = Language.objects.all()
    blog = Blog.objects.all()
    aboutme = AboutMe.objects.all()
    category = SkillCategory.objects.all()
    personal_skill = PersonalSkill.objects.all()
    return render(request, 'index.html', {'jobs': jobs, 
    'education': edu,
    'skills': skill,
    'languages': lang,
    'blogs': blog,
    "categories": category,
    "aboutme": aboutme,
    "personal_skill": personal_skill
    })

def mail(request):
    if request.method == 'POST':
        print("sdfhsdfb")
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website'] if 'website' in request.POST else None
        subject = request.POST['subject'] if 'subject' in request.POST else None
        message = request.POST['message']
        sendmail(name, email, website, subject, message)
        return HttpResponse('Success')

def sendmail(name, email, website, subject, message):
    message = "email = "+ email +", website = "+ website +", message = "+ message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER,]
    send_mail( subject, message, email_from, recipient_list )
    return True