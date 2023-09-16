# Generated by Django 4.2.5 on 2023-09-15 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.user'),
        ),
    ]