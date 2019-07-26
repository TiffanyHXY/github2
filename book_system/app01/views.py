from django.shortcuts import render,redirect,reverse,HttpResponse

# Create your views here.

from app01 import models

def home(request):
    return render(request, 'home.html')

def show_book(request):
    book_list = models.Book.objects.all()
    return render(request, 'show_book.html', locals())


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('date')
        publish_id = request.POST.get('publish')
        authors = request.POST.getlist('authors')
        book_obj = models.Book.objects.create(title=title, price=price,publish_time=publish_date, publish_id=publish_id)
        book_obj.authors.add(*authors)
        return redirect(reverse('book_list'))
    publish_list = models.Publish.objects.all()
    author_list = models.Author.objects.all()
    print(author_list)
    return render(request, 'add_book.html', locals())


def edit_book(request, edit_id):
    edit_obj = models.Book.objects.filter(pk=edit_id).first()
    if request.method == 'POST':
        # print(request.POST)
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish_date = request.POST.get("date")
        publish_id = request.POST.get("publish")
        authors = request.POST.getlist("authors")
        models.Book.objects.filter(pk=edit_id).update(title=title, price=price, publish_time=publish_date,
                                                      publish_id=publish_id)
        edit_obj.authors.set(authors)
        return redirect(reverse('book_list'))
    publish_list = models.Publish.objects.all()
    author_list = models.Author.objects.all()
    return render(request, 'edit.html', locals())


def delete_book(request, delete_id):
    models.Book.objects.filter(pk=delete_id).delete()
    return redirect(reverse('book_list'))

def show_author(request):
    author_list = models.Author.objects.all()
    return render(request, 'show_authors.html',locals())

def author_edit(request ,edit_id):
    edit_obj = models.Author.objects.filter(pk=edit_id).first()
    if request.method == 'POST':
        # print(request.POST)
        name = request.POST.get("name")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        addr = request.POST.get("addr")
        models.AuthorDetail.objects.filter(pk=edit_obj.authordetail_id).update(phone=phone,addr=addr)
        models.Author.objects.filter(pk=edit_id).update(name=name, age=age,authordetail_id=edit_obj.authordetail_id)
        return redirect(reverse('show_author'))
    return render(request, 'edit_author.html', locals())


def author_delete(request,delete_id):
    models.Author.objects.filter(pk=delete_id).delete()
    return redirect(reverse('show_author'))


def author_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        age = request.POST.get('age')
        phone = request.POST.get('phone')
        addr = request.POST.get('addr')

        detail_obj = models.AuthorDetail.objects.create(phone=phone,addr=addr)

        models.Author.objects.create(name=name,age=age,authordetail=detail_obj)
        return redirect(reverse('show_author'))
    return render(request, 'add_author.html')

