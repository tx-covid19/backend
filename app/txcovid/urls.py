from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views.beiwe import BeiweDataSubmit
from .views.overview import OverviewView
from .views.tracker import TrackerListView
from .views.user import UserCreate, UserProfile

urlpatterns = [
    path('user/create/', UserCreate.as_view(), name='create_user'),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('user/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/profile', UserProfile.as_view(), name='user_profile'),

    path('beiwe/submit/', BeiweDataSubmit.as_view()),
    path('tracker/', TrackerListView.as_view()),
    path('overview/', OverviewView.as_view())
]
