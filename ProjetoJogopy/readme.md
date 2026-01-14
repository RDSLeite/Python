Relatório Técnico do Projeto Jogo das Naves
1. Introdução
O projeto Jogo das Naves consiste num jogo de estratégia em modo consola, desenvolvido em Python 3, no qual o jogador interage com um conjunto de naves espaciais posicionadas num tabuleiro. O objetivo principal é atingir e destruir todas as naves inimigas através de tiros manuais ou automáticos, respeitando limites de tiros e regras de energia.
Este projeto foi concebido como trabalho de avaliação, tendo como foco principal:
Aplicação prática de Programação Orientada a Objetos (POO)
Modularização do código em vários ficheiros
Persistência de dados utilizando ficheiros JSON
Organização, legibilidade e reutilização de código
Interação com o utilizador em ambiente de terminal
O jogo apresenta funcionalidades adicionais como energia extra, estatísticas de eficácia, sistema de saves e interface visual melhorada através de cores ANSI.







2. Estrutura Geral do Projeto
O projeto encontra-se organizado de forma modular, distribuindo responsabilidades por diferentes ficheiros:
jogo.py – Ficheiro principal, responsável pelo menu, fluxo do jogo e interação com o utilizador
nave.py – Contém as classes que representam as naves e a lógica associada à energia
tabuleiro.py – Responsável pela criação, desenho e apresentação do tabuleiro
funcao.py – Agrupa funções auxiliares como guardar, carregar, limpar e cálculo de estatísticas
saves/ – Diretório onde são armazenados os ficheiros de jogo em formato JSON
Esta separação melhora a organização, facilita a manutenção e torna o código mais legível e escalável.
FICHEIRO: funcao.py
IMPORTS
import json
import os
from nave import *
json
 Serve para guardar e carregar o jogo em ficheiros .json.
 JSON é texto simples → perfeito para saves.


os
 Permite:


Criar pastas


Ver ficheiros


Limpar o ecrã


Saber se estás em Windows ou Linux


from nave import *
 Importa:


NaveModelo


NaveComExtra


barra_energia


CORES


Isto é necessário porque o save guarda naves e depois precisa recriá-las.
PASTA DE SAVES
SAVE_FOLDER = "saves"

Define o nome da pasta onde os jogos guardados vão ficar.
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

Verifica se a pasta saves/ existe


Se não existir, cria-a



FUNÇÃO: limpar_ecra
def limpar_ecra():
    os.system("cls" if os.name == "nt" else "clear")
os.name == "nt" → Windows


"cls" limpa ecrã no Windows


"clear" limpa ecrã no Linux/Mac

 Deixa o jogo limpo e legível a cada ronda.

FUNÇÃO: guardar_jogo
def guardar_jogo(caminho, naves, total_tiros, total_certos):

Parâmetros:
caminho → nome do ficheiro (ex: saves/save_1.json)


naves → lista de objetos Nave


total_tiros → tiros disparados


total_certos → tiros que acertaram


Criação do dicionário principal
dados = {
    "naves": [],
    "total_tiros": total_tiros,
    "total_certos": total_certos
}
Aqui estás a preparar os dados num formato que o JSON aceita

Guardar cada nave
for nav in naves:
    dados["naves"].append({
        "classe": type(nav).__name__,
        "nome": nav.nome,
        "cor": nav.cor,
        "energia": nav.energia,
        "perda_energia": nav.perda_energia,
        "simbolo": nav.simbolo,
        "energia_extra": getattr(nav, "energia_extra", 0),
        "viva": nav.viva,
        "pos": nav.pos
    })
type(nav).__name__
 Guarda se é:


NaveModelo


NaveComExtra


getattr(nav, "energia_extra", 0)
 Se a nave não tiver energia_extra, devolve 0
 Evita crash com naves normais


pos
 Guarda (linha, coluna) da nave


Escrever o ficheiro JSON
with open(caminho, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4)

Abre o ficheiro em modo escrita


indent=4 → deixa o JSON bonito e legível


Guarda tudo como texto


print(f"Jogo guardado em: {caminho}")

Feedback visual para o jogador.
FUNÇÃO: guardar_jogo_auto
def guardar_jogo_auto(naves, total_tiros, total_certos):

Objetivo:
Criar saves automáticos numerados, sem sobrescrever.
existentes = [
    f for f in os.listdir(SAVE_FOLDER)
    if f.startswith("save_") and f.endswith(".json")
]

Lista todos os ficheiros da pasta saves


Filtra apenas save_X.json


numero = len(existentes) + 1

Se existem 3 saves → próximo é save_4.json

ficheiro = os.path.join(SAVE_FOLDER, f"save_{numero}.json")

Cria o caminho completo:
 saves/save_4.json

guardar_jogo(ficheiro, naves, total_tiros, total_certos)
return ficheiro

Guarda e devolve o nome do ficheiro criado.
FUNÇÃO: carregar_jogo
def carregar_jogo(ficheiro, NaveModelo, NaveComExtra):

Recebe:
Nome do ficheiro


Classes como parâmetro (boa prática)


with open(ficheiro, "r", encoding="utf-8") as f:
    dados = json.load(f)

Lê o JSON e transforma novamente em dicionário Python.
Reconstrução das naves
naves = []

Lista nova para colocar as naves recriadas.
for d in dados["naves"]:
    classe = d.get("classe", "NaveModelo")

Lê a classe guardada no JSON.
if classe == "NaveModelo":
    nav = NaveModelo(...)
else:
    nav = NaveComExtra(...)

Restaurar estado
nav.energia = d["energia"]
nav.viva = d["viva"]
nav.pos = tuple(d["pos"]) if d.get("pos") else None

Agora a nave fica exatamente como estava.
return naves, dados["total_tiros"], dados["total_certos"]

O jogo continua do ponto exato onde foi guardado.


FUNÇÃO: eficacia
def eficacia(total, certos):
    return (certos * 100 / total) if total > 0 else 0

Evita a divisão zero.
 Calcula a percentagem de tiros certeiros.
 FICHEIRO: jogo.py
IMPORTS
from nave import *
from tabuleiro import *
from funcao import *
import os
import time
from datetime import datetime

O que cada um faz:
nave
 Classes das naves + barra de energia + cores


tabuleiro
 Tudo que envolve matriz, posições, tiros e impressão


funcao
 Guardar, carregar, limpar e estatísticas


os
 Usado para ficheiros e paths


time
 Usado para pequenos atrasos (efeito visual)


datetime
 Mostrar data/hora dos saves


FUNÇÃO: criar_naves
def criar_naves():
    n1 = NaveModelo("Falcon", "vermelho", 20, "F")
    n2 = NaveComExtra("Guardian", "azul", 15, "G", 20)
    n3 = NaveComExtra("Viper", "magenta", 10, "V", 25)
    return [n1, n2, n3]

O que isto faz:
Cria as naves iniciais do jogo.
Falcon
 Nave normal, perde muita energia quando é atingida


Guardian
 Nave com energia extra moderada


Viper
 Nave mais fraca por tiro, mas com mais energia extra


FUNÇÃO: capa
def capa():
    limpar_ecra()
    print(""" ... """)
    input("ENTER para continuar...")

Explicação:
Limpa o ecrã


Mostra ASCII ART (só estética)


Pausa até o jogador carregar ENTER


 FUNÇÃO loop_jogo:
def loop_jogo(naves, total_tiros=0, total_certos=0, ficheiro_atual=None):

Parâmetros:
naves → lista de naves


total_tiros → continua contador se veio de save


total_certos → idem


ficheiro_atual → save atual (para sobrescrever)


energia_extra_usada = False

Evita que a energia extra seja aplicada mais de uma vez.
CORES LOCAIS
CORES = {
    "Falcon": "\033[90m",
    "Guardian": "\033[94m",
    "Viper": "\033[95m",
    "reset": "\033[0m"
}

Estas cores são usadas só neste ficheiro, para os nomes das naves.
ESCOLHA DO MODO DE TIRO
print("1 - Tiros automáticos")
print("2 - Tiros manuais")
modo_tiros = input("Escolha: ")

O jogador escolhe uma vez só.
if modo_tiros not in ["1","2"]:
    modo_tiros = "1"

Fallback seguro → automático.
 LOOP PRINCIPAL DO JOGO
while True:

Este loop só termina quando:
Jogador sai


Todas as naves morrem


Limite de tiros é atingido



LIMPAR ECRÃ
limpar_ecra()

Evita acumular lixo visual.
MOVER NAVES
colocar_naves_aleatorio(naves)

Cada ronda:
As naves mudam de posição


O jogador não memoriza posições


DETERMINAR TIROS
tiros = []

Lista vazia para a ronda atual.

MODO AUTOMÁTICO
if modo_tiros == "1":
    tiros = gerar_tiros_aleatorios(3)

3 tiros


Coordenadas aleatórias


Sem repetição


MODO MANUAL
elif modo_tiros == "2":

Loop para pedir 3 coordenadas.
coord = input("linha,coluna")
r, c = map(int, coord.split(","))

if 0 <= r < 10 and 0 <= c < 10:
0 <= r < LINHAS and 0 <= c < COLUNAS
CONTADOR DE TIROS
total_tiros += len(tiros)

Conta tudo, manual ou automático.

VERIFICAR ACERTOS
mensagens_acerto = {}

Dicionário para mostrar mensagens ao lado das naves.

for tiro in tiros:
    for nav in naves:

Verifica cada tiro contra cada nave.

if nav.viva and nav.pos == tiro:

Só conta se:
A nave está viva


A posição coincide



nav.perder_energia()
total_certos += 1

Atualiza estado da nave e estatísticas.

mensagens_acerto[nav.nome] = f"Acertou {nav.nome}"
time.sleep(0.2)

Mensagem visual + pequeno atraso.

ENERGIA EXTRA AUTOMÁTICA
if total_tiros >= 45 and not energia_extra_usada:

Garante:
Só ativa depois de 45 tiros


Só uma vez



if hasattr(nav, "adicionar_energia_extra"):
    nav.adicionar_energia_extra()

Só naves com energia extra recebem boost.
Uso correto de herança e polimorfismo.

MOSTRAR TABULEIROS
imprimir_com_borda(desenhar_naves(naves))
imprimir_com_borda(desenhar_tiros(tiros))

Separação perfeita:
Lógica → desenhar_*


Visual → imprimir_*



DADOS DAS NAVES
for nav in naves:
    barra = barra_energia(nav.energia)

Mostra:
Nome


Energia gráfica


Energia numérica


Mensagem de acerto (se houver)


ESTATÍSTICAS
print(f"Tiros totais: {total_tiros}")
print(f"Certeiros: {total_certos}")
print(f"Eficácia: {eficacia(...)}")

Feedback contínuo ao jogador.

MENU DA RONDA
print("ENTER = Continuar")
print("2 = Guardar")
print("3 = Sair")


GUARDAR
if ficheiro_atual:
    guardar_jogo(...)
else:
    ficheiro_atual = guardar_jogo_auto(...)

Se veio de save → sobrescreve
 Se não → cria novo

CONDIÇÕES DE FIM
if all(not n.viva for n in naves):

Fim por vitória.

if total_tiros >= 105:

Fim por limite.

🔹 HISTÓRICO DE SAVES
def escolher_save_com_horario():

Lista saves e mostra data/hora real.
datetime.fromtimestamp(os.path.getmtime(caminho))

Muito bem usado.

🔹 MENU PRINCIPAL
def menu():

Centraliza tudo:
Novo jogo


Carregar


Sair



if __name__ == "__main__":
    menu()

Garante que o menu só corre se este ficheiro for o principal.

Projeto: Jogo das Naves

 FICHEIRO nave.py
Este ficheiro contém as classes principais do jogo, responsáveis por representar as naves, o seu estado e o comportamento associado à energia.

IMPORTAÇÃO E CORES ANSI
CORES = {
    "vermelho": "\033[91m",
    "verde": "\033[92m",
    "amarelo": "\033[93m",
    "azul": "\033[94m",
    "magenta": "\033[95m",
    "reset": "\033[0m"
}

Explicação:
Este dicionário define códigos ANSI para colorir o texto no terminal.
Objetivo:
Melhorar a legibilidade


Diferenciar visualmente as naves


Tornar a interface mais intuitiva


CLASSE NaveModelo
class NaveModelo:

Razão da criação da classe:
Esta classe representa o modelo base de uma nave, contendo atributos e comportamentos comuns a todas as naves do jogo.
Cumpre o princípio de abstração, pois define o que é uma nave no contexto do jogo.



CONSTRUTOR
def __init__(self, nome: str, cor: str, perda_energia: int, simbolo: str):

Atributos:
self.nome = nome

Nome identificador da nave.
self.cor = cor

Define a cor usada no terminal.
self.energia = 100

Todas as naves começam com energia máxima.
self.perda_energia = perda_energia

Quantidade de energia perdida quando a nave é atingida.
self.simbolo = simbolo

Carácter que representa a nave no tabuleiro.
self.pos = None

Guarda a posição atual da nave no tabuleiro.
self.viva = True

Indica se a nave ainda está ativa.



MÉTODO perder_energia
def perder_energia(self):

Função:
Reduz a energia da nave quando esta é atingida.
if not self.viva:
    return self.energia

Evita que naves destruídas continuem a sofrer dano.
self.energia -= self.perda_energia

Aplica o dano definido.
if self.energia <= 0:
    self.energia = 0
    self.viva = False

Se a energia chegar a zero:
A nave é destruída


O estado muda para viva = False


👉 Cumpre a lógica de destruição do jogo.

MÉTODO energia_atual
def energia_atual(self):
    return self.energia

Devolve a energia atual da nave.
Utilidade:
Encapsulamento


Facilita futuras alterações


MÉTODO mostrar_dados
def mostrar_dados(self):

Cria uma string formatada com:
Nome


Barra de energia


Energia numérica


Símbolo


Usado para apresentar informação ao jogador de forma clara.
CLASSE NaveComExtra
class NaveComExtra(NaveModelo):

Justificação:
Esta classe herda de NaveModelo e adiciona uma funcionalidade extra.
Cumpre:
Herança


Reutilização de código


Polimorfismo




CONSTRUTOR
super().__init__(nome, cor, perda_energia, simbolo)
self.energia_extra = energia_extra

Inicializa a nave base e adiciona o atributo de energia extra.

MÉTODO adicionar_energia_extra
def adicionar_energia_extra(self):

Adiciona energia adicional à nave, respeitando o limite máximo.
if self.energia > 100:
    self.energia = 100

Evita valores inválidos.
Este método é usado automaticamente após um certo número de tiros.

FUNÇÃO barra_energia
def barra_energia(energia):

Cria uma barra visual com 10 posições.
cheios = int(energia / 10)

Cada bloco representa 10 pontos de energia.
Melhora a experiência do utilizador e leitura rápida do estado.

 FICHEIRO tabuleiro.py
Este ficheiro é responsável por toda a lógica do tabuleiro: criação, desenho, tiros e impressão.
CONSTANTES
LINHAS = 6
COLUNAS = 6

Define o tamanho do tabuleiro de forma centralizada.
Fácil alteração


Evita valores mágicos no código


FUNÇÃO criar_matriz
def criar_matriz(vazia='.'):

Cria uma matriz 6x6 preenchida com um símbolo vazio.
Utilizada para:
Tabuleiro de naves


Tabuleiro de tiros


FUNÇÃO colocar_naves_aleatorio
def colocar_naves_aleatorio(naves):

Função:
Distribui as naves aleatoriamente pelo tabuleiro.
posicoes = [(r, c) for r in range(LINHAS) for c in range(COLUNAS)]

Gera todas as posições possíveis.
random.shuffle(posicoes)

Baralha as posições para garantir aleatoriedade.
nav.pos = posicoes[i]

Atribui uma posição única a cada nave.
Evita sobreposição automaticamente.
FUNÇÃO desenhar_naves
def desenhar_naves(naves):

Cria uma matriz com as naves vivas desenhadas.
if nav.viva and nav.pos:
Naves vivas


Com posição válida






FUNÇÃO desenhar_tiros
def desenhar_tiros(lista_tiros):

Marca os tiros da ronda atual com o símbolo X.
Este tabuleiro é limpo a cada ronda.

FUNÇÃO imprimir_com_borda
def imprimir_com_borda(mat):

Imprime o tabuleiro com:
Coordenadas


Bordas


Numeração de linhas e colunas


 Essencial para o modo de tiros manuais.

FUNÇÃO gerar_tiros_aleatorios
def gerar_tiros_aleatorios(quantidade=3):

Gera tiros aleatórios sem repetição.
return random.sample(livres, quantidade)

Evita tiros duplicados na mesma ronda.







POSSÍVEIS MELHORIAS (PARA REFERIR NO RELATÓRIO)
Criar uma classe Jogo para centralizar o loop


Corrigir validação do modo manual (usar LINHAS e COLUNAS)


Criar classe SaveManager


Melhorar tratamento de exceções ao carregar saves


