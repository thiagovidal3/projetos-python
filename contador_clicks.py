import tkinter as tk

janela = tk.Tk()
janela.geometry('500x500')
janela.title('Contador de clicks')
janela.configure(background='#1d1d1d')

numero = 0

def acrescentar():
    global numero
    numero = numero + 1
    contagem_click.configure(text=numero)

def diminuir():
    global numero
    numero = numero - 1
    contagem_click.configure(text=numero)


margem = tk.Canvas(janela, height=200, background='#1d1d1d', bd=0, highlightthickness=0, relief='flat')
margem.pack()
botao_acrescentar = tk.Button(janela, bg='#FFFFFF', text='+', font=('Montserrat', 16, 'bold'), padx=10, command=acrescentar)
botao_acrescentar.pack()
contagem_click = tk.Label(janela, text=numero, fg='#FFFFFF', bg='#1d1d1d', font=('Montserrat',16, 'bold'))
contagem_click.pack()
botao_diminuir = tk.Button(janela, bg='#FFFFFF', text='-', font=('Montserrat', 16, 'bold'), padx=10, command=diminuir)
botao_diminuir.pack()

janela.mainloop()