from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CreatePostForm, UpdatePostForm, CreateCateForm, UpdateCateForm
from django.urls import reverse_lazy, reverse
from django.views import View
from post import models, forms
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
# ================= POST ======================

class Posts(View):

    @staticmethod
    def get(request):
        lst_category = models.Category.objects.all()
        lst_post = models.Post.objects.all()
        # lst_post = models.Post .objects.filter(lst_category[])
        return render(request, 'MediCom/posts.html', {'list_cat': lst_category, 'list_p': lst_post})


class post_detail(View):
    def get(self, request, Post_Id):
        post = models.Post.objects.get(pk=Post_Id)
        lst_post_same = models.Post.objects.filter(category=post.category)
        lst_comment = models.Comment.objects.filter(post=post.id).order_by('-date')  # get list comment and sort them
        form = forms.CommentForm()

        stuff = get_object_or_404(models.Post, id=self.kwargs['Post_Id'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.users_like.filter(id=self.request.user.id).exists():
            liked = True

        # stuff_comment = get_object_or_404(models.Comment, id=request.POST.get('comment_id'))
        # liked_comment = False
        #
        # if stuff_comment.users_comment.filter(id=self.request.user.id).exists():

        liked_comment = []
        for item in lst_comment:
            if item.users_comment.filter(id=self.request.user.id).exists():
                liked_comment.append(False)

        context = {'form_comment': form, 'lst_post_same': lst_post_same, 'post': post, 'lst_comment': lst_comment,
                   'total_likes': total_likes, 'liked': liked, 'liked_comment': liked_comment}
        return render(request, 'MediCom/post_content_detail.html', context)

    @staticmethod
    def post(request, Post_Id, *args, **kwargs):
        if request.method == "POST":
            g = forms.CommentForm(request.POST)
            if g.is_valid():
                g.save()
                return HttpResponseRedirect(reverse('post_detail', args=[str(Post_Id)]))  # page previous
            elif request.POST["comment_id"]:
                comment = get_object_or_404(models.Comment, id=request.POST.get('comment_id'))
                comment.users_comment.add(request.user)
                return HttpResponseRedirect(reverse('post_detail', args=[str(comment.post.id)]))
            # elif request.POST["unlike_comment_id"]:
            #     comment = get_object_or_404(models.Comment, id=request.POST.get('unlike_comment_id'))
            #     if comment.users_comment.filter(id=request.user.id).exists():
            #         comment.users_comment.remove(request.user)
            #         return HttpResponseRedirect(reverse('post_detail', args=[str(comment.post.id)]))
            else:
                return HttpResponse("Invalid !!!")
        else:
            return render(request, 'MediCom/post_content_detail.html')
        # if request.method == "POST":
        #     g = forms.CommentForm(request.POST)
        #     if g.is_valid():
        #         g.save()
        #         return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # page previous
        #     else:
        #         return HttpResponse("Invalid !!!")
        # else:
        #     return render(request, 'MediCom/post_content_detail.html')


class SiteAddPost(LoginRequiredMixin, CreateView):
    model = models.Post
    template_name = 'MediCom/post_add.html'
    form_class = CreatePostForm


class SiteUpdatePost(LoginRequiredMixin, UpdateView):
    model = models.Post
    template_name = 'MediCom/post_update.html'
    form_class = UpdatePostForm
    # success_url = reverse_lazy('posts/<int:pk>')


class SiteDeletePost(LoginRequiredMixin, DeleteView):
    model = models.Post
    template_name = 'MediCom/post_delete.html'
    success_url = reverse_lazy('home')


def LikeView(request, pk):
    post = get_object_or_404(models.Post, id=request.POST.get('post_id'))  # get id của button có name là post_id
    liked = False
    if post.users_like.filter(id=request.user.id).exists():
        post.users_like.remove(request.user)
        liked = False
    else:
        post.users_like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))  # page previous


# def LikeCommentView(request, pk):
#     comment = get_object_or_404(models.Comment, id=request.POST.get('comment_id'))
#     liked = False
#     if comment.users_comment.filter(id=request.user.id).exists():
#         comment.users_comment.remove(request.user)
#         liked = False
#     else:
#         comment.users_comment.add(request.user)
#         liked = True
#     return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

# ================= CATEGORY======================


def Category_Detail(request, Category_Id):
    cat_id = models.Category.objects.get(id=Category_Id)
    lst_category = models.Category.objects.all()
    lst_post = models.Post.objects.filter(category=Category_Id)
    return render(request, 'MediCom/posts_category_detail.html',  {'cat_id': cat_id, 'list_p': lst_post, 'list_cat': lst_category})


class SiteAddCate(LoginRequiredMixin, CreateView):
    model = models.Category
    template_name = 'MediCom/category_add.html'
    form_class = CreateCateForm


class SiteUpdateCate(LoginRequiredMixin, UpdateView):
    model = models.Category
    template_name = 'MediCom/category_update.html'
    form_class = UpdateCateForm
    # success_url = reverse_lazy('category/<int:pk>')


class SiteDeleteCate(LoginRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'MediCom/category_delete.html'
    success_url = reverse_lazy('home')
