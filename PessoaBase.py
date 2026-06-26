"""
Classe abstrata PessoaBase — define a interface comum a todas as pessoas.

Conceitos aplicados:
  - Abstração: métodos abstratos obrigam subclasses a implementar o contrato
  - Encapsulamento: atributos protegidos acessados via @property
"""

from abc import ABC, abstractmethod


class PessoaBase(ABC):
    """
    Classe abstrata que define o contrato para qualquer tipo de pessoa
    que possa ter seu IMC calculado.

    Subclasses concretas devem implementar:
        - calcular_imc()  → float
        - classificar()   → str
        - tipo()          → str
        - resumo()        → str
    """

    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        """
        Inicializa os atributos comuns. As validações ficam nos setters
        das subclasses concretas.
        """
        self._nome: str = nome
        self._idade: int = idade
        self._peso: float = peso
        self._altura: float = altura

    # ── Interface abstrata ───────────────────────────────────────────────────

    @abstractmethod
    def calcular_imc(self) -> float:
        """Calcula e retorna o Índice de Massa Corporal (IMC)."""
        ...

    @abstractmethod
    def classificar(self) -> str:
        """Classifica o IMC e retorna a categoria correspondente."""
        ...

    @abstractmethod
    def tipo(self) -> str:
        """Retorna uma string descrevendo o tipo de pessoa (ex.: 'Pessoa', 'Atleta')."""
        ...

    @abstractmethod
    def resumo(self) -> str:
        """Retorna um resumo textual formatado com os dados da pessoa."""
        ...

    # ── Propriedades comuns ──────────────────────────────────────────────────

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self) -> int:
        return self._idade

    @property
    def peso(self) -> float:
        return self._peso

    @property
    def altura(self) -> float:
        return self._altura

    # ── Representação ────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"nome={self._nome!r}, "
            f"idade={self._idade}, "
            f"peso={self._peso}, "
            f"altura={self._altura})"
        )

    def __str__(self) -> str:
        return (
            f"{self._nome} ({self.tipo()}) "
            f"— IMC: {self.calcular_imc():.2f} [{self.classificar()}]"
        )
