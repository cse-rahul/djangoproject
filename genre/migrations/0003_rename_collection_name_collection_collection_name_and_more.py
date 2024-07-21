# Generated by Django 5.0.7 on 2024-07-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0002_alter_collection_collcover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='collection_name',
            new_name='Collection_name',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='collcover',
        ),
        migrations.RemoveField(
            model_name='piece',
            name='piececover',
        ),
        migrations.AlterField(
            model_name='piece',
            name='typ',
            field=models.CharField(default='article', max_length=200),
        ),
        migrations.AddField(
            model_name='collection',
            name='Collcover',
            field=models.CharField(default='img', max_length=1000),
        ),
        migrations.AddField(
            model_name='piece',
            name='Piececover',
            field=models.CharField(default='img', max_length=1000),
        ),
    ]
