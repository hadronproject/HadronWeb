from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from markdown import markdown


class Document(models.Model):
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
        super(Document, self).save(*args, **kwargs)
