
from django.http import HttpRequest
from django.shortcuts import render, redirect

def is_mobile(request: HttpRequest):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    mobile_keywords = ['mobile', 'android', 'iphone', 'ipad', 'tablet']
    return any(keyword in user_agent for keyword in mobile_keywords)

# Exemplo de uso na View
