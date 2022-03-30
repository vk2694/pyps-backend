import json
from tkinter import E
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from demo.models import Users, Projects, ProjectTasks

# Create your views here.

class userCRUD(View):
    # Get the User list
    def get(self, request):
        try:
            userList = list(Users.objects.values())
        except Exception as e:
            raise e

        return JsonResponse({'response': userList, 'status': 200})
    
    # Create a User
    def post(self, request):
        user_data = json.loads(request.body)

        try:
            user_created = Users.objects.create(**user_data)
        except Exception as e:
            raise e

        if user_created:
            return JsonResponse({'response': 'User has been created Successfully!', 'status': 200})
        else:
            return JsonResponse({'response': 'User not created, Please try again later!', 'status': 400})

    # Update a User
    def put(self, request):
        user_data = json.loads(request.body)
        user_id = request.GET['user_id']

        try:
            user_updated = Users.objects.filter(id=user_id).update(**user_data)
        except Exception as e:
            raise e
            
        if user_updated:
            return JsonResponse({'response': 'User has been updated Successfully!', 'status': 200})
        else:
            return JsonResponse({'response': 'User not updated, Please try again later!', 'status': 400})

    # Delete a User
    def delete(self, request):
        user_id = request.GET['user_id']
        try:
            Users.objects.filter(id=user_id).delete()
        except Exception as e:
            raise e

        return JsonResponse({'response': 'User deleted successfully!', 'status': 202})

class projectCRUD(View):
    # Get the Project list
    def get(self, request):
        try:
            projectList = Projects.objects.all()
        except Exception as e:
            raise e

        return JsonResponse({'response': projectList, 'status': 200})
    
    # Create a Project
    def post(self, request):
        project_data = json.loads(request.body)

        try:
            project_created = Projects.objects.create(**project_data)
        except Exception as e:
            raise e

        if project_created:
            return JsonResponse({'response': 'Project has been created Successfully!', 'status': 200})
        else:
            return JsonResponse({'response': 'Project not created, Please try again later!', 'status': 400})
    
    # Update a Project
    def put(self, request):
        project_data = json.loads(request.body)
        project_id = request.GET['project_id']

        try:
            project_updated = Projects.objects.filter(id=project_id).update(**project_data)
        except Exception as e:
            raise e
            
        if project_updated:
            return JsonResponse({'response': 'Project has been updated Successfully!', 'status': 200})
        else:
            return JsonResponse({'response': 'Project not updated, Please try again later!', 'status': 400})

    # Delete a Project
    def delete(self, request):
        project_id = request.GET['project_id']
        try:
            Projects.objects.filter(id=project_id).delete()
        except Exception as e:
            raise e

        return JsonResponse({'response': 'Project deleted successfully!', 'status': 202})


class taskCRUD(View):
    # Get the Task list
    def get(self, request):
        project_id = request.GET['project_id']
        try:
            taskList = ProjectTasks.objects.filter(project_id=project_id).all()
        except Exception as e:
            raise e

        return JsonResponse({'response': taskList, 'status': 200})
    
    # Create a Task
    def post(self, request):
        task_data = json.loads(request.body)

        try:
            task_created = ProjectTasks.objects.create(**task_data)
        except Exception as e:
            raise e

        if task_created:
            return JsonResponse({'response': 'Task has been created Successfully!', 'status': 200})
        else:
            return JsonResponse({'response': 'Task not created, Please try again later!', 'status': 400})
    
    # Update a Task
    def put(self, request):
        task_data = json.loads(request.body)
        task_id = request.GET['task_id']

        try:
            task_updated = ProjectTasks.objects.filter(id=task_id).update(**task_data)
        except Exception as e:
            raise e
            
        if task_updated:
            return JsonResponse({'response': 'Task has been updated Successfully!', 'status': 200})
        else:
            return JsonResponse({'response': 'Task not updated, Please try again later!', 'status': 400})

    # Delete a Task
    def delete(self, request):
        task_id = request.GET['task_id']
        try:
            ProjectTasks.objects.filter(id=task_id).delete()
        except Exception as e:
            raise e

        return JsonResponse({'response': 'Task deleted successfully!', 'status': 202})     