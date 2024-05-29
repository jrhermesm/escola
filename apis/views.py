from django.db.migrations import serializer
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import render

def index (request):
    contex = {'dados':'Apis para o curso Django'}
    return render(request,'index.html',contex)

class CursoApiView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AlunoApiView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoTrilhaApiView(generics.ListCreateAPIView):
    queryset = CursoTrilha.objects.all()
    serializer_class = CursoTrilhaSerializer


class TrilhaApiView(generics.ListCreateAPIView):
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer


class TurmaApiView(generics.ListCreateAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer


