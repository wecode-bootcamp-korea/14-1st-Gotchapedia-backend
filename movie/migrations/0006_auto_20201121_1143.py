# Generated by Django 3.1.3 on 2020-11-21 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20201119_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieStaffPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'movie_staff_positions',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'positions',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('proflie_image', models.URLField(max_length=1000)),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.RemoveField(
            model_name='movieactor',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='movieactor',
            name='movie',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='movies',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='country',
            new_name='contry',
        ),
        migrations.AlterModelTable(
            name='moviegenre',
            table='movie_genre',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='MovieActor',
        ),
        migrations.AddField(
            model_name='staff',
            name='movie',
            field=models.ManyToManyField(through='movie.MovieStaffPosition', to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='moviestaffposition',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie'),
        ),
        migrations.AddField(
            model_name='moviestaffposition',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.position'),
        ),
        migrations.AddField(
            model_name='moviestaffposition',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.staff'),
        ),
    ]
