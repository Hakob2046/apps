from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from .forms import *

class HomeView(ListView):
    model=HeaderTitle
    template_name='index.html'
   
    forlogo=ForLogo.objects.get()
    headertitle=HeaderTitle.objects.get()
    services=Services.objects.get()
    prmision=Prmision.objects.all()
    whatwedo=WhatWeDo.objects.all()
    problems=Problems.objects.all().order_by('-id')
    thecleantsay=TheCleantSay.objects.get()
    about=About.objects.all()
    about_f=About.objects.first()
    # subabout=About.objects.filter()
    getting=Getting.objects.get()
    tickets=Tickets.objects.all().order_by('storage')

    
    context={
            'forlogo':forlogo,
            'headertitle':headertitle,
            'services':services,
            'prmision':prmision,
            'whatwedo':whatwedo,
            'problems':problems,
            'thecleantsay':thecleantsay,
            'about':about,
            'about_f':about_f,
            # 'subabout':subabout,
            'getting':getting,
            'tickets':tickets,
            


        }    
    

    def get(self,request):
        contactus=ContactUs.objects.get()
        self.context['contactus']=contactus
        

       

        return render(request,self.template_name,self.context)
    
    def post(self,request):
        form=SubscribeModelForm(request.POST)
        messages=None
        if form.is_valid():
            form.save()
        else:
            messages=form.errors
        self.context['form']=form
        self.context['messages']=messages
        return render(request,self.template_name,context=self.context)



    
