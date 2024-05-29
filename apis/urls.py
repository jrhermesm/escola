from django.urls import path
from .views import *

urlpatterns = [
    path('cursos/', CursoApiView.as_view(), name='curso'),
    path('alunos/', AlunoApiView.as_view(), name='aluno'),
    path('cursotrilha/', CursoTrilhaApiView.as_view(), name='cursotrilha'),
    path('trilhas/', TrilhaApiView.as_view(), name='trilha'),
    path('turmas/', TurmaApiView.as_view(), name='turma'),
    path('',index),
]

