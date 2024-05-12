
from django.urls import path, include
from.views import *


urlpatterns = [
    # path('chatbot/', chatbot, name='chatbot'),
    path('generate/', generate_slides, name='generate'),
    path('generate-slides/', GenerateSlidesAPIView.as_view(), name='generate_slides_api'),
    path('zlide/<int:pk>/', ZlideDetailView.as_view(), name='zlide-detail'),
]