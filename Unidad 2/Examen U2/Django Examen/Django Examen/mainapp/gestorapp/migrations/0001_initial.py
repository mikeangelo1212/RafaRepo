# Generated by Django 4.1.2 on 2022-10-31 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calleDom', models.CharField(max_length=255)),
                ('no_calleDom', models.CharField(max_length=255)),
                ('colonia', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEscuela', models.CharField(max_length=255)),
                ('CapacidadAlumnos', models.IntegerField()),
                ('calleEsc', models.CharField(max_length=255)),
                ('no_calleEsc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('materia', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('domicilio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.domicilio')),
                ('escuela', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.escuela')),
            ],
        ),
        migrations.CreateModel(
            name='Directivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('puesto', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('domicilio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.domicilio')),
                ('escuela', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.escuela')),
            ],
        ),
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('domicilio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.domicilio')),
                ('escuela', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.escuela')),
            ],
        ),
    ]