# Generated by Django 4.2.13 on 2024-08-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0015_alter_customerprofile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='code',
            field=models.CharField(blank=True, choices=[('29', '29'), ('33', '33'), ('25', '25')], max_length=2, null=True, verbose_name='Код мобильного оператора'),
        ),
    ]
