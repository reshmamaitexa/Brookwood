from django.urls import path
from brookwoodapp import views

urlpatterns = [
    path('login_users', views.LoginUserAPIView.as_view(),name='login_users'),
    
    path('user_register', views.UserRegisterSerializeraAPIView.as_view(),name='user_register'),

    path('product',views.ProductAPIView.as_view(),name='add_product'),

    path('feedback',views.FeedbackAPIView.as_view(),name='add_feedback'),

    path('complaint',views.ComplaintAPIView.as_view(),name='complaint'),

    path('cart',views.CartAPIView.as_view(),name='cart'),

    path('order',views.OrderAPIView.as_view,name='order')


]