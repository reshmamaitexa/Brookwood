from django.urls import path
from brookwoodapp import views

urlpatterns = [
    path('login_users', views.LoginUserAPIView.as_view(),name='login_users'),
    
    path('user_register', views.UserRegisterSerializeraAPIView.as_view(),name='user_register'),

    # path('product',views.ProductAPIView.as_view(),name='add_product'),

    # path('feedback',views.FeedbackAPIView.as_view(),name='add_feedback'),

    path('complaint',views.ComplaintAPIView.as_view(),name='complaint'),

    path('complaintsingle_view/<int:id>', views.ComplaintSingleAPIView.as_view(), name='complaintsingle_view'),

    # path('cart',views.CartAPIView.as_view(),name='cart'),

    # path('order',views.OrderAPIView.as_view,name='order'),

    path('single_user/<int:id>', views.SingleUserAPIView.as_view(), name='single_user'),

    path('update_user/<int:id>', views.Update_UserAPIView.as_view(), name='update_user'),


    path('get_product', views.Get_ProductAPIView.as_view(), name='get_product'),
    path('single_product/<int:id>', views.SingleProductAPIView.as_view(), name='single_product'),


]