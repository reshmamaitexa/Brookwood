from django.urls import path
from woodapp import views

urlpatterns = [
    path('', views.admin_dashboard,name='admin_dashboard'),
    path('admin_view_users', views.admin_view_users,name='admin_view_users'),
    path('admin_view_complaints_report',views.admin_view_complaint_report,name='admin_view_complaint_report'),
    path('admin_view_bill_report',views.admin_view_bill_report,name='admin_view_bill_report'),
    path('admin_view_feedback',views.admin_view_feedback,name='admin_view_feedback'),
    path('admin_add_product',views.admin_add_product,name='admin_add_product'),
    path('admin_add_all_product',views.admin_add_all_product,name='admin_add_all_product'),
    path('admin_view_product',views.admin_view_product,name='admin_view_product'),
    path('admin_view_all_product',views.admin_view_all_product,name='admin_view_all_product'),
    path('admin_delete_product/<int:id>', views.admin_delete_product, name='admin_delete_product'),
    path('admin_edit_product/<int:id>', views.admin_edit_product, name='admin_edit_product'),
    path('<int:id>/productformupdate/', views.productformupdate, name='productformupdate'),
    path('admin_add_category_page', views.admin_add_category_page,name='admin_add_category_page'),
    path('admin_add_category', views.admin_add_category,name='admin_add_category'),
    path('admin_single_complaints/<int:id>', views.admin_single_complaints,name='admin_single_complaints'),
    path('admin_add_replay/<int:id>', views.admin_add_replay,name='admin_add_replay'),
    # path('',views.admin_login,name='admin_login'),
    # path('login_admin',views.login_admin,name='login_admin'),

]