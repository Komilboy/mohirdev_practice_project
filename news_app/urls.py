from django.urls import path
from .views import news_list, news_detail, homePageView, ContactPageView

urlpatterns = [
    path('', homePageView, name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
]