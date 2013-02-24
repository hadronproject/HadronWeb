from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from markdown import markdown


class Page(models.Model):
    title = models.CharField(max_length=256)
    entry = models.TextField()
    entry_html = models.TextField(editable=False, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True)
    published = models.NullBooleanField()
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return unicode(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
        self.entry_html = markdown(self.entry)
        super(Page, self).save(*args, **kwargs)


class News(models.Model):
    title = models.CharField(max_length=256)
    entry = models.TextField()
    entry_html = models.TextField(editable=False, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True)
    published = models.NullBooleanField()
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return unicode(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
        self.entry_html = markdown(self.entry)
        super(News, self).save(*args, **kwargs)


class Developer(models.Model):
    name = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    alias = models.CharField(max_length=128)
    occupation = models.CharField(max_length=512)
    roles = models.CharField(max_length=512)
    website = models.URLField(null=True)
    interests = models.CharField(max_length=512)
    published = models.NullBooleanField()

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.name+"::"+self.alias


class FrontendImage(models.Model):
    developer = models.ForeignKey(Developer, related_name='images')
    image = models.ImageField(upload_to="images")
