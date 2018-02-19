from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import View

from .models import *


class HomeView(View):
    def get(self,request, *args, **kwargs):
        listed_properties = Room.objects.filter(published=True)
        context_variables = {'properties': listed_properties}
        return render(request,'index.html',context_variables)      
        
class RoomsView(View):
    def get(self,request, *args, **kwargs):
        listed_properties = Room.objects.filter(published=True)
        context_variables = {'properties': listed_properties}
        return render(request,'products.html',context_variables)      

class RoomView(View):
    def get(self,request, *args, **kwargs):
        listed_property = get_object_or_404(Room,slug=kwargs.get('slug'))
        context_variables = {'room': listed_property}
        return render(request,'about.html',context_variables) 
