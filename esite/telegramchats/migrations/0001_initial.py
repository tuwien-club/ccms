# Generated by Django 3.1.11 on 2021-05-18 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("members", "0001_initial"),
        ("studies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TelegramChat",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("chat_id", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TelegramChatGroup",
            fields=[
                (
                    "telegramchat_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="telegramchats.telegramchat",
                    ),
                ),
                ("name", models.CharField(max_length=39)),
            ],
            options={
                "abstract": False,
            },
            bases=("telegramchats.telegramchat",),
        ),
        migrations.CreateModel(
            name="TelegramChatGroupClub",
            fields=[
                (
                    "telegramchatgroup_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="telegramchats.telegramchatgroup",
                    ),
                ),
                (
                    "member",
                    models.ManyToManyField(
                        blank=True,
                        related_name="telegram_club_group",
                        to="members.Member",
                    ),
                ),
                (
                    "study",
                    models.ManyToManyField(
                        blank=True,
                        related_name="telegram_club_group",
                        to="studies.Study",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("telegramchats.telegramchatgroup",),
        ),
        migrations.CreateModel(
            name="TelegramChatGroupClubStudy",
            fields=[
                (
                    "telegramchatgroupclub_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="telegramchats.telegramchatgroupclub",
                    ),
                ),
                ("lva_nummer", models.CharField(max_length=39)),
                ("semester", models.CharField(max_length=39)),
            ],
            options={
                "abstract": False,
            },
            bases=("telegramchats.telegramchatgroupclub",),
        ),
        migrations.CreateModel(
            name="TelegramChatGroupClubTopic",
            fields=[
                (
                    "telegramchatgroupclub_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="telegramchats.telegramchatgroupclub",
                    ),
                ),
                ("topic", models.CharField(max_length=39)),
            ],
            options={
                "abstract": False,
            },
            bases=("telegramchats.telegramchatgroupclub",),
        ),
    ]
