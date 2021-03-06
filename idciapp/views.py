from dal import autocomplete

from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Papers, Authors, Keywords, Citations, Urls, Affiliations
from django.utils import timezone
from .forms import PaperForm, PaperSearch,AuthorSearch,PublisherSearch, PaperFilter
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
    cite = ""
    
    for c in citedd:
        cited = Papers.ea.filter(id=c.paperid).order_by('id')
                                                             
    for a in key:
        cite = Papers.ea.filter(title__icontains=a.keyword).order_by('id')
            
    dl = Urls.objects.get(paperid=pk)
    return render(request, 'idciapp/detail.html', {'paperdetail': detailPaper, 'keyword':key, 'ref':ref, 'author':author, 'title':cite, 'cited':citedd, 'url':dl})

def paperlist(request):
    
    f = PaperFilter(request.GET, queryset=Papers.ea.all())
    return render_to_response('idciapp/title.html', {'filter': f})

def authorlist(request, nama):
    author = Authors.objects.filter(name=nama).order_by('id')
                                         
    for a in author:
        print ("paperid based on author > "+str(a.paperid))
        cite = Papers.ea.filter(title=a.paperid)

    return render(request, 'idciapp/authorlist.html', {'lists': cite})

def afflist(request, nama):
    aff = Affiliations.objects.filter(name=nama).order_by('ndocs')
                                         
    for a in aff:
        affs = Papers.ea.filter(affiliasi=a.id)

    return render(request, 'idciapp/publisherlist.html', {'lists': cite})

def about (request):
    return render(request, 'idciapp/about.html', {})

def search (request):
    formw = PaperForm()
    return render(request, 'idciapp/adsearch.html', {'forme':formw})

def titlesearch (request):
    form = PaperSearch(request.GET)
    paperLists = Papers.ea.filter(title__icontains=form['title'].value())
    f = PaperFilter(request.GET, queryset=Papers.ea.filter(title__icontains=form['title'].value()))
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

    return render_to_response('idciapp/title.html', {"filter": contacts, "form":form, "fd":f})

    #return render(request, 'idciapp/title.html', {'list':paperLists})
    #return render(request, 'idciapp/title.html', {})

def authorsearch (request):
    aform = AuthorSearch(request.GET)
    author = Authors.objects.filter(name__icontains=aform['name'].value())[:15]

    for a in author:
        pap = Authors.objects.filter(name=a.name).count()
        
    return render(request, 'idciapp/author.html', {'author':author, 'pap':pap, "form":aform})

def publishersearch (request):
    pform = PublisherSearch(request.GET)
    publisher = Affiliations.objects.filter(name__icontains=pform['name'].value())[:15]
    return render(request, 'idciapp/publisher.html', {'publisher':publisher, "form":pform})

class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Papers.ea.none()

        qs = Papers.ea.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs
