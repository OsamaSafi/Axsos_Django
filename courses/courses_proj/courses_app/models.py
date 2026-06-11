from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def course_validate(self,data):
        errors = {}
        name = data.get('name','')
        description = data.get('desc','')
        if len(name) < 5:
            errors['name'] = 'Enter name and must grater than 5 char'

        if len(description) < 15:
            errors['description'] = 'Enter description and must grater than 15 char'
        
        return errors
    
    def createCourse(self,data):
        course = Course.objects.create(
            name = data.get('name','')
        )
        desc = Description.objects.create(
            content = data.get('desc',''),
            course_id = course.id
        )
        return course
    
    def deleteCourse(self,id):
        course = Course.objects.get(id=id)
        course.delete()
        return



class CommentManager(models.Manager):
    def comment_validate(self,data):
        errors = {}
        comment = data.get('comment','')
        if len(comment) < 2:
            errors['comment'] = 'Enter comment and must grater than 2 char'
        return errors
    
    def createComment(self,data,course):
        comment = course.comments.create(comment = data.get('comment',''))
        return comment
    
    def deleteComment(self,id):
        comment = Comment.objects.get(id=id)
        course_id = comment.course.id
        comment.delete()
        return course_id




class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()


class Description(models.Model):
    content = models.TextField()
    course = models.OneToOneField(Course,on_delete=models.CASCADE,related_name='course_desc')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CommentManager()