# Generated by Django 5.0.7 on 2024-07-14 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='sport',
            old_name='naziv_sporta',
            new_name='name',
        ),
        migrations.CreateModel(
            name='UserSportPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.sport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
