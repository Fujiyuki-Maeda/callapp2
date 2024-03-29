from django.urls import path
#views.pyからimport
from . import views
from .views import TaskCreate,TaskList,TaskDetail,TaskDelete,TaskListLoginView,TaskUpdate,RegisterCallApp,HomeTemplateView
from django.contrib.auth.views import LogoutView
#urlや関数をviewに渡す

urlpatterns = [
    path("",TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/",TaskDetail.as_view(), name="task"),
    path("create-task/",TaskCreate.as_view(), name="create-task"),
    path("edit-task/<int:pk>/",TaskUpdate.as_view(), name="edit-task"),
    path("delete-task/<int:pk>/",TaskDelete.as_view(), name="delete-task"),
    path("login/",TaskListLoginView.as_view(), name="login"),
    path("logout/",LogoutView.as_view(next_page="login"), name="logout"),
    path("register/",RegisterCallApp.as_view(), name="register"),
    path("index/",HomeTemplateView.as_view(template_name = "callapp/index.html"), name="blogs"),
    
    
]
