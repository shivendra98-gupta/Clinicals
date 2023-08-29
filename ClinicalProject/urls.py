"""
URL configuration for ClinicalProject project.

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
from ClinicalApp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.PatientListView.as_view(),name='index'),  #yeh name=index vo hai jo reverse_lazy meh diya hai
    path("create/",views.PatientCreateView.as_view()),
    path("update/<int:pk>/",views.PatientUpdateView.as_view()),
    path("delete/<int:pk>/",views.PatientDeleteView.as_view()),
    path("adddata/<int:pk>/",views.addData),
    path("analyse/<int:pk>/",views.analyse), #<int:pk> ka mtlb hai ke 127.0.0.1:8000/analyse/2/ ye likho geh toh show hoga yaha 2 ka mtlb patientID seh hai
]
