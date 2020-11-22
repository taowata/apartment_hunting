# Generated by Django 2.2.6 on 2020-11-22 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='アパート名')),
                ('goodNumber', models.IntegerField(verbose_name='いいね数')),
            ],
            options={
                'db_table': 'apartment',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='部屋番号')),
                ('isRentable', models.BooleanField(verbose_name='空部屋かどうか')),
                ('rent', models.IntegerField(verbose_name='家賃')),
                ('floorPlan', models.CharField(max_length=255, verbose_name='間取り')),
                ('areBathAndToiletSeparated', models.BooleanField(verbose_name='バストイレ')),
                ('age', models.IntegerField(verbose_name='築年数')),
                ('buildingStructure', models.CharField(max_length=255, verbose_name='建物構造')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apartment.Apartment', verbose_name='アパート')),
            ],
            options={
                'db_table': 'room',
            },
        ),
    ]
