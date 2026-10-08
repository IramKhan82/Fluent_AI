from django.urls import path
from . import views


urlpatterns = [

    path("", views.landing, name="landing"),

    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "api/dashboard-stats/",
        views.dashboard_stats_api,
        name="dashboard_stats_api"
    ),

    path(
        "learning-path/",
        views.learning_path,
        name="learning_path"
    ),

    path(
        "lesson/<int:lesson_id>/",
        views.lesson_detail,
        name="lesson_detail"
    ),

    path(
        "lesson/<int:lesson_id>/complete/",
        views.complete_lesson,
        name="complete_lesson"
    ),

    path(
        "lesson/<int:lesson_id>/test/",
        views.lesson_test,
        name="lesson_test"
    ),

    path(
        "practice/",
        views.practice,
        name="practice"
    ),

    path(
        "practice/<str:practice_type>/submit/",
        views.practice_submit,
        name="practice_submit"
    ),

    path("games/", views.games, name="games"),

    path(
        "games/<str:game_type>/",
        views.game_page,
        name="game_page"
    ),

    path(
        "games/save/",
        views.save_game_result,
        name="save_game_result"
    ),

    path(
        "leaderboard/",
        views.leaderboard,
        name="leaderboard"
    ),

    path(
        "assessment/",
        views.assessment,
        name="assessment"
    ),

    path(
        "assessment/writing/<int:attempt_id>/",
        views.assessment_writing,
        name="assessment_writing"
    ),

    path(
        "assessment/result/<int:attempt_id>/",
        views.assessment_result,
        name="assessment_result"
    ),

    path(
        "ai-tutor/",
        views.ai_tutor,
        name="ai_tutor"
    ),

    path(
        "vnotes/",
        views.vnotes,
        name="vnotes"
    ),

    path(
        "profile/",
        views.profile,
        name="profile"
    ),

    path(
        "settings/",
        views.settings_view,
        name="settings"
    ),

##ik
    path(
        "learning-path/<str:module_name>/",
        views.module_detail,
        name="module_detail"
    ),
]

