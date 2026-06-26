"""
╔══════════════════════════════════════════════════════════════════╗
║         CALCULADORA DE IMC — Sistema via Linha de Comando        ║
║                                                                  ║
║  Conceitos de POO demonstrados:                                  ║
║    • Encapsulamento  — atributos protegidos com getters/setters  ║
║    • Herança         — Atleta extends Pessoa extends PessoaBase  ║
║    • Polimorfismo    — classificar() com comportamentos distintos ║
║    • Composição      — SistemaIMC composto por Historico         ║
║    • Interface       — CalculadoraIMC (contrato abstrato)        ║
║    • Recursão        — CalculadoraRecursiva                      ║
║    • Exceções custom — hierarquia EntradaInvalidaException       ║
╚══════════════════════════════════════════════════════════════════╝

Ponto de entrada da aplicação. Execute com:
    python Main.py
"""

import os
import sys
import re

# Garante que o diretório atual (src/main/py) esteja no path de importação
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from SistemaIMC import SistemaIMC
from EntradaInvalidaException import (
    EntradaInvalidaException,
    NomeInvalidoError,
    IdadeInvalidaError,
    PesoInvalidoError,
    AlturaInvalidaError,
    EsporteInvalidoError,
    OpcaoInvalidaError,
    NenhumaCadastraError,
)
from Atleta import Atleta
from CalculadoraRecursiva import CalculadoraRecursiva


# ── Constantes de formatação ────────────────────────────────────────────────

LINHA  = "═" * 62
LINHA2 = "─" * 62
COR_TITULO    = "\033[1;36m"   # Ciano brilhante
COR_OPCAO     = "\033[1;33m"   # Amarelo
COR_SUCESSO   = "\033[1;32m"   # Verde
COR_ERRO      = "\033[1;31m"   # Vermelho
COR_INFO      = "\033[0;37m"   # Cinza claro
COR_DESTAQUE  = "\033[1;35m"   # Magenta
COR_RESET     = "\033[0m"


def limpar_tela():
    """Limpa o terminal (compatível com Windows e Unix)."""
    os.system("cls" if os.name == "nt" else "clear")


def cor(texto: str, codigo: str) -> str:
    """Aplica código de cor ANSI ao texto."""
    return f"{codigo}{texto}{COR_RESET}"


def cabecalho():
    """Exibe o cabeçalho estilizado da aplicação."""
    print(cor(f"\n  {LINHA}", COR_TITULO))
    print(cor("  ║  🏋️  CALCULADORA DE IMC — CLI                           ║", COR_TITULO))
    print(cor("  ║  Índice de Massa Corporal com Suporte a Atletas          ║", COR_TITULO))
    print(cor(f"  {LINHA}\n", COR_TITULO))


def separador(titulo: str = ""):
    """Imprime um separador com título opcional."""
    if titulo:
        print(cor(f"\n  ── {titulo} {'─' * (56 - len(titulo))}", COR_DESTAQUE))
    else:
        print(cor(f"\n  {LINHA2}", COR_INFO))


def menu_principal() -> str:
    """Exibe o menu interativo e retorna a opção escolhida."""
    print(cor(f"  {LINHA2}", COR_INFO))
    print(cor("  MENU PRINCIPAL", COR_TITULO))
    print(cor(f"  {LINHA2}\n", COR_INFO))

    opcoes = [
        ("1", "👤  Cadastrar Pessoa Comum"),
        ("2", "🏅  Cadastrar Atleta"),
        ("3", "📊  Calcular IMC de pessoa cadastrada"),
        ("4", "📋  Exibir Histórico completo"),
        ("5", "📈  Ver Estatísticas da sessão"),
        ("6", "🔢  Relatório recursivo de classificações"),
        ("7", "🗑   Limpar Histórico"),
        ("8", "ℹ️   Sobre o sistema / Tabelas de IMC"),
        ("0", "🚪  Sair"),
    ]

    for num, descricao in opcoes:
        print(f"  {cor(f'[{num}]', COR_OPCAO)}  {descricao}")

    print()
    opcao = input("  Digite sua opção: ").strip()
    return opcao


# ── Utilitários de leitura de entradas ──────────────────────────────────────

def ler_nome(prompt: str = "Nome") -> str:
    """Lê e valida um nome do usuário."""
    while True:
        try:
            valor = input(f"  {prompt}: ").strip()
            if not valor or len(valor) < 2:
                raise NomeInvalidoError(valor)
            if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s\-']+$", valor):
                raise NomeInvalidoError(valor)
            return valor.title()
        except NomeInvalidoError as e:
            print(f"\n  {e}\n")


def ler_idade(prompt: str = "Idade (anos)") -> int:
    """Lê e valida uma idade do usuário."""
    while True:
        try:
            valor = input(f"  {prompt}: ").strip()
            if not valor:
                raise IdadeInvalidaError(valor)
            idade = int(valor)
            if not (0 <= idade <= 130):
                raise IdadeInvalidaError(valor)
            return idade
        except ValueError:
            print(f"\n  [ERRO] Idade inválida. Digite um número inteiro (ex.: 25).\n")
        except IdadeInvalidaError as e:
            print(f"\n  {e}\n")


def ler_peso(prompt: str = "Peso em kg (ex.: 70.5)") -> float:
    """Lê e valida um peso do usuário."""
    while True:
        try:
            valor = input(f"  {prompt}: ").strip().replace(",", ".")
            if not valor:
                raise PesoInvalidoError(valor)
            peso = float(valor)
            if not (0.1 <= peso <= 500):
                raise PesoInvalidoError(valor)
            return peso
        except ValueError:
            print(f"\n  [ERRO] Peso inválido. Digite um número (ex.: 70.5 ou 70,5).\n")
        except PesoInvalidoError as e:
            print(f"\n  {e}\n")


def ler_altura(prompt: str = "Altura em metros (ex.: 1.75)") -> float:
    """Lê e valida uma altura do usuário."""
    while True:
        try:
            valor = input(f"  {prompt}: ").strip().replace(",", ".")
            if not valor:
                raise AlturaInvalidaError(valor)
            altura = float(valor)
            if not (0.5 <= altura <= 3.0):
                raise AlturaInvalidaError(valor)
            return altura
        except ValueError:
            print(f"\n  [ERRO] Altura inválida. Digite um número (ex.: 1.75 ou 1,75).\n")
        except AlturaInvalidaError as e:
            print(f"\n  {e}\n")


def ler_esporte(prompt: str = "Esporte praticado (ex.: Natação)") -> str:
    """Lê e valida o esporte de um atleta."""
    while True:
        try:
            valor = input(f"  {prompt}: ").strip()
            if not valor:
                raise EsporteInvalidoError(valor)
            return valor.title()
        except EsporteInvalidoError as e:
            print(f"\n  {e}\n")


def ler_nivel(prompt: str = "Nível") -> str:
    """Lê e valida o nível de treinamento de um atleta."""
    niveis = Atleta.NIVEIS_VALIDOS
    while True:
        print(f"\n  Níveis disponíveis:")
        for i, nivel in enumerate(niveis, start=1):
            print(f"    {i}. {nivel}")
        try:
            escolha = input(f"  {prompt} (1-{len(niveis)}): ").strip()
            idx = int(escolha) - 1
            if 0 <= idx < len(niveis):
                return niveis[idx]
            print(f"\n  [ERRO] Escolha um número entre 1 e {len(niveis)}.\n")
        except ValueError:
            print(f"\n  [ERRO] Entrada inválida. Digite um número entre 1 e {len(niveis)}.\n")


# ── Ações do menu ───────────────────────────────────────────────────────────

def cadastrar_pessoa(sistema: SistemaIMC):
    """Coleta dados e cria um objeto Pessoa via SistemaIMC."""
    separador("Cadastrar Pessoa Comum")
    print(cor("  Preencha os dados da pessoa:\n", COR_INFO))

    nome   = ler_nome()
    idade  = ler_idade()
    peso   = ler_peso()
    altura = ler_altura()

    pessoa = sistema.cadastrar_pessoa(nome, idade, peso, altura)
    print(cor(f"\n  ✅  Pessoa '{pessoa.nome}' cadastrada com sucesso!", COR_SUCESSO))


def cadastrar_atleta(sistema: SistemaIMC):
    """Coleta dados e cria um objeto Atleta via SistemaIMC."""
    separador("Cadastrar Atleta")
    print(cor(
        "  ⚡  Atletas possuem tabela de IMC diferenciada\n"
        "      (maior massa muscular eleva o IMC sem indicar sobrepeso).\n",
        COR_INFO,
    ))
    print(cor("  Preencha os dados do atleta:\n", COR_INFO))

    nome    = ler_nome()
    idade   = ler_idade()
    peso    = ler_peso()
    altura  = ler_altura()
    esporte = ler_esporte()
    nivel   = ler_nivel()

    atleta = sistema.cadastrar_atleta(nome, idade, peso, altura, esporte, nivel)
    print(cor(f"\n  ✅  Atleta '{atleta.nome}' ({atleta.esporte}) cadastrado com sucesso!", COR_SUCESSO))


def selecionar_pessoa(sistema: SistemaIMC):
    """Exibe a lista de pessoas e permite o usuário selecionar uma."""
    pessoas = sistema.listar_pessoas()
    if not pessoas:
        raise NenhumaCadastraError()

    print(cor("\n  Pessoas cadastradas:\n", COR_INFO))
    for i, p in enumerate(pessoas, start=1):
        tipo_label = cor(f"[{p.tipo()}]", COR_DESTAQUE)
        print(f"    {cor(str(i), COR_OPCAO)}. {p.nome} {tipo_label}")

    print(f"    {cor('0', COR_OPCAO)}. Cancelar\n")

    while True:
        try:
            escolha = input("  Selecione o número da pessoa: ").strip()
            if escolha == "0":
                return None
            idx = int(escolha) - 1
            if 0 <= idx < len(pessoas):
                return pessoas[idx]
            print(cor(f"\n  [ERRO] Escolha um número entre 1 e {len(pessoas)}, ou 0 para cancelar.\n", COR_ERRO))
        except ValueError:
            print(cor(f"\n  [ERRO] Entrada inválida. Digite um número.\n", COR_ERRO))


def calcular_e_exibir(sistema: SistemaIMC):
    """Permite selecionar uma pessoa, calcula o IMC e salva no histórico."""
    separador("Calcular IMC")

    pessoa = selecionar_pessoa(sistema)
    if pessoa is None:
        print(cor("\n  Operação cancelada.", COR_INFO))
        return

    # Delega ao SistemaIMC (composição + polimorfismo)
    registro = sistema.calcular_e_registrar(pessoa)

    print(cor(f"\n  {LINHA2}", COR_SUCESSO))
    print(cor("  RESULTADO DO CÁLCULO", COR_SUCESSO))
    print(cor(f"  {LINHA2}\n", COR_SUCESSO))
    print(pessoa.resumo())
    print(cor(f"\n  {LINHA2}\n", COR_SUCESSO))
    print(cor(f"  ✅  Registro salvo no histórico da sessão.", COR_INFO))


def exibir_historico(sistema: SistemaIMC):
    """Exibe o histórico completo de cálculos."""
    separador("Histórico de Cálculos")
    print()
    print(sistema.obter_historico().exibir())


def exibir_estatisticas(sistema: SistemaIMC):
    """Exibe estatísticas do histórico e dados recursivos."""
    separador("Estatísticas da Sessão")
    print()
    print(sistema.obter_historico().estatisticas())

    pessoas = sistema.listar_pessoas()
    if pessoas:
        media = sistema.media_imc_sessao()
        maior = sistema.pessoa_maior_imc()
        print(cor(f"\n  ── Dados via CalculadoraRecursiva ──────────────────────", COR_DESTAQUE))
        print(f"  Média IMC (recursão) : {media:.2f}")
        if maior:
            print(f"  Maior IMC cadastrado : {maior.nome} — {maior.calcular_imc():.2f}")


def exibir_relatorio_recursivo(sistema: SistemaIMC):
    """Exibe o relatório de classificações gerado recursivamente."""
    separador("Relatório Recursivo de Classificações")

    pessoas = sistema.listar_pessoas()
    if not pessoas:
        print(cor("\n  Nenhuma pessoa cadastrada ainda.", COR_INFO))
        return

    classificacoes = sistema.relatorio_classificacoes()
    print(cor("\n  Classificação de todos os cadastrados (via recursão):\n", COR_INFO))
    for i, linha in enumerate(classificacoes, start=1):
        print(f"    {cor(str(i), COR_OPCAO)}. {linha}")


def limpar_historico(sistema: SistemaIMC):
    """Limpa o histórico após confirmação do usuário."""
    separador("Limpar Histórico")
    hist = sistema.obter_historico()

    if hist.total() == 0:
        print(cor("\n  O histórico já está vazio.", COR_INFO))
        return

    print(cor(f"\n  ⚠️   Atenção: serão removidos {hist.total()} registro(s).", COR_OPCAO))
    confirmacao = input("  Confirmar limpeza? (s/N): ").strip().lower()

    if confirmacao == "s":
        qtd = hist.limpar()
        print(cor(f"\n  ✅  {qtd} registro(s) removido(s) com sucesso.", COR_SUCESSO))
    else:
        print(cor("\n  Operação cancelada. Histórico preservado.", COR_INFO))


def exibir_sobre():
    """Exibe informações sobre o sistema e as tabelas de classificação."""
    separador("Sobre o Sistema")

    print(cor("""
  FÓRMULA DO IMC
  ──────────────
  IMC = Peso (kg) ÷ Altura² (m²)
  Exemplo: 70 kg ÷ (1,75 m)² = 22,86

  TABELA OMS — PESSOA COMUM
  ──────────────────────────
  < 18,5       Abaixo do peso
  18,5 – 24,9  Peso normal
  25,0 – 29,9  Sobrepeso
  30,0 – 34,9  Obesidade Grau I
  35,0 – 39,9  Obesidade Grau II
  ≥ 40,0       Obesidade Grau III

  TABELA ADAPTADA — ATLETA
  ─────────────────────────
  < 17,0       Abaixo do peso (atleta)
  17,0 – 22,9  Peso normal (atleta)
  23,0 – 27,9  Levemente acima (atleta)
  28,0 – 32,9  Sobrepeso (atleta)
  ≥ 33,0       Obesidade (atleta)

  ⚠  Nota: atletas possuem maior densidade muscular, o que pode
     elevar o IMC sem representar excesso de gordura corporal.
     A tabela adaptada ajusta essa diferença fisiológica.

  CONCEITOS POO APLICADOS
  ────────────────────────
  • Encapsulamento  → atributos protegidos com @property
  • Herança         → Atleta → Pessoa → PessoaBase (ABC)
  • Polimorfismo    → classificar() tem comportamento distinto
  • Composição      → SistemaIMC possui Historico e Pessoas
  • Interface       → CalculadoraIMC (contrato abstrato)
  • Recursão        → CalculadoraRecursiva (soma, média, maior IMC)
  • Exceções custom → hierarquia EntradaInvalidaException
""", COR_INFO))


# ── Loop principal ──────────────────────────────────────────────────────────

def executar():
    """
    Loop principal do sistema.

    Mantém o menu ativo até o usuário escolher a opção de saída (0).
    Trata exceções personalizadas e erros inesperados sem encerrar o programa.
    """
    sistema = SistemaIMC()  # COMPOSIÇÃO: orquestra Pessoa, Atleta, Historico

    limpar_tela()
    cabecalho()
    print(cor("  Bem-vindo! Utilize o menu abaixo para começar.\n", COR_INFO))

    while True:
        try:
            opcao = menu_principal()

            if opcao == "1":
                cadastrar_pessoa(sistema)

            elif opcao == "2":
                cadastrar_atleta(sistema)

            elif opcao == "3":
                calcular_e_exibir(sistema)

            elif opcao == "4":
                exibir_historico(sistema)

            elif opcao == "5":
                exibir_estatisticas(sistema)

            elif opcao == "6":
                exibir_relatorio_recursivo(sistema)

            elif opcao == "7":
                limpar_historico(sistema)

            elif opcao == "8":
                exibir_sobre()

            elif opcao == "0":
                separador()
                hist = sistema.obter_historico()
                print(cor(
                    f"\n  👋  Encerrando o sistema...\n"
                    f"      Total de cálculos realizados nesta sessão: {hist.total()}\n"
                    f"      Obrigado por usar a Calculadora de IMC!\n",
                    COR_SUCESSO,
                ))
                break

            else:
                raise OpcaoInvalidaError(opcao)

        except NenhumaCadastraError as e:
            print(cor(f"\n  {e}\n", COR_ERRO))

        except OpcaoInvalidaError as e:
            print(cor(f"\n  {e}\n", COR_ERRO))

        except EntradaInvalidaException as e:
            print(cor(f"\n  {e}\n", COR_ERRO))

        except KeyboardInterrupt:
            print(cor("\n\n  ⚠️   Interrupção detectada (Ctrl+C).", COR_OPCAO))
            print(cor("  Para sair, use a opção [0] do menu.\n", COR_INFO))

        except Exception as e:
            print(cor(f"\n  [ERRO INESPERADO] {type(e).__name__}: {e}", COR_ERRO))
            print(cor("  O sistema continuará funcionando normalmente.\n", COR_INFO))

        # Pausa antes de exibir o menu novamente
        if opcao != "0":
            input(cor("\n  Pressione Enter para continuar...", COR_INFO))
            limpar_tela()
            cabecalho()


# ── Ponto de entrada ────────────────────────────────────────────────────────

if __name__ == "__main__":
    executar()
