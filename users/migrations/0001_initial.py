# Generated by Django 3.1.7 on 2021-03-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('state_level', 'State Level'), ('district_level', 'District Level')], max_length=20)),
                ('tournament', models.CharField(choices=[('football', 'Football'), ('cricket', 'Cricket'), ('volley_ball', 'Volley Ball'), ('hockey', 'Hockey'), ('badminton', 'Badminton'), ('basket_ball', 'Basket Ball')], max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('date', models.DateTimeField()),
                ('venue', models.CharField(max_length=60)),
            ],
        ),
    ]
