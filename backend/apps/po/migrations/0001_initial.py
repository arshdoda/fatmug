# Generated by Django 4.2.7 on 2023-11-18 05:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('order_date', models.DateTimeField()),
                ('expected_delivery_date', models.DateTimeField()),
                ('actual_delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')], max_length=10)),
                ('quality_rating', models.FloatField(null=True)),
                ('issue_date', models.DateTimeField()),
                ('acknowledgment_date', models.DateTimeField(null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_po', to='vendors.vendor')),
            ],
            options={
                'verbose_name_plural': 'Purchase Orders',
                'db_table': 'purchase_orders',
                'indexes': [models.Index(fields=['po_number'], name='purchase_or_po_numb_656941_idx')],
            },
        ),
    ]