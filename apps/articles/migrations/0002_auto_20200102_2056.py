# Generated by Django 2.2.5 on 2020-01-02 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, verbose_name='название категория')),
            ],
            options={
                'verbose_name': 'Категорий',
                'verbose_name_plural': 'Катерогии',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books_name', models.CharField(max_length=200, verbose_name='название книги')),
                ('author_name', models.CharField(max_length=200, verbose_name='имя автора')),
                ('image_url', models.CharField(max_length=300, verbose_name='ссылка картинки')),
                ('book_url', models.CharField(max_length=300, verbose_name='ссылка книги')),
                ('qr_book_url', models.CharField(max_length=300, verbose_name='ссылка qr')),
                ('pub_date', models.DateTimeField(verbose_name='дата публикации')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Categories')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]