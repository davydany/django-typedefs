# Generated by Django 2.2.6 on 2019-10-29 19:51

from django.db import migrations, models
import django_mysql.models
import typedefs.definitions
import typedefs.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20, verbose_name='Field Name')),
                ('help_text', models.CharField(max_length=255)),
                ('typedef', django_mysql.models.ListCharField(models.CharField(choices=[('boolean', typedefs.definitions.Boolean), ('integer', typedefs.definitions.Integer), ('float', typedefs.definitions.Float), ('date', typedefs.definitions.Date), ('datetime', typedefs.definitions.DateTime)], max_length=20), max_length=210, size=10)),
                ('validators', django_mysql.models.ListCharField(models.CharField(choices=[('future-date-validator', typedefs.validators.FutureDateValidator), ('minimum-numeric-validator', typedefs.validators.MinimumNumericValidator), ('maximum-numeric-validator', typedefs.validators.MaximumNumericValidator)], max_length=20), max_length=210, size=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20, verbose_name='Form Name')),
                ('help_text', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('fields', models.ManyToManyField(to='typedefs.FieldDefinition')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]