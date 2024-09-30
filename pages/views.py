from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    name = request.GET.get("name") or "world!"
    return HttpResponse("Hello, " + name)

def index2(request, val1=0):  # إضافة دالة العرض (index2)
    return HttpResponse("value1 = " + str(val1))

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "pages/index.html")

def index(request):
     name = request.GET.get("name") or "world!"
     context = {'name': name}
     return render(request, "pages/index.html", context)

def index(request):
    name = request.GET.get("name") or "world!"  # الحصول على المتغير 'name' من طلب HTTP
    return render(request, "pages/index.html", {"name": name})  # إرسال القاموس إلى القالب

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'pages/show.html', context)
