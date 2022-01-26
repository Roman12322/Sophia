from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import User
from .forms import ShiphrForm
from .models import Message
from django.db.utils import IntegrityError
from django.contrib import messages


def showRegHTML(request):
    return render(request, 'Registration/registration.html')

def signUpUser(request):
    try:
        if request.method == "POST":
            user = User()
            checkLogin = request.POST.get("username")
            checkPass = request.POST.get("pass")
            if len(checkLogin) > 4 and len(checkPass) > 4:
                user.Login = request.POST.get("username")
                user.Password = request.POST.get("pass")
                user.save()
                return HttpResponseRedirect("http://127.0.0.1:8000/encrypter")
            else:
                messages.error(request, 'Login and password must be over 4 letters')
                return redirect('http://127.0.0.1:8000/')
    except IntegrityError:
        messages.error(request, 'User with this login is already exist')
        return redirect('http://127.0.0.1:8000/')

def showEncrypterHTML(request):
    form = ShiphrForm()
    data = {
        'form': form
    }
    return render(request, 'Encrypter/encrypter.html', data)

def Encr(request):
    form = ShiphrForm(request.POST)
    if request.method == "POST" and form.is_valid():
        username = request.POST.get("Log")
        password = request.POST.get("pass")
        try:
            checkUserLogin = User.objects.get(Login=username, Password=password)
            if checkUserLogin is not None:
                msg = form.cleaned_data['Mess']
                key = form.cleaned_data['Key']
                mapped_key = msg_and_key(msg, key)
                EncMes = cipher_encryption(msg, mapped_key)
                tmp = Message.objects.create(EncryptMessage=EncMes, Mess=msg, Username_Id=checkUserLogin.id)
                messages.success(request, "Your encrypted message: "+EncMes)
                return HttpResponseRedirect("http://127.0.0.1:8000/encrypter")
        except User.DoesNotExist:
            messages.error(request, "Wrong login or password")
            return HttpResponseRedirect("http://127.0.0.1:8000/encrypter")
    return HttpResponseRedirect("http://127.0.0.1:8000/encrypter")

def msg_and_key(msg, key):
    if msg == '' or key == '':
        key_map = 'Error'
        return key_map
    else:
        key_map = ""
        j = 0
        for i in range(len(msg)):
            if 1040 <= ord(msg[i]) <= 1071:
                if j < len(key):
                    key_map += key[j].upper()
                    j += 1
                else:
                    j = 0
                    key_map += key[j].upper()
                    j += 1
            elif 1072 <= ord(msg[i]) <= 1103:
                if j < len(key):
                    key_map += key[j]
                    j += 1
                else:
                    j = 0
                    key_map += key[j]
                    j += 1
            else:
                key_map += " "
        return key_map

def create_vigenere_table():
    table = []
    for i in range(32):
        table.append([])
    for row in range(32):
        for column in range(32):
            if (row + 1040) + column > 1071:
                table[row].append(chr((row + 1040) + column - 32))
            else:
                table[row].append(chr((row + 1040) + column))
    return table

def create_vigenere_table_1():
    table = []
    for i in range(32):
        table.append([])
    for row in range(32):
        for column in range(32):
            if (row + 1072) + column > 1103:
                table[row].append(chr((row + 1072) + column - 32))
            else:
                table[row].append(chr((row + 1072) + column))
    return table

def cipher_encryption(message, mapped_key):
    table = create_vigenere_table()
    table1 = create_vigenere_table_1()
    encrypted_text = ""
    if mapped_key == 'Error':
        return encrypted_text
    for i in range(len(message)):
        if 1071 >= ord(message[i]) >= 1040:
            row = ord(message[i]) - 1040
            column = ord(mapped_key[i]) - 1040
            encrypted_text += table[row][column]
        elif 1072 <= ord(message[i]) <= 1103:
            row = ord(message[i]) - 1072
            column = ord(mapped_key[i]) - 1072
            encrypted_text += table1[row][column]
        else:
            encrypted_text += message[i]
    return encrypted_text