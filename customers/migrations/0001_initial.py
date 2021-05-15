# Generated by Django 3.0.8 on 2021-05-15 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price_total', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('user', models.CharField(max_length=120, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.Mobile')),
            ],
        ),
    ]