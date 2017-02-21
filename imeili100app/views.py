from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from pymongo import  MongoClient
import pymongo
from .data import mongo as imongodata
from .data.Imeili100Result import  Imeili100Result,Imeili100ResultStatus
from django.http import JsonResponse
import bson.json_util
import json
import jsonpickle
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request,'index.html')
@csrf_exempt
def queryBrands(request):
    page = 0
    categoryIndex = 0
    if request.method == 'GET':
        page = request.GET.get('page',0)
        categoryIndex = request.GET.get('category',0)
    elif request.method == 'POST':
        page = request.POST.get('page',0)
        categoryIndex = request.POST.get('category',0)
    collection = imongodata.db['t_brands']
    bransList =  list(collection.find({'category':int(categoryIndex)}))
    print(type(categoryIndex))
    jsonlist = bson.json_util.dumps(bransList)
    imeilires = Imeili100Result()
    imeilires.status = Imeili100ResultStatus.ok.value
    imeilires.res = json.loads(jsonlist)
    return HttpResponse(json.dumps(imeilires.__dict__,ensure_ascii=False))

@csrf_exempt
def queryBrandCategory(request):
    page = 0
    if request.method == 'GET':
        page = request.GET.get('page',0)
    elif request.method == 'POST':
        page = request.POST.get('page',0)
    collection = imongodata.db['t_brands_category']
    categories = list(collection.find())
    categoriesJsonStr =  jsonlist = bson.json_util.dumps(categories)
    imeilires = Imeili100Result()
    imeilires.status = Imeili100ResultStatus.ok.value
    imeilires.res = json.loads(categoriesJsonStr)
    return HttpResponse(json.dumps(imeilires.__dict__, ensure_ascii=False))
