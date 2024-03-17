from django.urls import path
from library import views
from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('library.urls')),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('library.urls')),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/add_review/', views.add_review, name='add_review'),
    # Add other URLs as needed
]
