import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import  gettext_lazy as  _

def validaCPF(cpf):
    cpf = str(cpf)
    cpf = re.sub('[^0-9]', '', cpf)
    cpf.split()
    cpf = cpf.rjust(11, '0')
    soma = 0
    val = True

    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        val = False

    for i in range (9):
        soma += int(cpf[i]) * (10 - i)
    resto = (soma * 10) % 11

    if resto == 10 or resto == 11:  resto = 0;
    if resto != int(cpf[9]): val = False

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = (soma * 10) % 11

    if resto == 10 or resto == 11:  resto = 0;
    print(resto, cpf[10])
    if resto != int(cpf[10]): val = False

    if not val:
        raise ValidationError(
            _('CPF Inválido')
)
class Base(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True,
                                        db_column='t_____criacao',
                                        db_comment='Data de Inclusão do Objeto')
    data_atualizacao = models.DateTimeField(auto_now=True,
                                        db_column='t_____ulat',
                                        db_comment='Data de Atualização do Objeto')
    ativo = models.BooleanField(default=True,
                                db_column= 'f_____ativo',
                                db_comment='Indicador se objeto ainda está ativo')

    class Meta:
        abstract= True

class CursoTrilha(Base):
    id=models.BigAutoField(primary_key=True,
                           db_column='ccurtrsequencial',
                           db_comment='Chave da tabela tbcursotrilha')
    id_curso = models.ForeignKey('Curso', on_delete=models.RESTRICT,
                                 db_column='ccursosequencial',
                                 db_comment='Chave de ligação com a tabela tbcurso'
                                 )
    id_trilha = models.ForeignKey('Trilha', on_delete=models.RESTRICT,
                                db_column='ctrilhasequencial',
                                db_comment='Chave de ligação com a tabela tbtrilha'
                                )

    class Meta:
        verbose_name = 'Curso Trilha'
        verbose_name_plural = 'Cursos Trilhas'
        unique_together = ('id_trilha', 'id_curso')
        db_table = "tbcursotrilha"
        indexes = (models.Index(fields=['id'], name='pcurtrchave'),
                   models.Index(fields=['id_trilha', 'id_curso'], name='ucurtrchave'),
                   models.Index(fields=['id_trilha'], name='icurtridtrilha'),
                   models.Index(fields=['id_curso'], name='icurtridcurso'),
                   )

    def __str__(self):
        return 'Trilha: ' + str(self.id_trilha) + ', Curso: ' + str(self.id_curso)


class Trilha(Base):
    id = models.BigAutoField(primary_key=True,
                            db_column='ctrilhsequencial',
                            db_comment='Chave da tabela tbtrilha')
    nome = models.CharField(max_length=50, unique=True,
                            blank=False, null=False,
                            db_column='ntrilhnome',
                            db_comment='Nome da trilha')
    valor_trilha = models.DecimalField(max_digits=9,decimal_places=2,
                                       db_column='vtrilhpreco',
                                       db_comment='Valor da trilha'
                                       )
    descricao = models.TextField(db_column='etrilhdescricao',
                                 db_comment='Descrição da trilha'
                                 )
    publico_alvo = models.TextField(db_column='etrilhpublico',
                                 db_comment='Público alvo da trilha'
                                 )
    carga_horaria = models.IntegerField(db_column='atrilhcarga', db_comment='Carga horaria da trilha'
                                        )

    class Meta:
        verbose_name = 'Trilha'
        verbose_name_plural = 'Trilhas'
        db_table = 'tbtrilha'
        indexes = [models.Index(fields=['id'], name='ptrilhchave'),
                   models.Index(fields=['nome'], name='utrilhnome'),
                   ]

    def __str__(self):
        return self.nome

class Curso(Base):
    id = models.BigAutoField(primary_key=True,
                            db_column='ccursosequencial',
                            db_comment='Chave da tabela tbcurso')
    nome = models.CharField(max_length=50, unique=True,
                            blank=False, null=False,
                            db_column='ncursonome',
                            db_comment='Nome do curso')
    valor = models.DecimalField(max_digits=9,decimal_places=2,
                                       db_column='vcursopreco',
                                       db_comment='Valor do curso'
                                       )
    descricao = models.TextField(db_column='ecursodescricao',
                                 db_comment='Descrição do curso'
                                 )
    publico_alvo = models.TextField(db_column='ecursopublico',
                                 db_comment='Público alvo do curso'
                                 )
    carga_horaria = models.IntegerField(db_column='acursocarga',
                                 db_comment='Carga horaria do curso'
                                        )

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        db_table = 'tbcurso'
        indexes = [models.Index(fields=['id'], name='pcursochave'),
                   models.Index(fields=['nome'], name='ucursonome'),
                   ]

    def __str__(self):
        return self.nome

class Turma(Base):
    TURNO_CHOICE = (
        ('M','Manhã'),
        ('T','Tarde'),
        ('V','Vespertino'),
        ('N','Noite'),
        ('I','Integral'),
    )
    id = models.BigAutoField(primary_key=True, db_column='cturmasequencial', db_comment='Identificador do Curso')
    id_curso = models.ForeignKey('Curso', on_delete=models.RESTRICT, db_column='ccursosequencial',
                                 related_name='curso_participa_turma', blank=False, null=False)
    professor = models.CharField( max_length=50, blank=False, null=False, db_column='nturmaprofessor',
                            db_comment='Nome do Professor')
    turno = models.CharField(max_length=1, blank=False, null=False, db_column='cturmaturno',
                            db_comment='Turno da Turma', choices=TURNO_CHOICE)
    seg = models.BooleanField(default=False, db_column='fturmasegunda',
                              db_comment='Indicador se acontece nas segundas feiras')
    ter = models.BooleanField(default=False, db_column='fturmaterca',
                              db_comment='Indicador se acontece nas terças feiras')
    qua = models.BooleanField(default=False, db_column='fturmaquarta',
                              db_comment='Indicador se acontece nas quartas feiras')
    qui = models.BooleanField(default=False, db_column='fturmaquinta',
                              db_comment='Indicador se acontece nas quintas feiras')
    sex = models.BooleanField(default=False, db_column='fturmasexta',
                              db_comment='Indicador se acontece nas sextas feiras')
    sab = models.BooleanField(default=False, db_column='fturmasabado',
                              db_comment='Indicador se acontece nos sábados')
    inicio = models.DateField(blank=False, null=False, db_column='dturmainicio',
                                    db_comment='Data do início da turma')
    final = models.DateField(blank=False, null=False, db_column='dturmafinal',
                                  db_comment='Data do final da turma')
    horario = models.CharField(blank=False, null=False, db_column='eturmahorario',
                                        db_comment='Horário da turma', max_length=13)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        db_table = 'tbturma'
        indexes = [models.Index(fields=['id'], name='pturmachave'),
                   models.Index(fields=['id_curso'], name='fturmacurso'),
                   ]

    def _str_(self):
        return 'Curso: ' + str(self.id_curso) + 'Início: ' + str(self.inicio)

class Aluno(Base):
    cpf = models.CharField(max_length=14, primary_key=True,
                           db_column='calunochave',
                           db_comment='CPF do aluno',
                           verbose_name='CPF',
                           validators=[validaCPF]
                           )
    nome = models.CharField(blank=False, null=False, max_length=100,
                            db_column='nalunonome',
                            db_comment='Nome do aluno',
                            verbose_name='Nome'
                            )
    nome_social = models.CharField(blank=True, null=True,
                                   max_length=100,
                                   db_column='nalunosocial',
                                   db_comment='Nome Social do aluno',
                                   verbose_name='Nome Social'
                                   )
    data_nascimento = models.DateField(blank=False, null=False,
                                       db_column='dalunonascimento',
                                       db_comment='Data de Nascimento',
                                       verbose_name='Data Nascimento'
                                       )

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        db_table = 'tbaluno'
        indexes = [models.Index(fields=['cpf'], name='palunochave'),
                   models.Index(fields=['nome'], name='ialunonome'),
                   ]