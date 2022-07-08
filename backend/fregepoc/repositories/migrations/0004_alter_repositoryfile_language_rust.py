# Generated by Django 4.0.5 on 2022-06-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0003_alter_repositoryfile_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositoryfile',
            name='language',
            field=models.CharField(
                choices=[('Python', 'Python'), ('C', 'C'), ('C++', 'Cpp'), ('C#', 'C Sharp'), ('CSS', 'Css'), ('Java', 'Java'),
                         ('JS', 'Js'), ('PHP', 'Php'), ('Ruby', 'Ruby'), ('Kotlin', 'Kotlin'), ('Rust', 'Rust')],
                help_text='Programming language present in the repository.',
                max_length=20,
                verbose_name='programming language'),
        ),
    ]