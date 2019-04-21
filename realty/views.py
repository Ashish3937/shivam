from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking, Contact, ContactForm, BookingForm, Listing, CustomerForm
from django.contrib import messages


def homepage(request):
    listings_obj=Listing.objects.all()
    if request.method=='POST':
        
        bForm=BookingForm(request.POST)


        if bForm.is_valid():
            bForm.save()
        
            bForm=BookingForm()
            messages.success(request, 'Thank you for showing interest. We will get back to you soon.')
        
    else:
       
        bForm=BookingForm()
    return render(request,'home.html',{'bForm':bForm,'listings':listings_obj})    
        

def contact(request):
    
    if request.method=='POST':
        
        cForm=ContactForm(request.POST)
        if cForm.is_valid():
       
            cForm.save()

            cForm=ContactForm()
            messages.success(request, 'Thank you for showing interest. We will get back to you soon.')
        
    else:
       
        cForm=ContactForm()
    return render(request,'contact.html',{'cForm':cForm,})  

def about_us(request):
    return render(request,'about_us.html')

def property(request, pk):
    prop_id=pk
    property_obj=Listing.objects.get(pk=prop_id)
    if request.method=='POST':
        
        bForm=CustomerForm(request.POST)


        if bForm.is_valid():
            temp=bForm.save(commit=False)
            temp.property_type=property_obj
            temp.save()
        
            bForm=CustomerForm()
            messages.success(request, 'Thank you for showing interest. We will get back to you soon.')
        
    else:
       
        bForm=CustomerForm()
    return render(request,'property.html',{'property':property_obj,'bForm':bForm})  



