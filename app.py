# Interface da calculadora de Valproato
import customtkinter as ctk
from tkinter import ttk
from calculadora import calcular_mensal

ctk.set_appearance_mode("dark")

janela = ctk.CTk()
janela.title("Calculadora Valproato (Depakene)")
janela.geometry("860x620")

# titulo
titulo = ctk.CTkLabel(janela, text="Calculadora Valproato", font=("Arial", 20, "bold"))
titulo.pack(pady=(15, 0))
sub = ctk.CTkLabel(janela, text="Caixa com 50 cp - sem fracionar caixa")
sub.pack(pady=(0, 10))

# campos
campo_frame = ctk.CTkFrame(janela)
campo_frame.pack(padx=16, pady=5, fill="x")

ctk.CTkLabel(campo_frame, text="Miligramagem (250 ou 500)").grid(row=0, column=0, padx=10, pady=5)
ctk.CTkLabel(campo_frame, text="Meses").grid(row=0, column=1, padx=10, pady=5)
ctk.CTkLabel(campo_frame, text="Comprimidos por mes").grid(row=0, column=2, padx=10, pady=5)
ctk.CTkLabel(campo_frame, text="Sobra inicial").grid(row=0, column=3, padx=10, pady=5)

entry_mg = ctk.CTkEntry(campo_frame)
entry_mg.insert(0, "500")
entry_mg.grid(row=1, column=0, padx=10, pady=5)

entry_meses = ctk.CTkEntry(campo_frame, placeholder_text="ex: 6")
entry_meses.grid(row=1, column=1, padx=10, pady=5)

entry_cp = ctk.CTkEntry(campo_frame, placeholder_text="ex: 60")
entry_cp.grid(row=1, column=2, padx=10, pady=5)

entry_sobra = ctk.CTkEntry(campo_frame)
entry_sobra.insert(0, "0")
entry_sobra.grid(row=1, column=3, padx=10, pady=5)

lbl_erro = ctk.CTkLabel(campo_frame, text="", text_color="red")
lbl_erro.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

lbl_total = ctk.CTkLabel(janela, text="Preencha os dados e clique em Calcular.", font=("Arial", 14))
lbl_total.pack(pady=10)

botao = ctk.CTkButton(campo_frame, text="Calcular")
botao.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# tabela preta e simples
tabela = ttk.Treeview(janela, columns=("Mes", "Caixas", "Sobra"), show="headings", height=12)
tabela.heading("Mes", text="Mês")
tabela.heading("Caixas", text="Caixas")
tabela.heading("Sobra", text="Sobra pro prox. mes")
tabela.column("Mes", width=150, anchor="center")
tabela.column("Caixas", width=150, anchor="center")
tabela.column("Sobra", width=150, anchor="center")
tabela.pack(padx=16, pady=10, fill="both", expand=True)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="black", fieldbackground="black", foreground="white", rowheight=28)
style.configure("Treeview.Heading", background="#1a1a1a", foreground="white")


def calcular():
    lbl_erro.configure(text="")

    try:
        mg = int(entry_mg.get())
        meses = int(entry_meses.get())
        cp = int(entry_cp.get())
        sobra = int(entry_sobra.get())
    except:
        lbl_erro.configure(text="Digite apenas numeros inteiros.")
        return

    try:
        r = calcular_mensal(mg, meses, cp, sobra)
    except ValueError as e:
        lbl_erro.configure(text=str(e))
        return

    for i in tabela.get_children():
        tabela.delete(i)

    for linha in r["linhas"]:
        tabela.insert("", "end", values=(linha["mes"], linha["caixas"], linha["sobra_final"]))

    lbl_total.configure(text="Total de caixas: %d   |   Sobra final: %d cp" % (r["total_caixas"], r["sobra_final"]))


botao.configure(command=calcular)

janela.mainloop()
