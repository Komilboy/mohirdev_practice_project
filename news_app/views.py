from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import News, Category
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)
# Create your views here.
def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }

    return render(request, 'news/news_detail.html', context)


def homePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:5]
    local_one = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[:1]
    local_news = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]
    xorij_xabarlari = News.published.all().filter(category__name='Xorij').order_by('-publish_time')[1:6]
    sport_xabarlari = News.published.all().filter(category__name='Sport').order_by('-publish_time')[1:6]
    texnologiya_xabarlari = News.published.all().filter(category__name='Texnologiya').order_by('-publish_time')[1:6]


    context = {
        'news_list': news_list,
        'categories': categories,
        'local_one': local_one,
        'local_news': local_news,
        'xorij_xabarlari': xorij_xabarlari,
        'sport_xabarlari': sport_xabarlari,
        'texnologiya_xabarlari': texnologiya_xabarlari,
    }

    return render(request, 'news/home.html', context)


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog`langaningiz uchun tashakkur </h2>")
        context = {
            "form": form
        }

        return render(request, 'news/contact.html', context)