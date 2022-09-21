from multiprocessing import context
from operator import truediv
from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = WatchList.objects.all()

    jumlah_sudah_ditonton = 0
    jumlah_belum_ditonton = 0
    pesan = ""
    for x in data_mywatchlist:
        if x.watched == True:
            jumlah_sudah_ditonton+=1
        else :
            jumlah_belum_ditonton+=1
    if jumlah_sudah_ditonton >= jumlah_belum_ditonton :
        pesan = ("Selamat, kamu sudah banyak menonton!")
    else :
        pesan = ("Wah kamu masih sedikit menonton!")

    context = {
        'list_mywatchlist': data_mywatchlist,
        'nama': 'Syarief Ahmad Al-Muhajir',
        'npm': '2106653445',
        'pesan': pesan
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_xml = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_xml), content_type="application/xml")

def show_json(request):
    data_json = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_json), content_type="application/json")

def show_json_id(request, id):
    data_json_id = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_json_id), content_type="application/json")

def show_xml_id(request, id):
    data_xml_id = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_xml_id), content_type="application/xml")