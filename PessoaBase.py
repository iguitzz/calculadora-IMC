from abc import ABC, abstractmethod


class PessoaBase(ABC):
    def __init__(self, nome: str, idade: int, peso: float, altura: float):      
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
