# pylint: disable=E1120, C0103
from __future__ import absolute_import
from django.urls import re_path, path
from django.views.generic import TemplateView
from games.views import pages as views


urlpatterns = [
    re_path('^/?$', views.GameList.as_view(), name='game_list'),
    re_path(r'^/year/(\d+)/?$',
            views.GameListByYear.as_view(),
            name='games_by_year'),
    re_path(r'^/genre/([\w-]+)/?$',
            views.GameListByGenre.as_view(),
            name='games_by_genre'),
    re_path(r'^/by/([\w-]+)/?$',
            views.GameListByCompany.as_view(),
            name='games_by_company'),
    re_path(r'^/platform/(?P<slug>[\w\-]+)/?$',
            views.GameListByPlatform.as_view(),
            name="games_by_plaform"),
    path('/publish/<int:game_id>',
         views.publish_game,
         name='game-publish'),
    path('/add-game/', views.submit_game, name='game-submit'),
    path('/game-submitted',
         TemplateView.as_view(template_name='games/submitted.html'),
         name="game-submitted"),

    path('/game-issue',
         views.submit_issue,
         name='game-submit-issue'),
    path('/banner/<slug:slug>.jpg',
         views.get_banner,
         name='get_banner'),
    path('/icon/<slug:slug>.png',
         views.get_icon,
         name='get_icon'),
    path('/install/<int:id>/view',
         views.view_installer,
         name='view_installer'),

    # Deprecated! Remove after 0.5.0 release!
    path('/install/<slug:slug>/',
         views.get_installers,
         name='get_installers'),

    re_path(r'/(?P<slug>[\w\-]+)/suggest-changes/?$',
            views.edit_game,
            name='game-edit'),
    path('/<slug:slug>/changes-submitted',
         views.changes_submitted,
         name='game-submitted-changes'),
    path('/<slug:slug>/installer/new',
         views.new_installer,
         name="new_installer"),
    re_path(r'/(?P<slug>[\w\-]+)/installer/edit/?$',
            views.edit_installer,
            name='edit_installer'),
    path('/<slug:slug>/installer/delete',
         views.delete_installer,
         name='delete_installer'),
    path('/<slug:slug>/installer/fork',
         views.fork_installer,
         name='fork_installer'),
    re_path(r'(?P<slug>[\w\-]+)/installer/publish/?$',
            views.publish_installer,
            name='publish_installer'),
    re_path(r'(?P<slug>[\w\-]+)/installer/complete/?$',
            views.installer_complete,
            name='installer_complete'),
    path('/installer/feed/',
         views.InstallerFeed(),
         name='installer_feed'),
    path('/installer/submissions',
         views.installer_submissions,
         name='installer_submissions'),

    re_path(r'/([\w\-]+)/screenshot/add/',
            views.screenshot_add,
            name='screenshot_add'),
    path('/screenshot/<int:screenshot_id>/publish/',
         views.publish_screenshot,
         name='publish_screenshot'),

    path('/game-for-installer/<slug:slug>/',
         views.game_for_installer,
         name='game_for_installer'),
    path('/<slug:slug>/',
         views.game_detail,
         name="game_detail"),
]
