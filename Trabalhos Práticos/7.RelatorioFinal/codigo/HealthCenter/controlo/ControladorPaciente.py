#!/usr/bin/python
#-*- coding: utf-8 -*-

from controlo.Controlador import Controlador
from modelo.servicos.ServicoConsultas import ServicoConsultas

class ControladorPaciente(Controlador):
    def ControladorPaciente(self, vista):
        self.__servicoConsultas = ServicoConsultas()
        self.__vista = vista

    def adicionarConsulta(self, idPaciente, especialidade, dataMarcacao):
        consultas = self.__servicoConsultas.adicionarConsulta(idPaciente, especialidade, dataMarcacao)
        self.__vista.mostrarEcraConsultas(consultas)

    def cancelarConsulta(self, codigoConsulta):
        pass

    def reagendarConsulta(self, codigoConsulta, novaData):
        pass

    def consultarReceitas(self, codigoConsulta):
        pass

    def exportarReceitas(self, codigoConsulta):
        pass

    def consultarExames(self, codigoConsulta):
        pass

    def submeterResultadoExame(self, codigoConsulta, nomeExame, resultado):
        pass

    def exportarExames(self, codigoConsulta):
        pass

