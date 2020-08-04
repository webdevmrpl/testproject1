from .views import BbCreateView, BbDetailView, index, by_rubric, BbEditView, BbDeleteView, register_view, detail_view, RubricModelViewSet
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('rubrics',RubricModelViewSet)


urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='main/registration/login.html'), name="login"),
    path('accounts/logout', LogoutView.as_view(next_page='index')),
    path('accounts/password_change/',
         PasswordChangeView.as_view(template_name='main/registration/change_password.html', ),
         name='password_change'),
    path('accounts/password_changed/done/',
         PasswordChangeDoneView.as_view(template_name='main/registration/password_changed.html'),
         name='password_change_done'),
    path('accounts/password_reset/done',
         PasswordResetDoneView.as_view(template_name='main/registration/email_sent.html'), name='password_reset_done'),

    path('accounts/password_reset/', PasswordResetView.as_view(template_name='main/registration/reset_password.html',
                                                               subject_template_name='main/registration/reset_subject.txt',
                                                               email_template_name='main/registration/reset_email.html',
                                                               from_email='kritart369@gmail.com'
                                                               ),
         name='password_reset'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='main/registration/confirm_password.html'),
         name='password_reset_confirm'),
    path('accounts/reset/done', PasswordResetCompleteView.as_view(template_name='main/registration/password_confirmed.html'),
         name='password_reset_complete'),
    path('accounts/register', register_view, name='register'),
    path('detail/<int:pk>/edit/delete/', BbDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/edit/', BbEditView.as_view(), name='edit'),
    path('detail/<int:pk>/', detail_view, name='detail'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('api/', include(router.urls)),
    path('', index, name='index')
]
