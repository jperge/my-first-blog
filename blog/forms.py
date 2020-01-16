from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
