import requests
from datetime import datetime, timezone
from dateutil import parser

API_BASE = "http://localhost:8080/skygreen"

api_login = f"{API_BASE}/auth/login"

api_cadastrarFornecedor = f"{API_BASE}/fornecedor/adicionar"
api_listarFornecedores = f"{API_BASE}/fornecedor/"
api_editarFornecedores = f"{API_BASE}/fornecedor/update"
api_editarSementesFornecedores = f"{API_BASE}/fornecedor/"

api_cadastrarSementes = f"{API_BASE}/sementes/adicionar"
api_listarSementes = f"{API_BASE}/sementes/"

api_perfilUser = f"{API_BASE}/usuario/personal/"
api_listarUsuario = f"{API_BASE}/usuario/"
api_especificoUsuario = f"{API_BASE}/usuario/"
api_cadastrarUsuario = f"{API_BASE}/auth/register"
api_editarUsuario = f"{API_BASE}/usuario/update"

api_cadastrarProducao = f"{API_BASE}/producao/adicionar"
api_listarProducao = f"{API_BASE}/producao/"
api_listarPrateleira = f"{API_BASE}/prateleira/"
api_listarEstoque = f"{API_BASE}/estoque/"

api_listarPedidosCompras = f"{API_BASE}/compras/"
api_CadastrarPedidosCompras = f"{API_BASE}/compras/pedido"

api_listarPedidosVenda = f"{API_BASE}/vendas/"
api_CadastrarPedidosVenda = f"{API_BASE}/vendas/pedido"

api_listarClientes = f"{API_BASE}/cliente/"

class Funcoes:

    def calcular_dias_restantes(data_inicio, tempo_cultivo):
        data_inicio = parser.isoparse(data_inicio)  # Lida com o formato ISO 8601
        data_atual = datetime.now(timezone.utc)
        dias_passados = (data_atual - data_inicio).days  # Calcula a diferença em dias
        dias_restantes = tempo_cultivo - dias_passados  # Subtrai dos dias totais de cultivo

        return dias_restantes if dias_restantes > 0 else 0
    
class Access:
    token = None
    userId = None

    @staticmethod #deixa a função como estatica, não precisando passar o self
    def login(user, senha, app):
        login_data = {
            "cpf": user,
            "senha": senha
        }
        try:
            response = requests.post(api_login, json=login_data)
            
            if response.status_code == 200:
                data = response.json()
                Access.token = data.get("token")
                Access.userId = data.get("userId")
                app.iniciar_interface()
            else:
                return False

        except requests.exceptions.RequestException:
            return "conexão"
            
    def cadastroFornecedor(status, email, tel, end, cid, est, pais, ie, rs, cnpj, sementeid=None):
        cadatro_data = {
            "ativo": status,
            "email": email,
            "telefone": tel,
            "endereco": end,
            "cidade": cid,
            "estado": est,
            "pais": pais,
            "inscricaoEstadual": ie,
            "razaoSocial": rs,
            "cnpj": cnpj
        }
        
        if sementeid is not None:
            cadatro_data["sementes"] = [{"sementeId": sementeid}]

        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}

        response = requests.post(api_cadastrarFornecedor, json=cadatro_data, headers=headers)
        
        if response.status_code == 200:
            print('Fornecedor Adicionado')
            return True
        else:
            print('Fornecedor Não Adicionado', response.text)
            return False

    def listarFornecedores():
        headers = {"Authorization": f"Bearer {Access.token}"}

        response = requests.get(api_listarFornecedores, headers=headers)
        
        if response.status_code == 200:
            
            fornecedores_api = response.json()
            fornecedores = []
            
            for fornecedor in fornecedores_api:
                sementes = fornecedor.get('sementes', [])
                
                if sementes:
                    nomesemente = sementes[0].get('nome', '')
                else:
                    nomesemente = ''
                
                fornecedores.append({
                    "id": f"{fornecedor.get('fornecedorId')}",
                    "nome": fornecedor.get('razaoSocial'),
                    "cnpj": fornecedor.get('cnpj'),
                    "endereco": fornecedor.get('endereco'),
                    "status": fornecedor.get('ativo'),
                    "email": fornecedor.get('email'),
                    "telefone": fornecedor.get('telefone'),
                    "cidade": fornecedor.get('cidade'),
                    "estado": fornecedor.get('estado'),
                    "pais": fornecedor.get('pais'),
                    "inscricaoEstadual": fornecedor.get('inscricaoEstadual'),
                    "semente":nomesemente
                })
            return fornecedores 
        else:
            print('Falha ao listar fornecedores:', response.text)

    def editarFornecedor(idfornecedor,status,email,tel,end,cid,est,pais,isced,rzsocial,cnpj,sementeid=None):
        
        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}
        
        data = {
            "fornecedorId" : idfornecedor,
            "ativo" : status,
            "email" : email,
            "telefone" : tel,
            "endereco" : end,
            "cidade" : cid,
            "estado" : est,
            "pais" : pais,
            "inscricaoEstadual" : isced,
            "razaoSocial" : rzsocial,
            "cnpj" : cnpj
        }
        if sementeid is not None:
            datasemente = [
                {
                    "sementeId" : sementeid
                }
            ]
            api_editarSementes = f"{api_editarSementesFornecedores}{idfornecedor}/sementes"
            requests.put(api_editarSementes, json=datasemente, headers=headers)
        
        response = requests.put(api_editarFornecedores, json=data, headers=headers)
    
        if response.status_code == 200:
            return True
        else:
            return False
    
    def cadastrarSementes(nome,desc):

        data = {
            "nome": nome,
            "descricao": desc
        }

        headers = {"Authorization": f"Bearer {Access.token}"}

        response_semente = requests.post(api_cadastrarSementes, json=data, headers=headers)

        if response_semente.status_code == 200:
            print('Semente cadastrada com sucesso!')
            return True
        else:
            print('Falha ao cadastrar a semente:', response_semente.status_code)
            return False

    def listarSementes():
        headers = {"Authorization": f"Bearer {Access.token}"}

        response = requests.get(api_listarSementes, headers=headers)
        
        if response.status_code == 200:
            sementes_api = response.json()
            sementes = []
            for i in sementes_api:
                sementes.append({
                    "id": i.get('sementeId'),
                    "nome": i.get('nome'),
                    "descricao": i.get('descricao')
                })
            return sementes 
        else:
            print('Falha ao listar sementes:',  response.text)
    
    def visualizarPerfil():
        
        headers = {"Authorization": f"Bearer {Access.token}"}
            
        api_MperfilUser = f"{api_perfilUser}{Access.userId}"
        response = requests.get(api_MperfilUser, headers=headers)
        
        if response.status_code == 200:
            perfil_api = response.json()
            dados_perfil = []
            
            dados_perfil.append({
                "id": perfil_api.get('id'),
                "email": perfil_api.get('email'),
                "ativo": perfil_api.get('ativo'),
                "cargo": perfil_api.get('role'),
                "nome": perfil_api.get('nome'),
                "cpf": perfil_api.get('cpf') 
            })
            return dados_perfil
        
        else:
            print('Falha ao acessar informações:',response.text)
            
    def listarUsuarios(comand=None,iduser=None):
        
        headers = {"Authorization": f"Bearer {Access.token}"}

        if comand == 0:
            api_Usuario = f"{api_especificoUsuario}{iduser}"
        else:
            api_Usuario = api_listarUsuario
            
        response = requests.get(api_Usuario, headers=headers)
        
        if response.status_code == 200:
            
            usuarios_api = response.json()
            usuarios = []
            
            for user in usuarios_api:
                
                usuarios.append({
                    "id":user.get('id'),
                    "cpf": user.get('cpf'),
                    "cargo": user.get('role'),
                    "nome": user.get('nome'),
                    "status": user.get('ativo'),
                    "email": user.get('email')
                })
            return usuarios 
        else:
            return False
  
    def cadastroUsuario(cpf,senha,cargo,nome,status,email):
        
        cadatro_data = {
            "cpf" : f"{cpf}",
            "senha" : f"{senha}",
            "role" : f"{cargo}",
            "nome" : f"{nome}",
            "ativo" : f"{status}",
            "email" : f"{email}"
        }

        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}
        
        response = requests.post(api_cadastrarUsuario, json=cadatro_data, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
                
    def editarUsuario(iduser,cargo,nome,status,email):
        data = {
            "id":iduser,
            "role" : f"{cargo}",
            "nome" : f"{nome}",
            "ativo" : f"{status}",
            "email" : f"{email}"
        }
        
        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}
         
        response = requests.put(api_editarUsuario, json=data, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
                    
    def listarProducao():
        
        headers = {"Authorization": f"Bearer {Access.token}"}

        response = requests.get(api_listarProducao, headers=headers)
        
        if response.status_code == 200:
            producao_api = response.json()
            producao = []
            list_sementes = Access.listarSementes()
            
            def nome_semente(id_semente):
                for semente in list_sementes:
                    if semente['id'] == id_semente:
                        return semente['nome']
                return None
            
            for prod in producao_api:
                id_semente = prod.get('sementeId')
                producao.append({
                    "id": prod.get('producaoId'),
                    "nome_semente": nome_semente(id_semente),
                    "qtd": prod.get('sementeQuantidade'),
                    "status": "Ativo" if prod.get('ativo') == True else "Inativo",
                    "tempoCultivo": prod.get('tempoCultivo'),
                    "diasRestantes": Funcoes.calcular_dias_restantes(prod.get('dataInicio'), prod.get('tempoCultivo')),
                    "dataInicio": prod.get('dataInicio')
                })
            return producao
        else:
            print('Falha ao listar Producao:', response.text)
    
    def listarEstoque():
        headers = {"Authorization": f"Bearer {Access.token}"}

        response = requests.get(api_listarEstoque, headers=headers)
        
        if response.status_code == 200:
            estoque_api = response.json()
            estoque = []
        
            for est in estoque_api:
                semente = est.get('semente')
                
                estoque.append({
                    "id": f"{est.get('estoqueId')}",
                    "qtd": est.get('quantidade'),
                    "nome_semente": semente.get('nome'),
                    "desc": semente.get('descricao')
                })
            return estoque
        else:
            print('Falha ao listar Estoque:', response.text)
    
    def listarPrateleira():
        headers = {"Authorization": f"Bearer {Access.token}"}
        response = requests.get(api_listarPrateleira, headers=headers)
        
        if response.status_code == 200:

            prateleira_api = response.json()
            list_sementes = {semente['id']: semente['nome'] for semente in Access.listarSementes()}
            prateleira = []
            
            for prat in prateleira_api:
                producao = prat.get('producao')
                statusprat = prat.get('disponivel')
                
                if producao and 'dataInicio' in producao and 'tempoCultivo' in producao:
                    diasRestantes = Funcoes.calcular_dias_restantes(producao['dataInicio'], producao['tempoCultivo'])
                    tempoCultivo = producao.get('tempoCultivo')
                else:
                    diasRestantes = None
                    tempoCultivo = None
                
                prateleira.append({
                    "id": prat.get('prateleira_id'),
                    "disponivel": "Produção" if not statusprat else "Disponivel",
                    "producao": {
                        "idseed": producao.get('sementeId'),
                        "nome_semente": list_sementes.get(producao.get('sementeId')),
                        "dataInicio": producao.get('dataInicio'),
                        "status": "Ativo" if producao.get('ativo') else "Inativo",
                        "graf_valor": [tempoCultivo,diasRestantes]
                    } if not statusprat and producao else None
                })

            return prateleira
        else:
            return False
        
    def cadastrarProducao(Idsemente,qtd,tempo):
        
        datainicio = datetime.now().strftime("%Y-%m-%d")
    
        data = {
            "sementeId": f"{Idsemente}",
            "sementeQuantidade": f"{qtd}",
            "tempoCultivo" : f"{tempo}",
            "dataInicio" : f"{datainicio}",
            "fotoSemente" : "",
            "ativo": True
        }

        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}

        response_semente = requests.post(api_cadastrarProducao, json=data, headers=headers)

        if response_semente.status_code == 200:
            print('Producao cadastrada com sucesso!')
            return True
        else:
            print('Falha ao cadastrar a producao:', response_semente.status_code)
            return False
     
    def listarpedidosCompra():
        headers = {"Authorization": f"Bearer {Access.token}"}
            
        response = requests.get(api_listarPedidosCompras, headers=headers)
        
        if response.status_code == 200:
            
            compras_api = response.json()
            listcompras = []
            
            for compras in compras_api:
                
                listcompras.append({
                    "idcompra":compras.get('pedidoCompraId'),
                    "fornecedor":compras.get('fornecedor'),
                    "qtd":compras.get('quantidade'),
                    "semente":compras.get('semente')
                })
            return listcompras 
        else:
            return False
     
    def cadastroPedidoCompra(fornecedorid,qtd,sementeid):
        
        cadastro_data = {
            "fornecedor": {
                "fornecedorId" : fornecedorid
            },
            "quantidade" : qtd,
            "semente" : {
                "sementeId" : sementeid
            }
        }

        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}
        
        response = requests.post(api_CadastrarPedidosCompras, json=cadastro_data, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
   
    def listarpedidosVenda():
        headers = {"Authorization": f"Bearer {Access.token}"}
            
        response = requests.get(api_listarPedidosVenda, headers=headers)
        
        if response.status_code == 200:
            
            vendas_api = response.json()
            listvendas = []
    
            for vendas in vendas_api:
                
                listvendas.append({
                    "idvenda":vendas.get('pedidoVendaId'),
                    "cliente":vendas.get('cliente'),
                    "qtd":vendas.get('quantidade'),
                    "semente":vendas.get('semente'),
                    "tempocultivo":vendas.get('tempoCultivo'),
                    "status":vendas.get('ativo')
                })
            return listvendas 
        else:
            return False
     
    def cadastroPedidoVenda(clienteid,qtd,sementeid,tempocultivo):
        
        cadastro_data = {
            "cliente": {
                "clienteId" : clienteid
            },
            "quantidade" : qtd,
            "semente" : {
                "sementeId" : sementeid
            },
            "tempoCultivo": tempocultivo,
            "ativo": True
        }

        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}
        
        response = requests.post(api_CadastrarPedidosVenda, json=cadastro_data, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
      
    def listarClientes():
        headers = {"Authorization": f"Bearer {Access.token}"}
            
        response = requests.get(api_listarClientes, headers=headers)
        
        if response.status_code == 200:
            
            clientes_api = response.json()
            listClientes= []
            
            for cli in clientes_api:
                
                listClientes.append({
                    "clienteid":cli.get('clienteId'),
                    "status":cli.get('ativo'),
                    "email":cli.get('email'),
                    "telefone":cli.get('telefone'),
                    "endereco":cli.get('endereco'),
                    "cidade":cli.get('cidade'),
                    "estado":cli.get('estado'),
                    "pais":cli.get('pais'),
                    "razaoSocial":cli.get('razaoSocial'),
                    "cnpj":cli.get('cnpj')
                })
                
            return listClientes
        else:
            return False
          
    def verificar_permissoes(self,n):
        
        #0 - botao
        perfil = Access.visualizarPerfil()
    
        for i in perfil:
            cargo = i['cargo']

        if cargo == 'GERENTEPRODUCAO' :
            if n == 6:
                return False
            else:
                return True
        elif cargo == 'ASSISTENTEPRODUCAO':
            if n == 6:
                return False
            elif n == 0: #botoes
                return False
            else:
                return True
        else:
            return True