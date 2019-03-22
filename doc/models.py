from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    """
    Tags used to classify a document.
    """
    name = models.CharField(max_length=10, unique=True)
    description = models.TextField()


class Doc(models.Model):
    """
    This is where contents get stored
    """
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
