# Generated by Django 4.2.5 on 2023-09-16 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_test.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_test.profile')),
            ],
        ),
    ]