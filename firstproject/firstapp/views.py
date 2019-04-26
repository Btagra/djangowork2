from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'header': 'This is the image of flower!'}
    return render(request, 'index.html', context=my_dict)

def detail(request):
    context = {'detail': 'This is the detail view!-----A flower, sometimes known as a bloom or blossom, is the reproductive structure found in flowering plants.'}
    return render(request, 'index.html', context)
