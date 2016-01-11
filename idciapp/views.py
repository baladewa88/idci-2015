from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Papers, Authors, Keywords, Citations, Urls
from django.utils import timezone
from .forms import PaperForm, PaperSearch,AuthorSearch,PublisherSearch
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain

# Create your views here.

def index(request):
    formd = PaperSearch()
    aform = AuthorSearch()
    pform = PublisherSearch()
    paperList = Papers.ea.order_by('-crawldate')[:5]
    popularPaperList = Papers.ea.order_by('-ncites')[:5]
    return render(request, 'idciapp/index.html', {'paper':paperList, 'popular_paper':popularPaperList, 'tform':formd, 'aform':aform, 'pform':pform})

def paperdetail(request, pk, judul):
    detailPaper = get_object_or_404(Papers,pk=pk)
    key = Keywords.objects.filter(paperid=pk).order_by('id')
    ref = Citations.objects.filter(paperid=pk).order_by('id')
    author = Authors.objects.filter(paperid=pk).order_by('id')
    citedd = Citations.objects.filter(title=judul).order_by('id')

    for c in citedd:
        cited = Papers.ea.filter(id=c.paperid).order_by('id')
                                                             
    for a in key:
        cite = Papers.ea.filter(title__icontains=a.keyword).order_by('id')
            
    dl = Urls.objects.get(paperid=pk)
    return render(request, 'idciapp/detail.html', {'paperdetail': detailPaper, 'keyword':key, 'ref':ref, 'author':author, 'title':cite, 'cited':citedd, 'url':dl})

def about (request):
    return render(request, 'idciapp/about.html', {})

def search (request):
    formw = PaperForm()
    return render(request, 'idciapp/adsearch.html', {'forme':formw})

def titlesearch (request):
    form = PaperSearch(request.GET)
    paperLists = Papers.ea.filter(title__icontains=form['title'].value())
    paginator = Paginator(paperLists, 5)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('idciapp/title.html', {"list": contacts})

    #return render(request, 'idciapp/title.html', {'list':paperLists})
    #return render(request, 'idciapp/title.html', {})

def authorsearch (request):
    aform = AuthorSearch(request.GET)
    author = Authors.objects.filter(name__icontains=aform['name'].value())[:15]
    return render(request, 'idciapp/author.html', {'author':author})

def publishersearch (request):
    pform = PublisherSearch(request.GET)
    publisher = Papers.ea.filter(publisher__icontains=pform['publisher'].value())[:15]
    return render(request, 'idciapp/publisher.html', {'publisher':publisher})
