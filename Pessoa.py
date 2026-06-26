"""
Classe Pessoa — representa uma pessoa comum para cálculo de IMC.

Conceitos aplicados:
  - Herança: herda de PessoaBase (classe abstrata)
  - Encapsulamento: atributos validados via @property (getters/setters)
  - Polimorfismo: classificar() é sobrescrito por subclasses como Atleta
"""

import re
from PessoaBase import PessoaBase
from EntradaInvalidaException import (
    NomeInvalidoError,
    IdadeInvalidaError,
    PesoInvalidoError,
    AlturaInvalidaError,
)


class Pessoa(PessoaBase):
    """
    Representa uma pessoa comum para fins de cálculo de IMC.

    Implementa todos os métodos abstratos de PessoaBase e adiciona
    validação completa via setters (encapsulamento).

    Atributos:
        _nome   (str)   : Nome completo da pessoa.
        _idade  (int)   : Idade em anos.
        _peso   (float) : Peso em quilogramas.
        _altura (float) : Altura em metros.
    """

    # Tabela de classificação da OMS para pessoas comuns
    _TABELA_OMS = [
        (18.5, "Abaixo do peso"),
        (25.0, "Peso normal"),
        (30.0, "Sobrepeso"),
        (35.0, "Obesidade Grau I"),
        (40.0, "Obesidade Grau II"),
        (float("inf"), "Obesidade Grau III"),
    ]

    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        # Inicializa PessoaBase com valores temporários e depois aplica setters
        super().__init__(nome, idade, peso, altura)
        # Reaplica via setters para garantir validação
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    # ── Propriedades com validação (Encapsulamento) ──────────────────────────

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise NomeInvalidoError(valor)
        valor = valor.strip()
        if len(valor) < 2:
            raise NomeInvalidoError(valor)
        # Permite letras (incluindo acentuadas), espaços e hífens
        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s\-']+$", valor):
            raise NomeInvalidoError(valor)
        self._nome = valor.title()

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, valor):
        try:
            valor = int(valor)
        except (TypeError, ValueError):
            raise IdadeInvalidaError(valor)
        if not (0 <= valor <= 130):
            raise IdadeInvalidaError(valor)
        self._idade = valor

    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, valor):
        try:
            valor = float(valor)
        except (TypeError, ValueError):
            raise PesoInvalidoError(valor)
        if not (0.1 <= valor <= 500):
            raise PesoInvalidoError(valor)
        self._peso = valor

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, valor):
        try:
            valor = float(valor)
        except (TypeError, ValueError):
            raise AlturaInvalidaError(valor)
        if not (0.5 <= valor <= 3.0):
            raise AlturaInvalidaError(valor)
        self._altura = valor

    # ── Implementação dos métodos abstratos ──────────────────────────────────

    def calcular_imc(self) -> float:
        """Calcula e retorna o IMC: Peso / Altura²."""
        return self._peso / (self._altura ** 2)

    def classificar(self) -> str:
        """
        Classifica o IMC conforme a tabela da OMS.
        Este método é polimórfico — subclasses podem sobrescrevê-lo.
        """
        imc = self.calcular_imc()
        for limite, classificacao in self._TABELA_OMS:
            if imc < limite:
                return classificacao
        return "Obesidade Grau III"

    def tipo(self) -> str:
        """Retorna o tipo de pessoa (para exibição no histórico)."""
        return "Pessoa"

    def resumo(self) -> str:
        """Retorna um resumo formatado dos dados da pessoa."""
        imc = self.calcular_imc()
        classificacao = self.classificar()
        return (
            f"  Nome         : {self._nome}\n"
            f"  Tipo         : {self.tipo()}\n"
            f"  Idade        : {self._idade} anos\n"
            f"  Peso         : {self._peso:.1f} kg\n"
            f"  Altura       : {self._altura:.2f} m\n"
            f"  IMC          : {imc:.2f}\n"
            f"  Classificação: {classificacao}"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"nome={self._nome!r}, "
            f"idade={self._idade}, "
            f"peso={self._peso}, "
            f"altura={self._altura})"
        )

    def __str__(self) -> str:
        return f"{self._nome} ({self.tipo()}) — IMC: {self.calcular_imc():.2f} [{self.classificar()}]"
