# Generated by Django 4.1.6 on 2023-02-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(choices=[('PayPal', 'PayPal'), ('Bank Transfer', 'Bank Transfer'), ('PayNow', 'PayNow'), ('Cash / Nets', 'Cash / Nets')], db_column='payment_mode', max_length=20)),
                ('payment_status', models.CharField(choices=[('None', 'None'), ('Paid', 'Paid'), ('Not Yet', 'Not Yet')], db_column='payment_status', default='None', max_length=10)),
                ('payment_receipt', models.CharField(choices=[('Sent', 'Sent'), ('Not Yet', 'Not Yet')], db_column='payment_receipt', default='Not Yet', max_length=10)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]