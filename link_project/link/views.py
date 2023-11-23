from django.shortcuts import render
from django.http import HttpResponse
import os

def save_data(request):
    if request.method == 'POST':
        submit_btn_value = request.POST.get('submit_btn')
        box_value = request.POST.get(submit_btn_value, '')

        # Create a directory named 'data' if it doesn't exist
        directory = 'data'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Save the box value to a text file
        file_path = os.path.join(directory, f'{submit_btn_value}.txt')
        with open(file_path, 'w') as file:
            file.write(box_value)

        return HttpResponse(f'Data saved successfully for {submit_btn_value}.')

    return HttpResponse('Invalid request method.')

def index(request):
    return render(request, 'link/index.html')