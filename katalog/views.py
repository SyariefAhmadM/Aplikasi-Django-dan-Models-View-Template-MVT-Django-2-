from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def show_katalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_catalog': data_katalog_item,
        'nama': 'mas Syarief',
        'npm': '2106653445'
    }
    return render(request, "katalog.html", context)
