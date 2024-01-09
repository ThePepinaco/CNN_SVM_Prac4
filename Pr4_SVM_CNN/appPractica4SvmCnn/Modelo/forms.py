# En forms.py
from django import forms

class ImagenForm(forms.Form):
    imagen = forms.ImageField()
    opcion = forms.ChoiceField(choices=(('svm', 'SVM'), ('cnn', 'CNN')), widget=forms.RadioSelect)

