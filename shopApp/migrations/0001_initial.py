# Generated by Django 3.2.10 on 2024-03-14 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDB',
            fields=[
                ('ProductId', models.AutoField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Size', models.CharField(blank=True, max_length=100, null=True)),
                ('Color', models.CharField(blank=True, max_length=100, null=True)),
                ('Status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopApp.productdb')),
            ],
        ),
    ]