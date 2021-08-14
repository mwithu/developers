from django.urls import path, include
from rest_framework import routers
from . import views

userRouter = routers.DefaultRouter()
userRouter.register(r'users', views.UserDetailsViewSet)

credRouter = routers.DefaultRouter()
credRouter.register(r'cred', views.CredentialViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(userRouter.urls)),
    path('', include(credRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('<str:pageName>', views.userDetails, name='userDetails'),
]
