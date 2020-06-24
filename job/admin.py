from django.contrib import admin
from .models import Job, Education, SkillCategory, Skill, Language, Blog, AboutMe, PersonalSkill

admin.site.register([
        Job, 
        Education, 
        SkillCategory, 
        Skill, 
        Language,
        Blog,
        AboutMe,
        PersonalSkill
    ])
