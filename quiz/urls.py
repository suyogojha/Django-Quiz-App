from django.urls import re_path as url
import quiz.views as quiz_views

urlpatterns = [
	url(r'^$', quiz_views.qpage),	
]
