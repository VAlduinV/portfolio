# Generated by Django 4.2.1 on 2023-11-19 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("chats", "0003_request_chat"),
        ("power_chat", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="powerchat",
            name="answer",
        ),
        migrations.RemoveField(
            model_name="powerchat",
            name="question",
        ),
        migrations.AlterField(
            model_name="powerchat",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="power_chats",
                to="chats.userprofile",
            ),
        ),
        migrations.CreateModel(
            name="PowerChatMessage",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.CharField(max_length=512)),
                ("answer", models.CharField(max_length=512, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "chat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="power_chat.powerchat",
                    ),
                ),
            ],
        ),
    ]
