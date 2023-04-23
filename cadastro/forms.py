from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, min_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, min_length=5, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    assunto = forms.CharField(label='Assunto', max_length=100, min_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class': 'form-control'}))


