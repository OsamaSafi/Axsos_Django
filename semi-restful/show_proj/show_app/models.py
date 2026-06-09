from datetime import date
from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def validate_show(self,data,show_instance=None):
        errors={}
        title = data.get('title','')
        network = data.get('network','')
        release_date = data.get('release_date','')
        if len(title) == 0:
            errors['title'] = 'Enter title field !'
        elif len(title) < 2 :
            errors['title'] = 'Enter title grater than 2 char'
        else:
            shows = Show.objects.filter(title=title)
            if show_instance:
                shows = shows.exclude(id=show_instance.id)
            if shows.exists():
                errors['title'] = 'Title must be unique'

        if len(network) == 0:
            errors['network'] = 'Enter network field !'
        elif len(network) < 3 :
            errors['network'] = 'Enter network grater than 3 char'

        if not release_date:
            errors['release_date'] = 'Enter release date field !'
        elif release_date > str(date.today()):
            errors['release_date'] = 'Release date must be in the past!'
        
        return errors


    def create_show(self, data):
        show = self.create(
            title = data.get('title',''),
            network = data.get('network',''),
            desc = data.get('desc',''),
            release_date = data.get('release_date',''),
        )
        return show
    
    def update_show(self, data,show_id):
        errors = Show.objects.validate_show(data)
        show = self.get(id=show_id)
        show.title = data.get('title','')
        show.network = data.get('network','')
        show.desc = data.get('desc','')
        show.release_date = data.get('release_date','')
        show.save()
        return show
    
    def delete_show(self,show_id):
        show = Show.objects.get(id=show_id)
        show.delete()
        return




class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()