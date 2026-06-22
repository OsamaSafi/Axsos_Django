from django import forms
from .models import *
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
                'title',
                'author',
                'book_img',
                'author_img',
                'pages',
                'price',
                'rental_price_day',
                'rental_period',
                'total_rental',
                'status',
                'category'
            ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'book_img':forms.FileInput(attrs={'class':'form-control'}),
            'author_img':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_day':forms.NumberInput(attrs={'class':'form-control','id':'rental_day'}),
            'rental_period':forms.NumberInput(attrs={'class':'form-control','id':'rental_period'}),
            'total_rental':forms.NumberInput(attrs={'class':'form-control','id':'total_rental'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }
    

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title and len(title.strip()) < 3: 
            raise forms.ValidationError("The book title must be more than 3 characters long!")
        return title

    def clean_author(self):
        author = self.cleaned_data.get("author")
        if author and len(author.strip()) < 3:
            raise forms.ValidationError("The author name must be more than 3 characters long!")
        return author


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control mb-3'})
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if name and len(name) < 3:
            raise forms.ValidationError("The name must be more than 3 characters long!")
            
        return name
