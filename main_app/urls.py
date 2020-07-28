
from django.contrib import admin
from django.urls import path, include

from apps.common.views import HomeView, SignUpView, DashboardView
from apps.myblog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView
from apps.userprofile.views import ProfileUpdateView, ProfileView, ProfileViewFriend
from apps.userprofile.apis import (LoginView, LogoutView)
# from apps.common.apis import RegisterAPI, LoginAPI
from apps.myblog.apis import GenericAPIView, GenericAPIViewDetail, GenericAPIViewCreatePost
from django.contrib.auth import views as auth_views
from knox import views as knox_views
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),


    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    
    path('profile/', ProfileView.as_view(), name='profile'),

    path('profile/<str:username>', ProfileViewFriend.as_view(), name='profile-friend'),

    path('register/', SignUpView.as_view(), name='register'),

    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
    ), name='logout'),

    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='common/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('post_new/', PostCreateView.as_view(), name='post_new'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('blogs/', PostListView.as_view(), name='blogs'),

    # path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('post/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    # path('oauth/', include('social_django.urls', namespace='social')),  # <-- here

    #apis here
    # path('api/blogs/', GenericAPIView.as_view()),
    # path('api/blog/<int:id>/', GenericAPIViewDetail.as_view()),
    # path('api/blog/post/', GenericAPIViewCreatePost.as_view()),

    #use knox
    # path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('', include('apps.common.api_urls')),

    #use usual auth
    path('api/v1/auth/login/', LoginView.as_view()),
    path('api/v1/auth/logout/', LogoutView.as_view()),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)