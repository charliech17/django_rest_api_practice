# Generated by Django 4.2.5 on 2023-11-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0002_alter_stdcoursestatus_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesinfo',
            name='final_grade',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
