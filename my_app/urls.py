from django.urls import path
from . import views

app_name="my_app"

urlpatterns=[
	path('',views.SearchView.as_view(),name='home'),
	path('new_search/',views.SearchView1,name='new_search'),
]