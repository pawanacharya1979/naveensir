# Generated by Django 2.2rc1 on 2019-04-22 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restate', '0002_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='Looking_for',
            field=models.CharField(choices=[('AP', 'Apartment (2/3 BHK)'), ('Villa', 'Villa / Independent house'), ('Re', 'Residental Plot'), ('Ag', 'Agriculture Plot')], default='Apartment (2/3 BHK)', max_length=100),
        ),
    ]
