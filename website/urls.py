"""
URL configuration for website project.

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

from uit_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.IndexView.as_view(),name="index"),
    path("about/",views.AboutView.as_view(),name="about"),
    path("courses/bsc_cs/",views.BscComputerScienceView.as_view(),name="bsc-cs"),
    path("courses/bsc_cs/",views.BscComputerScienceView.as_view(),name="bsc-cs"),
    path("infastructures/lab/",views.ComputerLabView.as_view(),name="lab"),
    path("courses/bca_cs",views.BcaComputerScienceView.as_view(),name="bca"),
    path("courses/bcom_ap",views.BcomFinanceView.as_view(),name="bcom-finance"),
    path("courses/bcom_tax",views.BcomCooperationView.as_view(),name="bcom-cop"),

    path("other_staffs/",views.OtherStaffsView.as_view(),name="other-staffs"),
    path("achievements/",views.AchievementsView.as_view(),name="achievements"),
    path("clubs/",views.ClubsView.as_view(),name="clubs"),
    path("nss/",views.NssView.as_view(),name="nss"),
]
