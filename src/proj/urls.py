"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from proj import settings
from refs import views as ref_views
from goods import views as goods_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('author-list/', ref_views.AuthorList.as_view()),
    path('author-detail/<int:pk>/', ref_views.AuthorDetail.as_view()),
    path('author-create/', ref_views.AuthorCreate.as_view()),
    path('author-update/<int:pk>/', ref_views.AuthorUpdate.as_view()),
    path('author-delete/<int:pk>/', ref_views.AuthorDelete.as_view()),

    path('genre-list/', ref_views.GenreList.as_view()),
    path('genre-detail/<int:pk>/', ref_views.GenreDetail.as_view()),
    path('genre-create/', ref_views.GenreCreate.as_view()),
    path('genre-update/<int:pk>/', ref_views.GenreUpdate.as_view()),
    path('genre-delete/<int:pk>/', ref_views.GenreDelete.as_view()),

    path('series-list/', ref_views.SeriesList.as_view()),
    path('series-detail/<int:pk>/', ref_views.SeriesDetail.as_view()),
    path('series-create/', ref_views.SeriesCreate.as_view()),
    path('series-update/<int:pk>/', ref_views.SeriesUpdate.as_view()),
    path('series-delete/<int:pk>/', ref_views.SeriesDelete.as_view()),

    path('publisher-list/', ref_views.PublisherList.as_view()),
    path('publisher-detail/<int:pk>/', ref_views.PublisherDetail.as_view()),
    path('publisher-create/', ref_views.PublisherCreate.as_view()),
    path('publisher-update/<int:pk>/', ref_views.PublisherUpdate.as_view()),
    path('publisher-delete/<int:pk>/', ref_views.PublisherDelete.as_view()),

    path('book-list/', goods_views.BookList.as_view()),
    path('book-create/', goods_views.BookCreate.as_view()),
    path('book-detail/<int:pk>/', goods_views.BookDetail.as_view()),
    path('book-update/<int:pk>/', goods_views.BookUpdate.as_view()),
    path('book-delete/<int:pk>/', goods_views.BookDelete.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
