from dataclasses import dataclass

from pickle import FALSE
from django.shortcuts import render
from .models import store
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request,"index.html")
@csrf_exempt 
def insert(request):
    try:
        bot=request.POST.get('messageText')
        user = store.objects.filter(name = bot).values_list("lname", flat=True)
        bot_response =user[0]
        bot_response = str(bot_response)      
        print(bot_response)
        return JsonResponse({'status':'OK','answer':bot_response})
    except:
        #user1="sorry i don't understand "
        bot_response = "sorry i don't understand "      
        print(bot_response)
        return JsonResponse({'status':'OK','answer':bot_response})
def input(request):
    return render(request,'commands.html')
def addcommant(request):
    catch=store()
    catch.name=request.POST.get('user')
    catch.lname=request.POST.get('bot')
    catch.save()
    return render(request,'index.html')

