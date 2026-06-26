"""
Módulo CalculadoraRecursiva — demonstra o uso de recursão no cálculo de IMC.

Conceito aplicado:
  - Recursão: funções que se chamam a si mesmas para validar entradas
    e processar listas de pessoas de forma recursiva.
"""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Pessoa import Pessoa


class CalculadoraRecursiva:
    """
    Fornece operações recursivas sobre listas de pessoas e IMCs.

    Métodos estáticos que demonstram recursão aplicada ao domínio do IMC:
      - soma_imc_recursiva()    → soma todos os IMCs de uma lista
      - media_imc_recursiva()   → calcula a média recursivamente
      - maior_imc_recursiva()   → encontra o maior IMC por recursão
      - classificar_lista()     → classifica cada pessoa da lista recursivamente
    """

    @staticmethod
    def soma_imc_recursiva(pessoas: List["Pessoa"], indice: int = 0) -> float:
        """
        RECURSÃO: soma os IMCs de todas as pessoas na lista.

        Caso base  : indice >= len(pessoas) → retorna 0.0
        Caso rec.  : IMC da pessoa atual + soma do restante da lista.

        Args:
            pessoas: Lista de objetos Pessoa/Atleta.
            indice : Posição atual na lista (padrão 0).

        Returns:
            Soma total dos IMCs.
        """
        if indice >= len(pessoas):
            return 0.0
        return pessoas[indice].calcular_imc() + CalculadoraRecursiva.soma_imc_recursiva(pessoas, indice + 1)

    @staticmethod
    def media_imc_recursiva(pessoas: List["Pessoa"]) -> float:
        """
        Calcula a média dos IMCs usando soma_imc_recursiva().

        Args:
            pessoas: Lista de objetos Pessoa/Atleta.

        Returns:
            Média dos IMCs, ou 0.0 se a lista estiver vazia.
        """
        if not pessoas:
            return 0.0
        total = CalculadoraRecursiva.soma_imc_recursiva(pessoas)
        return total / len(pessoas)

    @staticmethod
    def maior_imc_recursiva(pessoas: List["Pessoa"], indice: int = 0) -> "Pessoa | None":
        """
        RECURSÃO: encontra a pessoa com maior IMC na lista.

        Caso base  : indice == len(pessoas) - 1 → retorna a última pessoa.
        Caso rec.  : compara a pessoa atual com o maior do restante.

        Args:
            pessoas: Lista de objetos Pessoa/Atleta (não vazia).
            indice : Posição atual na lista (padrão 0).

        Returns:
            Objeto Pessoa com o maior IMC, ou None se a lista estiver vazia.
        """
        if not pessoas:
            return None
        if indice == len(pessoas) - 1:
            return pessoas[indice]
        candidato = CalculadoraRecursiva.maior_imc_recursiva(pessoas, indice + 1)
        if pessoas[indice].calcular_imc() >= candidato.calcular_imc():
            return pessoas[indice]
        return candidato

    @staticmethod
    def classificar_lista(pessoas: List["Pessoa"], indice: int = 0) -> List[str]:
        """
        RECURSÃO: classifica cada pessoa da lista e retorna uma lista de strings.

        Caso base  : indice >= len(pessoas) → retorna lista vazia.
        Caso rec.  : classificação da pessoa atual + classificações do restante.

        Args:
            pessoas: Lista de objetos Pessoa/Atleta.
            indice : Posição atual na lista (padrão 0).

        Returns:
            Lista de strings no formato "Nome → Classificação (IMC: X.XX)".
        """
        if indice >= len(pessoas):
            return []
        p = pessoas[indice]
        entrada = f"{p.nome} → {p.classificar()} (IMC: {p.calcular_imc():.2f})"
        return [entrada] + CalculadoraRecursiva.classificar_lista(pessoas, indice + 1)
