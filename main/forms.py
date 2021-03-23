from .models import Obratnaya, Svoyamodel, Zakazmodel, Product
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput


class ObratnayaForm(ModelForm):
    class Meta:
        model = Obratnaya
        fields = ["name", "telefon", "opisanie", "temaobrash"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',

            }),
            "telefon": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш номер телефона',
                'value': "+7",

            }),
            "opisanie": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "temaobrash": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема обращения'
            })
        }


class SvoyaForm(ModelForm):

    class Meta:
        model = Svoyamodel
        fields = ["name", "telefon", "shirina", "visota", "glubina","opisanie", "chertej"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',

            }),
            "telefon": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш номер телефона',

            }),
            "shirina": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ширину мм',

            }),
            "visota": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите высоту мм',

            }),
            "glubina": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите глубину мм',

            }),
            "opisanie": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "chertej": ClearableFileInput(attrs={
                'class': 'form-control',
                'type': 'file'
            })

        }


class ZakazForm(ModelForm):

    class Meta:
        model = Zakazmodel
        fields = ["name", "telefon", "shirina", "visota", "glubina", "name_house"]
        widgets = {
            "name_house": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'

            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',

            }),
            "telefon": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш номер телефона',

            }),
            "shirina": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ширину мм',

            }),
            "visota": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите высоту мм',

            }),
            "glubina": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите глубину мм'

            })

        }