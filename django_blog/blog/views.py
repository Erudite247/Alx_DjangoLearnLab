# blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import (CustomUserCreationForm, UserProfileForm, 
                    PostForm, CommentForm)
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import (ListView, DetailView, 
                                  CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from taggit.models import Tag
from django.db.models import Q

# User Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})
    
# Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
        
    return render(request, 'blog/profile.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to 'home'after success
    else:
        form = AuthenticationForm()

    return render(request, 'blog/login.html', {'form': form})

# Homepage
def homepage(request):
    return render(request, 'blog/home.html')

# Class-based views for list, detail, create, update, and delete operations
# List all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date'] # Order posts by date published
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.filter(tags__in=[tag])
        return queryset
    
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Return all posts, no filtering by tags here
        return Post.objects.all().order_by('-published_date')

# View details of a specific post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        context['comment_form'] = CommentForm()
        return context

# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    # Set the author automatically based on logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update an existing post (only if the user is the author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author # To ensure user is the author

# Delete a post (only if the user is the author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# Comment Views
# Create a Comment
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']  # Link comment to the post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})

# Edit a Comment
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/update_comment.html'
    
    def get_queryset(self):
        # Ensure only the author of the comment can update it
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

# Delete a Comment
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_queryset(self):
        """Ensure that only the author can delete the comment."""
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})
    
# Search View
def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})