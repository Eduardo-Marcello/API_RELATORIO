from fastapi import FastAPI
import pandas as pd
from datetime import datetime

app = FastAPI()

class Usuario:
  def __init__(self, ID_Usuario, Nome, Departamento, CPF, Email, Cargo):
      self.ID_Usuario = ID_Usuario
      self.Nome = Nome
      self.Departamento = Departamento
      self.CPF = CPF
      self.Email = Email
      self.Cargo = Cargo

class Departamento:
  def __init__(self, Codigo, Nome_Departamento, Descricao):
      self.Codigo = Codigo
      self.Nome_Departamento = Nome_Departamento
      self.Descricao = Descricao

class Chamado:
  def __init__(self, ID, Titulo, Descricao, Data_Abertura, Hora, Status, Usuario):
      self.ID = ID
      self.Titulo = Titulo
      self.Descricao = Descricao
      self.Data_Abertura = Data_Abertura
      self.Hora = Hora
      self.Status = Status
      self.Usuario = Usuario

class Maquina:
  def __init__(self, codigo_maquina, Nome_do_Computador, Numero_de_Serie, Data_Aquisicao, Status, Usuario):
      self.codigo_maquina = codigo_maquina
      self.Nome_do_Computador = Nome_do_Computador
      self.Numero_de_Serie = Numero_de_Serie
      self.Aquisicao = Data_Aquisicao
      self.Status = Status
      self.Usuario = Usuario

class Software:
  def __init__(self, ID_Software, Nome_do_Software, Versao, Fornecedor, codigo_maquina):
      self.ID_Software = ID_Software
      self.Nome_do_Software = Nome_do_Software
      self.Versao = Versao
      self.Fornecedor = Fornecedor
      self.codigo_maquina = codigo_maquina

class Licenca:
  def __init__(self, ID, Data_Aquisicao, Chave_Licenca, ID_Software):
      self.ID = ID
      self.Data_Aquisicao = Data_Aquisicao
      self.Chave_Licenca = Chave_Licenca
      self.ID_Software = ID_Software

dados_usuarios = pd.read_csv('usuarios.csv', delimiter=',', encoding='utf-8').to_dict(orient='records')
dados_departamentos = pd.read_csv('departamentos.csv', delimiter=',', encoding='utf-8').to_dict(orient='records')
dados_chamados = pd.read_csv('chamados.csv', delimiter=',', encoding='utf-8').to_dict(orient='records')
dados_maquinas = pd.read_csv('maquina.csv', delimiter=',', encoding='utf-8').to_dict(orient='records')
dados_softwares = pd.read_csv('software.csv', delimiter=',', encoding='utf-8').to_dict(orient='records')
dados_licencas = pd.read_csv('licença.csv', delimiter=',', encoding='utf-8').to_dict(orient='records')

usuario1 = Usuario(dados_usuarios[0]['ID_Usuario'],
                   dados_usuarios[0]['Nome'],
                   dados_usuarios[0]['Departamento'],
                   dados_usuarios[0]['CPF'],
                   dados_usuarios[0]['Email'],
                   dados_usuarios[0]['Cargo'] )

usuario2 = Usuario(dados_usuarios[1]['ID_Usuario'],
                   dados_usuarios[1]['Nome'],
                   dados_usuarios[1]['Departamento'],
                   dados_usuarios[1]['CPF'],
                   dados_usuarios[1]['Email'],
                   dados_usuarios[1]['Cargo'])

usuario3 = Usuario(dados_usuarios[2]['ID_Usuario'],
                   dados_usuarios[2]['Nome'],
                   dados_usuarios[2]['Departamento'],
                   dados_usuarios[2]['CPF'],
                   dados_usuarios[2]['Email'],
                   dados_usuarios[2]['Cargo'] )

usuario4 = Usuario(dados_usuarios[3]['ID_Usuario'],
                   dados_usuarios[3]['Nome'],
                   dados_usuarios[3]['Departamento'],
                   dados_usuarios[3]['CPF'],
                   dados_usuarios[3]['Email'],
                   dados_usuarios[3]['Cargo'] )

usuario5 = Usuario(dados_usuarios[4]['ID_Usuario'],
                   dados_usuarios[4]['Nome'],
                   dados_usuarios[4]['Departamento'],
                   dados_usuarios[4]['CPF'],
                   dados_usuarios[4]['Email'],
                   dados_usuarios[4]['Cargo'] )

usuario6 = Usuario(dados_usuarios[5]['ID_Usuario'],
                   dados_usuarios[5]['Nome'],
                   dados_usuarios[5]['Departamento'],
                   dados_usuarios[5]['CPF'],
                   dados_usuarios[5]['Email'],
                   dados_usuarios[5]['Cargo'] )

usuario7 = Usuario(dados_usuarios[6]['ID_Usuario'],
                   dados_usuarios[6]['Nome'],
                   dados_usuarios[6]['Departamento'],
                   dados_usuarios[6]['CPF'],
                   dados_usuarios[6]['Email'],
                   dados_usuarios[6]['Cargo'] )

usuario8 = Usuario(dados_usuarios[7]['ID_Usuario'], 
                   dados_usuarios[7]['Nome'], 
                   dados_usuarios[7]['Departamento'],
                   dados_usuarios[7]['CPF'], 
                   dados_usuarios[7]['Email'], 
                   dados_usuarios[7]['Cargo'])

usuario9 = Usuario(dados_usuarios[8]['ID_Usuario'], 
                   dados_usuarios[8]['Nome'], 
                   dados_usuarios[8]['Departamento'], 
                   dados_usuarios[8]['CPF'], 
                   dados_usuarios[8]['Email'], 
                   dados_usuarios[8]['Cargo'])

usuario10 = Usuario(dados_usuarios[9]['ID_Usuario'], 
                    dados_usuarios[9]['Nome'], 
                    dados_usuarios[9]['Departamento'],
                    dados_usuarios[9]['CPF'], 
                    dados_usuarios[9]['Email'], 
                    dados_usuarios[9]['Cargo'])


lista_usuarios = [
    usuario1,
    usuario2,
    usuario3,
    usuario4,
    usuario5,
    usuario6,
    usuario7,
    usuario8,
    usuario9,
    usuario10
]

departamento1 = Departamento(dados_departamentos[0]['Codigo'], 
                             dados_departamentos[0]['Nome_Departamento'],
                             dados_departamentos[0]['Descricao'])

departamento2 = Departamento(dados_departamentos[1]['Codigo'], 
                             dados_departamentos[1]['Nome_Departamento'], 
                             dados_departamentos[1]['Descricao'])

departamento3 = Departamento(dados_departamentos[2]['Codigo'], 
                             dados_departamentos[2]['Nome_Departamento'], 
                             dados_departamentos[2]['Descricao'])

departamento4 = Departamento(dados_departamentos[3]['Codigo'], 
                             dados_departamentos[3]['Nome_Departamento'], 
                             dados_departamentos[3]['Descricao'])

departamento5 = Departamento(dados_departamentos[4]['Codigo'], 
                             dados_departamentos[4]['Nome_Departamento'], 
                             dados_departamentos[4]['Descricao'])

departamento6 = Departamento(dados_departamentos[5]['Codigo'], 
                             dados_departamentos[5]['Nome_Departamento'], 
                             dados_departamentos[5]['Descricao'])

departamento7 = Departamento(dados_departamentos[6]['Codigo'], 
                             dados_departamentos[6]['Nome_Departamento'], 
                             dados_departamentos[6]['Descricao'])

lista_departamentos = [
    departamento1,
    departamento2,
    departamento3,
    departamento4,
    departamento5,
    departamento6,
    departamento7
]

chamado1 = Chamado(
    dados_chamados[0]['ID'],
    dados_chamados[0]['Titulo'],
    dados_chamados[0]['Descricao'],
    datetime.strptime(dados_chamados[0]['Data_Abertura'], '%Y-%m-%d').date(),
    datetime.strptime(dados_chamados[0]['Hora'].strip(), '%H:%M:%S').time(),
    dados_chamados[0]['Status'],
    dados_chamados[0]['Usuario']
)

chamado2 = Chamado(
    dados_chamados[1]['ID'],
    dados_chamados[1]['Titulo'],
    dados_chamados[1]['Descricao'],
    datetime.strptime(dados_chamados[1]['Data_Abertura'], '%Y-%m-%d').date(),
    datetime.strptime(dados_chamados[1]['Hora'].strip(), '%H:%M:%S').time(),
    dados_chamados[1]['Status'],
    dados_chamados[1]['Usuario']
)

chamado3 = Chamado(
    dados_chamados[2]['ID'],
    dados_chamados[2]['Titulo'],
    dados_chamados[2]['Descricao'],
    datetime.strptime(dados_chamados[2]['Data_Abertura'], '%Y-%m-%d').date(),
    datetime.strptime(dados_chamados[2]['Hora'].strip(), '%H:%M:%S').time(),
    dados_chamados[2]['Status'],
    dados_chamados[2]['Usuario']
)

chamado4 = Chamado(
    dados_chamados[3]['ID'],
    dados_chamados[3]['Titulo'],
    dados_chamados[3]['Descricao'],
    datetime.strptime(dados_chamados[3]['Data_Abertura'], '%Y-%m-%d').date(),
    datetime.strptime(dados_chamados[3]['Hora'].strip(), '%H:%M:%S').time(),
    dados_chamados[3]['Status'],
    dados_chamados[3]['Usuario']
)

chamado5 = Chamado(
    dados_chamados[4]['ID'],
    dados_chamados[4]['Titulo'],
    dados_chamados[4]['Descricao'],
    datetime.strptime(dados_chamados[4]['Data_Abertura'], '%Y-%m-%d').date(),
    datetime.strptime(dados_chamados[4]['Hora'].strip(), '%H:%M:%S').time(),
    dados_chamados[4]['Status'],
    dados_chamados[4]['Usuario']
)

chamado6 = Chamado(
    dados_chamados[5]['ID'],
    dados_chamados[5]['Titulo'],
    dados_chamados[5]['Descricao'],
    datetime.strptime(dados_chamados[5]['Data_Abertura'], '%Y-%m-%d').date(),
    datetime.strptime(dados_chamados[5]['Hora'].strip(), '%H:%M:%S').time(),
    dados_chamados[5]['Status'],
    dados_chamados[5]['Usuario']
)

chamado7 = Chamado(
    dados_chamados[6]['ID'],
    dados_chamados[6]['Titulo'],
    dados_chamados[6]['Descricao'],
    datetime.strptime(dados_chamados[6]['Data_Abertura'], '%Y-%m-%d').date(),
    datetime.strptime(dados_chamados[6]['Hora'].strip(), '%H:%M:%S').time(),
    dados_chamados[6]['Status'],
    dados_chamados[6]['Usuario']
)

chamado8 = Chamado(
  dados_chamados[7]['ID'],
  dados_chamados[7]['Titulo'],
  dados_chamados[7]['Descricao'],
  datetime.strptime(dados_chamados[7]['Data_Abertura'], '%Y-%m-%d').date(),
  datetime.strptime(dados_chamados[7]['Hora'].strip(), '%H:%M:%S').time(),
  dados_chamados[7]['Status'],
  dados_chamados[7]['Usuario']
)

chamado9 = Chamado(
  dados_chamados[8]['ID'],
  dados_chamados[8]['Titulo'],
  dados_chamados[8]['Descricao'],
  datetime.strptime(dados_chamados[8]['Data_Abertura'], '%Y-%m-%d').date(),
  datetime.strptime(dados_chamados[8]['Hora'].strip(), '%H:%M:%S').time(),
  dados_chamados[8]['Status'],
  dados_chamados[8]['Usuario']
  )

chamado10 = Chamado(
  dados_chamados[9]['ID'],
  dados_chamados[9]['Titulo'],
  dados_chamados[9]['Descricao'],
  datetime.strptime(dados_chamados[9]['Data_Abertura'], '%Y-%m-%d').date(),
  datetime.strptime(dados_chamados[9]['Hora'].strip(), '%H:%M:%S').time(),
  dados_chamados[9]['Status'],
  dados_chamados[9]['Usuario']
  )

lista_chamados = [
    chamado1,
    chamado2,
    chamado3,
    chamado4,
    chamado5,
    chamado6,
    chamado7,
    chamado8,
    chamado9,
    chamado10
]

maquina1 = Maquina(dados_maquinas[0]['codigo_maquina'],
   dados_maquinas[0]['Nome do Computador'],
   dados_maquinas[0]['Numero de Serie'],
   dados_maquinas[0]['Data_Aquisicao'],
   dados_maquinas[0]['Status'],
   dados_maquinas[0]['ID_Usuario_Responsavel'])

maquina2 = Maquina(dados_maquinas[1]['codigo_maquina'],
   dados_maquinas[1]['Nome do Computador'],
   dados_maquinas[1]['Numero de Serie'],
   dados_maquinas[1]['Data_Aquisicao'],
   dados_maquinas[1]['Status'],
   dados_maquinas[1]['ID_Usuario_Responsavel'])

maquina3 = Maquina(dados_maquinas[2]['codigo_maquina'],
   dados_maquinas[2]['Nome do Computador'],
   dados_maquinas[2]['Numero de Serie'],
   dados_maquinas[2]['Data_Aquisicao'],
   dados_maquinas[2]['Status'],
   dados_maquinas[2]['ID_Usuario_Responsavel'])

maquina4 = Maquina(dados_maquinas[3]['codigo_maquina'],
   dados_maquinas[3]['Nome do Computador'],
   dados_maquinas[3]['Numero de Serie'],
   dados_maquinas[3]['Data_Aquisicao'],
   dados_maquinas[3]['Status'],
   dados_maquinas[3]['ID_Usuario_Responsavel'])

maquina5 = Maquina(dados_maquinas[4]['codigo_maquina'],
   dados_maquinas[4]['Nome do Computador'],
   dados_maquinas[4]['Numero de Serie'],
   dados_maquinas[4]['Data_Aquisicao'],
   dados_maquinas[4]['Status'],
   dados_maquinas[4]['ID_Usuario_Responsavel'])

maquina6 = Maquina(dados_maquinas[5]['codigo_maquina'],
   dados_maquinas[5]['Nome do Computador'],
   dados_maquinas[5]['Numero de Serie'],
   dados_maquinas[5]['Data_Aquisicao'],
   dados_maquinas[5]['Status'],
   dados_maquinas[5]['ID_Usuario_Responsavel'])

maquina7 = Maquina(dados_maquinas[6]['codigo_maquina'],
   dados_maquinas[6]['Nome do Computador'],
   dados_maquinas[6]['Numero de Serie'],
   dados_maquinas[6]['Data_Aquisicao'],
   dados_maquinas[6]['Status'],
   dados_maquinas[6]['ID_Usuario_Responsavel'])

maquina8 = Maquina(dados_maquinas[7]['codigo_maquina'],
   dados_maquinas[7]['Nome do Computador'],
   dados_maquinas[7]['Numero de Serie'],
   dados_maquinas[7]['Data_Aquisicao'],
   dados_maquinas[7]['Status'],
   dados_maquinas[7]['ID_Usuario_Responsavel'])

maquina9 = Maquina(dados_maquinas[8]['codigo_maquina'],
   dados_maquinas[8]['Nome do Computador'],
   dados_maquinas[8]['Numero de Serie'],
   dados_maquinas[8]['Data_Aquisicao'],
   dados_maquinas[8]['Status'],
   dados_maquinas[8]['ID_Usuario_Responsavel'])

maquina10 = Maquina(dados_maquinas[9]['codigo_maquina'],
   dados_maquinas[9]['Nome do Computador'],
   dados_maquinas[9]['Numero de Serie'],
   dados_maquinas[9]['Data_Aquisicao'],
   dados_maquinas[9]['Status'],
   dados_maquinas[9]['ID_Usuario_Responsavel'])

lista_maquinas = [
    maquina1,
    maquina2,
    maquina3,
    maquina4,
    maquina5,
    maquina6,
    maquina7,
    maquina8,
    maquina9,
    maquina10
]

software1 = Software(dados_softwares[0]['ID_Software'],
   dados_softwares[0]['Nome do Software'],
   dados_softwares[0]['Versao'],
   dados_softwares[0]['Fornecedor'],
   dados_softwares[0]['codigo_maquina'])

software2 = Software(dados_softwares[1]['ID_Software'],
   dados_softwares[1]['Nome do Software'],
   dados_softwares[1]['Versao'],
   dados_softwares[1]['Fornecedor'],
   dados_softwares[1]['codigo_maquina'])

software3 = Software(dados_softwares[2]['ID_Software'],
   dados_softwares[2]['Nome do Software'],
   dados_softwares[2]['Versao'],
   dados_softwares[2]['Fornecedor'],
   dados_softwares[2]['codigo_maquina'])

software4 = Software(dados_softwares[3]['ID_Software'],
   dados_softwares[3]['Nome do Software'],
   dados_softwares[3]['Versao'],
   dados_softwares[3]['Fornecedor'],
   dados_softwares[3]['codigo_maquina'])

software5 = Software(dados_softwares[4]['ID_Software'],
   dados_softwares[4]['Nome do Software'],
   dados_softwares[4]['Versao'],
   dados_softwares[4]['Fornecedor'],
   dados_softwares[4]['codigo_maquina'])

software6 = Software(dados_softwares[5]['ID_Software'],
   dados_softwares[5]['Nome do Software'],
   dados_softwares[5]['Versao'],
   dados_softwares[5]['Fornecedor'],
   dados_softwares[5]['codigo_maquina'])

software7 = Software(dados_softwares[6]['ID_Software'],
   dados_softwares[6]['Nome do Software'],
   dados_softwares[6]['Versao'],
   dados_softwares[6]['Fornecedor'],
   dados_softwares[6]['codigo_maquina'])

software8 = Software(dados_softwares[7]['ID_Software'],
   dados_softwares[7]['Nome do Software'],
   dados_softwares[7]['Versao'],
   dados_softwares[7]['Fornecedor'],
   dados_softwares[7]['codigo_maquina'])

software9 = Software(dados_softwares[8]['ID_Software'],
   dados_softwares[8]['Nome do Software'],
   dados_softwares[8]['Versao'],
   dados_softwares[8]['Fornecedor'],
   dados_softwares[8]['codigo_maquina'])

software10 = Software(dados_softwares[9]['ID_Software'],
   dados_softwares[9]['Nome do Software'],
   dados_softwares[9]['Versao'],
   dados_softwares[9]['Fornecedor'],
   dados_softwares[9]['codigo_maquina'])

lista_softwares = [
    software1,
    software2,
    software3,
    software4,
    software5,
    software6,
    software7,
    software8,
    software9,
    software10
]

licenca1 = Licenca(dados_licencas[0]['ID'],
   dados_licencas[0]['Data_Aquisicao'],
   dados_licencas[0]['Chave_Licenca'],
   dados_licencas[0]['ID_Software'])

licenca2 = Licenca(dados_licencas[1]['ID'],
   dados_licencas[1]['Data_Aquisicao'],
   dados_licencas[1]['Chave_Licenca'],
   dados_licencas[1]['ID_Software'])

licenca3 = Licenca(dados_licencas[2]['ID'],
   dados_licencas[2]['Data_Aquisicao'],
   dados_licencas[2]['Chave_Licenca'],
   dados_licencas[2]['ID_Software'])

licenca4 = Licenca(dados_licencas[3]['ID'],
   dados_licencas[3]['Data_Aquisicao'],
   dados_licencas[3]['Chave_Licenca'],
   dados_licencas[3]['ID_Software'])

licenca5 = Licenca(dados_licencas[4]['ID'],
   dados_licencas[4]['Data_Aquisicao'],
   dados_licencas[4]['Chave_Licenca'],
   dados_licencas[4]['ID_Software'])

licenca6 = Licenca(dados_licencas[5]['ID'],
   dados_licencas[5]['Data_Aquisicao'],
   dados_licencas[5]['Chave_Licenca'],
   dados_licencas[5]['ID_Software'])

licenca7 = Licenca(dados_licencas[6]['ID'],
   dados_licencas[6]['Data_Aquisicao'],
   dados_licencas[6]['Chave_Licenca'],
   dados_licencas[6]['ID_Software'])

lista_licencas = [
    licenca1,
    licenca2,
    licenca3,
    licenca4,
    licenca5,
    licenca6,
    licenca7
]

@app.get("/")
async def root():
  return { "API Funcionários em funcionamento" }

@app.get("/usuarios")
async def get_usuarios():
  print(lista_usuarios)
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
