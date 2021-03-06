from django.conf.urls import url

from resources.api import ResourceListAPIView, ResourceDetailAPIView, ResourceVotesAPIView
from votes.api import VoteListAPIView, VoteDetailAPIView
from userprofile.api import NotificationListAPIView, \
    NotificationDetailAPIView, FollowDetailAPIView, \
    FollowListAPIView, UserProfileDetailAPIView, \
    UserProfileListAPIView, LanguageDetailAPIView, LanguageListAPIView
from comments.api import CommentListAPIView, CommentDetailAPIView
from pairprogram.api import SessionDetailAPIView, SessionListAPIView,\
    ParticipantDetailAPIView, ParticipantListAPIView
from account.api import UserRegisterAPIView, UserLogoutAPIView
from account.api import UserListAPIView, UserDetailAPIView, UserFollowAPIView
from account.api import UserSettingsAPIView, ContactAPIView


urlpatterns = [
    url(r'auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'auth/logout/', UserLogoutAPIView.as_view(), name='logout'),
    url(r'auth/register/', UserRegisterAPIView.as_view(), name='register'),
    url(r'^resources/$', ResourceListAPIView.as_view()),
    url(r'^resources/(?P<pk>[0-9]+)/$', ResourceDetailAPIView.as_view()),
    url(r'^resources/(?P<pk>[0-9]+)/votes/$', ResourceVotesAPIView.as_view()),
    url(r'^votes/', VoteListAPIView.as_view()),
    url(r'^votes/(?P<pk>[0-9]+)', VoteDetailAPIView.as_view()),
    url(r'^userprofile/$', UserProfileListAPIView.as_view()),
    url(r'^userprofile/(?P<pk>[0-9]+)', UserProfileDetailAPIView.as_view()),
    url(r'^userprofile/follows/', FollowListAPIView.as_view()),
    url(r'^userprofile/follows/(?P<pk>[0-9]+)', FollowDetailAPIView.as_view()),
    url(r'^userprofile/languages/', LanguageListAPIView.as_view()),
    url(r'^userprofile/languages/(?P<pk>[0-9]+)',
        LanguageDetailAPIView.as_view()),
    url(r'^userprofile/notifications/', NotificationListAPIView.as_view()),
    url(r'^userprofile/notifications/(?P<pk>[0-9]+)',
        NotificationDetailAPIView.as_view()),
    url(r'^resources/(?P<pk>[0-9]+)/comments/$', CommentListAPIView.as_view()),
    url(r'^resources/(?P<resource_id>[0-9]+)/comments/(?P<pk>[0-9]+)/$',
        CommentDetailAPIView.as_view()),
    url(r'^pairprogram/sessions/$', SessionListAPIView.as_view()),
    url(r'^pairprogram/sessions/(?P<pk>[0-9]+)/$',
        SessionDetailAPIView.as_view()),
    url(r'^pairprogram/sessions/(?P<session_id>[0-9]+)/participants/$',
        ParticipantListAPIView.as_view()),
    url(r'^pairprogram/sessions/(?P<session_id>[0-9]+)/participants/(?P<id>[0-9]+)/$',
        ParticipantDetailAPIView.as_view()),

    url(r'^users/$', UserListAPIView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', UserDetailAPIView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/follow/', UserFollowAPIView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/settings/', UserSettingsAPIView.as_view()),
    url(r'^contact/$', ContactAPIView.as_view(), name='contact')

]
