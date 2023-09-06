from django.shortcuts import render

def for_loop(request):
    context = {'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']}
    return render(request, 'w3school/for.html', context)

def for_counter0(request):
    context = {'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']}
    return render(request, 'w3school/for_counter0.html', context)

def for_first(request):
    context = {'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']}
    return render(request, 'w3school/for.first.html', context)

def for_last(request):
    context = {'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']}
    return render(request, 'w3school/for.last.html', context)

def for_parent(request):
   #context = {'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
   context = {'cars': ['Ford', 'Volvo', 'BMW'],
              'colors': ['Red', 'Green', 'Blue']}
   return render(request, 'w3school/for.parent.html', context)


