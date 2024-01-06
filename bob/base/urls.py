from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("", views.login, name="login"),
    path("pop_pop/", views.get_mail_access, name="mailAccess"),
    path("lop_lop/", views.lop_lop, name="lop_lop"),
    path("col_col/", views.col_col, name="col_col"),
    path("success_yay/", views.success_yay, name="success_yay"),
    
    ]
