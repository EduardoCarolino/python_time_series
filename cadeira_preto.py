
#Cabeçalho em Python
""" Um conjunto de informações, geralmente na forma de um comentário ou metadado, localizado no início 
do ficheiro para descrever o seu conteúdo, propósito e, em alguns casos, a sua licença, autor e data de criação """

#Para o que serve
""" Para criar uma documentação e orientar o desenvolvedor como utilizar aquele código """

#Docstring e para o que serve
""" Docstring strings usadas para documentar módulos, classes, funções e métodos. São strings literais,
geralmente delimitadas por aspas triplas (# ou """ """) """

#Diferença
""" 
Cabeçalhos: Passa dados, cobre o código de maneira geral, entrega contexto e instrução
Docstring: Serve para comentários e documentação especificas no código, sobre funções, métodos 
 """

# formate o cabeçalho do arquivo e resolva os exercicios abaixo


def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    # TODO: retorne se n é par
    ...

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    # TODO: implemente de forma iterativa (sem recursão)
    ...

import re

def limpa_texto(s: str) -> str:
    """Deixa minúsculo e remove pontuação comum."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """Conta vogais (a,e,i,o,u) em s (desconsidere acentos)."""
    # TODO: conte as vogais simples
    ...


def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)
    ...

