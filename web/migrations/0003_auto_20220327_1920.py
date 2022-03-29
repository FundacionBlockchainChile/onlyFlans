# Generated by Django 3.2.4 on 2022-03-27 22:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='contactform',
            name='contact_form_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.TextField(default='uuid.uuid4'),
        ),
    ]