class EntradaInvalidaException(Exception):
   
    def __init__(self, mensagem: str):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

    def __str__(self):
        return f"[ERRO] {self.mensagem}"


# Alias para compatibilidade
IMCBaseError = EntradaInvalidaException


class PesoInvalidoError(EntradaInvalidaException):
  
    def __init__(self, peso=None):
        if peso is not None:
            mensagem = (
                f"Peso inválido: '{peso}'. "
                "O peso deve ser um número positivo entre 0.1 kg e 500 kg."
            )
        else:
            mensagem = "Peso inválido. O peso deve ser um número positivo entre 0.1 kg e 500 kg."
        super().__init__(mensagem)


class AlturaInvalidaError(EntradaInvalidaException):
    """Levantada quando a altura informada é inválida."""

    def __init__(self, altura=None):
        if altura is not None:
            mensagem = (
                f"Altura inválida: '{altura}'. "
                "A altura deve ser um número positivo entre 0.5 m e 3.0 m."
            )
        else:
            mensagem = "Altura inválida. A altura deve ser um número positivo entre 0.5 m e 3.0 m."
        super().__init__(mensagem)


class IdadeInvalidaError(EntradaInvalidaException):

    def __init__(self, idade=None):
        if idade is not None:
            mensagem = (
                f"Idade inválida: '{idade}'. "
                "A idade deve ser um número inteiro entre 0 e 130 anos."
            )
        else:
            mensagem = "Idade inválida. A idade deve ser um número inteiro entre 0 e 130 anos."
        super().__init__(mensagem)


class NomeInvalidoError(EntradaInvalidaException):
   
    def __init__(self, nome=None):
        if nome is not None and isinstance(nome, str) and nome.strip() == "":
            mensagem = "Nome inválido: o nome não pode ser vazio ou conter apenas espaços."
        elif nome is not None:
            mensagem = (
                f"Nome inválido: '{nome}'. "
                "O nome deve conter apenas letras e espaços, com pelo menos 2 caracteres."
            )
        else:
            mensagem = "Nome inválido."
        super().__init__(mensagem)


class OpcaoInvalidaError(EntradaInvalidaException):
    
    def __init__(self, opcao=None):
        if opcao is not None:
            mensagem = f"Opção '{opcao}' não reconhecida. Por favor, escolha uma opção válida do menu."
        else:
            mensagem = "Opção inválida. Por favor, escolha uma opção válida do menu."
        super().__init__(mensagem)


class NenhumaCadastraError(EntradaInvalidaException):

    def __init__(self):
        super().__init__(
            "Nenhuma pessoa cadastrada. Cadastre ao menos uma pessoa antes de continuar."
        )


class EsporteInvalidoError(EntradaInvalidaException):

    def __init__(self, esporte=None):
        if esporte is not None:
            mensagem = (
                f"Esporte inválido: '{esporte}'. "
                "O esporte não pode ser vazio."
            )
        else:
            mensagem = "Esporte inválido. Por favor, informe um esporte válido."
        super().__init__(mensagem)
