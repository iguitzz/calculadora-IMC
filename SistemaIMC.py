from typing import List

from CalculadoraIMC import CalculadoraIMC
from Pessoa import Pessoa
from Atleta import Atleta
from Historico import Historico, RegistroIMC
from CalculadoraRecursiva import CalculadoraRecursiva


class SistemaIMC(CalculadoraIMC):
    
    def __init__(self):
        self._pessoas: List[Pessoa] = []
        self._historico: Historico = Historico()  # COMPOSIÇÃO

    # ── Implementação da interface CalculadoraIMC ────────────────────────────

    def cadastrar_pessoa(self, nome: str, idade: int, peso: float, altura: float) -> Pessoa:
        pessoa = Pessoa(nome, idade, peso, altura)
        self._pessoas.append(pessoa)
        return pessoa

    def cadastrar_atleta(
        self,
        nome: str,
        idade: int,
        peso: float,
        altura: float,
        esporte: str,
        nivel: str = "Profissional",
    ) -> Atleta:
        atleta = Atleta(nome, idade, peso, altura, esporte, nivel)
        self._pessoas.append(atleta)
        return atleta

    def calcular_e_registrar(self, pessoa: Pessoa) -> RegistroIMC:      
        return self._historico.adicionar(pessoa)

    def obter_historico(self) -> Historico:
        return self._historico

    def listar_pessoas(self) -> List[Pessoa]:
        return list(self._pessoas)

    # ── Métodos de estatísticas (usa CalculadoraRecursiva) ───────────────────

    def media_imc_sessao(self) -> float:      
        return CalculadoraRecursiva.media_imc_recursiva(self._pessoas)

    def pessoa_maior_imc(self) -> "Pessoa | None":       
        return CalculadoraRecursiva.maior_imc_recursiva(self._pessoas)

    def relatorio_classificacoes(self) -> List[str]:      
        return CalculadoraRecursiva.classificar_lista(self._pessoas)

    def total_cadastrados(self) -> int:       
        return len(self._pessoas)
