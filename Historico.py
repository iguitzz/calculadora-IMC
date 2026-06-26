"""
Módulo Historico — armazena registros de IMC da sessão atual.

Conceito aplicado:
  - Composição: Historico é composto por objetos RegistroIMC,
    que por sua vez referenciam objetos Pessoa (ou Atleta).
    Historico NÃO herda de Pessoa — ele *possui* pessoas.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Pessoa import Pessoa


@dataclass
class RegistroIMC:
    """
    Representa um único cálculo de IMC registrado no histórico.

    Conceito: dataclass usada para manter simplicidade e imutabilidade
    dos registros — um cálculo feito no passado não deve ser alterado.
    """

    pessoa: "Pessoa"
    imc: float
    classificacao: str
    timestamp: datetime = field(default_factory=datetime.now)

    def __str__(self) -> str:
        hora = self.timestamp.strftime("%d/%m/%Y %H:%M:%S")
        return (
            f"[{hora}] {self.pessoa.nome} ({self.pessoa.tipo()}) "
            f"— IMC: {self.imc:.2f} → {self.classificacao}"
        )


class Historico:
    """
    COMPOSIÇÃO: armazena e gerencia os registros de IMC da sessão.

    Historico é composto por uma lista de RegistroIMC.
    Ele não sabe nem se importa se a pessoa é Pessoa ou Atleta —
    apenas chama os métodos da interface comum (polimorfismo transparente).
    """

    def __init__(self):
        self._registros: List[RegistroIMC] = []

    # ── Métodos públicos ────────────────────────────────────────────────────

    def adicionar(self, pessoa: "Pessoa") -> RegistroIMC:
        """
        Calcula o IMC da pessoa, classifica e armazena no histórico.

        Args:
            pessoa: Objeto Pessoa (ou subclasse — polimorfismo em ação).

        Returns:
            O RegistroIMC criado e armazenado.
        """
        imc = pessoa.calcular_imc()
        classificacao = pessoa.classificar()  # ← polimorfismo: Atleta retorna classificação diferente
        registro = RegistroIMC(pessoa=pessoa, imc=imc, classificacao=classificacao)
        self._registros.append(registro)
        return registro

    def listar(self) -> List[RegistroIMC]:
        """Retorna a lista de registros em ordem cronológica."""
        return list(self._registros)

    def limpar(self) -> int:
        """Limpa o histórico. Retorna a quantidade de registros removidos."""
        quantidade = len(self._registros)
        self._registros.clear()
        return quantidade

    def total(self) -> int:
        """Retorna a quantidade total de registros no histórico."""
        return len(self._registros)

    def exibir(self) -> str:
        """
        Gera uma string formatada com todo o histórico da sessão.

        Returns:
            String multilinha com todos os registros, ou mensagem de vazio.
        """
        if not self._registros:
            return "  Nenhum cálculo realizado nesta sessão ainda."

        linhas = []
        for i, registro in enumerate(self._registros, start=1):
            hora = registro.timestamp.strftime("%d/%m/%Y %H:%M:%S")
            linhas.append(
                f"  {i:>3}. [{hora}]\n"
                f"       Nome          : {registro.pessoa.nome}\n"
                f"       Tipo          : {registro.pessoa.tipo()}\n"
                f"       IMC calculado : {registro.imc:.2f}\n"
                f"       Classificação : {registro.classificacao}\n"
            )
        return "\n".join(linhas)

    def estatisticas(self) -> str:
        """
        Gera estatísticas básicas do histórico da sessão.

        Returns:
            String com média, maior e menor IMC registrado.
        """
        if not self._registros:
            return "  Sem dados para calcular estatísticas."

        imcs = [r.imc for r in self._registros]
        media = sum(imcs) / len(imcs)
        maior = max(imcs)
        menor = min(imcs)

        reg_maior = next(r for r in self._registros if r.imc == maior)
        reg_menor = next(r for r in self._registros if r.imc == menor)

        return (
            f"  Total de cálculos : {self.total()}\n"
            f"  IMC médio         : {media:.2f}\n"
            f"  Maior IMC         : {maior:.2f} ({reg_maior.pessoa.nome})\n"
            f"  Menor IMC         : {menor:.2f} ({reg_menor.pessoa.nome})"
        )
