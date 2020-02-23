# Generated by Django 3.0.3 on 2020-02-23 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('semester', models.CharField(max_length=30, unique=True)),
                ('lectureid', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('lecturename', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('userpw', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('quality', models.IntegerField()),
                ('challenge', models.IntegerField()),
                ('recommend', models.IntegerField()),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture', to='swuapp.Lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='swuapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserLecture',
            fields=[
                ('myuserid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='myuserid', serialize=False, to='swuapp.User', unique=True)),
                ('rating', models.CharField(choices=[('on', 'on'), ('off', 'off')], default='off', max_length=10)),
                ('mylectureid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mylectureid', to='swuapp.Lecture')),
            ],
        ),
    ]
