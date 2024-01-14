#!/usr/bin/python
#-*- coding: utf-8 -*-

from modelo.dao.DaoConsulta import DaoConsulta

class Consulta:

    def Consulta(self):
        self.__dao = DaoConsulta()

    def Consulta(self, codigoConsulta):
        self.__codigoConsulta = codigoConsulta
        self.__dao = DaoConsulta()

    def agendarConsulta(self, paciente, especialidade, dataMarcacao):
        self.__paciente = paciente
        self.__especialidade = especialidade
        self.__dataMarcacao = dataMarcacao
        return (self.__dao.criar(self))

    def confirmarConsulta(self, medico):
        pass

    def cancelarConsulta(self):
        pass

    def reagendarConsulta(self, paciente, novaData):
        pass

    def adicionarReceita(self, receita):
        pass

    def obterReceitas(self):
        pass

    def adicionarPaciente(self, paciente):
        pass

    def adicionarEspecialidade(self, especialidade):
        pass

    def adicionarDataMarcacao(self, dataMarcacao):
        pass

    def adicionarAdministrativo(self, administrativo):
        pass

    def adicionarMedico(self, medico):
        pass

    def adicionarExame(self, exame):
        pass

    def obterExames(self):
        pass

    def obterExame(self, nomeExame):
        pass

    def obterCodigo(self):
        pass

