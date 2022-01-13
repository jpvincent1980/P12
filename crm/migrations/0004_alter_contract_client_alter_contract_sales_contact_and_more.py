# Generated by Django 4.0 on 2022-01-13 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_options_alter_customuser_department'),
        ('crm', '0003_alter_contract_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.RESTRICT, to='crm.client'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='sales_contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='accounts.customuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='client',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.RESTRICT, to='crm.client'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='contract',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='crm.contract'),
            preserve_default=False,
        ),
    ]
