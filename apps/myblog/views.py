from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Preference, Comment
from django.urls import reverse_lazy
from .forms import BlogPostForm, NewCommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count
# Create your views here.


def is_users(post_user, logged_user):
    return post_user == logged_user


PAGINATION_COUNT = 5


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'myblog/blogs.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = PAGINATION_COUNT

    def get_context_data(self, **kwargs):
        ##membuat/generate context/dict
        data = super().get_context_data(**kwargs)
        all_users = []
        data_counter = Post.objects.values('author')\
            .annotate(author_count=Count('author'))\
            .order_by('-author_count')[:6]
        for aux in data_counter:
            all_users.append(User.objects.filter(pk=aux['author']).first())

        data['preference'] = Preference.objects.all()
        data['all_users'] = all_users
        return data


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','image','content']
    template_name = 'myblog/post_new.html'
    success_url = reverse_lazy("blogs")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Add a new post'
        return data

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'myblog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(post_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        data['form'] = NewCommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
                              author=self.request.user,
                              post_connected=self.get_object())
        new_comment.save()

        return self.get(self, request, *args, **kwargs)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','image','content']
    template_name = 'myblog/post_new.html'
    success_url = reverse_lazy("blogs")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Edit a post'
        return data


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'myblog/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy("blogs")

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

# class PostCreateView(LoginRequiredMixin, TemplateView):
#     # user_form = UserForm
#     # profile_form = ProfileForm
#     blog_form = BlogPostForm
#     template_name = 'myblog/post_new.html'

#     def post(self, request):

#         post_data = request.POST or None
#         file_data = request.FILES or None

#         blog_form = BlogPostForm(post_data, file_data, instance=request.user.profile)

#         if blog_form.is_valid():
#             blog_form.save()
#             messages.error(request, 'Your profile is updated successfully!')
#             return HttpResponseRedirect(reverse_lazy('home'))

#         context = self.get_context_data(
#                                         blog_form=blog_form
#                                     )

#         return self.render_to_response(context)     

#     def get(self, request, *args, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['tag_line'] = 'Add a new post'
#         return data

