# Generated by Django 4.2 on 2023-12-26 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name_plural': 'Jobs'},
        ),
        migrations.AlterModelOptions(
            name='jobseeker',
            options={'verbose_name_plural': 'JobSeekers'},
        ),
        migrations.AlterModelOptions(
            name='provinces',
            options={'verbose_name_plural': 'Provinces'},
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.category'),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.provinces'),
        ),
    ]