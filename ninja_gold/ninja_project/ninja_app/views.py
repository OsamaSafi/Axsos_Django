from django.shortcuts import redirect, render
import random
from datetime import datetime  # استيراد مكتبة الوقت

def index(request):
    if 'gold_money' not in request.session:
        request.session['gold_money'] = 0
        request.session['status'] = []
    
    context = {
        'gold_money': request.session['gold_money'],
        'activities': request.session['status']
    }
    print( request.session['status'])
    return render(request, 'index.html', context)


def process_money(request, type):
    if request.method == 'POST':
        now = datetime.now().strftime("%B %dth %Y %I:%M %p")

        if type == 'farm':
            gold = random.randint(10, 20)
            message = f"You entered a farm and earned {gold} gold. ({now})"
            color = "green"
            
        elif type == 'cave':
            gold = random.randint(5, 10)
            message = f"You entered a cave and earned {gold} gold. ({now})"
            color = "green"
            
        elif type == 'house':
            gold = random.randint(2, 5)
            message = f"You entered a house and earned {gold} gold. ({now})"
            color = "green"
            
        elif type == 'quest':
            gold = random.randint(-50, 50)
            if gold >= 0:
                message = f"You completed a quest and earned {gold} gold. ({now})"
                color = "green"
            else:
                message = f"You failed a quest and lost {abs(gold)} gold. Ouch. ({now})"
                color = "red"
        else:
            return redirect('/')

        request.session['gold_money'] += gold

        new_activity = {
            'message': message,
            'color': color
        }

        request.session['status'].insert(0, new_activity)

    return redirect('/')