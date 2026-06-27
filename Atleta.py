from Pessoa import Pessoa
from EntradaInvalidaException import EsporteInvalidoError


class Atleta(Pessoa):
  
    # Tabela de IMC adaptada para atletas (considera maior massa muscular)
    _TABELA_ATLETA = [
        (17.0, "Abaixo do peso (atleta — risco de deficiência nutricional)"),
        (23.0, "Peso normal (atleta — composição corporal ideal)"),
        (28.0, "Levemente acima (atleta — possível excesso de massa muscular)"),
        (33.0, "Sobrepeso (atleta — avaliação complementar recomendada)"),
        (float("inf"), "Obesidade (atleta — consulte um médico especialista)"),
    ]

    NIVEIS_VALIDOS = ("Amador", "Semiprofissional", "Profissional")

    def __init__(
        self,
        nome: str,
        idade: int,
        peso: float,
        altura: float,
        esporte: str,
        nivel: str = "Profissional",
    ):
        # Chama o construtor da classe pai (Pessoa → PessoaBase)
        super().__init__(nome, idade, peso, altura)
        self.esporte = esporte
        self.nivel = nivel

    # ── Propriedades adicionais ─────────────────────────────────────────────

    @property
    def esporte(self) -> str:
        return self._esporte

    @esporte.setter
    def esporte(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise EsporteInvalidoError(valor)
        self._esporte = valor.strip().title()

    @property
    def nivel(self) -> str:
        return self._nivel

    @nivel.setter
    def nivel(self, valor: str):
        # Normaliza capitalização antes de validar
        valor_norm = valor.strip().title() if isinstance(valor, str) else valor
        if valor_norm not in self.NIVEIS_VALIDOS:
            raise ValueError(
                f"Nível inválido: '{valor}'. "
                f"Escolha entre: {', '.join(self.NIVEIS_VALIDOS)}."
            )
        self._nivel = valor_norm

    # ── Polimorfismo ────────────────────────────────────────────────────────

    def classificar(self) -> str:
        
        imc = self.calcular_imc()
        for limite, classificacao in self._TABELA_ATLETA:
            if imc < limite:
                return classificacao
        return "Obesidade (atleta — consulte um médico especialista)"

    def tipo(self) -> str:
      
        return f"Atleta ({self._nivel})"

    def resumo(self) -> str:
       
        imc = self.calcular_imc()
        classificacao = self.classificar()
        return (
            f"  Nome                  : {self._nome}\n"
            f"  Tipo                  : {self.tipo()}\n"
            f"  Esporte               : {self._esporte}\n"
            f"  Idade                 : {self._idade} anos\n"
            f"  Peso                  : {self._peso:.1f} kg\n"
            f"  Altura                : {self._altura:.2f} m\n"
            f"  IMC                   : {imc:.2f}\n"
            f"  Classificação (atleta): {classificacao}\n"
            f"  ⚠  Nota: atletas possuem maior massa muscular,\n"
            f"     o que pode elevar o IMC sem indicar sobrepeso real."
        )
