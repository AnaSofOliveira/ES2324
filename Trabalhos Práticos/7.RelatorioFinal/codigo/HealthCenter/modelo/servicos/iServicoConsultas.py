#!/usr/bin/python
#-*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class iServicoConsultas(ABC):

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    
    @abstractmethod
    def adicionarConsulta(self, paciente, especialidade, data):
        raise NotImplementedError

    
    @abstractmethod
    def confirmarConsulta(self, consulta, medico, administrativo):
        raise NotImplementedError

    
    @abstractmethod
    def cancelarConsulta(self, consulta):
        raise NotImplementedError

    
    @abstractmethod
    def reagendarConsulta(self, consulta, data):
        raise NotImplementedError

    
    @abstractmethod
    def submeterReceitas(self, consulta, medicamentos):
        raise NotImplementedError

    
    @abstractmethod
    def consultarReceitas(self, consulta):
        raise NotImplementedError

    
    @abstractmethod
    def exportarReceitas(self, consulta):
        raise NotImplementedError

    
    @abstractmethod
    def submeterExames(self, consulta, exames):
        raise NotImplementedError

    
    @abstractmethod
    def consultarExames(self, consulta):
        raise NotImplementedError

    
    @abstractmethod
    def submeterResultadoExame(self, consulta, exame):
        raise NotImplementedError

    
    @abstractmethod
    def exportarExames(self, consulta):
        raise NotImplementedError

