# Generated by Django 4.2.7 on 2024-03-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emoji_password_evaluation', '0003_userresponse_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.TextField()),
                ('identifier', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserResponse',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
