# Generated by Django 4.0 on 2021-12-11 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btest', '0002_rubric_alter_bb_options_alter_bb_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('email', models.CharField(max_length=50, verbose_name='e-mail')),
                ('adress', models.TextField(blank=True, null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=50, verbose_name='Номер заказа')),
                ('paymentMethod', models.CharField(max_length=12, verbose_name='Способ оплаты')),
                ('shipMethod', models.CharField(max_length=50, verbose_name='Способ доставки')),
                ('currentPrice', models.FloatField(blank=True, null=True, verbose_name='Текущая цена')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата заказа')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='btest.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['date'],
            },
        ),
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['title'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveField(
            model_name='bb',
            name='price',
        ),
        migrations.RemoveField(
            model_name='bb',
            name='published',
        ),
        migrations.RemoveField(
            model_name='bb',
            name='rubric',
        ),
        migrations.AddField(
            model_name='bb',
            name='article',
            field=models.FloatField(blank=True, null=True, verbose_name='Артикул'),
        ),
        migrations.AddField(
            model_name='bb',
            name='basePrice',
            field=models.FloatField(blank=True, null=True, verbose_name='Базовая цена'),
        ),
        migrations.AddField(
            model_name='bb',
            name='capacity',
            field=models.FloatField(blank=True, null=True, verbose_name='Количество на складе'),
        ),
        migrations.AddField(
            model_name='bb',
            name='currentPrice',
            field=models.FloatField(blank=True, null=True, verbose_name='Текущая цена'),
        ),
        migrations.AddField(
            model_name='bb',
            name='description',
            field=models.CharField(max_length=50, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='bb',
            name='minCapacity',
            field=models.FloatField(blank=True, null=True, verbose_name='Мин. кол-во в заказе'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='Rubric',
        ),
        migrations.AddField(
            model_name='order',
            name='good',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='btest.bb', verbose_name='Товар'),
        ),
    ]
