from django.shortcuts import render, get_object_or_404
from .models import Papers, Authors, Keywords, Citations
from django.utils import timezone
from .forms import PaperForm, PaperSearch

# Create your views here.

def index(request):
    formd = PaperSearch()
    paperList = Papers.row.order_by('-crawldate')[:5]
    popularPaperList = Papers.row.order_by('-ncites')[:5]
    return render(request, 'idciapp/index.html', {'paper':paperList, 'popular_paper':popularPaperList, 'form':formd})

def paperdetail(request, pk, judul):
    detailPaper = get_object_or_404(Papers,pk=pk)
    key = Keywords.objects.filter(paperid=pk).order_by('id')
    ref = Citations.objects.filter(paperid=pk).order_by('id')
    author = Authors.objects.filter(paperid=pk).order_by('id')
    cite = Citations.objects.filter(title=judul).order_by('id')

    return render(request, 'idciapp/detail.html', {'paperdetail':detailPaper, 'keyword':key, 'ref':ref, 'author':author, 'title':cite})

def about (request):
    return render(request, 'idciapp/about.html', {})

def search (request):
    form = PaperForm()
    return render(request, 'idciapp/adsearch.html', {'form':form})

def titlesearch (request):
    return render(request, 'search/search.html', {})
