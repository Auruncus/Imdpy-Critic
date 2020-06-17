# Generated by Django 3.0.7 on 2020-06-16 23:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_movie_id', models.CharField(default='', max_length=100, unique=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('genre1', models.CharField(default='', max_length=255)),
                ('genre2', models.CharField(default='', max_length=255)),
                ('genre3', models.CharField(default='', max_length=255)),
                ('director', models.CharField(default='', max_length=255)),
                ('director_id', models.CharField(default='', max_length=100)),
                ('writer', models.CharField(default='', max_length=255)),
                ('writer_id', models.CharField(default='', max_length=100)),
                ('actor1', models.CharField(default='', max_length=255)),
                ('actor1_id', models.CharField(default='', max_length=100)),
                ('actor2', models.CharField(default='', max_length=255)),
                ('actor2_id', models.CharField(default='', max_length=100)),
                ('actor3', models.CharField(default='', max_length=255)),
                ('actor3_id', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WriterRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('writer', models.CharField(default='', max_length=255)),
                ('imdb_person_id', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('title', models.CharField(default='', max_length=255)),
                ('imdb_movie_id', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GenreRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('genre', models.CharField(default='', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DirectorRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('director', models.CharField(default='', max_length=255)),
                ('imdb_person_id', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActorRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('actor', models.CharField(default='', max_length=255)),
                ('imdb_person_id', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
