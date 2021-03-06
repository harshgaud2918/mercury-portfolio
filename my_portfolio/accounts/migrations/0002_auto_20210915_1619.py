# Generated by Django 3.2.7 on 2021-09-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='body',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='code_link',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='organization',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='other_link',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='thumbnail',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='code_link',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='other_link',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
