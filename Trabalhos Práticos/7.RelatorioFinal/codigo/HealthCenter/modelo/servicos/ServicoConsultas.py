#!/usr/bin/python
#-*- coding: utf-8 -*-

from modelo.servicos.iServicoConsultas import iServicoConsultas
from modelo.entidades.Consulta import Consulta

class ServicoConsultas(iServicoConsultas):
    def ServicoConsultas(self):
        self.__consultas = []

    def adicionarConsulta(self, idPaciente, especialidade, dataMarcacao):
        self.__consulta = Consulta().agendarConsulta(idPaciente, especialidade, dataMarcacao)
        if isinstance(self.__consulta, Consulta): 
            self.__consultas.append(self.__consulta)
            return self.__consultas
        return None

    def confirmarConsulta(self, codigoConsulta, cedulaMedico, idAdmin):
        pass

    def cancelarConsulta(self, codigoConsulta):
        pass

    def reagendarConsulta(self, codigoCosulta, novaData):
        pass

    def sumeterReceitas(self, codigoConsulta, medicamentos, int):
        pass

    def consultarReceitas(self, codigoConsulta):
        pass

    def exportarReceitas(self, codigoConsulta):
        pass

    def submeterExames(self, codigoConsulta, exames):
        pass

    def consultarExames(self, codigoConsulta):
        pass

    def submeterResultadoExame(self, codigoConsulta, nomeExame, resultado):
        pass

    def exportarExames(self, codigoConsulta):
        pass

    def adicionarConsultaServico(self, consulta):
        pass

    def atualizarConsultaServico(self, novaConsulta):
        pass

    def removerConsultaServico(self, consulta):
        pass

