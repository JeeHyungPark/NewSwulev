# Generated by Django 3.0.3 on 2020-02-23 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swuapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='swuapp.Profile'),
        ),
    ]