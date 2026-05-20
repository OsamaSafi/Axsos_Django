from django.shortcuts import render
from datetime import datetime

def index(request):
    now = datetime.now()
    context = { 
            "time": now.strftime("%b %d, %Y \n %I:%M %p")
        }
    return render(request,'index.html',context)

# now = datetime.now() return the object with full details about the time
# now() used to ask my device, what is the time and date ?????
# strftime() used to format the time to display it in best way
# %b display the name of the month like May 3-char
# %d display the number of the day 
# %Y display the year in 4-char like 2026
# %I convert the time that returned from now() from 24 system to 12 system , 01 - 12 hour
# %M display the min
# %p display the time indicator like PM or AM


