# Generated by Django 4.2.20 on 2025-03-24 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jdr_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('effects', models.TextField(blank=True, null=True)),
                ('is_consumable', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='charactersheet',
            name='inventory',
        ),
        migrations.CreateModel(
            name='CharacterInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='jdr_manager.charactersheet')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jdr_manager.item')),
            ],
        ),
    ]
