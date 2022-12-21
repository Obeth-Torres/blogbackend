from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class PhilosophyManager(models.Manager):
    def get_queryset(self):
        return super(PhilosophyManager,
                     self).get_queryset().filter(subject='philosophy')


class PsychologyManager(models.Manager):
    def get_queryset(self):
        return super(PsychologyManager,
                     self).get_queryset().filter(subject='psychology')


class PsychoanalysisManager(models.Manager):
    def get_queryset(self):
        return super(PsychoanalysisManager,
                     self).get_queryset().filter(subject='psychoanalysis')


class Post(models.Model):
    SUBJET_CHOICES = (
        ('psychology', 'Psychology'),
        ('philosophy', 'Philosophy'),
        ('psychoanalysis', 'Psychoanalysis'),
    )
    subject = models.CharField(
        max_length=200, choices=SUBJET_CHOICES, default='philosophy')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')

    abstract = RichTextField()
    importantWords = models.CharField(max_length=500)
    body = models.TextField(default='', blank=True)
    references = models.TextField(default='', blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    image2 = models.ImageField(blank=True, upload_to='images/')

    publish = models.DateTimeField(default=timezone.now)

    objects = models.Manager()  # The default manager.
    philosophy = PhilosophyManager()  # Our custom manager.
    psychology = PsychologyManager()  # Our custom manager.
    psychoanalysis = PsychoanalysisManager()  # Our custom manager.

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class Capitulo(models.Model):
    post = models.ForeignKey(
        Post, related_name='capitulos', on_delete=models.CASCADE)

    cap_title = models.CharField(max_length=250)
    cap_body = RichTextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    cita1 = models.TextField(default='', blank=True)
    cita2 = models.TextField(default='', blank=True)
    referencias1 = models.TextField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    sub_title1 = models.CharField(max_length=250, default='', blank=True)
    sub_body1 = RichTextField(default='', blank=True)
    image1 = models.ImageField(blank=True, upload_to='images/')
    cita3 = models.TextField(default='', blank=True)
    cita4 = models.TextField(default='', blank=True)
    referencias2 = models.TextField(default='', blank=True)

    sub_title2 = models.CharField(max_length=250, default='', blank=True)
    sub_body2 = RichTextField(default='', blank=True)
    image2 = models.ImageField(blank=True, upload_to='images/')
    cita5 = models.TextField(default='', blank=True)
    cita6 = models.TextField(default='', blank=True)
    referencias3 = models.TextField(default='', blank=True)

    sub_title3 = models.CharField(max_length=250, default='', blank=True)
    sub_body3 = RichTextField(default='', blank=True)
    image3 = models.ImageField(blank=True, upload_to='images/')
    cita7 = models.TextField(default='', blank=True)
    cita8 = models.TextField(default='', blank=True)
    referencias4 = models.TextField(default='', blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Capitulo {self.cap_title} on {self.post}'
