import customtkinter as ctk
from tkinter import messagebox
from db import conectar_banco

def cadastrar_candidato():
    conn = conectar_banco()
    cursor = conn.cursor()

    if all([entrada_nome.get(), entrada_email.get(), entrada_telefone.get(), entrada_habilidades.get(), entrada_experiencia.get(), entrada_formacao.get(),
            entrada_endereco.get(), entrada_data_nascimento.get(), entrada_objetivo.get(), entrada_idiomas.get(), entrada_certificacoes.get(), entrada_linkedin.get()]):
        cursor.execute('''
        INSERT INTO candidatos (nome, email, telefone, habilidades, experiencia, formacao, endereco, data_nascimento, objetivo_profissional, idiomas, certificacoes, linkedin)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (entrada_nome.get(), entrada_email.get(), entrada_telefone.get(), entrada_habilidades.get(), entrada_experiencia.get(), entrada_formacao.get(),
         entrada_endereco.get(), entrada_data_nascimento.get(), entrada_objetivo.get(), entrada_idiomas.get(), entrada_certificacoes.get(), entrada_linkedin.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Candidato cadastrado com sucesso!")
        limpar_campos()
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")

def limpar_campos():
    entrada_nome.delete(0, ctk.END)
    entrada_email.delete(0, ctk.END)
    entrada_telefone.delete(0, ctk.END)
    entrada_habilidades.delete(0, ctk.END)
    entrada_experiencia.delete(0, ctk.END)
    entrada_formacao.delete(0, ctk.END)
    entrada_endereco.delete(0, ctk.END)
    entrada_data_nascimento.delete(0, ctk.END)
    entrada_objetivo.delete(0, ctk.END)
    entrada_idiomas.delete(0, ctk.END)
    entrada_certificacoes.delete(0, ctk.END)
    entrada_linkedin.delete(0, ctk.END)

def abrir_tela_candidato():
    janela_candidato = ctk.CTkToplevel()
    janela_candidato.title("Cadastro de Candidato")
    janela_candidato.geometry("600x700")

    global entrada_nome, entrada_email, entrada_telefone, entrada_habilidades, entrada_experiencia, entrada_formacao
    global entrada_endereco, entrada_data_nascimento, entrada_objetivo, entrada_idiomas, entrada_certificacoes, entrada_linkedin

    # Configuração da grade para melhor layout
    for i in range(12):
        janela_candidato.grid_rowconfigure(i, weight=1)
    janela_candidato.grid_columnconfigure(0, weight=1)
    janela_candidato.grid_columnconfigure(1, weight=2)

    # Campos de cadastro do candidato
    ctk.CTkLabel(janela_candidato, text="Nome", anchor="w").grid(row=0, column=0, padx=20, pady=5, sticky="w")
    entrada_nome = ctk.CTkEntry(janela_candidato, width=400); entrada_nome.grid(row=0, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="Email", anchor="w").grid(row=1, column=0, padx=20, pady=5, sticky="w")
    entrada_email = ctk.CTkEntry(janela_candidato, width=400); entrada_email.grid(row=1, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="Telefone", anchor="w").grid(row=2, column=0, padx=20, pady=5, sticky="w")
    entrada_telefone = ctk.CTkEntry(janela_candidato, width=400); entrada_telefone.grid(row=2, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="Habilidades", anchor="w").grid(row=3, column=0, padx=20, pady=5, sticky="w")
    entrada_habilidades = ctk.CTkEntry(janela_candidato, width=400); entrada_habilidades.grid(row=3, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="Experiência", anchor="w").grid(row=4, column=0, padx=20, pady=5, sticky="w")
    entrada_experiencia = ctk.CTkEntry(janela_candidato, width=400); entrada_experiencia.grid(row=4, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="Formação", anchor="w").grid(row=5, column=0, padx=20, pady=5, sticky="w")
    entrada_formacao = ctk.CTkEntry(janela_candidato, width=400); entrada_formacao.grid(row=5, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="Endereço", anchor="w").grid(row=6, column=0, padx=20, pady=5, sticky="w")
    entrada_endereco = ctk.CTkEntry(janela_candidato, width=400); entrada_endereco.grid(row=6, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="Data de Nascimento", anchor="w").grid(row=7, column=0, padx=20, pady=5, sticky="w")
    entrada_data_nascimento = ctk.CTkEntry(janela_candidato, width=400); entrada_data_nascimento.grid(row=7, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="Objetivo Profissional", anchor="w").grid(row=8, column=0, padx=20, pady=5, sticky="w")
    entrada_objetivo = ctk.CTkEntry(janela_candidato, width=400); entrada_objetivo.grid(row=8, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="Idiomas", anchor="w").grid(row=9, column=0, padx=20, pady=5, sticky="w")
    entrada_idiomas = ctk.CTkEntry(janela_candidato, width=400); entrada_idiomas.grid(row=9, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="Certificações", anchor="w").grid(row=10, column=0, padx=20, pady=5, sticky="w")
    entrada_certificacoes = ctk.CTkEntry(janela_candidato, width=400); entrada_certificacoes.grid(row=10, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_candidato, text="LinkedIn", anchor="w").grid(row=11, column=0, padx=20, pady=5, sticky="w")
    entrada_linkedin = ctk.CTkEntry(janela_candidato, width=400); entrada_linkedin.grid(row=11, column=1, padx=20, pady=5)

    ctk.CTkButton(janela_candidato, text="Cadastrar", command=cadastrar_candidato).grid(row=12, columnspan=2, pady=20)
