from django.shortcuts import render
from django.http import HttpResponse
import os

from django.shortcuts import render
from django.http import HttpResponse
import os

def get_links():
    directory = 'data'  # Replace with your actual directory
    links = {}

    for i in range(1, 5):
        file_path = os.path.join(directory, f'box{i}.txt')
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                links[f'box{i}'] = file.read().strip()
        else:
            links[f'box{i}'] = ''

    return links

def update_links(request):
    if request.method == 'POST':
        submit_btn_value = request.POST.get('submit_btn')
        box_value = request.POST.get(submit_btn_value, '')

        directory = 'data'  # Replace with your actual directory
        file_path = os.path.join(directory, f'{submit_btn_value}.txt')
        
        with open(file_path, 'w') as file:
            file.write(box_value)

    links = get_links()
    return render(request, 'link/index.html', {'links': links})
