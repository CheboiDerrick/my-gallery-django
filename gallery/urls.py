from django.urls import path, register_converter
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.all_images,name='home'),
    path('category/',views.category_images ,name = 'category_results'),
    path('category/<category>', views.views_images, name='view_category'),
    # path('article/<int:article_id>/', views.article,name ='article')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)