# ===============================================================
# COMO ESTE PROGRAMA FUNCIONA — explicado na ordem em que executa
# ===============================================================
# Este arquivo é comentado "Ato" por "Ato", seguindo a ORDEM DE
# EXECUÇÃO real do programa. O Python lê o script de cima para
# baixo, uma instrução de cada vez.
#
# ATENÇÃO: este programa possui uma FUNÇÃO. Quando o Python lê o
# "def" (Ato 2), ele apenas GUARDA a função na memória, mas NÃO a
# executa. A função só trabalha de verdade quando é CHAMADA pelo
# nome, o que acontece nos Atos 4 e 7. Por isso, aqui a ordem das
# linhas no arquivo e a ordem de execução não são exatamente iguais.
#
# Antes de executar, a biblioteca externa colorama precisa estar
# instalada. No terminal do VS Code (Terminal -> New Terminal):
#     pip install colorama
#
# Resumo da peça inteira:
#   Ato 0 -> Importa os recursos da biblioteca colorama
#   Ato 1 -> Cria a lista com os 5 níveis do reservatório
#   Ato 2 -> Define a função que escolhe a cor de cada nível
#   Ato 3 -> Exibe o cabeçalho do sistema
#   Ato 4 -> Exibe todos os níveis, cada um com a sua cor
#   Ato 5 -> Restaura o estilo padrão do terminal
#   Ato 6 -> Pergunta o nível atual e valida o valor digitado
#   Ato 7 -> Exibe a situação atual com a cor correspondente
#   Ato 8 -> Restaura o estilo padrão do terminal (final)
# ===============================================================

# ---------------------------------------------------------------
# Ato 0: Importação da biblioteca colorama
# ---------------------------------------------------------------
# "from colorama" indica de qual biblioteca vamos buscar recursos.
# "import Fore, Style" traz apenas o que será usado:
#   - Fore  -> define a COR do texto (Fore.RED, Fore.GREEN...).
#   - Style -> usado no final para RESTAURAR o estilo padrão.
# A importação sempre fica no início do programa.
from colorama import Fore, Style

# ---------------------------------------------------------------
# Ato 1: Criação da lista com os níveis do reservatório
# ---------------------------------------------------------------
# Uma lista guarda vários dados relacionados em um único lugar.
# Ela é criada com colchetes [ ] e os itens são separados por
# vírgula. O nome está no plural (niveis) porque guarda vários
# valores. A ordem vai do nível mais baixo ao mais alto.
#
# Lembre-se: os índices (posições) da lista começam em ZERO:
#   niveis[0] -> Nível 1     niveis[3] -> Nível 4
#   niveis[1] -> Nível 2     niveis[4] -> Nível 5
#   niveis[2] -> Nível 3
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# ---------------------------------------------------------------
# Ato 2: Definição da função que escolhe a cor
# ---------------------------------------------------------------
# "def" cria uma função chamada definir_cor. Ela recebe um
# PARÂMETRO chamado nivel (o número do nível, de 1 a 5).
# Tudo o que está recuado (indentado) abaixo do "def" pertence
# à função.
#
# A estrutura if/elif/else testa as condições NA ORDEM e executa
# apenas o primeiro bloco verdadeiro:
#   - "==" compara se o nível é igual ao número testado;
#   - "return" DEVOLVE a cor escolhida para quem chamou a função
#     e encerra a função naquele momento;
#   - o "else" cobre o caso restante, que é o nível 5 (azul).
#
# Lembrete: aqui a função só é GUARDADA. Ela será executada
# quando for chamada nos Atos 4 e 7.
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED       # vermelho -> muito baixo (crítico)
    elif nivel == 2:
        return Fore.YELLOW    # amarelo  -> baixo
    elif nivel == 3:
        return Fore.GREEN     # verde    -> médio
    elif nivel == 4:
        return Fore.CYAN      # ciano    -> alto
    else:
        return Fore.BLUE      # azul     -> muito alto (alerta)

# ---------------------------------------------------------------
# Ato 3: Exibição do cabeçalho
# ---------------------------------------------------------------
# print() mostra um texto na tela. Aqui é a "moldura" visual do
# sistema de monitoramento. O print() vazio pula uma linha.
print("=======================================================")
print("   💧 MONITORAMENTO DO RESERVATÓRIO DE ÁGUA 💧")
print("=======================================================")
print()

# ---------------------------------------------------------------
# Ato 4: Exibição de todos os níveis com as suas cores
# ---------------------------------------------------------------
# A variável numero funciona como um CONTADOR e começa em 1,
# porque o primeiro item da lista é o Nível 1.
#
# O "for mensagem in niveis" percorre a lista, um item por vez.
# A cada volta (repetição), a variável mensagem recebe o próximo
# texto da lista. Dentro do for:
#   1) definir_cor(numero) CHAMA a função do Ato 2, enviando o
#      número do nível como ARGUMENTO. A cor devolvida pelo
#      return fica guardada na variável cor;
#   2) print(cor + mensagem) junta (concatena) a cor com o texto
#      usando o "+", e a mensagem aparece colorida na tela;
#   3) numero += 1 soma 1 ao contador, para a próxima volta
#      representar o próximo nível.
# O for termina sozinho quando chega ao fim da lista (5 voltas).
numero = 1
for mensagem in niveis:
    cor = definir_cor(numero)
    print(cor + mensagem)
    numero += 1

# ---------------------------------------------------------------
# Ato 5: Restauração do estilo padrão do terminal
# ---------------------------------------------------------------
# Style.RESET_ALL desliga as cores aplicadas. Sem ele, a última
# cor usada (azul) continuaria ativa nas próximas mensagens.
print(Style.RESET_ALL)

# ---------------------------------------------------------------
# Ato 6: Pergunta do nível atual e validação do valor digitado
# ---------------------------------------------------------------
# input() pausa o programa, mostra a pergunta e espera o usuário
# digitar. O que for digitado chega SEMPRE como texto (string) e
# fica guardado na variável entrada.
#
# opcoes_validas é uma lista com os únicos valores aceitos. Eles
# estão entre aspas porque o input() devolve texto, e precisamos
# comparar texto com texto.
#
# O while repete o bloco ENQUANTO a condição for verdadeira:
#   - "in" verifica se a entrada está dentro da lista;
#   - "not" inverte o resultado, ou seja, a condição fica
#     verdadeira quando a entrada NÃO está na lista.
# Assim, se o usuário digitar 7, 0, "dez", "abc" ou deixar vazio,
# o programa mostra o aviso e pergunta de novo. A repetição só
# termina quando um valor de 1 a 5 for digitado.
#
# Por fim, int() converte o texto válido em número inteiro,
# pois a função definir_cor e o índice da lista trabalham com
# números. Essa conversão só acontece DEPOIS da validação, por
# isso o programa nunca trava com letras.
opcoes_validas = ["1", "2", "3", "4", "5"]

entrada = input("❓ Qual o nível de água no reservatório? (digite de 1 a 5): ")
while entrada not in opcoes_validas:
    print("⚠️  Valor inválido! Digite apenas um número de 1 a 5, conforme a lista de níveis acima.")
    entrada = input("❓ Qual o nível de água no reservatório? (digite de 1 a 5): ")

nivel_atual = int(entrada)

# ---------------------------------------------------------------
# Ato 7: Exibição da situação atual do reservatório
# ---------------------------------------------------------------
# niveis[nivel_atual - 1] busca a mensagem certa na lista. O
# "- 1" é necessário porque a lista começa no índice 0
# (exemplo: nível 3 -> índice 2 -> "Nível 3 - Médio").
#
# definir_cor(nivel_atual) CHAMA a função novamente, agora com
# o nível informado pelo usuário, e o "+" junta a cor com a
# mensagem.
print()
print("📡 Situação atual do reservatório:")
print(definir_cor(nivel_atual) + niveis[nivel_atual - 1])

# ---------------------------------------------------------------
# Ato 8: Restauração final do estilo padrão do terminal
# ---------------------------------------------------------------
# Mais uma vez o Style.RESET_ALL garante que o terminal volte ao
# normal depois da última mensagem colorida do programa.
print(Style.RESET_ALL)

# ===============================================================
# Para fixar:
#   - Por que a função definir_cor não é executada no momento em
#     que o Python lê o "def" (Ato 2)?
#   - Por que os valores da lista opcoes_validas estão entre
#     aspas, e não como números (Ato 6)?
#   - Por que o int() é usado só DEPOIS do while, e não junto
#     com o input()? (dica: troque a ordem, digite uma letra e
#     observe a mensagem de erro do Python)
#   - Por que é necessário usar "nivel_atual - 1" para buscar a
#     mensagem na lista (Ato 7)?
#   - O que aconteceria com as mensagens seguintes se o
#     Style.RESET_ALL fosse retirado do programa?
# ===============================================================
