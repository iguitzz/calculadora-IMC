from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Pessoa import Pessoa
    from Atleta import Atleta
    from Historico import Historico


class CalculadoraIMC(ABC):    

    @abstractmethod
    def cadastrar_pessoa(self, nome: str, idade: int, peso: float, altura: float) -> "Pessoa":
        """Cria e registra uma Pessoa no sistema."""
        ...

    @abstractmethod
    def cadastrar_atleta(
        self,
        nome: str,
        idade: int,
        peso: float,
        altura: float,
        esporte: str,
        nivel: str,
    ) -> "Atleta":
        """Cria e registra um Atleta no sistema."""
        ...

    @abstractmethod
    def calcular_e_registrar(self, pessoa: "Pessoa") -> float:
        """Calcula o IMC da pessoa e salva no histórico."""
        ...

    @abstractmethod
    def obter_historico(self) -> "Historico":
        """Retorna o histórico de cálculos da sessão."""
        ...

    @abstractmethod
    def listar_pessoas(self) -> List["Pessoa"]:
        """Retorna a lista de pessoas cadastradas."""
        ...
