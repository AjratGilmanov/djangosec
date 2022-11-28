from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    form = {'form':f'''
    <form action="">
        <input type="text" name="fio" id="fio" placeholder="ФИО">
        <input type="email" name="email" id="email" placeholder="e-mail">
        <input type="radio" name="pol" id="pol" value="пол">
        <label for="pol">Ж</label>
        <input type="radio" name="pol" id="pol1">
        <label for="pol1">М</label>
        <input type="submit" value="submit">
    </form>
    '''}
    return render(request, "Gilmanovapp/index.html", context = form)

def about(request):
    aboutme = {'name':'Айрат', 'height':'1,70 м', 'weight':'60 кг', 'age':'16 лет'}
    return render(request, "Gilmanovapp/about.html", context = aboutme)

def contact(request):
    contactslov = {'tel': 89093144983, 'vk':'https://vk.com/ajratgilm', 'tg':'https://t.me/AjratGilmanov'}
    return render(request,"Gilmanovapp/contact.html", context = {'contactslov': contactslov})


def form(request):
    return render(request,'Gilmanovapp/form.html')