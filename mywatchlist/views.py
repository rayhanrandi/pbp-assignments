from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_mywatchlist': data_mywatchlist,
        'nama': 'Rayhan Putra Randi',
        'id' : '2106705644',
        'jumlah_nonton': 0,
        'output_nonton': 'Wah, kamu masih sedikit menonton!'
    }
    for movie in context.get('list_mywatchlist'):
        if movie.watched == "\u2713":
            context['jumlah_nonton'] += 1
    if context.get('jumlah_nonton') >= (len(context.get('list_mywatchlist')) - context.get('jumlah_nonton')):
        context['output_nonton'] = "Selamat, kamu sudah banyak menonton!"
    
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), 
                        content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data),
                        content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
