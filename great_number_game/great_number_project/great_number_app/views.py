from django.shortcuts import redirect, render
import random

def index(request):
    if 'guess_number' not in request.session:
        request.session['guess_number'] = random.randint(1, 100)
        request.session['status'] = ''
        request.session['attemps'] = 0
        request.session['game_over'] = False

    return render(request, 'index.html')

def result(request):
    if request.session['game_over'] is True:
        return redirect('/')
    currentNumber = int(request.POST.get('number', 0))
    sessionNumber = request.session['guess_number']
    request.session['attemps'] = int(request.session['attemps']) + 1
    attemps = request.session['attemps']
    print(attemps)
    if currentNumber > sessionNumber:
        request.session['status'] = 'Too High!'
    elif currentNumber < sessionNumber:
        request.session['status'] = 'Too Low!'
    else:
        request.session['status'] = f'{sessionNumber} was the number! You got it {attemps}!'
        request.session['game_over'] = True
    return redirect('/')

def reset(request):
    # دالة بسيطة ومستقلة لتصفير اللعبة بالكامل وبدء مرحلة جديدة
    request.session.flush() # تمسح كل بيانات الجلسة القديمة بضربة واحدة
    return redirect('/')