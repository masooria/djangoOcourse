from django.shortcuts import render

#from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<h1>The Defcon20 Homepage</h1>")
    #return render(request, 'base.html')
    return render(request, 'pages/page.html')
