from .models import *
from django.forms import CheckboxInput, EmailInput, ModelForm, NumberInput, Select, TextInput, Textarea


class AccForm(ModelForm):
    class Meta:
        model = Accounts
        fields = ["first_name", "second_name", "phonenumber", "email", "role", "age", "corp", "flag", "choice"]
        widgets = {

            "first_name": TextInput(attrs={
                'class': 'form__value',
                'placeholder': 'Введите фамилию',

            }),

            "second_name": TextInput(attrs={
                'class': 'form__value',
                'placeholder': 'Введите имя'

            }),

            "email": EmailInput(attrs={
                'class': 'form__value',
                'placeholder': 'Введите email',

            }),

            "phonenumber": TextInput(attrs={
                'class': 'form__value',
                'placeholder': 'Введите номер'

            }),

            "age": NumberInput(attrs={
                'class': 'form__value',
                'placeholder': 'Введите возраст (от 14 до 100)'

            }),

            "corp": TextInput(attrs={
                'class': 'form__value',
                'placeholder': 'Введите название университета или организации или если самостоятельно'

            }),

            "role": Textarea(attrs={
                'class': 'form__value',
                'placeholder': 'Опишите свою роль в команде'

            }),
            "flag": CheckboxInput(attrs={
                'class': 'form__value',
            }),

            "choice": Select(attrs={
                'class': 'form__value',
            }),

        }
