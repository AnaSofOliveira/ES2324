from HealthCenter.apresentacao.VistaPaciente import VistaPaciente
from HealthCenter.controlo.ControladorPaciente import ControladorPaciente

class TestesConsulta: 

    def main(self):
        print("Testes de Consulta")
        print("1. Teste de Consulta de um Paciente")

        vista = VistaPaciente()
        controlador = ControladorPaciente(vista)
        listaConsultas = controlador.adicionarConsulta(1, "Cardiologia", "2019-12-12")
        vista.mostrarConsultas(listaConsultas)

