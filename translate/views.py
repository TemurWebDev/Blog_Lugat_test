from django.shortcuts import render
from .models import Translate

# Create your views here.

def translate_view(request):
    soz = request.GET.get('q','')
    if soz and soz != '':
        natija = Translate.objects.filter(inglizcha__contains=soz).all()[:3]
    else:
        natija = None

    return render(request,'main/translate.html',{'q': soz,'natija': natija})

