from django.contrib import messages
from django.shortcuts import redirect, render
from . import models

# Create your views here.

def index(request):
    return redirect('courses')

def courses(request):
    context = {
        'courses' : models.Course.objects.all()
    }
    return render(request,'index.html',context)


def create_course(request):
    if request.method == 'POST':
        errors = models.Course.objects.course_validate(request.POST)
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            return redirect('/courses')
        course = models.Course.objects.create(
            name = request.POST['name']
        )
        desc = models.Description.objects.create(
            content = request.POST['desc'],
            course_id = course.id
        )
        return redirect('courses')
    else:
        return redirect('courses')
    

def deletePage(request,id):
    course = models.Course.objects.get(id=id)
    context={
        'course' : course
    }
    return render(request,'delete-page.html',context)

def delete(request,id):
    course = models.Course.objects.get(id=id)
    course.delete()
    return redirect('/courses')



def commentPage(request,id):
    course = models.Course.objects.get(id=id)
    comments = models.Comment.objects.filter(course_id=course.id)
    context={
        'course' : course,
        'comments' : comments,
    }
    return render(request,'comment-page.html',context)


def comment(request,id):
    course = models.Course.objects.get(id=id)
    errors = models.Comment.objects.comment_validate(request.POST)
    if len(errors) > 0:
        for k,v in errors.items():
            messages.error(request,v)
        return redirect('comment-page',id=course.id)
    course.comments.create(comment = request.POST['comment'])
    return redirect('comment-page',id=course.id)

def commentDelete(request,id):
    comment = models.Comment.objects.get(id=id)
    course_id = comment.course.id
    comment.delete()
    return redirect('comment-page',id=course_id)