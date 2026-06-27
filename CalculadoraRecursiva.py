from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Pessoa import Pessoa


class CalculadoraRecursiva:
   
    @staticmethod
    def soma_imc_recursiva(pessoas: List["Pessoa"], indice: int = 0) -> float:
        
        if indice >= len(pessoas):
            return 0.0
        return pessoas[indice].calcular_imc() + CalculadoraRecursiva.soma_imc_recursiva(pessoas, indice + 1)

    @staticmethod
    def media_imc_recursiva(pessoas: List["Pessoa"]) -> float:
       
        if not pessoas:
            return 0.0
        total = CalculadoraRecursiva.soma_imc_recursiva(pessoas)
        return total / len(pessoas)

    @staticmethod
    def maior_imc_recursiva(pessoas: List["Pessoa"], indice: int = 0) -> "Pessoa | None":
       
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
        
        if indice >= len(pessoas):
            return []
        p = pessoas[indice]
        entrada = f"{p.nome} → {p.classificar()} (IMC: {p.calcular_imc():.2f})"
        return [entrada] + CalculadoraRecursiva.classificar_lista(pessoas, indice + 1)
