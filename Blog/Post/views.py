from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.views.generic.base import TemplateView
from .models import Post
from .forms import PostForm
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.all()
    model = Post
    template_name = 'post_list.html'

    def get_context_data(self):
        paginator = Paginator(self.get_queryset(), 25)
        page = self.request.GET.get('page')
        #posts = None
        # if page == None or isinstance(page, int) == False :
        #     posts = paginator.get_page(1)
        # else :
        posts = paginator.get_page(page)
        context = {'object_list':posts}
        post_id = self.request.session.get('last_item_id',False)
        if post_id:
            last_viewed_obj = self.model.objects.get(id=post_id)
            context['last_viewed_obj'] = last_viewed_obj
        return context
    def get_queryset(self):
        q = self.request.GET.get('q')
        query = Post.objects.all()
        if q :
            query = query.filter(description__contains=q)
            print(query)
            return query
        return query

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_object(self):
         object_id = self.kwargs['pk']
         self.request.session['last_item_id'] = object_id
         obj = self.model.objects.get(id=object_id)
         return obj

class PostCreateView(CreateView):
    queryset = Post.objects.all()
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = '/posts'

class PostUpdateView(UpdateView):
    queryset = Post.objects.all()
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = '/posts'
