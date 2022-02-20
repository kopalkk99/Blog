from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,
UpdateView,DeleteView)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class AboutView(TemplateView):

    template_name = 'about.html'

class PostListView(ListView):

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):

    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin,UpdateView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class DeletePostView(LoginRequiredMixin,DeleteView):

    model = Post
    success_url = reverse_lazy('post_list_view')

class DraftListView(LoginRequiredMixin,ListView):

    template_name='draft_list.html'
    context_object_name='draft_post'
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('-created_date')


@login_required
def post_publish(req,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail_view',pk=pk)


@login_required
def comment_approve(req,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail_view',pk=pk)

@login_required
def comment_remove(req,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail_view',pk=post_pk)

@login_required
def add_comment_to_post(req,pk):
    post = get_object_or_404(Post,pk=pk)
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail_view', pk=post.pk)
    else:
        form = CommentForm()
    return render(req, 'blog/comment_form.html', {'form': form})
