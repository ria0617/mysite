#from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 


# Create your views here.
class BookmarkLV (ListView):
    model = Bookmark
    template_name = 'bookmark/bookmark_list.html'
    # 페이지당 나오는 북마크의 갯수
    pagenate_by = 2 
    
class BookmarkDV(DetailView):
    template_name = 'bookmark/bookmark_detail.html'
    model = Bookmark
    
    
#편집기능 클래스    
class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'
    
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
    
class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')
    
class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
        
        
        
        
        
    