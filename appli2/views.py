from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'name':'ashu'}
    return render(request,'a2_first.html',context=d)