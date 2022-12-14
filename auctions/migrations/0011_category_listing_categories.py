# Generated by Django 4.1.1 on 2022-10-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='listings', to='auctions.category'),
        ),
    ]
