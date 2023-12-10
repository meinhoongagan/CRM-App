"""
URL configuration for CRM project.

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
from django.urls import path,include
from core.views import *
from member.views import *
from dashboard.views import *
from django.contrib.auth import views
from leads.views import *
# from client.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',include("django.contrib.auth.urls")),
    # path('dashboard/',include("dashboard.urls")),
    path('client/',include("client.urls")),
    path("",index,name='index'),
    path('signup/', sign_up, name='signup'),
    path('login/', views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path("about/",about,name='about'),
    path("dashboard/",dashboard,name="dashboard"),
    path("add-lead/",add_leads,name="add-lead"),
    path("leads-list/",leads_list,name="lead-list"),
    path("<int:pk>/",leads_details,name="lead-details"),
    path('<int:pk>/delete/', leads_delete, name='lead-delete'),
    path('<int:pk>/edit/', leads_edit, name='lead-edit'),
    path('<int:pk>/client/',Convert_to_client, name='lead-client'),
    
]
