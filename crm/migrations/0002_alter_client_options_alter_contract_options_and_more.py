# Generated by Django 4.0 on 2022-01-13 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_options_alter_customuser_department'),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['last_name'], 'verbose_name': 'Client'},
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Contrat'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Evénement'},
        ),
        migrations.AlterField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customuser'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.client'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='sales_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customuser'),
        ),
        migrations.AlterField(
            model_name='event',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.client'),
        ),
        migrations.AlterField(
            model_name='event',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.contract'),
        ),
        migrations.AlterField(
            model_name='event',
            name='support_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customuser'),
        ),
    ]