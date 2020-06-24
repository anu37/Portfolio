from django.db import models
from portfolio import settings


class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    about_yourself = models.TextField()
    birth_date = models.DateField()
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    profile_photo = models.ImageField(upload_to='images/')
    cover_photo_1 = models.ImageField(upload_to='images/')
    cover_photo_2 = models.ImageField(upload_to='images/')
    resume = models.FileField(upload_to='resume')
    favicon = models.ImageField(upload_to='images/')


class PersonalSkill(models.Model):
    personal_skill = models.CharField(max_length=100)

class Job(models.Model):
    role = models.CharField(max_length=100)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    years_from = models.IntegerField(blank=True)
    years_to = models.IntegerField(blank=True)

    def __str__(self):
        return self.company_name


class Education(models.Model):
    course_name = models.CharField(max_length=25)
    subject = models.CharField(max_length=35)
    college = models.CharField(max_length=100)
    years_from = models.IntegerField(blank=True)
    years_to = models.IntegerField(blank=True)

    def __str__(self):
        return self.course_name

class SkillCategory(models.Model):
    category= models.CharField(max_length=25, unique=True)
    def __str__(self):
        return self.category

class Skill(models.Model):
    skill_name = models.CharField(max_length=25)
    category = models.ForeignKey(SkillCategory, to_field="category", on_delete=models.CASCADE)
    expert_percent = models.IntegerField()

    def __str__(self):
        return self.skill_name

class Language(models.Model):
    lang_name = models.CharField(max_length=25)
    expert_level = models.IntegerField()

    def __str__(self):
        return self.lang_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    
