from rest_framework.routers import DefaultRouter, SimpleRouter
from .apis import PostViewSet, PageDetail
from django.urls import path, include
from apps.myblog.views import PostDetailView




# router = DefaultRouter()
# router.register('blog-posts', PostViewSet)


poll_list_view = PostViewSet.as_view({
    "get": "list",
    "post": "create"
})

urlpatterns = [
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('api/v1/blog-posts/', poll_list_view, name='blog-posts'),
    path('api/v1/blog-posts/<int:pk>/', PageDetail.as_view(), name='blog-posts-detail'),       
]

# urlpatterns = [
#     path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
#     # path('api/v1/', include(router.urls)),
#     path('poll/', PollAPIView.as_view()),
# ]
# urlpatterns = [
#     path('', include('apps.pages.urls')),
    # path('api/v1/', include('apps.common.api_urls')),
# app_name = 'pages'

# urlpatterns = [
#     path('', login_required(views.Index.as_view(), login_url=reverse_lazy('crm_users:crmuser_signin')), name='dashboard'),
#     path('api/', include('apps.pages.urls_api')),
# ]
