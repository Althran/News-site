from django.http import HttpRequest
from django.views.generic import ListView, DetailView, TemplateView

from .forms import ContactForm, CommentForm, NewsletterForm
from .models import Post, Comment


class ContextMixin:
    paginate_by = 3

    context = {
        'site_title': 'Sunny',
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'linkedin': 'https://linkedin.com',
        'instagram': 'https://instagram.com',
    }


class PostListView(ContextMixin, ListView):
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        context['newsletter_form'] = NewsletterForm()
        return context

    def post(self, request, post_slug):
        if request.POST.get('form') == 'newsletter':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
        return self.get(request=request, post_slug=post_slug)


class NewsListView(ContextMixin, ListView):
    model = Post
    template_name = 'core/blog.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-date_published')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsListView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        context['newsletter_form'] = NewsletterForm()
        context['comments'] = Comment.objects
        context['recent_posts'] = Post.objects.filter(is_published=True).order_by('-date_published')[:5]
        return context

    def get(self, request, *args, **kwargs):
        return super(NewsListView, self).get(request=request)

    def post(self, request, post_slug):
        if request.POST.get('form') == 'newsletter':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
        return self.get(request=request, post_slug=post_slug)


class PostDetailView(ContextMixin, DetailView):
    model = Post
    template_name = 'core/blog-single.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        context['comments'] = Comment.objects.filter(post__id=context[self.context_object_name].id)
        context['comment_form'] = CommentForm()
        context['newsletter_form'] = NewsletterForm()
        return context

    def post(self, request, post_slug):
        if request.POST.get('form') == 'comment':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
        elif request.POST.get('form') == 'newsletter':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
        return self.get(request=request, post_slug=post_slug)


class AboutTemplateView(ContextMixin, TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        context['newsletter_form'] = NewsletterForm()
        return context

    def post(self, request, post_slug):
        if request.POST.get('form') == 'newsletter':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
        return self.get(request=request, post_slug=post_slug)


class ContactCreateView(ContextMixin, TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data()
        context.update(self.context)
        context['heading'] = 'Contact us'
        context['subheading'] = 'If you want'
        context['contact_form'] = ContactForm()
        context['user'] = self.request.user
        context['newsletter_form'] = NewsletterForm()
        return context

    def post(self, request: HttpRequest):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request=request)

    def post_newsletter(self, request, post_slug):
        if request.POST.get('form') == 'newsletter':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
        return self.get(request=request, post_slug=post_slug)

