from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from bookmark.models import Bookmark


class BookmarkList(ListView):  # bookmark_list.html
    model = Bookmark


class BookmarkCreateView(CreateView):  # bookmark_form.html - form 이름이 흔해서 아래처럼 create로 바꿔준 거
    model = Bookmark
    fields = ['site_name', 'url']      # <form> -> fields
    template_name_suffix = '_create'   # bookmark_create.html
    success_url = reverse_lazy('bookmark:list')
