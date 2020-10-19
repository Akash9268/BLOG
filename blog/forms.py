from django import forms
from django.forms import ModelForm
from blog.models import post,comment

class PostForm(ModelForm):
	class Meta():
		model  = post
		fields = ("author","title","text")

		widgets =  {
			'title' : forms.TextInput(attrs={'class' : 'textinputclass form-control'}), #textinputclass is our class made
			'text'  : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent form-control'}), #post conetent is our class other two are inbuilt
		}
		

class CommentForm(ModelForm):
	class Meta():
		model  = comment
		fields = ("author","text")
		
		widgets  = {

			'author' : forms.TextInput(attrs={'class' : 'textinputclass form-control' }),
			'text'  : forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control'}),
		}