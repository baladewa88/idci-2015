from django.shortcuts import render, get_object_or_404
from .models import Papers, Keywords, Citations
from django.utils import timezone

# Create your views here.

def index(request):
    paperList = Papers.objects.all()[:4]
    popularPaperList = Papers.objects.order_by('-ncites')[:5]
    return render(request, 'idciapp/index.html', {'paper':paperList, 'popular_paper':popularPaperList})

def paperdetail(request, pk):
    detailPaper = get_object_or_404(Papers,pk=pk)
    key = Keywords.objects.filter(paperid=pk).order_by('id')
    ref = Citations.objects.filter(paperid=pk).order_by('id')
    return render(request, 'idciapp/detail.html', {'paperdetail':detailPaper, 'keyword':key, 'ref':ref, 'inc':0})
