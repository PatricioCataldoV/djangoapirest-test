# Generated by Django 4.1.7 on 2023-05-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('var1', models.CharField(max_length=60)),
                ('var2', models.CharField(max_length=60)),
                ('var3', models.CharField(max_length=60)),
                ('var4', models.CharField(max_length=60)),
                ('var5', models.CharField(max_length=60)),
                ('var6', models.CharField(max_length=60)),
                ('var7', models.CharField(max_length=60)),
                ('var8', models.CharField(max_length=60)),
                ('var9', models.CharField(max_length=60)),
                ('var10', models.CharField(max_length=60)),
                ('var11', models.IntegerField()),
                ('var12', models.IntegerField()),
                ('var13', models.IntegerField()),
                ('var14', models.IntegerField()),
                ('var15', models.IntegerField()),
                ('var16', models.IntegerField()),
                ('var17', models.IntegerField()),
                ('var18', models.IntegerField()),
                ('var19', models.IntegerField()),
                ('var20', models.IntegerField()),
                ('var21', models.GenericIPAddressField()),
                ('var22', models.GenericIPAddressField()),
                ('var23', models.GenericIPAddressField()),
                ('var24', models.GenericIPAddressField()),
                ('var25', models.GenericIPAddressField()),
                ('var26', models.GenericIPAddressField()),
                ('var27', models.GenericIPAddressField()),
                ('var28', models.GenericIPAddressField()),
                ('var29', models.GenericIPAddressField()),
                ('var30', models.GenericIPAddressField()),
            ],
        ),
    ]
