from django import forms
from .models import Comment, Post, Category
from django.db import models

#================= COMMENT ======================


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'post', 'author']
        widgets = {
            'content': forms.TextInput(attrs={"class": "form-control"}),
            'post': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'post_id', 'type': 'hidden'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
        }



#================= POST ======================


class CreatePostForm(forms.ModelForm):
    img_main = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'author', 'description', 'img_main', 'category', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class UpdatePostForm(forms.ModelForm):
    img_main = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'description', 'img_main', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

#================= CATEGORY======================


class CreateCateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UpdateCateForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
