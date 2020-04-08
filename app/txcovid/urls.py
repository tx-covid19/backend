from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views.user import UserCreate
from .views.beiwe import BeiweDataView
from .views.tracker import TrackerListView
from .views.overview import OverviewView

urlpatterns = [
    path('user/create/', UserCreate.as_view(), name='create_user'),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('user/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('beiwe/', BeiweDataView.as_view()),
    path('tracker/', TrackerListView.as_view()),
    path('overview/', OverviewView.as_view())
]
