import tkinter as tk
import pickle

class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Gravar Conteúdo", command=self.on_button)
        self.entry.pack()
        self.button.pack()

    def on_button(self):
        conteudo = self.entry.get()
        #gravando os dados
        afile = open(r'C:\Users\agushi\Desktop\Python\Pickle\conteudo.pkl', 'wb')
        pickle.dump(conteudo, afile)
        afile.close()
        #recuperando os dados
        file2 = open(r'C:\Users\agushi\Desktop\Python\Pickle\conteudo.pkl', 'rb')
        novod = pickle.load(file2)
        file2.close()
        #imprimindo os dados
        print("Conteúdo gravado:")
        print(novod)
        
w = SampleApp()

w.mainloop()
