#!/usr/bin/python
#-*- coding: utf-8 -*-

class Controlador:
    def __init__(self):
        pass

    def adicionarConsulta(self, idPaciente, especialidade, dataMarcacao):
        pass

    def confirmarConsulta(self, codigoConsulta, cedulaMedico, idAdmin):
        pass

    def cancelarConsulta(self, codigoConsulta):
        pass

    def reagendarConsulta(self, codigoConsulta, novaData):
        pass

    def consultarReceitas(self, codigoConsulta):
        pass

    def exportarReceitas(self, codigoConsulta):
        pass

    def submeterReceitas(self, codigoConsulta, medicamentos, int):
        pass

    def submeterExames(self, codigoConsulta, exames):
        pass

    def consultarExames(self, codigoConsulta):
        pass

    def submeterResultadoExame(self, codigoConsulta, nomeExame, resultado):
        pass

    def exportarExames(self, codigoConsulta):
        pass

