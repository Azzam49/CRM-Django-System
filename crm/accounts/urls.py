from django.urls import path
from .views import (
    home,
    products,
    customer,
    createOrder,
    updateOrder,
    deleteOrder,
    registerPage,
    loginPage,
    logoutUser,
    userPage,
    accountSettings
)

#to be able use settings.py
from django.conf import settings
#to be able make url for static files (images)
from django.conf.urls.static import static

urlpatterns = [
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),

    path('', home, name="home"),

    path('user/', userPage, name="user-page"),
    path('account/', accountSettings, name="account"),

    path('products/', products, name="products"),
    path('customer/<str:pk>/', customer, name="customer"),


    path('create_order/<str:customer_pk>', createOrder, name="create_order"),
    path('update_order/<str:pk>/', updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', deleteOrder, name="delete_order"),
]

#the url for static files (images)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)