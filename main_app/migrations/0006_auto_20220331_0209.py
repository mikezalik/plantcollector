# Generated by Django 3.1.2 on 2022-03-31 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='care',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='care',
            name='plant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.plant'),
        ),
    ]
