# Generated by Django 5.1.6 on 2025-02-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
            options={
                'indexes': [models.Index(fields=['price'], name='RestAPIs_bo_price_4c0742_idx')],
            },
        ),
    ]
