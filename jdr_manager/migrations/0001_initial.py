# Generated by Django 4.2.20 on 2025-03-18 12:23

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('max_players', models.IntegerField(default=4)),
                ('game_style', models.CharField(choices=[('D&D', 'Dungeons & Dragons'), ('Cthulhu', 'Cthulhu'), ('Pathfinder', 'Pathfinder'), ('Other', 'Other')], max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_campaigns', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(blank=True, related_name='campaigns', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=255)),
                ('race', models.CharField(blank=True, max_length=100, null=True)),
                ('inventory', models.TextField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('current_health', models.IntegerField()),
                ('max_health', models.IntegerField()),
                ('mana_points', models.IntegerField(default=100)),
                ('skill_points', models.IntegerField(default=10)),
                ('character_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jdr_manager.characterclass')),
            ],
        ),
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('severity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('stats_template', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='XpSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_cap', models.IntegerField(default=20)),
                ('xp_formula', models.TextField(blank=True, null=True)),
                ('campaign', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='xp_system', to='jdr_manager.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('mana_cost', models.IntegerField(default=0)),
                ('spell_level', models.IntegerField(default=1)),
                ('required_spells', models.ManyToManyField(blank=True, to='jdr_manager.spell')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requires_level', models.IntegerField(default=0)),
                ('skill_level', models.IntegerField(default=1)),
                ('game_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='jdr_manager.gametemplate')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterXP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('current_xp', models.IntegerField(default=0)),
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='xp', to='jdr_manager.charactersheet')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mastery_level', models.IntegerField(default=1)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_skills', to='jdr_manager.charactersheet')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jdr_manager.skill')),
            ],
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='injuries',
            field=models.ManyToManyField(blank=True, related_name='characters', to='jdr_manager.damage'),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='character_sheets', to='jdr_manager.skill'),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='spells',
            field=models.ManyToManyField(blank=True, related_name='characters', to='jdr_manager.spell'),
        ),
        migrations.AddField(
            model_name='charactersheet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_sheets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='characterclass',
            name='available_skills',
            field=models.ManyToManyField(blank=True, to='jdr_manager.skill'),
        ),
        migrations.AddField(
            model_name='characterclass',
            name='available_spells',
            field=models.ManyToManyField(blank=True, to='jdr_manager.spell'),
        ),
    ]
