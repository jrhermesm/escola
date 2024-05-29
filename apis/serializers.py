from rest_framework import serializers
from .models import *


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        read_only_fields = ['ativo']


class CursoTrilhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoTrilha
        fields = '__all__'
        read_only_fields = ['ativo']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        read_only_fields = ['ativo']


class TrilhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trilha
        fields = '__all__'
        read_only_fields = ['ativo']


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
        read_only_fields = ['ativo']