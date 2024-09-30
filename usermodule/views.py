from django.shortcuts import render

# Create your views here.
def index3(request):
   return render(request, 'usermodule/index3.html', {'Name':'Usermodule'})
