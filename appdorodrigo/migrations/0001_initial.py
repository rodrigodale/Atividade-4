# Generated by Django 3.2.13 on 2023-09-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curiosidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_paisagem', models.CharField(max_length=50)),
                ('frequencia', models.CharField(choices=[('N', 'Never'), ('A', 'Always'), ('S', 'Sometimes')], max_length=1)),
                ('prioridade_de_visita', models.IntegerField()),
                ('categoria', models.CharField(choices=[('F', 'FRIENDS'), ('D', 'DATE'), ('P', 'PARENTS')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Paisagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_paisagem', models.CharField(max_length=50)),
                ('localizacao', models.CharField(max_length=50)),
                ('clima', models.DateField(max_length=50)),
                ('altitude', models.CharField(max_length=50)),
            ],
        ),
    ]
