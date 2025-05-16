from django.shortcuts import render , redirect
from .models import Book
# Create your views here.
def create(request):
    if request.method == "POST":
        bname = request.POST.get('bname')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        genre = request.POST.get('genre')
        prize = request.POST.get('price')
        # print(bname,author,isbn,genre,prize)
        Book.objects.create(name = bname,isbn_number = isbn , author = author,genre = genre , prize = prize)
        print("added  successfully")
        return redirect("display")
    return render(request,'create.html')


def display(request):
    data = Book.objects.all()
    return render(request,'display.html',{'data':data})


def single(request , id):
    
    data = Book.objects.get(id = id)
    return render(request,"single.html",{'data':data})

def edit(request,pk):
    data = Book.objects.get(id = pk)
    if request.method == "POST":
        bname = request.POST.get('bname')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        genre = request.POST.get('genre')
        prize = request.POST.get('price')
        # print(bname,author,isbn,genre,prize)
        data.name = bname
        data.author = author 
        data.isbn_number = isbn
        data.genre = genre 
        data.prize = prize
        data.save()
        return redirect("display")


    return render(request,'update.html',{'data':data})


def delete(request , jk):
    data = Book.objects.get(id = jk)
    data.delete()
    return redirect("display")