#!/usr/bin/python
#-*- coding: utf-8 -*-

from modelo.dao.iDao import iDao

class DaoConsulta(iDao):
    def __init__(self):
        pass

    def daoConsultas(self, ):
        pass

    def criar(self, entidade):
        with open(".\codigo\consultas.txt", 'w') as f:
            f.write(str(entidade))
        

    def ler(self, entidade):
        with open(".\codigo\consultas.txt", 'r') as f:
            for line in f:
                if line.startswith(entidade.id):
                    return line

    def atualizar(self, entidade):
        pass

    def eliminar(self, entidade):
        pass

