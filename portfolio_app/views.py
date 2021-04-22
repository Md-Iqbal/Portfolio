from django.shortcuts import render, HttpResponseRedirect
from .models import Personal_detail, CoCurricular_activity, Skill, Project, ContactMessage
from django.shortcuts import get_object_or_404
from .forms import ContactMessageForm

# Create your views here.


def HomeView(request):
    portfolio = get_object_or_404(Personal_detail)
    CoCurricular_activities = CoCurricular_activity.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            response = ContactMessage()
            response.name = form.cleaned_data['name']
            response.email = form.cleaned_data['email']
            response.subject = form.cleaned_data['subject']
            response.message = form.cleaned_data['message']
            response.ip = request.META.get('REMOTE_ADDR')
            response.save()
            return HttpResponseRedirect('/')
    form = ContactMessageForm
    context = {
        'form': form,
        'portfolio': portfolio,
        'CoCurricular_activities': CoCurricular_activities,
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'index.html', context)
