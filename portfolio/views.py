from django.shortcuts import render
from .models import ProfileModel, SkillModel, WorkModel
# Create your views here.


def index(request):
    profile = ProfileModel.objects.all().last()
    skills = SkillModel.objects.all()
    works = WorkModel.objects.all()

    context = {
        'profile': profile,
        'skills': skills,
        'works': works,
    }
    return render(request, 'index.html', context)
