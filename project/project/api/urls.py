from rest_framework.routers import DefaultRouter
from app.api.urls import Post_router
from django.urls import path,include

router = DefaultRouter()

router.registry.extend(Post_router.registry)

urlpatterns = [
    path('',include(router.urls))
]