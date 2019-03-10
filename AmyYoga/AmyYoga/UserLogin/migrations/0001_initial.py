# Generated by Django 3.0 on 2019-03-10 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('birthday', models.DateField()),
                ('profession', models.CharField(max_length=20)),
                ('sex', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityQA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('securityQuestion1', models.CharField(max_length=20)),
                ('securityQuestion2', models.CharField(max_length=20)),
                ('securityQuestion3', models.CharField(max_length=20)),
                ('securityAnswer1', models.TextField()),
                ('securityAnswer2', models.TextField()),
                ('securityAnswer3', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('authoritySignal', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('personalInformation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UserLogin.PersonalInformation')),
                ('securityQA', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UserLogin.SecurityQA')),
            ],
        ),
    ]
