from django.db import models
from core.models import BaseModel, SlugModel

from typedefs.definitions import TYPE_DEFINITIONS
from typedefs.validators import VALIDATORS
from django_mysql.models import ListCharField

BUILT_IN_TYPES = (
  ('bool', 'Boolean'),
  ('int', 'Integer'),
  ('double', 'Double'),
)


class FieldDefinition(SlugModel):

  name = models.CharField(verbose_name="Field Name", max_length=20)

  help_text = models.CharField(max_length=255)
  
  typedef = ListCharField(
    base_field=models.CharField(max_length=20, choices=TYPE_DEFINITIONS),
    size=10,
    max_length=(10 * 21),  # 10 * 21 character nominals, plus commas
  )
  
  validators = ListCharField(
    base_field=models.CharField(max_length=20, choices=VALIDATORS),
    size=10,
    max_length=(10 * 21),  # 10 * 21 character nominals, plus commas
  )


class FormDefinition(SlugModel):

  name = models.CharField(verbose_name='Form Name', max_length=20)
  help_text = models.CharField(max_length=255)
  notes = models.TextField()

  fields = models.ManyToManyField(FieldDefinition)