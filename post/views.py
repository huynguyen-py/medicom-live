from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CreatePostForm, UpdatePostForm, CreateCateForm, UpdateCateForm
from django.urls import reverse_lazy
from django.views import View
from post import models, forms
# Create your views here.

#================= POST ======================


class Posts(View):
    def get(self, request):
        lst_category = models.Category.objects.all()
        lst_post = models.Post.objects.all()
        return render(request, 'Medicom/posts.html', {'list_cat': lst_category, 'list_p': lst_post})


def Post_Detail(request, Post_Id):
    post = models.Post.objects.get(id=Post_Id)
    # lst_content = models.Content.objects.filter(post_id=Post_Id)
    lst_post_same = models.Post.objects.filter(category=post.category)
    form = forms.CommentForm()
    context = {'form_comment': form, 'lst_post_same': lst_post_same, 'post': post}
    return render(request, 'Medicom/post_content_detail.html', context)


class SiteAddPost(LoginRequiredMixin, CreateView):
    model = models.Post
    template_name = 'MediCom/post_add.html'
    form_class = CreatePostForm


class SiteUpdatePost(LoginRequiredMixin, UpdateView):
    model = models.Post
    template_name = 'Medicom/post_update.html'
    form_class = UpdatePostForm
    #success_url = reverse_lazy('posts/<int:pk>')


class SiteDeletePost(LoginRequiredMixin, DeleteView):
    model = models.Post
    template_name = 'Medicom/post_delete.html'
    success_url = reverse_lazy('home')

#================= CATEGORY======================


def Category_Detail(request, Category_Id):
    cat_id = models.Category.objects.get(id=Category_Id)
    lst_category = models.Category.objects.all()
    lst_post = models.Post.objects.filter(category=Category_Id)
    return render(request, 'Medicom/posts_category_detail.html',  {'cat_id': cat_id, 'list_p': lst_post, 'list_cat': lst_category})


class SiteAddCate(LoginRequiredMixin, CreateView):
    model = models.Category
    template_name = 'MediCom/category_add.html'
    form_class = CreateCateForm


class SiteUpdateCate(LoginRequiredMixin, UpdateView):
    model = models.Category
    template_name = 'Medicom/category_update.html'
    form_class = UpdateCateForm
    #success_url = reverse_lazy('category/<int:pk>')


class SiteDeleteCate(LoginRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'Medicom/category_delete.html'
    success_url = reverse_lazy('home')
