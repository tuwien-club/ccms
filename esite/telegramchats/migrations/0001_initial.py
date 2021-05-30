# Generated by Django 3.1.11 on 2021-05-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        ('studies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramChatGroupClub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chat_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=39, null=True)),
                ('topic', models.CharField(blank=True, max_length=39, null=True)),
                ('lva_nummer', models.CharField(blank=True, max_length=39, null=True)),
                ('semester', models.CharField(blank=True, max_length=39, null=True)),
                ('member', models.ManyToManyField(blank=True, related_name='me_telegram_club_group', to='members.Member')),
                ('study', models.ManyToManyField(blank=True, related_name='st_telegram_club_group', to='studies.Study')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
