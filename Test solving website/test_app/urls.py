from django.urls import path,include
from .views import(
    home,
    login_view,
    logout_view,
    leaderboard,
    play,
    submission_result,
    user_home,register
)

app_name = 'test_app'

urlpatterns = [
    path('', home, name='home'),
    path('register/',register, name='register'),
    path('leaderboard', leaderboard, name='leaderboard'),
    path('play', play, name='play'),
    path('submission-result/<int:attempted_question_pk>', submission_result, name='submission_result'),
    path('user-home', user_home, name='user_home'),
    path('login', login_view, name='login'),
    path('logout',logout_view, name='logout'),

]


