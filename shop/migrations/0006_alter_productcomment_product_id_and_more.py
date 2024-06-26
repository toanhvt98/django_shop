# Generated by Django 5.0.6 on 2024-05-22 12:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_isactive_carouselpageindex_is_active_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, related_name='product_id_comment', to='shop.listingproduct'),
        ),
        migrations.RenameModel(
            old_name='ListingProduct',
            new_name='Product',
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('total', models.FloatField(default=0)),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, related_name='product_id_order', to='shop.product')),
                ('user_order_id', models.ForeignKey(db_column='user_order_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_order_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
