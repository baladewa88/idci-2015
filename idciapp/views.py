from django.shortcuts import render
from .models import Papers
from django.utils import timezone

# Create your views here.

def index(request):
    paperList = Papers.objects.all()[:5]
    popularPaperList = Papers.objects.order_by('-ncites')[:5]
    return render(request, 'idciapp/index.html', {'paper':paperList, 'popular_paper':popularPaperList})

def popularPaper(request):
    popularPaperList = Papers.objects.order_by('ncites')[:5]
    return render(request, 'idciapp/index.html', {'popular_paper':popularPaperList})
