from django.urls import path, include
# from .views import ArticleApiView, ArticleDetails, ArticleViewset, GenericApiView
from .views import ArticleViewSet, GenericApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename = 'article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', ArticleApiView.as_view()),
    # path('article/detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericApiView.as_view()),
    path('generic/article/', GenericApiView.as_view())
]
