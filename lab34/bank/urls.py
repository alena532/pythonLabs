from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordChangeDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.urls import path
from django.contrib import admin

from bank.views import *

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('login/', LoginView.as_view(), name='login'),


    path('password_reset/', PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done', PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(),  name='password_change_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    path('client/', ClientPageView.as_view(), name='client_page'),
    path('client/banks',ClientBanksView.as_view(),name='client_banks'),
    path('client/bank_application/<int:pk>',SendApplicationView.as_view(),name="bank_application"),

    path('manager/', ManagerPageView.as_view(), name='manager_page'),
    path('manager/applications',ApplicationsView.as_view(),name='watch_applications'),
]


