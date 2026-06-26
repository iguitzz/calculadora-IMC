# 🏋️ Calculadora de IMC

Sistema de cálculo de **Índice de Massa Corporal (IMC)** via linha de comando, desenvolvido em Python com foco nos pilares de **Programação Orientada a Objetos (POO)**.

---

## 📐 Estrutura do Projeto

```
calculadora-imc/
│   ├── CalculadoraIMC.py           ← interface (contrato abstrato)
│   ├── PessoaBase.py               ← classe abstrata (ABC)
│   ├── Pessoa.py                   ← herança + encapsulamento
│   ├── Atleta.py                   ← herança + polimorfismo
│   ├── Historico.py                ← composição (RegistroIMC)
│   ├── SistemaIMC.py               ← composição + orquestração
│   ├── CalculadoraRecursiva.py     ← recursão
│   ├── EntradaInvalidaException.py ← exceção personalizada
│   └── Main.py                     ← ponto de entrada + menu CLI
├── pom.xml                         ← metadados e dependências
└── README.md                       ← instruções de uso
```

---

## 🧩 Conceitos de POO Aplicados

| Conceito | Onde é aplicado |
|---|---|
| **Encapsulamento** | `Pessoa.py` — atributos `_privados` com `@property` e setters com validação |
| **Herança** | `Atleta → Pessoa → PessoaBase` |
| **Polimorfismo** | `classificar()` tem comportamento distinto em `Pessoa` e `Atleta` |
| **Abstração** | `PessoaBase` (ABC) e `CalculadoraIMC` definem contratos obrigatórios |
| **Composição** | `SistemaIMC` possui `Historico`; `Historico` possui `RegistroIMC` |
| **Recursão** | `CalculadoraRecursiva` — soma, média e maior IMC por recursão |
| **Exceções custom** | Hierarquia `EntradaInvalidaException` com subclasses especializadas |

---

## ✅ Pré-requisitos

- **Python 3.8** ou superior
- Nenhuma biblioteca externa — utiliza apenas a **biblioteca padrão do Python**

Para verificar a versão do Python instalada:

```bash
python --version
# ou
python3 --version
```

---

## 🚀 Como Compilar e Rodar

> Python é uma linguagem interpretada — não há etapa de compilação. O projeto roda diretamente.

### 1. Clone ou baixe o projeto

```bash
# Se estiver usando Git:
git clone <url-do-repositorio>
cd calculadora-imc

# Ou simplesmente acesse a pasta onde salvou o projeto.
```

### 2. Navegue até a pasta do projeto

```bash
# Windows (Prompt de Comando ou PowerShell)
cd "caminho\para\calculadora 1"

# Unix / macOS / Linux
cd "caminho/para/calculadora 1"
```

### 3. Execute o sistema

```bash
# Windows (Prompt de Comando ou PowerShell)
python src\main\py\Main.py

# Unix / macOS / Linux
python3 src/main/py/Main.py
```

> ⚠️ **Atenção:** O `Main.py` **deve** ser executado a partir da **raiz do projeto** (a pasta que contém `src/` e `pom.xml`), e não de dentro da pasta `src/main/py/`, pois o script ajusta o `sys.path` automaticamente.

---

## 🖥️ Exemplo de Uso

Ao iniciar, você verá o menu principal:

```
  ══════════════════════════════════════════════════════════════════
  ║  🏋️  CALCULADORA DE IMC — CLI                                 ║
  ║  Índice de Massa Corporal com Suporte a Atletas                ║
  ══════════════════════════════════════════════════════════════════

  ──────────────────────────────────────────────────────────────
  MENU PRINCIPAL
  ──────────────────────────────────────────────────────────────

  [1]  👤  Cadastrar Pessoa Comum
  [2]  🏅  Cadastrar Atleta
  [3]  📊  Calcular IMC de pessoa cadastrada
  [4]  📋  Exibir Histórico completo
  [5]  📈  Ver Estatísticas da sessão
  [6]  🔢  Relatório recursivo de classificações
  [7]  🗑   Limpar Histórico
  [8]  ℹ️   Sobre o sistema / Tabelas de IMC
  [0]  🚪  Sair
```

### Fluxo básico

1. Pressione **1** para cadastrar uma pessoa comum (nome, idade, peso, altura).
2. Pressione **2** para cadastrar um atleta (inclui esporte e nível de treinamento).
3. Pressione **3** para calcular o IMC de um cadastrado e salvá-lo no histórico.
4. Pressione **4** para ver todos os registros da sessão.
5. Pressione **6** para ver um relatório de classificações gerado recursivamente.
6. Pressione **0** para encerrar.

---

## 📊 Tabelas de Classificação de IMC

### Pessoa Comum (OMS)

| IMC | Classificação |
|---|---|
| < 18,5 | Abaixo do peso |
| 18,5 – 24,9 | Peso normal |
| 25,0 – 29,9 | Sobrepeso |
| 30,0 – 34,9 | Obesidade Grau I |
| 35,0 – 39,9 | Obesidade Grau II |
| ≥ 40,0 | Obesidade Grau III |

### Atleta (Tabela Adaptada)

| IMC | Classificação |
|---|---|
| < 17,0 | Abaixo do peso (atleta) |
| 17,0 – 22,9 | Peso normal (atleta) |
| 23,0 – 27,9 | Levemente acima (atleta) |
| 28,0 – 32,9 | Sobrepeso (atleta) |
| ≥ 33,0 | Obesidade (atleta) |

> ⚠️ Atletas possuem maior densidade muscular, o que pode elevar o IMC sem representar excesso de gordura corporal.

---

## 📁 Descrição dos Arquivos

| Arquivo | Responsabilidade |
|---|---|
| `EntradaInvalidaException.py` | Hierarquia de exceções personalizadas do sistema |
| `PessoaBase.py` | Classe abstrata com o contrato de `calcular_imc()`, `classificar()`, etc. |
| `Pessoa.py` | Implementação concreta com validação via `@property` (encapsulamento) |
| `Atleta.py` | Herda de `Pessoa`, sobrescreve `classificar()` com tabela de atleta |
| `Historico.py` | `RegistroIMC` (dataclass) + `Historico` (lista de registros da sessão) |
| `SistemaIMC.py` | Orquestra `Pessoa`, `Atleta`, `Historico` e `CalculadoraRecursiva` |
| `CalculadoraIMC.py` | Interface abstrata que define o contrato público do sistema |
| `CalculadoraRecursiva.py` | Funções recursivas: soma, média, maior IMC, classificação em lista |
| `Main.py` | Menu CLI, funções de I/O com validação e loop principal |

---

## 🧪 Testando Manualmente

Sugestão de cenário de teste:

1. Cadastre uma **pessoa comum**: Nome `João Silva`, Idade `30`, Peso `90`, Altura `1.75`
   - IMC esperado: `29.39` → Sobrepeso

2. Cadastre um **atleta**: Nome `Maria Santos`, Idade `25`, Peso `75`, Altura `1.68`, Esporte `Natação`, Nível `Profissional`
   - IMC esperado: `26.57` → Levemente acima (atleta)

3. Calcule o IMC de ambos (opção 3).

4. Visualize o histórico (opção 4) e as estatísticas (opção 5).

5. Veja o relatório recursivo de classificações (opção 6).

---

## 👥 Autoria

Projeto desenvolvido para demonstração dos pilares de **Programação Orientada a Objetos** em Python.
