from django.core.mail import send_mail
from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.template.context_processors import csrf
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView
from .forms import EmailPostForm

from .models import Article, Comment, Books, Categories
from django.urls import reverse


# class IndexView(generic.ListView):
#     template_name = 'articles/list.html'
#     context_object_name = 'books_list'
#
#     def get_queryset(self):
#         return Books.objects.all()


class SearchResultsView(ListView):
    model = Books
    template_name = 'articles/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Books.objects.filter(Q(author_name__contains=query) | Q(books_name__contains=query))
        return object_list


def index(request):
    categories = Categories.objects.all()
    books_list = Books.objects.order_by('-books_name')[:30]
    top_book_list = Books.objects.order_by('-downloaded')[:15]
    bestsellers = Books.objects.filter(bestseller=True)
    total_down = Books.objects.get(books_name="Амир Темур").total_downloads
    print(total_down)
    # print(Books.objects.filter(books_name__in=bs_name[all(Bestsellers.bestseller_id.id)]))
    return render(request, 'articles/index.html', {'books_list': books_list,
                                                   'categories': categories,
                                                   'top_book_list': top_book_list,
                                                   'bestsellers': bestsellers,
                                                   'sum': total_down},
                  )


def base(request):
    categories = Categories.objects.all()
    return render(request, 'base.html', {'categories': categories})


def detail(request, category_id):
    categories = Categories.objects.all()
    category = Categories.objects.get(id=category_id)

    a = Books.objects.filter(category_id=category.id)
    # except Exception:
    #     raise Http404("Статья не найдена")
    return render(request, 'articles/detail.html', {'article': a, 'categories': categories, 'category': category})


def onClicks(request, book_id):
    b = Books.objects.update(total_downloads=F("total_downloads") + 1)
    a = Books.objects.filter(id=book_id).update(downloaded=F("downloaded") + 1)
    print(Books.objects.get(id=book_id).downloaded, Books.objects.get(id=book_id).books_name)
    return redirect('articles:index')


def onClicksCategory(request, category_id, book_id):
    c = Books.objects.update(total_downloads=F("total_downloads") + 1)
    b = Books.objects.filter(id=book_id).update(downloaded=F("downloaded") + 1)
    categories = Categories.objects.all()
    category = Categories.objects.get(id=category_id)

    a = Books.objects.filter(category_id=category.id)
    print(Books.objects.get(id=book_id).downloaded, Books.objects.get(id=book_id).books_name)
    return redirect('articles:detail', category_id)


def onClickSearch(request, book_id):
    c = Books.objects.update(total_downloads=F("total_downloads") + 1)
    b = Books.objects.filter(id=book_id).update(downloaded=F("downloaded") + 1)
    return redirect('articles:index')


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Exception:
        raise Http404("Статья не найдена")
    context = {}
    context.update(csrf(request))
    Comment.objects.create(
        article=a,
        author_name=request.POST.get('name'),
        comment_text=request.POST.get('text')
    )
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


def success(request):
    email = request.POST.get('email', '')
    name = request.POST.get('name', '')
    data = request.POST.get('message', '')
    send_mail(name, data + """ \n from : """ + email, 'humootahanov7@gmail.com',
              ['otahanovhumo@gmail.com'], fail_silently=False)
    return render(request, 'articles/list.html')
