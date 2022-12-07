from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from msilib.schema import Shortcut
from urllib import request
from django.shortcuts import render
from .models import Post
from marketing.models import Signup

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(tittle__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)



def index(request):
    # most_recent = post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = Paginator.page(Paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var
    }

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()


    return render(request, 'index.html', context)

def about(request):
            return render(request, 'about.html', {})
def book(request):
            return render(request, 'book.html', {})
def menu(request):
            return render(request, 'menu.html', {})