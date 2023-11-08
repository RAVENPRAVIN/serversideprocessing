from django.shortcuts import render
from django.template  import loader
from django.shortcuts import render




def prismarea(request):
    context={}
    context['area'] = "0"
    context['s'] = "0"
    context['b'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        s = request.POST.get('side','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('side=',s)
        print('height=',h)
        area = 2*int(s) **2+4*int(s)*int(h)
        context['area'] = area
        context['s'] = s
        context['h'] = h
        print('Area=',area)
    return render(request,'myapp/math.html',context)

# Create your views here.
