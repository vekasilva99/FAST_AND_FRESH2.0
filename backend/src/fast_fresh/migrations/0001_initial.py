# Generated by Django 3.0.3 on 2020-02-24 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.IntegerField()),
                ('elaboration_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('price_dolars_u', models.FloatField()),
                ('units_sold', models.IntegerField(default=0)),
                ('units_lost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_sub_total', models.FloatField()),
                ('bill_date', models.DateField(auto_now_add=True)),
                ('bill_time', models.TimeField(auto_now_add=True)),
                ('bill_sale', models.FloatField()),
                ('bill_delivery', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CashRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_last_name', models.CharField(max_length=100)),
                ('client_cedula', models.IntegerField(null=True)),
                ('client_phone', models.IntegerField(null=True)),
                ('client_gender', models.CharField(choices=[('F', 'Femenine'), ('M', 'Masculine')], max_length=1)),
                ('client_birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=30)),
                ('employee_last_name', models.CharField(max_length=30)),
                ('employee_cedula', models.IntegerField(unique=True)),
                ('employee_gender', models.CharField(choices=[('F', 'Femenine'), ('M', 'Masculine')], max_length=1)),
                ('employee_birth_date', models.DateField()),
                ('employee_phone', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='IVA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iva_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30, null=True)),
                ('is_special', models.BooleanField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Type_Of_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(editable=False, max_length=50)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona_name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.City')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=30, null=True)),
                ('open_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('store_phone', models.IntegerField(unique=True)),
                ('is_active', models.BooleanField()),
                ('supervisor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Employee')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Zona')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Product')),
                ('type_of_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Type_Of_Product')),
            ],
        ),
        migrations.CreateModel(
            name='PickUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_status', models.CharField(choices=[('Entregado', 'Entregado'), ('No Entregado', 'No Entregado')], max_length=15)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Bill')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.FloatField()),
                ('payment_method_instrument', models.IntegerField(null=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Bill')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.PaymentMethod')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_points', models.IntegerField(default=0)),
                ('member_email', models.EmailField(max_length=254)),
                ('member_start_date', models.DateField(auto_now_add=True)),
                ('member_end_date', models.DateField()),
                ('is_active', models.BooleanField()),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Client')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Zona')),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_rate', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('origin_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Currency')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Job'),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Store'),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_price', models.FloatField()),
                ('delivery_status', models.CharField(choices=[('Entregado', 'Entregado'), ('No Entregado', 'No Entregado')], max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('bill_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Bill')),
                ('employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Employee')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Zona')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.State'),
        ),
        migrations.CreateModel(
            name='CashRegisterIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_income_total', models.FloatField()),
                ('income_date', models.DateField(auto_now_add=True)),
                ('cash_register_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.CashRegister')),
            ],
        ),
        migrations.AddField(
            model_name='cashregister',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Store'),
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField()),
                ('product_discount', models.FloatField(default=0)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Bill')),
                ('product_batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Batch')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_iva',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.IVA'),
        ),
        migrations.AddField(
            model_name='bill',
            name='cash_register_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.CashRegister'),
        ),
        migrations.AddField(
            model_name='bill',
            name='client_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Client'),
        ),
        migrations.AddField(
            model_name='batch',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Product'),
        ),
        migrations.AddField(
            model_name='batch',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fast_fresh.Store'),
        ),
    ]
