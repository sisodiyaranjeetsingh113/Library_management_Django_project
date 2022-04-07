from .models import Book
from BookService.forms import BookForm
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required

def base(req):
    
    return render(req,'base.html')
@login_required
def all_book(req):
   
    book=Book.objects.all()
    
    return render(req,'allbook.html',{'booklist':book})
@login_required
def create_book(req):
    
    form=BookForm(req.POST or None)
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        return render(req,"createbook.html",{'form':form})
@login_required
def update_book(req,id):
    
    book=Book.objects.get(id=id)
    form = BookForm(req.POST or None, instance = book)
 
    if form.is_valid():
        form.save()
        return redirect("/accounts/profile/")
    else:
        return render(req,"updatebook.html",{'form':form})
@login_required
def delete_book(req,id):
    
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('/accounts/profile/')


