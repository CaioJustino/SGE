# Imports

from datetime import date
from datetime import datetime

# Classes

class Evento(): 
  def __init__(self, nome_event, data_event, tipo_event, valor_event):
    self.__nome_event = nome_event
    self.__data_event = data_event
    self.__tipo_event = tipo_event
    self.__valor_event = valor_event
    self._cadastro1 = {}
    self._lista1 = []

  @property
  def nome_event(self):
    return self.__nome_event

  @property
  def data_event(self):
    return self.__data_event

  @property
  def tipo_event(self):
    return self.__tipo_event
    
  @property
  def valor_event(self):
    return self.__valor_event

  def cadastrar(self):
        self.__nome_event = str(input('Digite o nome do Evento: '))
        self.__data_event = str(input('Digite a data do Evento: '))
        self.__tipo_event = str(input('Digite o tipo do Evento: '))
        self.__valor_event = float(input('Digite o valor do Evento: R$ '))
        self._cadastro1 = {"Nome": self.__nome_event, "Data": self.__data_event, "Tipo": self.__tipo_event, "Valor": self.__valor_event}
        self._lista1.append(self._cadastro1)
        for c in self._lista1:
          if self._cadastro1 == self._cadastro1 and self._lista1.count(self._cadastro1) > 1:
            self._lista1.remove(self._cadastro1)
            print('\nEsse Evento já foi cadastrado.')
          else:
            print('\nEvento cadastrado com sucesso.')

  def listar(self):
    print('Eventos Cadastrados:')
    if self._lista1 == []:
      print('\nNenhum Evento foi cadastrado.')
    else:
      for c in self._lista1:
        for k, v in c.items():
          print(k + ": " + str(v))

  def editar(self):
    self.__nome_event = str(input('Digite o nome do Evento que deseja editar: '))
    self.__data_event = str(input('Digite a data desse Evento: '))
    for c in self._lista1:
      if c["Nome"] == self.__nome_event and c["Data"] == self.__data_event:
        v = str(input('Deseja mesmo editar esse Evento? [Sim/Não]: '))
        if v == "Sim":
          self.__nome_event = str(input('Digite o nome do Evento: '))
          self.__data_event = str(input('Digite a data do Evento: '))
          self.__tipo_event = str(input('Digite o tipo do Evento: '))
          self.__valor_event = float(input('Digite o valor do Evento: R$ '))
          self._cadastro1.update({"Nome": self.__nome_event, "Data": self.__data_event, "Tipo": self.__tipo_event, "Valor": self.__valor_event})
          print('\nEvento editado com sucesso.')
        elif v == "Não":
          print('\nOperação encerrada.')
      elif c["Nome"] != self.__nome_event and c["Data"] != self.__data_event:
        print('\nEvento não encontrado.')
      
  def remover(self):
    self.__nome_event = str(input('Digite o nome do Evento que deseja remover: '))
    self.__data_event = str(input('Digite a data desse Evento: '))
    for c in self._lista1:
      if c["Nome"] == self.__nome_event and c["Data"] == self.__data_event:
        v = str(input('Deseja mesmo remover esse Evento? [Sim/Não]: '))
        if v == "Sim":
          self._lista1.remove(c)
          print('\nEvento removido com sucesso.')
        elif v == "Não":
          print('\nOperação encerrada.')
      elif c["Nome"] != self.__nome_event and c["Data"] != self.__data_event:
        print('\nEvento não encontrado.')
  
  def buscar(self):
    self.__nome_event = str(input('Digite o nome do Evento que deseja buscar: '))
    self.__data_event = str(input('Digite a data desse Evento: '))
    for c in self._lista1:
        if c["Nome"] == self.__nome_event and c["Data"] == self.__data_event:
          print('\nEvento encontrado:')
          for k, v in c.items():
            print(k + ": " + str(v))
        else:
          print('\nEvento não encontrado.')

class Ingresso(): 
  def __init__(self):
    self._ingressos = []
    
  def gerar_ingresso(self):
      print('Ingressos Comprados:')
      for c in self._ingressos:
        for k, v in c.items():
          print(k + ": " + str(v))

class Comprador(): 
  def __init__(self, nome_comp, idade, cpf):
    self.__nome_comp = nome_comp
    self.__idade = idade
    self.__cpf = cpf
    self._verificada = False
    self._cadastro2 = {}
    self._data_compra = date.today()
    self._quantidade_dias = 0
    self.__event = None
    self.__ingresso = None
    self.__gerar_ingresso = None
    
  @property
  def nome_comp(self):
    return self.__nome_comp

  @property
  def idade(self):
    return self.__idade

  @property
  def cpf(self):
    return self.__cpf

  @property
  def event(self):
    return self.__event

  @event.setter
  def event(self,event):
    self.__event = event

  @property
  def ingresso(self):
    return self.__ingresso

  @ingresso.setter
  def ingresso(self,ingresso):
    self.__ingresso = ingresso

  @property
  def gerar_ingresso(self):
    return self.__gerar_ingresso

  @ingresso.setter
  def gerar_ingresso(self,gerar_ingresso):
    self.__gerar_ingresso = gerar_ingresso

  def comprar_ingresso(self):
    if self.__idade >= 18:
      self._verificada = True
      self.__nome_event = str(input('Digite o nome do Evento que deseja ir: '))
      self.__data_event = str(input('Digite a data desse Evento: '))
      self.__nome_comp = str(input('Digite o seu nome: '))
      self.__cpf = str(input('Digite o seu CPF: '))
      self.__idade = int(input('Digite a sua idade: '))
      de = datetime.strptime(self.__data_event,'%d/%m/%Y')
      dc = datetime.strftime(self._data_compra,'%d/%m/%Y')
      dc1 = datetime.strptime(dc,'%d/%m/%Y')
      self._quantidade_dias = abs((de - dc1).days)
      self._cadastro2 = {"Comprador": {self.__nome_comp}, "CPF": {self.__cpf}, "Idade": {self.__idade}, "Data da Compra": {self._data_compra}, "Quantidade de dias que faltam": {self._quantidade_dias}}
      for c in self.__event:
        if c["Nome"] == self.__nome_event and c["Data"] == self.__data_event:
          self.__ingresso.append(c)
          self.__ingresso.append(self._cadastro2)
          print('\nCompra concluída.')
        else:
          print('\nEvento não encontrado, tente outro.')
    else:
      print('Você não possui idade suficiente.')

  def cancelar_compra(self):
    self.__nome_event = str(input('Digite o nome do Evento do seu ingresso: '))
    self.__data_event = str(input('Digite a data desse Evento: '))
    for c in self.__ingresso:
      if c["Nome"] == self.__nome_event and c["Data"] == self.__data_event:
        v = str(input('Deseja mesmo cancelar essa compra? [Sim/Não]: '))
        if v == "Sim":
          self.__ingresso.remove(c)
          self.__ingresso.remove(self._cadastro2)
          print('\nCompra cancelada.')
        elif v == "Não":
          print('\nOperação encerrada.')
      else:
        print('\nCompra não encontrada.')
