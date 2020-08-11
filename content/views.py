from django.shortcuts import render
from .models import RealStateArticle
from .models import RealStateNews
from .forms import ModalForm

# Create your views here.
def index(request):
    return render(request, 'content/index.html')


def view_articles(request):
    """
        View Articles View
    """
    # getting all data here
    querysets = RealStateArticle.objects.all()

    if 'author_name' in request.GET and 'date' in request.GET:
        author_name = request.GET.get('author_name')
        date_ = request.GET.get('date')

        if author_name:
            querysets = querysets.filter(author__contains=author_name).all()
        if date_:
            querysets = querysets.filter(date=date_).all()
    
    context = {
        "querysets" : querysets,
        'content_type' : 'Articles',
        'form' : ModalForm()
    }
    
    return render(request, 'content/view_data.html', context)


def view_news(request):
    """
        View News View
    """

    # getting all data here
    querysets = RealStateNews.objects.all()

    if 'author_name' in request.GET and 'date' in request.GET:
        author_name = request.GET.get('author_name')
        date_ = request.GET.get('date')

        if author_name:
            querysets = querysets.filter(author=author_name).all()
        if date_:
            querysets = querysets.filter(date=date_).all()
    
    context = {
        'querysets' : querysets,
        'content_type' : 'News',
        'form' : ModalForm()
    }
    return render(request, 'content/view_data.html', context)