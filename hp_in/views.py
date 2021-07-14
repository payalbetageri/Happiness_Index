from django.shortcuts import render
from .models import Information

def home(request):
    return render(request,'home.html')

def gdc(request):
    return render(request,'gdc.html')

def lsr(request):
    return render(request,'lsr.html')

def gdc_result(request):
    country = request.GET['CN']
    country = country.title()
    all_data = Information.objects.filter(Country_name=country)
    if all_data:
        return render(request,'lsr_result.html',{'all_data':all_data})
    else:
        return render(request,'error.html')
    
def lsr_result(request):
    low = float(request.GET['from'])
    high = float(request.GET['to'])
    all_data = Information.objects.filter(Ladder_score__gte=(low),Ladder_score__lte=(high))
    if all_data:
        return render(request,'lsr_result.html',{'all_data':all_data})
    else:
        return render(request,'error.html')