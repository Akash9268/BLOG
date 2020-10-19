
## we came here fter creating our models and their respecting forms
## after creating views we will create corresponding templates .html pages
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import post,comment
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
									DetailView,CreateView,
									UpdateView,DeleteView)
# Create your views here.

class AboutView(TemplateView):
	template_name = 'about.html'

class PostListView(ListView):
	model  = post

	def get_queryset(self):
		return post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # this - dash here allows to oder them in descending order
																									# lte = less than or equal to

class PostDetailView(DetailView):
	model = post
		
class CreatePostView(LoginRequiredMixin,CreateView):
	login_url = '/login/' #attribute of mixin
	redirect_field_name =  'blog/post_detail.html'
	form_class  = PostForm
	model  = post

class UpdatePostView(LoginRequiredMixin,UpdateView):
	login_url = '/login/' #attribute of mixin
	redirect_field_name =  'blog/post_detail.html'
	form_class  = PostForm
	model  = post

class PostDeleteView(LoginRequiredMixin,DeleteView):
	model = post
	success_url  = reverse_lazy('post_list') ## using reverse_lazy to amke sure after we delete out post it takes us back to homepage 
	## we dont want our success_url to activate before we delete our post thats why we use reverse_lazy

class DraftListView(LoginRequiredMixin,ListView):
	login_url = '/login/'
	redirect_field_name  = 'blog/post_list.html'
	model  = post
	

	def get_queryset(self):
		return post.objects.filter(published_date__isnull = True).order_by('created_date')					

######################################
######################################

@login_required
def post_publish(request,pk):
	posts  = get_object_or_404(post,pk=pk)
	posts.publish()
	return redirect('post_detail',pk=pk)


def add_comment_to_post(request,pk):
	posts  = get_object_or_404(post,pk=pk)
	if request.method =='POST':
		form  = CommentForm(request.POST)
		if form.is_valid():
			comment  = form.save(commit=False) #we are saving in memory but not in database so ewe can make some changes before saving it
			comment.post  = posts  #if we look our models there our comment's post is a foreignkwy for post for making sure it became here true too
			comment.save()
			return redirect('post_detail',pk=posts.pk)
		
	else:
		form  = CommentForm()
	return render(request,'blog/comments_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
	comments  = get_object_or_404(comment,pk=pk)
	comments.approve() ##these approve method come from the models we created 
	return redirect('post_detail',pk=comments.post.pk)


@login_required
def comment_remove(request,pk):
	Comment =  get_object_or_404(comment,pk=pk)
	post_pk = Comment.post.pk ## assgning it to other variable beore deleting
	Comment.delete() ##simply deleting
	return redirect('post_detail',pk=post_pk)
