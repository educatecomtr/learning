from django.db import models
from django.template.defaultfilters import slugify
import itertools


class SlugMixin(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ad')
    slug = models.SlugField(unique=True, verbose_name='Slug', editable=False)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for slug_id in itertools.count(1):
                if not self.__class__.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)

        super(SlugMixin, self).save()
