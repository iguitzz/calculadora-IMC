"""
Módulo SistemaIMC — orquestra Pessoa, Atleta e Historico (Composição).

Conceitos aplicados:
  - Composição: SistemaIMC possui uma lista de Pessoa/Atleta e um Historico.
    Ele orquestra as operações entre esses objetos sem herdar deles.
  - Implementação da interface CalculadoraIMC.
"""

from typing import List

from CalculadoraIMC import CalculadoraIMC
from Pessoa import Pessoa
from Atleta import Atleta
from Historico import Historico, RegistroIMC
from CalculadoraRecursiva import CalculadoraRecursiva


class SistemaIMC(CalculadoraIMC):
    """
    COMPOSIÇÃO + ORQUESTRAÇÃO: implementação concreta da interface CalculadoraIMC.

    SistemaIMC coordena:
      - Lista de Pessoa/Atleta cadastrados (composição)
      - Historico de registros da sessão (composição)
      - CalculadoraRecursiva para operações sobre a lista (associação)

    Não herda de Pessoa nem de Historico — apenas os *possui* e os orquestra.
    """

    def __init__(self):
        self._pessoas: List[Pessoa] = []
        self._historico: Historico = Historico()  # COMPOSIÇÃO

    # ── Implementação da interface CalculadoraIMC ────────────────────────────

    def cadastrar_pessoa(self, nome: str, idade: int, peso: float, altura: float) -> Pessoa:
        """Cria e registra uma Pessoa no sistema."""
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
        """Cria e registra um Atleta no sistema."""
        atleta = Atleta(nome, idade, peso, altura, esporte, nivel)
        self._pessoas.append(atleta)
        return atleta

    def calcular_e_registrar(self, pessoa: Pessoa) -> RegistroIMC:
        """
        Calcula o IMC da pessoa e salva o registro no histórico.

        Args:
            pessoa: Objeto Pessoa ou Atleta já cadastrado.

        Returns:
            O RegistroIMC criado.
        """
        return self._historico.adicionar(pessoa)

    def obter_historico(self) -> Historico:
        """Retorna o histórico de cálculos da sessão."""
        return self._historico

    def listar_pessoas(self) -> List[Pessoa]:
        """Retorna a lista de pessoas cadastradas (cópia defensiva)."""
        return list(self._pessoas)

    # ── Métodos de estatísticas (usa CalculadoraRecursiva) ───────────────────

    def media_imc_sessao(self) -> float:
        """
        Calcula a média de IMC de todas as pessoas cadastradas
        usando a CalculadoraRecursiva (recursão).
        """
        return CalculadoraRecursiva.media_imc_recursiva(self._pessoas)

    def pessoa_maior_imc(self) -> "Pessoa | None":
        """
        Encontra a pessoa com maior IMC usando a CalculadoraRecursiva (recursão).
        """
        return CalculadoraRecursiva.maior_imc_recursiva(self._pessoas)

    def relatorio_classificacoes(self) -> List[str]:
        """
        Retorna a classificação de cada pessoa cadastrada
        usando a CalculadoraRecursiva (recursão).
        """
        return CalculadoraRecursiva.classificar_lista(self._pessoas)

    def total_cadastrados(self) -> int:
        """Retorna a quantidade de pessoas cadastradas no sistema."""
        return len(self._pessoas)
