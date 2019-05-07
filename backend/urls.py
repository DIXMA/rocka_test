from django.urls import path, include

urlpatterns = [
    path('', include('moviesApp.urls')),
    path('movies/', include('moviesApp.urls')),
    # path(r'api/v1.0/', include('moviesApp.urls')),
]
