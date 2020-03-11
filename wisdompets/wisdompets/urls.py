from django.contrib import admin
from django.conf.urls import url

from adoptions import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^pets/(\d+)/', views.pet_detail, name='pet_detail'),
]

# {% url %}
