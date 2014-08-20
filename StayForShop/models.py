from django.db import models
from django.forms import ModelForm, Textarea
 
from django.forms.fields import CharField
from django import forms

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class Customer(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=10)

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

class CustomerForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()

class AuthorForm(ModelForm):
    name = CharField(label='My Name')
    title = CharField(label="Title")
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        widgets = {'name': Textarea(attrs={'cols':80, 'rows':10}),}
        
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'authors')
        