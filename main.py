import customtkinter as ctk
from candidato import abrir_tela_candidato
from recrutador import abrir_tela_recrutador
from db import conectar_banco

# Função para exibir relatório de candidatos
def exibir_relatorio_candidatos():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, email, telefone, habilidades, experiencia FROM candidatos")
    candidatos = cursor.fetchall()
    conn.close()

    janela_relatorio = ctk.CTkToplevel()
    janela_relatorio.title("Relatório de Candidatos")
    janela_relatorio.geometry("600x400")

    texto_relatorio = ctk.CTkTextbox(janela_relatorio, width=580, height=380)
    texto_relatorio.grid(row=0, column=0, padx=10, pady=10)

    for candidato in candidatos:
        texto_relatorio.insert(ctk.END, f"Nome: {candidato[0]}\nEmail: {candidato[1]}\nTelefone: {candidato[2]}\nHabilidades: {candidato[3]}\nExperiência: {candidato[4]}\n\n")

    texto_relatorio.configure(state=ctk.DISABLED)

# Função para exibir relatório de vagas e candidatos recomendados
def exibir_relatorio_vagas():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, descricao, requisitos FROM vagas")
    vagas = cursor.fetchall()

    janela_relatorio = ctk.CTkToplevel()
    janela_relatorio.title("Relatório de Vagas")
    janela_relatorio.geometry("600x400")

    texto_relatorio = ctk.CTkTextbox(janela_relatorio, width=580, height=380)
    texto_relatorio.grid(row=0, column=0, padx=10, pady=10)

    for vaga in vagas:
        texto_relatorio.insert(ctk.END, f"Título: {vaga[1]}\nDescrição: {vaga[2]}\nRequisitos: {vaga[3]}\n\n")

        # Buscar os melhores candidatos para essa vaga
        cursor.execute(f'''
            SELECT nome, experiencia, habilidades, email, telefone
            FROM candidatos
            WHERE {" OR ".join([f"LOWER(habilidades) LIKE \'%{req.lower()}%\'" for req in vaga[3].split(", ")])}
        ''')
        candidatos = cursor.fetchall()

        texto_relatorio.insert(ctk.END, "Candidatos Recomendados:\n")
        if candidatos:
            for candidato in candidatos:
                texto_relatorio.insert(ctk.END, f"  - {candidato[0]} (Experiência: {candidato[1]})\n    Contato: {candidato[3]}, {candidato[4]}\n")
        else:
            texto_relatorio.insert(ctk.END, "  Nenhum candidato recomendado encontrado para esta vaga.\n")

        texto_relatorio.insert(ctk.END, "\n---------------------------------------------\n\n")

    texto_relatorio.configure(state=ctk.DISABLED)

# Função para abrir a tela principal
def abrir_tela_principal():
    janela_principal = ctk.CTk()
    janela_principal.title("Sistema de Recrutamento")
    janela_principal.geometry("800x400")

    ctk.CTkLabel(janela_principal, text="Bem-vindo ao Sistema de Recrutamento", anchor="center", font=("Arial", 16)).pack(pady=20)

    ctk.CTkButton(janela_principal, text="Cadastrar Candidato", command=abrir_tela_candidato).pack(pady=10)
    ctk.CTkButton(janela_principal, text="Cadastrar Vaga", command=abrir_tela_recrutador).pack(pady=10)

    ctk.CTkButton(janela_principal, text="Relatório de Candidatos", command=exibir_relatorio_candidatos).pack(pady=10)
    ctk.CTkButton(janela_principal, text="Relatório de Vagas", command=exibir_relatorio_vagas).pack(pady=10)

    janela_principal.mainloop()

if __name__ == "__main__":
    abrir_tela_principal()
