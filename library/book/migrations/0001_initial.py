# Generated by Django 3.1.1 on 2021-03-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('count', models.IntegerField(default=10)),
                ('authors', models.ManyToManyField(related_name='author_books', to='author.Author')),
            ],
        ),
    ]
