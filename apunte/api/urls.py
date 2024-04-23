from django.urls import path
from apunte.api.views import ApunteList,ApunteDetail

urlpatterns = [
    path('',ApunteList.as_view(), name="listado"),
    path('<int:pk>', ApunteDetail.as_view(), name="apunteDetail")
]
