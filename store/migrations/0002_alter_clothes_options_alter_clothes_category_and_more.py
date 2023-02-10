# Generated by Django 4.1.5 on 2023-01-30 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clothes',
            options={'verbose_name_plural': 'Clothes'},
        ),
        migrations.AlterField(
            model_name='clothes',
            name='category',
            field=models.CharField(choices=[("Men's_Shirt", "Men's_Shirt"), ('Skirt', 'Skirt'), ('Trouser', 'Trouser'), ('Gown', 'Gown')], max_length=30),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='image',
            field=models.ImageField(default='cloth.jpg', upload_to='cloth_images'),
        ),
    ]
