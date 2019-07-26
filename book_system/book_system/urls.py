"""book_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from app01 import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'show_book/',views.show_book,name='book_list'),
    url(r'add_book/' , views.add_book,name='book_add'),
    url(r'edit_book/(\d+)/', views.edit_book, name='book_edit'),
    url(r'delete_book/(\d+)/', views.delete_book,name='book_delete'),
    url(r'show_author/', views.show_author,name='show_author'),
    url(r'author_edit/(\d+)/', views.author_edit, name='author_edit'),
    url(r'author_delete/(\d+)/', views.author_delete, name='author_delete'),
    url(r'author_add/',views.author_add, name='author_add'),
]
