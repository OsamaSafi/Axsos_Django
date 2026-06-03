from django.shortcuts import redirect, render

from dojo_ningas_app import models

# Create your views here.
def index(request):
    context = {
        'dojos': models.Dojo.objects.all().order_by('-created_at'),
    }
    return render(request,'index.html',context)

def dojoCreate(request):
    dojo = models.Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
    )
    dojo.save()
    return redirect('/')


def ninjaCreate(request):
    ninja = models.Ninga.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo_id = request.POST['dojo'],
    )
    ninja.save()
    return redirect('/')

def dojoDelete(request,id):
    dojo = models.Dojo.objects.get(id = id)
    dojo.delete()
    return redirect('/')