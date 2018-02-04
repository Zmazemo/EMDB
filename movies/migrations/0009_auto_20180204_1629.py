# Generated by Django 2.0 on 2018-02-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_actor_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('photo', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('photo', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='writer',
        ),
        migrations.AddField(
            model_name='writer',
            name='movies',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='director',
            name='movies',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
    ]