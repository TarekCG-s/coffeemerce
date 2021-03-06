# Generated by Django 3.0.5 on 2020-09-17 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_type', models.IntegerField(choices=[(0, 'Coffee Machine Small'), (1, 'Coffee Machine Large'), (2, 'Espresso Machine')], default=0)),
                ('product_class', models.IntegerField(choices=[(0, 'Base Model'), (1, 'Premium Model'), (2, 'Deluxe Model')], default=0)),
                ('water_line_compatible', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoffeePod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_type', models.IntegerField(choices=[(0, 'Coffee Pod Small'), (1, 'Coffee Pod Large'), (2, 'Espresso Pod')], default=0)),
                ('coffee_flavor', models.IntegerField(choices=[(0, 'Coffee Flavor Vanilla'), (1, 'Coffee Flavor Caramel'), (2, 'Coffee Flavor Psl'), (3, 'Coffee Flavor Mocha'), (4, 'Coffee Flavor Hazelnut')], default=0)),
                ('pack_size', models.IntegerField(choices=[(0, '1 Dozen (12)'), (1, '3 Dozen (36)'), (2, '5 Dozen (60)'), (3, '7 Dozen (84)')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
