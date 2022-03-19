from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Author
from .forms import BookFormSet
# Create your views here.


def first_page(request):
    return HttpResponse("start")


def index(request, pk):
    author = Author.objects.get(pk=pk)
    bookform = BookFormSet(request.POST or None)

    if request.method == 'POST':
        if bookform.is_valid():
            bookform.instance = author
            bookform.save()
            return redirect('index', pk=author.id)

    context = {
        "bookform": bookform,
        "author": author
    }

    return render(request, 'book/index.html', context)
