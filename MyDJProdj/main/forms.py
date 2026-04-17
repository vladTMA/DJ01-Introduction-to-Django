# main/forms.py
from django import forms
from .models import Article, Book
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser


class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Введите email"
        })
    )

    phone_number = forms.CharField(
        label="Номер телефона",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Необязательно"
        })
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Введите пароль"
        })
    )

    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Повторите пароль"
        })
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя пользователя"
            }),
        }


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "subtitle", "content", "author", "is_published"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "subtitle": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", 'author', "description", "review"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "review": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }