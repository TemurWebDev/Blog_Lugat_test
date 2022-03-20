from django.urls import path
from blog.views import home_blog_view,complete_blog_view,customer_delete_view,blog_css_view

urlpatterns = [
    path('r/<int:pk>/delete/',customer_delete_view,name='delete_url'),
    path('',home_blog_view,name='home-url'),
    path('r/<int:pk>',complete_blog_view,name='complate-url'),
    path('shablon/',blog_css_view,name='shablon-url')

]
