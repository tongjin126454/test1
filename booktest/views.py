from django.shortcuts import render
from booktest.models import AreaInfo
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.

def show_area(request,pindex):
    # 搜查所有父级为空的地区，即这个地区就是省地区
    areas = AreaInfo.objects.filter(aparent__isnull=True)
    # 分页，每页显示十条
    paginator = Paginator(areas, 10)
    # print(paginator.num_pages)
    if pindex ==  '':
        pindex = 1
    else:
        pindex =int(pindex)

    # 获取第一页的内容
    # page 是page类的实例对象
    page = paginator.page(pindex)
    return render(request, 'booktest/show_area.html',{
        'page':page
    })

def areas(request):

    return render(request,'booktest/areas.html')

def prov(request):
    areas = AreaInfo.objects.filter(aparent__isnull=True)
    area_list = []
    for area in areas:
        area_list.append((area.id,area.atitle))
    return JsonResponse({'data':area_list})

def city(request,pid):
    areas =AreaInfo.objects.filter(aparent__id=pid)
    area_list = []
    for area in areas:
        area_list.append((area.id, area.atitle))
    return JsonResponse({'data': area_list})

def dis(request,pid):
    areas =AreaInfo.objects.filter(aparent__id=pid)
    area_list = []
    for area in areas:
        area_list.append((area.id, area.atitle))
    return JsonResponse({'data': area_list})