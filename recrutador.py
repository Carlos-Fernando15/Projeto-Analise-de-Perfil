import customtkinter as ctk
from tkinter import messagebox
from db import conectar_banco

# Função para cadastrar vaga e recomendar candidatos com busca inteligente
def cadastrar_vaga():
    conn = conectar_banco()
    cursor = conn.cursor()

    if all([entrada_titulo.get(), entrada_descricao.get(), entrada_requisitos.get(), entrada_localizacao.get(), entrada_salario.get(), entrada_beneficios.get()]):
        cursor.execute('''
        INSERT INTO vagas (titulo, descricao, requisitos, localizacao, salario, beneficios)
        VALUES (?, ?, ?, ?, ?, ?)''', 
        (entrada_titulo.get(), entrada_descricao.get(), entrada_requisitos.get(), entrada_localizacao.get(), entrada_salario.get(), entrada_beneficios.get()))
        vaga_id = cursor.lastrowid
        conn.commit()

        # Exibir candidatos recomendados com busca inteligente
        recomendar_candidatos(vaga_id)
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
    
    conn.close()

# Função para recomendar candidatos com busca inteligente baseada em pontuação de compatibilidade
def recomendar_candidatos(vaga_id):
    conn = conectar_banco()
    cursor = conn.cursor()

    # Buscar detalhes da vaga
    cursor.execute("SELECT requisitos FROM vagas WHERE id = ?", (vaga_id,))
    vaga = cursor.fetchone()
    if vaga:
        requisitos_vaga = vaga[0].split(", ")  # Dividindo os requisitos para comparar com as habilidades dos candidatos

        # Buscar todos os candidatos
        cursor.execute("SELECT nome, experiencia, habilidades, email, telefone FROM candidatos")
        candidatos = cursor.fetchall()

        # Lista para armazenar os candidatos com suas respectivas pontuações
        candidatos_pontuados = []

        for candidato in candidatos:
            habilidades_candidato = candidato[2].split(", ")
            pontuacao = 0

            # Aumentar a pontuação se a habilidade do candidato corresponder ao requisito da vaga
            for habilidade in habilidades_candidato:
                if any(req.lower() in habilidade.lower() for req in requisitos_vaga):
                    pontuacao += 1

            if pontuacao > 0:
                candidatos_pontuados.append((pontuacao, candidato))

        # Ordenar os candidatos com base na pontuação (do mais compatível para o menos compatível)
        candidatos_pontuados.sort(reverse=True, key=lambda x: x[0])

        if candidatos_pontuados:
            exibir_candidatos_recomendados(candidatos_pontuados)
        else:
            messagebox.showinfo("Sem Resultados", "Nenhum candidato recomendado encontrado para esta vaga.")
    else:
        messagebox.showerror("Erro", "Vaga não encontrada.")

    conn.close()

# Função para exibir candidatos recomendados com base na busca inteligente
def exibir_candidatos_recomendados(candidatos_pontuados):
    janela_recomendados = ctk.CTkToplevel()
    janela_recomendados.title("Candidatos Recomendados")
    janela_recomendados.geometry("600x400")

    texto_recomendados = ctk.CTkTextbox(janela_recomendados, width=580, height=380)
    texto_recomendados.grid(row=0, column=0, padx=10, pady=10)

    for pontuacao, candidato in candidatos_pontuados:
        texto_recomendados.insert(ctk.END, f"Nome: {candidato[0]}\nExperiência: {candidato[1]}\nHabilidades: {candidato[2]}\nEmail: {candidato[3]}\nTelefone: {candidato[4]}\nPontuação: {pontuacao}\n\n")

    texto_recomendados.configure(state=ctk.DISABLED)

# Função para abrir a tela de cadastro de vaga
def abrir_tela_recrutador():
    janela_recrutador = ctk.CTkToplevel()
    janela_recrutador.title("Cadastro de Vaga")
    janela_recrutador.geometry("800x600")

    global entrada_titulo, entrada_descricao, entrada_requisitos, entrada_localizacao, entrada_salario, entrada_beneficios

    ctk.CTkLabel(janela_recrutador, text="Título da Vaga", anchor="w").grid(row=0, column=0, padx=20, pady=5, sticky="w")
    entrada_titulo = ctk.CTkEntry(janela_recrutador, width=600); entrada_titulo.grid(row=0, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_recrutador, text="Descrição", anchor="w").grid(row=1, column=0, padx=20, pady=5, sticky="w")
    entrada_descricao = ctk.CTkEntry(janela_recrutador, width=600); entrada_descricao.grid(row=1, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_recrutador, text="Requisitos", anchor="w").grid(row=2, column=0, padx=20, pady=5, sticky="w")
    entrada_requisitos = ctk.CTkEntry(janela_recrutador, width=600); entrada_requisitos.grid(row=2, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_recrutador, text="Localização", anchor="w").grid(row=3, column=0, padx=20, pady=5, sticky="w")
    entrada_localizacao = ctk.CTkEntry(janela_recrutador, width=600); entrada_localizacao.grid(row=3, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_recrutador, text="Salário", anchor="w").grid(row=4, column=0, padx=20, pady=5, sticky="w")
    entrada_salario = ctk.CTkEntry(janela_recrutador, width=600); entrada_salario.grid(row=4, column=1, padx=20, pady=5)

    ctk.CTkLabel(janela_recrutador, text="Benefícios", anchor="w").grid(row=5, column=0, padx=20, pady=5, sticky="w")
    entrada_beneficios = ctk.CTkEntry(janela_recrutador, width=600); entrada_beneficios.grid(row=5, column=1, padx=20, pady=5)

    ctk.CTkButton(janela_recrutador, text="Cadastrar Vaga e Recomendar Candidatos", command=cadastrar_vaga).grid(row=6, columnspan=2, pady=20)
