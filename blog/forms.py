from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	"""docstring for PostForm"forms.ModelFormf __init__(self, arg):
		super(PostForm,forms.ModelForm.__init__()
		self.arg = arg"""
		
	class Meta:
		model = Post
		fields = ('title','text',)