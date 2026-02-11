
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # Task CRUD
    path('add/', views.add_task, name='add'),
    path('edit/<int:task_id>/', views.edit_task, name='edit'),
    path('complete/<int:task_id>/', views.complete_task, name='complete'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),

    # Audio to Text
    path('audio-to-text/', views.audio_to_text, name='audio_to_text'),

    # Password Reset
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        views.CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        views.CustomPasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]