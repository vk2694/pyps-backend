

from django.urls import URLPattern
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from demo.views import userCRUD, projectCRUD, taskCRUD

urlpatterns = [
    # User
    path('form/v1/user',csrf_exempt(userCRUD.as_view())),

    # Project
    path('form/v1/project', csrf_exempt(projectCRUD.as_view())),

    # Tasks
    path('form/v1/task', csrf_exempt(taskCRUD.as_view())),
]