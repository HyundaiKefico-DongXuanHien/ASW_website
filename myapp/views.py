from django.shortcuts import render

# Create your views here.

# ============================================================================
# FILE NAME     : myapp/views.py
# AUTHOR        : DONG XUAN HIEN
# DIVISION      : HYUNDAI KEFICO Co.,Ltd.
# DESCRIPTION   : Handle logic to display
# HISTORY       : 05/11/2025
# ============================================================================

def index(request):
    return render(request, 'index.html')
