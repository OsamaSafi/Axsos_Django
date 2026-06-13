from django.contrib import messages
from django.shortcuts import redirect, render
from login_app.models import User
from wall_app import models

# Create your views here.
def allMessages(request):
    user_id = request.session.get('user_id')
    users = User.objects.filter(id=user_id)
    return render(request,'messages.html',{
        'msgs' : models.Message.objects.all().order_by('-created_at'),
        'user' : users[0],
    })

def messagesCreate(request):
    if request.method == "POST":
        user_id = request.session.get('user_id')
        if user_id:
            models.Message.objects.create(
                message = request.POST['message'],
                user_id = user_id
            )
            return redirect('/wall/messages')
        else:
            messages.error(request,'should be login!',extra_tags='login_error')
            return redirect('/home')
    else:
        messages.error(request,'something error,try again!',extra_tags='error')
        return redirect('/messages')
    

def messagesDelete(request,id):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    if user_id:
        message = models.Message.objects.get(id=id)
        if message.user_id == user_id:
            message.delete()
            return redirect('/wall/messages')
        else:
            messages.error(request,'just your message can be deleted',extra_tags='message_delete')
            return redirect('/wall/messages')
    else:
        messages.error(request,'should be login!',extra_tags='login_error')
        return redirect('/home')



def commentsCreate(request,id):
    if request.method == "POST":
        user_id = request.session.get('user_id')
        if user_id:
            models.Comment.objects.create(
                comment = request.POST['comment'],
                user_id = user_id,
                message_id = id
            )
            return redirect('/wall/messages')
        else:
            messages.error(request,'should be login!',extra_tags='login_error')
            return redirect('/home')
    else:
        messages.error(request,'something error,try again!',extra_tags='error')
        return redirect('/messages')
