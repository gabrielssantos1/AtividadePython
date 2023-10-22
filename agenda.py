# -*- coding: utf-8 -*-
"""Agenda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dPkbIDEe8j55WYqpyPHRILTp1ZGjyYUu
"""
#02: Agenda

import csv
import os

# Criar um arquivo CSV se não existir

def criar_arquivo_csv():
    if not os.path.exists('agenda.csv'):
        with open('agenda.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Telefone"])

# Adicionar um contato à agenda

def adiciona_contato(nome, telefone):
    with open('agenda.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, telefone])
    print(f"Contato {nome} adicionado com sucesso!")

# Listar todos os contatos na agenda

def listar_contatos():
    with open('agenda.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Pule o cabeçalho
        for row in reader:
            print(f"Nome: {row[0]}, Telefone: {row[1]}")

# Função para buscar um contato pelo nome

def buscar_contato(nome):
    with open('agenda.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Pule o cabeçalho
        for row in reader:
            if row[0] == nome:
                print(f"Contato encontrado - Nome: {row[0]}, Telefone: {row[1]}")
                return
        print(f"Contato não encontrado")

# Função para remover um contato pelo nome

def remover_contato(nome):
    with open('agenda.csv', 'r', newline='') as file:
        lines = list(csv.reader(file))
    removed = False
    with open('agenda.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Telefone"])  # Escreve o cabeçalho
        for row in lines:
            if row[0] == nome:
                print(f"Contato {nome} removido com sucesso!")
                removed = True
            else:
                writer.writerow(row)
    if not removed:
        print(f"Contato não encontrado")

# Cria o arquivo CSV se não existir

criar_arquivo_csv()
while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        adicionar_contato(nome, telefone)
    elif escolha == "2":
        print("\nLista de contatos:")
        listar_contatos()
    elif escolha == "3":
        nome = input("Nome a ser buscado: ")
        buscar_contato(nome)
    elif escolha == "4":
        nome = input("Nome a ser removido: ")
        remover_contato(nome)
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
