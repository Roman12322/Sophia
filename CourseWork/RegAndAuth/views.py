from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import User
from .forms import ShiphrForm
from .models import Message
from django.db.utils import IntegrityError
from django.contrib import messages
from django.core.files import File
import os


def showRegHTML(request):
    return render(request, 'Registration/registration.html')

def showCheckMessagesHTML(request):
    return render(request, 'CheckMessages/checkmessages.html')

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
    form = ShiphrForm(request.POST, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        username = request.POST.get("Log")
        password = request.POST.get("pass")

        try:
            checkUserLogin = User.objects.get(Login=username, Password=password)
            rb = request.POST.get("RB", None)
            if rb in ["Decrypt", "Encrypt"]:
                if rb == "Encrypt":
                    if checkUserLogin is not None:
                        ChosenFile = request.FILES['chosenFile']
                        chosenFile = ChosenFile.name
                        path = os.path.abspath(chosenFile)
                        chsFile = open(path, 'a')
                        myfile = File(chsFile)
                        msg = form.cleaned_data['Mess']
                        key = form.cleaned_data['Key']
                        EncMes = encrypt(msg, key)
                        tmp = Message.objects.create(EncryptMessage=EncMes, Mess=msg, Username_Id=checkUserLogin.id)
                        myfile.write("\nYour encrypted message: "+EncMes)
                        myfile.closed
                        messages.success(request, "Your encrypted message: " + EncMes)
                        return HttpResponseRedirect("http://127.0.0.1:8000/encrypter")
                elif rb == "Decrypt":
                    if checkUserLogin is not None:
                        msg = form.cleaned_data['Mess']
                        key = form.cleaned_data['Key']
                        try:
                            tmp = Message.objects.filter(EncryptMessage=msg, Username_Id=checkUserLogin.id)
                            if tmp is not None:
                                EncMes = decrypt(msg, key)
                                messages.success(request, "Your Decrypted message: " + EncMes)
                                return HttpResponseRedirect("http://127.0.0.1:8000/encrypter")
                        except Message.DoesNotExist:
                            messages.error(request, "Message is not found")
                            return HttpResponseRedirect("http://127.0.0.1:8000/encrypter")
        except User.DoesNotExist:
            messages.error(request, "Wrong login or password")
            return HttpResponseRedirect("http://127.0.0.1:8000/encrypter")
    return HttpResponseRedirect("http://127.0.0.1:8000/encrypter")

def encrypt(message, key):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.!?1234567890@#$%^&*()_-" \
               "+:;\/[]{}~`<>|"

    if len(message) == 0  or len(key) == 0:
        encrypted = "Error"
        return encrypted
    else:
        letter_to_index = dict(zip(alphabet, range(len(alphabet))))
        index_to_letter = dict(zip(range(len(alphabet)), alphabet))
        encrypted = ""
        split_message = [
            message[i : i + len(key)] for i in range(0, len(message), len(key))
        ]

        for each_split in split_message:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
                encrypted += index_to_letter[number]
                i += 1

        return encrypted

def decrypt(cipher, key):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.!?1234567890@#$%^&*()_-" \
               "+:;\/[]{}~`<>|"

    if len(cipher) == 0  or len(key) == 0:
        encrypted = "Error"
        return encrypted
    else:
        letter_to_index = dict(zip(alphabet, range(len(alphabet))))
        index_to_letter = dict(zip(range(len(alphabet)), alphabet))
        decrypted = ""
        split_encrypted = [
            cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
        ]

        for each_split in split_encrypted:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
                decrypted += index_to_letter[number]
                i += 1

        return decrypted

def CheckMessagesInDB(request):
    if request.method == "POST":
        username = request.POST.get("Log")
        password = request.POST.get("pass")
        try:
            checkUserLogin = User.objects.get(Login=username, Password=password)
            if checkUserLogin is not None:
                MesUser = Message.objects.filter(Username_Id=checkUserLogin.id)
                return render(request, "CheckMessages/checkmessages.html", {"MessFromUser": MesUser})
            else:
                messages.error(request, "Wrong login or password")
                return HttpResponseRedirect("http://127.0.0.1:8000/CheckMessages/")
        except User.DoesNotExist:
            messages.error(request, "Wrong login or password")
            return HttpResponseRedirect("http://127.0.0.1:8000/CheckMessages/")
    return HttpResponseRedirect("http://127.0.0.1:8000/CheckMessages/")