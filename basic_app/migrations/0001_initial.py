# Generated by Django 4.0.4 on 2022-05-17 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=13)),
                ('logo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=128)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='department', to='basic_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeID', models.DateTimeField(auto_created=True, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basic_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
                ('description', models.CharField(max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='technology', to='basic_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('attachments', models.ImageField(upload_to='docs/')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='project', to='basic_app.company')),
                ('employees', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basic_app.employee')),
                ('technologies', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectTech', to='basic_app.technologies')),
            ],
        ),
    ]
