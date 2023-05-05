from django.urls import path
from woodapp import views

urlpatterns = [
    path('admin_dashboard', views.admin_dashboard,name='admin_dashboard'),
    path('admin_view_users', views.admin_view_users,name='admin_view_users'),
    path('admin_view_complaints_report',views.admin_view_complaint_report,name='admin_view_complaint_report'),
    path('admin_view_bill_report',views.admin_view_bill_report,name='admin_view_bill_report'),
    path('admin_view_feedback',views.admin_view_feedback,name='admin_view_feedback'),
    path('admin_add_product',views.admin_add_product,name='admin_add_product'),
    path('admin_view_product',views.admin_view_product,name='admin_view_product'),
    path('',views.admin_login,name='admin_login'),
    path('login_admin',views.login_admin,name='login_admin'),

]