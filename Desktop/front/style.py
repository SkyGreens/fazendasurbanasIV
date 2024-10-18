import customtkinter as ctk
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #pip install customtkinter matplotlib
import matplotlib.pyplot as plt

class Style:
    def __init__(self):
        pass

    def color (color_nome):
        colors = {
            'fg' : "#316133",  # Cor para botões - Verde Escuro
            'hover' : "#5d732f",  # Cor ao passar o mouse - Verde Claro
            'bg' : "#D9D9D9",  # Cor de fundo - Cinza

            'bg_frame' : "#E7E7E7",  # Cor de fundo do frame - Quase Branco
            'fg_2' : "#cdcdcd", # Cor para botões - Cinza escuro
            'hover_2' : "#a0a0a0" # Cor ao passar o mouse - Cinza Claro
        }
        return colors.get(color_nome)
    
    def font_style():
        fontStyle = ("Lucida Grande",16)
        return fontStyle
    
    def img(img_nome):
        
        def abrir_img(caminho,size):

            img = ctk.CTkImage(Image.open(caminho), size=size)  
            return img  
      
        imgs={
            'img_icon_pedidoVenda':abrir_img("img\\icon_pedidoVenda.png",(80, 80)),
            'img_icon_pedidoCompra':abrir_img("img\\icon_pedidoCompra.png",(80, 80)),
            'img_icon_insumos':abrir_img("img\\icon_insumos.png",(40, 40)),
            'img_icon_relatorio':abrir_img("img\\icon_relatorio.png",(40, 40)),
            'img_icon_estoque':abrir_img("img\\icon_estoque.png",(40, 40)),
            'img_icon_producao':abrir_img("img\\icon_producao.png",(40, 40)),
            'img_icon_perfil':abrir_img("img\\icon_perfil.png",(26, 26)),
            'img_icon_saida':abrir_img("img\\icon_saida.png",(26, 26))
        }
        return imgs.get(img_nome)
        
    def criar_grafico_circular(tela,valor, desc, titulo):
        fig, ax = plt.subplots()
        fig.patch.set_alpha(0.0)
        ax.pie(valor, labels=desc, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Para manter o formato do gráfico como círculo
        plt.title(titulo, fontsize=12, color="black")  # Ajuste de título e tamanho da fonte
        canvas = FigureCanvasTkAgg(fig, tela)
        plt.close()
        return canvas