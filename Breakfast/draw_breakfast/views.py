from django.shortcuts import render
from django.http import HttpResponse
from .models import  food_cust, foodmenu, final
import re
from django.template.defaulttags import register

# Create your views here.
def home(request):
    all_food = foodmenu.objects.all()
    return render(request, 'home.html', {
        'foods': all_food,
    })

def choosefood(request):
    check_box_list = {}
    All_food = {}
    yourname = request.POST.get('yourname')
    for item in tuple(request.POST.items()):
        if re.search("^food", item[0]):
            check_box_list[item[0]] = request.POST.getlist(item[0])
    # 食物總價
    total_price = 0
    for item in check_box_list:
        everyfoodprice = 0
        everyfoodstr = ""
        foodcustoms = check_box_list[item]
        for foodcustom in foodcustoms:
            everyfoodstr += foodcustom
            price = re.split('[^(\-)?0-9]',foodcustom)[-1]
            if price != '':
                total_price += int(price)
                everyfoodprice += int(price)
            # 判斷DB裡面的ID
            #temp = final.objects.filter(name=yourname)
            #if (temp.exists()):
            #    next
            #else:
            #    member_Save.save()
    return render(request, 'choosefood.html', {
        'chooses': check_box_list,
        'total' : total_price,
        'yourname' : yourname,
    })

#def insertsql(request):
