from django.shortcuts import render, redirect
from django.views import View
from post import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class Landing_Page(View):
    def get(self, request):
        return render(request, 'MediCom/index.html')


class Home(View):
    def get(self, request):
        # lst_post = models.Post.objects.filter(date__month= 9)
        lst_category = models.Category.objects.all()

        lst_post = models.Post.objects.all().order_by('-date')# get list Post and sort them
        paginator = Paginator(lst_post, 3)  # Show 3 contacts mỗi page
        page_number = request.GET.get("page_number")

        try:
            posts = paginator.page(page_number)
        except PageNotAnInteger:
            # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
            posts = paginator.page(1)
        except EmptyPage:
            # Nếu page không có item nào, trả về page cuối cùng
            posts = paginator.page(paginator.num_pages)

        return render(request, 'MediCom/home_index.html', {'posts': posts, 'list_cat': lst_category})


class Diagnosis(View):
    def get(self, request):
        return render(request, 'MediCom/Diagnosis.html')
