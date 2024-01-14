#!/usr/bin/python
#-*- coding: utf-8 -*-

from apresentacao.Vista import Vista

class VistaPaciente(Vista):
    def VistaPaciente(self):
        self.__consultas = None

    def mostrarEcraConsultas(self, consultas):
        print("Consultas:")
        for consulta in consultas:
            print (consulta)


    def mostrarEcraExames(self):
        pass

    def mostrarEcraReceitas(self):
        pass

