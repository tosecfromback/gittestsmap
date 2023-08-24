from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # ViewVersion
    # ## Users 시작화면
    # path('', views.Index.as_view(), name='index'),
    # ## 정상구동 확인용
    path('check/', views.FuncCheck.as_view(), name='check'),
    ## 회원가입
    path('signin/', views.Signin.as_view(), name='signin'),
    ## 로그인
    path('login/', views.Login.as_view(), name='login'),
    ## 로그아웃
    path('logout/', views.Logout.as_view(), name='logout'),
    ## 회원정보
    path('detail/', views.UserDetail.as_view(), name='detail'),
    ## 회원정보 생성
    path('detailAPI/', views.UserDetailAPI.as_view(), name='detailAPI'),
    ## 회원수정
    path('update/', views.UserUpdate.as_view(), name='update'),
    ## 회원탈퇴
    path('sginout', views.Signout.as_view(), name='signout'),
    
    # APIViewVersion
    ## Users 시작화면
    path('', views.Index.as_view(), name='index'),
    ## 회원가입
    path('signinAPI/', views.SigninAPI.as_view(), name='SigninAPI'),
    ## 로그인
    path('loginAPI/', views.LoginAPI.as_view(), name='LoginAPI'),
    ## 로그아웃
    path('logoutAPI/', views.LogoutAPI.as_view(), name='LogoutAPI'),
    ## 회원정보
    path('detailAPI/', views.UserDetailAPI.as_view(), name='UserDetailAPI'),
    # ## 회원수정
    # path('update/', views.UserUpdate.as_view(), name='update'),
    # ## 회원탈퇴
    # path('sginout', views.Signout.as_view(), name='signout'),


]