from django.shortcuts import render

finches = [
  { 'name': 'Lucy', 'breed': 'Cardinal', 'description': 'this bird is red'},
  { 'name': 'Harvey', 'breed': 'Blue Jay', 'description': 'this bird is Canadian' }
]
# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })