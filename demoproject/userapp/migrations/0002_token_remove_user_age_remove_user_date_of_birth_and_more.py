# Generated by Django 4.0.3 on 2024-12-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('expires_at', models.DateTimeField()),
                ('user_id', models.IntegerField()),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$320000$kAdAiGWjWtkx2e2FgMiuIO$+og1PDjFQHvm7ZsifBHhjEwdMr+GHIr3omhau3k6zsw=', max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
