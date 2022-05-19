# Generated by Django 3.2.6 on 2022-05-16 10:23

from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.CharField(default=library.models.author_idno, editable=False, max_length=45, unique=True)),
                ('author_name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf_id', models.CharField(default=library.models.shelf_idno, editable=False, max_length=45, unique=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('no_of_books', models.IntegerField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, default='media/def_shelf.jpg', upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(default=library.models.staff_idno, editable=False, max_length=45, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('sex', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(default=library.models.book_idno, editable=False, max_length=45, unique=True)),
                ('book_name', models.CharField(max_length=1000)),
                ('edition', models.CharField(blank=True, max_length=1000, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('cover', models.ImageField(blank=True, default='media/def.jpg', upload_to='media')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.author')),
                ('shelf_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.shelf')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.staff')),
            ],
        ),
    ]
