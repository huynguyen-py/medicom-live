from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from post import models, forms
from django.utils import timezone
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView
from post.forms import CreatePostForm
# Create your views here.


class Home(View):

    def get(self, request):
        lst_post = models.Post.objects.filter(date__month= 8)
        lst_category = models.Category.objects.all()
        return render(request, 'MediCom/index.html', {'list_p': lst_post, 'list_cat': lst_category})


