from dataclasses import dataclass, field
from datetime import datetime
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Pessoa import Pessoa


@dataclass
class RegistroIMC:  

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

    def __init__(self):
        self._registros: List[RegistroIMC] = []

    # ── Métodos públicos ────────────────────────────────────────────────────

    def adicionar(self, pessoa: "Pessoa") -> RegistroIMC:
       
        imc = pessoa.calcular_imc()
        classificacao = pessoa.classificar()  # ← polimorfismo: Atleta retorna classificação diferente
        registro = RegistroIMC(pessoa=pessoa, imc=imc, classificacao=classificacao)
        self._registros.append(registro)
        return registro

    def listar(self) -> List[RegistroIMC]:
      
        return list(self._registros)

    def limpar(self) -> int:
       
        quantidade = len(self._registros)
        self._registros.clear()
        return quantidade

    def total(self) -> int:
       
        return len(self._registros)

    def exibir(self) -> str:
        
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
