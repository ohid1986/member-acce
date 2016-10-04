from django.db import models
from django.core.urlresolvers import reverse
from .file_validators import file_size, validate_file_extension
from django.conf import settings

from django_resized import ResizedImageField

import datetime
# Create your models here.



class Person(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(1970, datetime.date.today().year + 1)]
    name = models.CharField(max_length=175)
    present_position=models.CharField(max_length=100)
    organization= models.CharField(max_length=150,blank=True)
    address = models.CharField(max_length=250, blank=True)
    tele_land = models.CharField(max_length=15,blank=True)
    tele_cell = models.CharField(max_length=15, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='member_persons')
    photo= ResizedImageField(size=[70, 70],crop=['middle', 'center'],upload_to='persons/%Y/%m/%d/',null=True,
        blank=True,
        editable=True,
        help_text="Person Picture", validators=[file_size])
    website = models.URLField(blank=True)
    birth_date = models.DateField(null=True,blank=True)
    passing_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    category = models.ForeignKey('Membership', on_delete=models.CASCADE)
    member_since = models.DateField(null=True,blank=True)
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('member:member-detail', kwargs={'pk': self.pk})

    def __str__(self):              # __unicode__ on Python 2
        return self.name


    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

class Membership(models.Model):
    category = models.CharField(max_length=50, blank=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.category


class ExecMember(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE )
    committee_position = models.CharField(max_length=100)
    rank = models.IntegerField(blank=True)
    member_start_date = models.DateField(blank=True)
    member_end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering =['rank']

    def __str__(self):  # __unicode__ on Python 2
        return self.committee_position


class Constitution(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d/',null=True,
        blank=True,
        editable=True,
        help_text="Document File", validators=[file_size])

    def __str__(self):  # __unicode__ on Python 2
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    news = models.TextField()
    docfile = models.FileField(upload_to='news/%Y/%m/%d/', null=True,
                               blank=True,
                               editable=True,
                               help_text="News File",validators=[validate_file_extension, file_size])
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('member:book-detail', kwargs={'pk': self.pk})

class Event(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering =['-created']


    def __str__(self):  # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('member:event-detail', kwargs={'pk': self.pk})

class Gallery(models.Model):
    title = models.CharField(max_length=150)
    event = models.ForeignKey(Event, on_delete=models.CASCADE )
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(upload_to='events/%Y/%m/%d/', null=True,
                              blank=True,
                              editable=True,
                              help_text="Event Picture", validators=[file_size], width_field="width", height_field="height")
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    class Meta:
        get_latest_by = 'pub_date'

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    def get_absolute_url(self):
        return reverse('member:gallery-detail', kwargs={'pk': self.pk})