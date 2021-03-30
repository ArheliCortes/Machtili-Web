# Generated by Django 3.1.7 on 2021-03-29 22:33

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='ProfesorResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('paternal_surname', models.CharField(max_length=100, verbose_name='Apellido Paterno')),
                ('maternal_surname', models.CharField(max_length=100, verbose_name='Apellido Materno')),
                ('description', models.CharField(max_length=100, verbose_name='Rol')),
                ('urlImage', models.ImageField(upload_to='teachers/', verbose_name='Foto de Perfil')),
                ('phrase', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profesorresume')),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso')),
            ],
        ),
        migrations.CreateModel(
            name='ClientePotencial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=17)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso')),
                ('grado', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='curso', chained_model_field='curso', on_delete=django.db.models.deletion.CASCADE, to='core.grado')),
                ('plan', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='curso', chained_model_field='curso', on_delete=django.db.models.deletion.CASCADE, to='core.plan')),
            ],
        ),
    ]
