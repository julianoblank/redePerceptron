from tkinter import *
from tkinter import ttk
gui = Tk()
from redePerceptron import redePerceptron

class Janela:

    def __init__(self, janela):

        self.entradas = ''
        self.pesoA = ''
        self.pesoB = ''

        self.fontePadrao = ("Arial", "10")
        self.masterContainer = Frame(janela)
        self.masterContainer["pady"] = 10
        self.masterContainer.pack()

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(janela)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.fontePadrao = ("Arial", "10")
        self.segundoContainer = Frame(janela)
        self.segundoContainer["pady"] = 10
        self.segundoContainer.pack()
  
        self.fontePadrao = ("Arial", "10")
        self.terceiroContainer = Frame(janela)
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer.pack()
  
        self.fontePadrao = ("Arial", "10")
        self.quartoContainer = Frame(janela)
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        self.fontePadrao = ("Arial", "10")
        self.quintoContainer = Frame(janela)
        self.quintoContainer["pady"] = 10
        self.quintoContainer.pack()
 
        self.fontePadrao = ("Arial", "10")
        self.sextoContainer = Frame(janela)
        self.sextoContainer["pady"] = 10
        self.sextoContainer.pack()

        self.sextoContainer = Frame(janela)
        self.sextoContainer.pack(side=TOP)

        self.text = Text(self.sextoContainer, height=20, width=44)
        self.vsb = Scrollbar(self.sextoContainer, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set, state=DISABLED)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both")

        self.masterContainer = Frame(janela)
        self.masterContainer.pack(side=TOP)

        self.labelEntradas = Label(self.primeiroContainer, text="Entradas")
        self.labelEntradas.pack(side=LEFT)

        self.comboBoxEntrada = ttk.Combobox(janela)
        self.listaDeEntradas = ["AND", "OR"]
        self.comboBoxEntrada = ttk.Combobox(self.primeiroContainer, state = "readonly", values=self.listaDeEntradas)
        self.comboBoxEntrada.set("AND")
        self.comboBoxEntrada.pack()

        self.labelPesoA = Label(self.terceiroContainer, text="Peso A: ")
        self.labelPesoA.pack(side=LEFT)

        self.pesoA = Entry(self.terceiroContainer, width=30, textvariable=self.pesoA)
        self.pesoA.pack(side=LEFT)

        self.labelPesoB = Label(self.quartoContainer, text="Peso B: ")
        self.labelPesoB.pack(side=LEFT)

        self.pesoB = Entry(self.quartoContainer, width=30, textvariable=self.pesoB)
        self.pesoB.pack(side=LEFT)

        self.buttonTreinar = Button(self.quintoContainer, text="Treinar")
        self.buttonTreinar.bind("<Any-Button>", self.treinar)
        self.buttonTreinar.pack(side=LEFT)

        self.buttonEnviar = Button(self.quintoContainer, text="Enviar")
        self.buttonEnviar.bind("<Any-Button>", self.enviar)
        self.buttonEnviar.pack(side=RIGHT)

    def setText(self, texto):

        self.text.configure(state=NORMAL)
        self.text.see('end')
        self.text.insert(INSERT, texto + '\n')
        self.text.see('end')
        self.text.configure(state=DISABLED)

    def enviar(self, event):

            self.setText('Retorno do envio:  ')

    def treinar(self, event):
        
        self.setText('\n Treinando a rede, porta: ' + self.comboBoxEntrada.get())
        self.setText('\n'+redePerceptron.pegarOsPesos(redePerceptron,self.pesoA.get(),self.pesoB.get()))
        self.matrizResposta = str(redePerceptron.identificaEntrada(redePerceptron,self.comboBoxEntrada.get()))
        self.setText('\n Matriz que será treinada: ')
        self.setText(self.matrizResposta)
        
        #self.retornoDaRede = redePerceptron.setarVariaveis(self.entradaA.get())
        #self.setText('Resposta da rede: ' + self.retornoDaRede)
        

Janela(gui)
janela = Janela

gui.title('Rede Perceptron')
gui.mainloop()