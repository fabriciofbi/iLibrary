from rest_framework import serializers
from .models import Alunos, Livros, Categorias, Autores, Editoras

class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = '__all__'

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class EditorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editoras
        fields = '__all__'

class AutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = '__all__'

class LivrosSerializer(serializers.ModelSerializer):
    categoria = CategoriasSerializer(read_only=True)
    autor = AutoresSerializer(many=True, read_only=True)
    editora = EditorasSerializer(read_only=True)

    class Meta:
        model = Livros
        fields = '__all__'
