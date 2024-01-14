#!/usr/bin/python
#-*- coding: utf-8 -*-

from controlo.Controlador import Controlador

class ControladorAdministrativo(Controlador):
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

    def consultarExames(self, codigoConsulta):
        pass

    def submeterResultadoExame(self, codigoConsulta, nomeExame, resultado):
        pass

