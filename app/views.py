from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from .models import Kategoria, Ingatlan
from .forms import IngatlanForm

def index(request):
    ingatlanok = Ingatlan.objects.all()

    context = {
        'ingatlanok': ingatlanok
    }

    return render(request, 'index.html', context = context)

def ujIngatlan(request):
    form = IngatlanForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect(index)
    else:
        form = IngatlanForm()

    context = {
        'form': form
    }

    return render(request, 'uj_ingatlan.html', context = context)

def ingatlanTorlese(request, id):
    ingatlan = get_object_or_404(Ingatlan, pk = id)
    ingatlan.delete()

    return redirect(index)


def ingatlanJSON(request, id):
    ingatlan = list(Ingatlan.objects.filter(Q(id__exact = id)).values())
    return JsonResponse(ingatlan, safe = False)