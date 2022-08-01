from django.shortcuts import render, redirect
# Create your views here.
from board.models import Category,Post,Comment
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView,DeleteView,UpdateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin

def func(request):
    cat=Category.objects.all()
    post=Post.objects.all()
    comment=Comment.objects.all()
    return render(request,"board/home.html",context={"cat":cat,"post":post,"comment":comment})

def cat(request,id):
    cat=get_object_or_404(Category,pk=id)
    post=cat.post_category.all()
    comment=Comment.objects.all()
    return render(request,"board/category.html",context={"cat": cat, "post": post,"comment":comment})
class Add_Post(LoginRequiredMixin,CreateView):
    model = Post
    fields = ('title','post_pictures','content')
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        category = get_object_or_404(Category,pk=self.kwargs['id'])
        form.instance.category = category
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category,pk=self.kwargs['id'])
        context["category"] = category
        return context
    template_name = 'board/post.html'
    def get_success_url(self):
        category = get_object_or_404(Category, pk=self.kwargs['id'])
        return reverse('cat', kwargs={'id':category.id})

class Update_Post(UpdateView):
    model = Post
    fields = ('title', 'post_pictures', 'content')
    template_name = 'board/updatepost.html'
    def get_success_url(self):
        return reverse('cat', kwargs={'id':self.object.category.id})

class Delete_Post(DeleteView):
    model = Post
    template_name = 'board/delete.html'
    def get_success_url(self):
        return reverse('index')

class ListView_Post(ListView):
    model = Post
    template_name = 'board/postdetails.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        context["post"] = post
        return context

def post_detail(request,id):
    post = Post.objects.get(pk=id)
    return render(request, "board/postdetails.html", context={"post": post})


class Add_Comment(LoginRequiredMixin,CreateView):
    model = Comment
    fields = ('comment',)
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        post = get_object_or_404(Post,pk=self.kwargs['postid'])
        form.instance.post = post
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = get_object_or_404(Category, pk=self.kwargs['catid'])
        post = cat.post_category.all()
        comment=Comment.objects.all()
        context["post"] = post
        context['cat'] = cat
        context['postid'] = self.kwargs['postid']
        context['comment'] = comment
        return context
    template_name = 'board/category.html'
    def get_success_url(self,**kwargs):
        cat = get_object_or_404(Category, pk=self.kwargs['catid'])
        print(cat.id)
        return reverse('cat',args=[cat.id])
class Update_comment(LoginRequiredMixin,UpdateView):
    model = Comment
    fields = ('comment',)
    template_name='board/updatecommnet.html'
    def get_success_url(self,**kwargs):
        cat = get_object_or_404(Category, pk=self.kwargs['catid'])
        print(cat.id)
        return reverse('cat',args=[cat.id])
class Delete_Comment(LoginRequiredMixin,DeleteView):
    model = Comment
    template_name = 'board/delete.html'
    def get_success_url(self,**kwargs):
        cat = get_object_or_404(Category, pk=self.kwargs['catid'])
        print(cat.id)
        return reverse('cat',args=[cat.id])