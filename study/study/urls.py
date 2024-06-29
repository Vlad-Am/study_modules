from django.urls import path

from .apps import StudyConfig
from .views import StudyCreateAPIView, StudyListAPIView, StudyUpdateAPIView, StudyDestroyAPIView, StudyRetrieveAPIView

app_name = StudyConfig.name

urlpatterns = [
    path('lesson/create/', StudyCreateAPIView.as_view(), name='study_create'),  # Создание
    path('lesson/', StudyListAPIView.as_view(), name='study_list'),  # Список
    path('lesson/<int:pk>/update', StudyUpdateAPIView.as_view(), name='study_update'),  # Редактирование
    path('lesson/<int:pk>/delete', StudyDestroyAPIView.as_view(), name='study_delete'),  # Удаление
    path('lesson/<int:pk>/', StudyRetrieveAPIView.as_view(), name='study_retrieve'),  # Просмотр
]
