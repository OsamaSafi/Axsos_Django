from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request,'index.html')

def process(request):
    print(request.POST)
    selected_languages = request.POST.getlist('speak')
    request.session['form_data'] = {
        'name' : request.POST.get('name'),
        'lang' : request.POST.get('lang'),
        'location' : request.POST.get('location'),
        'gender' : request.POST.get('gender'),
        'comment' : request.POST.get('comment'),
        'speaks': selected_languages,
    }
    return redirect('/result')

def result(request):
    return render(request, 'result.html')