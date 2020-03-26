# Generated by Django 2.2.10 on 2020-03-27 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helios', '0006_election_deploy_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='election',
            old_name='questions_added_to_contract',
            new_name='no_questions_added_to_contract',
        ),
        migrations.CreateModel(
            name='QuestionBlockchain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_question', models.IntegerField()),
                ('transaction_hash', models.CharField(max_length=100, null=True)),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helios.Election')),
            ],
        ),
    ]
