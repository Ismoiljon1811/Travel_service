from django.contrib import admin
from django.urls import path
from project_app.views import (
    home, category, batafsil, update_travel, delete_travel, reys, create_travel
)
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name ='home'),
    path('category/<int:id>/', category,name ='category'),
    path('reys/<int:id>/', reys, name = 'reys'),
    path('batafsil/<int:id>/', batafsil, name ='batafsil'),
    path('update_product/<int:id>/', update_travel, name ='update'),
    path('create_product/', create_travel, name='create'),
    # path('create_product/', Create_tour.as_view(), name='create'),
    path('delete_product/<int:id>/', delete_travel, name ='delete')



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
