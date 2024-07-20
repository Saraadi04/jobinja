# Generated by Django 4.2 on 2023-12-21 06:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Website', models.CharField(max_length=300)),
                ('Industry', models.CharField(max_length=200)),
                ('EstablishedYear', models.CharField(max_length=200)),
                ('Introduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('TEH', 'Thran'), ('KHR', 'Khorasan Razavi'), ('ISF', 'Isfahan'), ('ALB', 'Alborz'), ('FA', 'Fars'), ('Q', 'Qom'), ('EA', 'East Azerbaijan'), ('M', 'Mazandaran'), ('G', 'Gilan'), ('K', 'Kerman'), ('KH', 'Khozestan'), ('Y', 'Yazd'), ('M', 'Markazi'), ('QA', 'Qazvin'), ('HO', 'Hormozgan'), ('GO', 'Golestan'), ('ZA', 'Zanjan'), ('HA', 'Hamedan'), ('SE', 'Semnan'), ('WA', 'West Azerbaijan'), ('BO', 'Boushehr'), ('KO', 'Kordestan'), ('KER', 'Kermanshah'), ('SB', 'Sistan Balouchestan'), ('CHB', 'Charmahal Bakhtiari'), ('A', 'Ardebil'), ('KB', 'Kohkiluyeh and Boyerahmad'), ('I', 'Ilam'), ('KHJ', 'Khorasan Jonoubi'), ('KHS', 'Khorestan Shomali'), ('LO', 'Lorestan')], max_length=3)),
            ],
        ),
        migrations.RenameField(
            model_name='jobseeker',
            old_name='bio',
            new_name='cv',
        ),
        migrations.RemoveField(
            model_name='jobseeker',
            name='user',
        ),
        migrations.AddField(
            model_name='job',
            name='max_salary',
            field=models.DecimalField(decimal_places=2, default=8000, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='min_salary',
            field=models.DecimalField(decimal_places=2, default=20000, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='email_adress',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='marital_status',
            field=models.CharField(choices=[('M', 'Married'), ('S', 'Single')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='phone_number',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='residence',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('SM', 'Sales and Marketing'), ('SP', 'Software and Programming'), ('FA', 'Finantial and Accounting'), ('O', 'Official'), ('DM', 'DigitalMarketing'), ('CP', 'ContentProduction'), ('IDS', 'It Devops Server'), ('D', 'Design'), ('CS', 'Customer Support'), ('IE', 'Industrial Enginerring'), ('EE', 'Electrical Engineering'), ('CE', 'Civil Engineering'), ('HR', 'Human Resources'), ('SF', 'Servise Force'), ('E', 'Education'), ('I', 'Inventory'), ('CF', 'Cinema Feild'), ('MAE', 'Mechanical and Aerospace Engineering'), ('T', 'Technician'), ('TO', 'Tourism'), ('PM', 'Product Manager'), ('M', 'Medical'), ('TR', 'Transportation'), ('HM', 'HotelManagement'), ('PR', 'Public Relations'), ('CP', 'Chemical Petronum'), ('IM', 'Insurance Management'), ('MME', 'Mine and Metalogy Engineering'), ('BE', 'Biomedical Engineering'), ('TE', 'Txtile Engineering'), ('PH', 'Pharmacology'), ('J', 'Journalist'), ('AE', 'Agricultural Engineering'), ('MSE', 'Musical and Sound Engineering'), ('PE', 'Physical Education')], max_length=3),
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.AlterField(
            model_name='job',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.company'),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.provinces'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
