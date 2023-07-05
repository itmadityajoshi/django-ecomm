# Generated by Django 4.2 on 2023-04-28 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Pending', max_length=100, null=True),
        ),
    ]
