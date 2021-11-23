# Generated by Django 3.2.8 on 2021-10-25 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookrating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, db_column='User_Id', null=True)),
                ('name', models.IntegerField(blank=True, db_column='Name', null=True)),
                ('rating', models.IntegerField(blank=True, db_column='Rating', null=True)),
            ],
            options={
                'db_table': 'bookrating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=999, null=True)),
                ('ratingdist1', models.CharField(blank=True, db_column='RatingDist1', max_length=999, null=True)),
                ('pagesnumber', models.IntegerField(blank=True, db_column='pagesNumber', null=True)),
                ('ratingdist4', models.CharField(blank=True, db_column='RatingDist4', max_length=999, null=True)),
                ('ratingdisttotal', models.CharField(blank=True, db_column='RatingDistTotal', max_length=999, null=True)),
                ('publishmonth', models.IntegerField(blank=True, db_column='PublishMonth', null=True)),
                ('publishday', models.IntegerField(blank=True, db_column='PublishDay', null=True)),
                ('publisher', models.CharField(blank=True, db_column='Publisher', max_length=999, null=True)),
                ('countsofreview', models.IntegerField(blank=True, db_column='CountsOfReview', null=True)),
                ('publishyear', models.IntegerField(blank=True, db_column='PublishYear', null=True)),
                ('language', models.CharField(blank=True, db_column='Language', max_length=999, null=True)),
                ('authors', models.CharField(blank=True, db_column='Authors', max_length=999, null=True)),
                ('rating', models.FloatField(blank=True, db_column='Rating', null=True)),
                ('ratingdist2', models.CharField(blank=True, db_column='RatingDist2', max_length=999, null=True)),
                ('ratingdist5', models.CharField(blank=True, db_column='RatingDist5', max_length=999, null=True)),
                ('isbn', models.CharField(blank=True, db_column='ISBN', max_length=999, null=True)),
                ('ratingdist3', models.CharField(blank=True, db_column='RatingDist3', max_length=999, null=True)),
            ],
            options={
                'db_table': 'books',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, db_column='UserID', max_length=100, null=True)),
                ('bookid', models.CharField(blank=True, db_column='BookID', max_length=100, null=True)),
            ],
            options={
                'db_table': 'cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User_cast',
            fields=[
                ('cast_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
