from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if 'number' in request.session:
        request.session['number'] = request.session.get('number', 0) + 1
    else:
        request.session['number'] = 0
    return render(request,'index.html')

def destroy(request):
    del request.session['number']
    return redirect('/')

def add(request):
    request.session['number'] = request.session.get('number', 0) + 1
    return redirect('/')

def increment(request):
    custom_increment = request.POST.get('number')
    if custom_increment:
        current_total = request.session.get('number', 0)
        request.session['number'] = current_total + int(custom_increment) - 1
    return redirect('/')