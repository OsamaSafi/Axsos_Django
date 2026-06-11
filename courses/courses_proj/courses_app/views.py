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
        models.Course.objects.createCourse(request.POST)
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
    models.Course.objects.deleteCourse(id)
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
    courses = models.Course.objects.filter(id=id)
    errors = models.Comment.objects.comment_validate(request.POST)
    if len(errors) > 0:
        for k,v in errors.items():
            messages.error(request,v)
        return redirect('comment-page',id=courses[0].id)
    comment = models.Comment.objects.createComment(request.POST,courses[0])
    return redirect('comment-page',id=comment.course.id)


def commentDelete(request,id):
    course_id = models.Comment.objects.deleteComment(id)
    return redirect('comment-page',id=course_id)