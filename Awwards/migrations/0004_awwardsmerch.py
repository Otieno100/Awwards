# Generated by Django 3.2.10 on 2022-06-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Awwards', '0003_alter_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwwardsMerch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
