from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("this is the index page")

def calculator(request):
    try:
        if request.method == "POST":
            n1 = 0
            n2 = 0
            c = 0
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == '+':
                c = n1+n2
            elif opr == '*':
                c = n1*n2
            elif opr == '-':
                c = n1-n2
            else:
                c = n1/n2
    except :
        c = "invalid operation"
    data = {
        'num11' : n1,
        'num21' : n2,
        'c' : c
    }
    return render(request, "calculator.html", data)
