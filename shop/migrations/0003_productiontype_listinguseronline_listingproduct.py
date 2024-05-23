# Generated by Django 5.0.6 on 2024-05-22 06:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_iscurrent_carouselpageindex_isactive'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('TP', 'Technologies'), ('CP', 'Clothes'), ('SP', 'Shoes')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ListingUserOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isOnline', models.BooleanField(default=False)),
                ('firsttime_login', models.DateTimeField(null=True)),
                ('onlineAt', models.DateTimeField(null=True)),
                ('offlineAt', models.DateTimeField(null=True)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('product_description', models.CharField(max_length=1000000, null=True)),
                ('product_price', models.FloatField()),
                ('product_folder_image', models.CharField(max_length=300)),
                ('product_type_id', models.ForeignKey(db_column='product_type_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_type_id', to='shop.productiontype')),
            ],
        ),
    ]
