from portfolio.models import DescriptionModel, ProfileModel, SkillModel, WorkModel
from django.contrib import admin

# Register your models here.
admin.site.register(ProfileModel)
admin.site.register(DescriptionModel)
admin.site.register(SkillModel)
admin.site.register(WorkModel)
