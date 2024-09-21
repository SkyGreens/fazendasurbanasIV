import requests #pip install requests
from tkinter import messagebox #pip install tkinter

#api para obter o token de acesso
api_login = "http://localhost:8080/skygreen/auth/login"

class Access:
    @staticmethod #deixa a função como estatica, não precisando passar o self
    
    def login(user,senha,app):
        login_data = {
            "cpf": f"{user}",
            "senha": f"{senha}"
        }
        
        try:  
            response = requests.post(api_login, json=login_data)
            
            if response.status_code == 200:
                global token
                token = response.json().get("token")
                #print(token)
                app.iniciar_interface()
            else:
                
                app.retornar_login() 
                return True

        except requests.exceptions.RequestException as e:
                messagebox.showinfo(title="Erro",message=f"Erro de Conexão: {e}")
                app.retornar_login()
            

