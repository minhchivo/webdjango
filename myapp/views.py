from django.shortcuts import render
from django.http import HttpResponse
import subprocess

def home(request):
    return render(request, 'myapp/index.html')

def play_game(request):
    # Chạy file game.py
    try:
        subprocess.Popen(['python', r'C:\Users\USER\Documents\vscode\code python\2048_game_new\game.py'])
        return HttpResponse("Game is running! Please check your local window to play.")
    except Exception as e:
        return HttpResponse(f"Error running the game: {e}")
    