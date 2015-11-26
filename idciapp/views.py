from django.shortcuts import render, get_object_or_404
from .models import Papers, Authors, Keywords, Citations
from django.utils import timezone
from .forms import PaperForm, PaperSearch

# Create your views here.

def index(request):
    formd = PaperSearch()
    paperList = Papers.objects.all()[:4]
    popularPaperList = Papers.objects.order_by('-ncites')[:5]
    return render(request, 'idciapp/index.html', {'paper':paperList, 'popular_paper':popularPaperList, 'form':formd})

def paperdetail(request, pk):
    detailPaper = get_object_or_404(Papers,pk=pk)
    key = Keywords.objects.filter(paperid=pk).order_by('id')
    ref = Citations.objects.filter(paperid=pk).order_by('id')
    author = Authors.objects.filter(paperid=pk).order_by('id')
    return render(request, 'idciapp/detail.html', {'paperdetail':detailPaper, 'keyword':key, 'ref':ref, 'author':author})

def about (request):
    return render(request, 'idciapp/about.html', {})

def search (request):
    form = PaperForm()
    return render(request, 'idciapp/adsearch.html', {'form':form})

def titlesearch (request):
    return render(request, 'search/search.html', {})
