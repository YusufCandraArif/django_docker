# from rest_framework.routers import DefaultRouter, SimpleRouter
# from .apis import PostViewSet
# from django.urls import path, include

# router = DefaultRouter()
# router.register('blog-posts', PostViewSet)


# poll_list_view = PostViewSet.as_view({
#     "get": "list",
#     "post": "create"
# })

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('poll/', PollAPIView.as_view()),
#     # path('poll/<int:id>/', PollDetailView.as_view()),
#     # path('generics/poll/', poll_list_view),
#     # path('generics/poll/<int:id>/', PollListView.as_view()),
#     # path('poll/search/', QuestionSearchViewSet.as_view({'get': 'list'})),
# ]
