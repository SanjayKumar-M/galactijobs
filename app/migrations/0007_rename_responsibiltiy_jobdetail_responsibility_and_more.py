# Generated by Django 5.0.3 on 2024-04-15 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_jobdetails_jobdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobdetail',
            old_name='responsibiltiy',
            new_name='responsibility',
        ),
        migrations.AddField(
            model_name='jobdetail',
            name='logo',
            field=models.ImageField(default=0, upload_to='app/img/companies/logo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobdetail',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
            preserve_default=False,
        ),
    ]