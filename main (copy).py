from fastapi import FastAPI
import pandas as pd
from datetime import datetime

app = FastAPI()

class Usuario:
  def __init__(self, ID_Usuario, Nome, Código_Departamento, CPF, Email, Cargo):
      self.ID_Usuario = ID_Usuario
      self.Nome = Nome
      self.Código_Departamento = Código_Departamento
      self.CPF = CPF
      self.Email = Email
      self.Cargo = Cargo

class Departamento:
  def __init__(self, Codigo, Nome_Departamento, Descrição):
      self.Codigo = Codigo
      self.Nome_Departamento = Nome_Departamento
      self.Descrição = Descrição

class Chamado:
  def __init__(self, ID, Título, Descrição, Data_Abertura, Hora, Status, ID_Usuário_Solicitante):
      self.ID = ID
      self.Título = Título
      self.Descrição = Descrição
      self.Data_Abertura = Data_Abertura
      self.Hora = Hora
      self.Status = Status
      self.ID_Usuário_Solicitante = ID_Usuário_Solicitante

class Maquina:
  def __init__(self, codigo_maquina, Nome_do_Computador, Numero_de_Série, Data_Aquisição, Status, ID_Usuario_Responsável):
      self.codigo_maquina = codigo_maquina
      self.Nome_do_Computador = Nome_do_Computador
      self.Numero_de_Série = Numero_de_Série
      self.Data_Aquisição = Data_Aquisição
      self.Status = Status
      self.ID_Usuário_Responsável = ID_Usuario_Responsável

class Software:
  def __init__(self, ID_Software, Nome_do_Software, Versão, Fornecedor, codigo_maquina):
      self.ID_Software = ID_Software
      self.Nome_do_Software = Nome_do_Software
      self.Versão = Versão
      self.Fornecedor = Fornecedor
      self.codigo_maquina = codigo_maquina

class Licenca:
  def __init__(self, ID, Data_Aquisição, Chave_Licença, ID_Software):
      self.ID = ID
      self.Data_Aquisição = Data_Aquisição
      self.Chave_Licença = Chave_Licença
      self.ID_Software = ID_Software

dados_usuarios = pd.read_csv('usuarios.csv', delimiter=',', encoding='utf-8', index_col=None)
dados_departamentos = pd.read_csv('departamentos.csv', delimiter=',', encoding='utf-8', index_col=None)
dados_chamados = pd.read_csv('chamados.csv',  delimiter=',', encoding='utf-8', index_col=None)
dados_maquinas = pd.read_csv('maquina.csv', delimiter=',', encoding='utf-8', index_col=None)
dados_softwares = pd.read_csv('software.csv',delimiter=',', encoding='utf-8', index_col=None)
dados_licencas = pd.read_csv('licença.csv', delimiter=',', encoding='utf-8', index_col=None)

# Lista de objetos Usuario
lista_usuarios = []
for _, row in dados_usuarios.iterrows():
    usuario = Usuario(
        ID_Usuario=row['ID_Usuario'],  # Updated parameter name to "ID_Usuario"
        Nome=row['Nome'],
        Código_Departamento=row['Código_Departamento'],
        CPF=row['CPF'],
        Email=row['Email'],
        Cargo=row['Cargo']
    )
    lista_usuarios.append(usuario)

# Lista de objetos Departamento
lista_departamentos = []
for _, row in dados_departamentos.iterrows():
    departamento = Departamento(
        Codigo=row['Codigo'],
        Nome_Departamento=row['Nome_Departamento'],
        Descrição=row['Descrição']
    )
    lista_departamentos.append(departamento)

# Lista de objetos Chamado
lista_chamados = []
for index, row in dados_chamados.iterrows():
    chamado = Chamado(
        ID=row['ID'],
        Título=row['Título'],
        Descrição=row['Descrição'],
        Data_Abertura=row['Data_Abertura'],
        Hora=row['Hora'],
        Status=row['Status'],
        ID_Usuário_Solicitante=row['ID_Usuário_Solicitante']
    )
    lista_chamados.append(chamado)

# Lista de objetos Maquina
lista_maquinas = []
for index, row in dados_maquinas.iterrows():
    maquina = Maquina(
        codigo_maquina=row['codigo_maquina'],
        Nome_do_Computador=row['Nome do Computador'],
        Numero_de_Série=row['Número de Série'],
        Data_Aquisição=row['Data_Aquisição'],  # Updated parameter name to "Data_Aquisição"
        Status=row['Status'],
        ID_Usuario_Responsável=row['ID_Usuario_Responsável']
    )
    lista_maquinas.append(maquina)

# Lista de objetos Software
lista_softwares = []
for index, row in dados_softwares.iterrows():
    software = Software(
        ID_Software=row['ID_Software'],
        Nome_do_Software=row['Nome do Software'],
        Versão=row['Versão'],
        Fornecedor=row['Fornecedor'],
        codigo_maquina=row['codigo_maquina']
    )
    lista_softwares.append(software)

# Lista de objetos Licenca
lista_licencas = []
for index, row in dados_licencas.iterrows():
    licenca = Licenca(
        ID=row['ID'],
        Data_Aquisição=row['Data_Aquisição'],
        Chave_Licença=row['Chave_Licença'],
        ID_Software=row['ID_Software']
    )
    lista_licencas.append(licenca)

@app.get("/")
async def root():
  print(lista_departamentos[0])
  return { "API Funcionários em funcionamento" }
  

@app.get("/usuarios")
async def get_usuarios():
  return lista_usuarios

@app.get("/departamentos")
async def get_departamentos():
  return lista_departamentos

@app.get("/chamados")
async def get_chamados():
  return lista_chamados

@app.get("/computadores")
async def get_todos_computadores():
    return lista_maquinas

@app.get("/softwares")
async def get_todos_softwares():
    return lista_softwares

@app.get("/licencas")
async def get_todas_licencas():
    return lista_licencas

@app.get("/usuario/{user_id}")
async def get_usuario_por_id(user_id: int):
    if user_id in dados_usuarios.index:
        usuario = dados_usuarios.loc[user_id].to_dict()
        print(f'Imprimindo o usuário')
        return usuario
    else:
        return {"message": "Usuário não encontrado"}

@app.get("/departamento/{codigo}")
async def get_departamento_por_codigo(codigo: int):
    departamento = dados_departamentos.loc[codigo].to_dict()
    return departamento

@app.get("/chamado/{chamado_id}")
async def get_chamado_por_id(chamado_id: int):
    chamado = dados_chamados[dados_chamados['ID'] == chamado_id].to_dict(orient='records')
    if not chamado:
        return {"message": "Chamado não encontrado"}
    return chamado[0]

@app.get("/computador/{codigo_maquina}")
async def get_computador_por_codigo(codigo_maquina: int):
    computador = dados_maquinas[dados_maquinas['codigo_maquina'] == codigo_maquina].to_dict(orient='records')
    if not computador:
        return {"message": "Computador não encontrado"}
    return computador[0]

@app.get("/software/{codigo_software}")
async def get_softwares_por_codigo(codigo_software: int):
    software = dados_softwares[dados_softwares['ID'] == codigo_software].to_dict(orient='records')
    if not software:
        return {"message": "Nenhum software encontrado com este código"}
    return software[0]

@app.get("/licenca/{id_licenca}")
async def get_licenca_por_id(id_licenca: int):
    licenca = dados_licencas[dados_licencas['ID'] == id_licenca].to_dict(orient='records')
    if not licenca:
        return {"message": "Nenhuma licença encontrada com este ID"}
    return licenca[0]