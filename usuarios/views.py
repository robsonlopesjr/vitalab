from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")

    elif request.method == "POST":
        primeiro_nome = request.POST.get("primeiro_nome")
        ultimo_nome = request.POST.get("ultimo_nome")
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if not senha == confirmar_senha:
            messages.add_message(
                request, messages.constants.ERROR, "As senhas não coincidem."
            )
            return redirect("/usuarios/cadastro")

        if len(senha) < 6:
            messages.add_message(
                request,
                messages.constants.ERROR,
                "Sua senha deve ter pelo menos 6 caracteres.",
            )
            return redirect("/usuarios/cadastro")

        try:
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )
            messages.add_message(
                request, messages.constants.SUCCESS, "Usuário cadastrado com sucesso!"
            )
        except:
            messages.add_message(
                request,
                messages.constants.ERROR,
                "Erro interno do sistema, contate um administrador.",
            )
            return redirect("/usuarios/cadastro")

        return redirect("/usuarios/cadastro")


def logar(request):
    if request.method == "GET":
        return render(request, "logar.html")

    elif request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)

            return redirect("/")
        else:
            messages.add_message(
                request, messages.constants.ERROR, "Usuario ou senha inválidos"
            )
            return redirect("/usuarios/login")
