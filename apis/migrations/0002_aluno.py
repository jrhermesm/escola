# Generated by Django 4.2.11 on 2024-05-27 22:24

import apis.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Aluno",
            fields=[
                (
                    "data_criacao",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_column="t_____criacao",
                        db_comment="Data de Inclusão do Objeto",
                    ),
                ),
                (
                    "data_atualizacao",
                    models.DateTimeField(
                        auto_now=True,
                        db_column="t_____ulat",
                        db_comment="Data de Atualização do Objeto",
                    ),
                ),
                (
                    "ativo",
                    models.BooleanField(
                        db_column="f_____ativo",
                        db_comment="Indicador se objeto ainda está ativo",
                        default=True,
                    ),
                ),
                (
                    "cpf",
                    models.CharField(
                        db_column="calunochave",
                        db_comment="CPF do aluno",
                        max_length=14,
                        primary_key=True,
                        serialize=False,
                        validators=[apis.models.validaCPF],
                        verbose_name="CPF",
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        db_column="nalunonome",
                        db_comment="Nome do aluno",
                        max_length=100,
                        verbose_name="Nome",
                    ),
                ),
                (
                    "nome_social",
                    models.CharField(
                        blank=True,
                        db_column="nalunosocial",
                        db_comment="Nome Social do aluno",
                        max_length=100,
                        null=True,
                        verbose_name="Nome Social",
                    ),
                ),
                (
                    "data_nascimento",
                    models.DateField(
                        db_column="dalunonascimento",
                        db_comment="Data de Nascimento",
                        verbose_name="Data Nascimento",
                    ),
                ),
            ],
            options={
                "verbose_name": "Aluno",
                "verbose_name_plural": "Alunos",
                "db_table": "tbaluno",
                "indexes": [
                    models.Index(fields=["cpf"], name="palunochave"),
                    models.Index(fields=["nome"], name="ialunonome"),
                ],
            },
        ),
    ]