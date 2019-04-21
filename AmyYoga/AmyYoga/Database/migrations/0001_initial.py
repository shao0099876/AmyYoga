# Generated by Django 2.2 on 2019-04-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyRecord',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('coursename', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now=True)),
                ('pay_flag', models.BooleanField(default=False)),
                ('valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('coursename', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('courseintroduction', models.CharField(default='', max_length=100)),
                ('courseprice', models.IntegerField(default=0)),
                ('course_flag', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('authoritySignal', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('phoneNumber', models.CharField(default='', max_length=20)),
                ('name', models.CharField(default='', max_length=20)),
                ('age', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'), (50, '50'), (51, '51'), (52, '52'), (53, '53'), (54, '54'), (55, '55'), (56, '56'), (57, '57'), (58, '58'), (59, '59'), (60, '60'), (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), (66, '66'), (67, '67'), (68, '68'), (69, '69'), (70, '70'), (71, '71'), (72, '72'), (73, '73'), (74, '74'), (75, '75'), (76, '76'), (77, '77'), (78, '78'), (79, '79'), (80, '80'), (81, '81'), (82, '82'), (83, '83'), (84, '84'), (85, '85'), (86, '86'), (87, '87'), (88, '88'), (89, '89'), (90, '90'), (91, '91'), (92, '92'), (93, '93'), (94, '94'), (95, '95'), (96, '96'), (97, '97'), (98, '98'), (99, '99'), (100, '100'), (101, '101'), (102, '102'), (103, '103'), (104, '104'), (105, '105'), (106, '106'), (107, '107'), (108, '108'), (109, '109'), (110, '110')], default=0)),
                ('birthday', models.DateField(default='1970-01-01')),
                ('profession', models.CharField(max_length=20)),
                ('sex', models.BooleanField(choices=[(False, '女'), (True, '男')], default=False)),
                ('height', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('bust', models.FloatField(default=0)),
                ('waistline', models.FloatField(default=0)),
                ('hipline', models.FloatField(default=0)),
                ('shoulderwidth', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhysicalAssessment',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('caption', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SecurityQA',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('securityQ1', models.CharField(max_length=50)),
                ('securityA1', models.CharField(max_length=50)),
                ('securityQ2', models.CharField(max_length=50)),
                ('securityA2', models.CharField(max_length=50)),
                ('securityQ3', models.CharField(max_length=50)),
                ('securityA3', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='user_course_used',
            fields=[
                ('record_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('coursename', models.CharField(max_length=20)),
            ],
        ),
    ]
