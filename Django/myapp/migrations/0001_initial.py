# Generated by Django 2.2 on 2019-04-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=100)),
                ('UserId', models.CharField(max_length=20)),
                ('UserPw', models.CharField(max_length=20)),
                ('UserAge', models.IntegerField()),
                ('UserEmail', models.TextField()),
                ('UserLike', models.IntegerField()),
            ],
        ),
    ]
