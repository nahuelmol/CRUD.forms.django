from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', views.IndexView.as_view(), name='index'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
    path('contacts/edit/<int:pk>/', views.edit, name='edit'),
    path('contacts/create/', views.create, name='create'),
    path('contacts/delete/<int:pk>/', views.delete, name='delete'),

	path('countries/',views.CountriesView.as_view(),name='index_countries'),
    path('countries/create/',views.entering_countries,name='country_create'),
    path('countries/<int:pk>',views.CountryDetail.as_view(),name='detail_country'),

]

