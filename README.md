# 💧 Controle de Níveis de Água – Monitoramento de Reservatório

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Biblioteca-colorama-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)
![Tema](https://img.shields.io/badge/Tema-Monitoramento%20💧-1E90FF?style=for-the-badge)

## 🎯 Objetivo

Sistema simples, executado no terminal, que **simula o monitoramento de um reservatório de água**. O programa trabalha com cinco níveis de água, do mais baixo ao mais alto, e exibe para cada um uma **mensagem de alerta com uma cor diferente**. Em seguida, pergunta qual é o nível atual do reservatório e mostra a situação com a cor correspondente, deixando a visualização mais clara e rápida. 🚰📊

## 📏 Níveis do reservatório

| Nível | Situação | Cor exibida |
|---|---|---|
| Nível 1 | Muito baixo (crítico) | 🔴 Vermelho |
| Nível 2 | Baixo | 🟡 Amarelo |
| Nível 3 | Médio | 🟢 Verde |
| Nível 4 | Alto | 🩵 Ciano |
| Nível 5 | Muito alto (alerta) | 🔵 Azul |

## 🐍 Tecnologias e conceitos utilizados

- **Python 3**.
- **Biblioteca externa colorama** (instalada com o `pip`), usando `Fore` para as cores e `Style.RESET_ALL` para restaurar o estilo padrão do terminal.
- Conceitos aplicados: **lista** com os níveis, **função** com parâmetro e `return`, estrutura condicional `if / elif / else`, estruturas de repetição `for` e `while`, operadores `in` e `not`, contador, acesso à lista por **índice**, entrada de dados com `input()`, conversão com `int()`, concatenação com `+` e `print()`.
- **Validação da entrada:** o programa só aceita valores de 1 a 5. Se o usuário digitar outro número, uma letra ou deixar vazio, aparece um aviso e a pergunta é feita novamente.
- Código comentado no modelo **"Ato por Ato"**, explicando o programa na ordem real em que ele é executado (do Ato 0 ao Ato 8), inclusive o momento em que a função é definida e o momento em que ela é chamada.

## ▶️ Como executar o programa

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/controle-niveis-agua.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd controle-niveis-agua
   ```
3. Instale a biblioteca colorama:
   ```bash
   pip install colorama
   ```
   > ⚠️ Se aparecer um aviso `[notice]` sobre uma nova versão do pip, não se preocupe: não é erro e não afeta o programa.
4. Execute o script com Python 3:
   ```bash
   python reservatorio.py
   ```
5. Veja os cinco níveis exibidos com suas cores.
6. Responda à pergunta **"Qual o nível de água no reservatório?"** digitando um número de 1 a 5 e veja a situação atual com a cor correspondente. ✅

## 💻 Exemplo de saída

```
=======================================================
   💧 MONITORAMENTO DO RESERVATÓRIO DE ÁGUA 💧
=======================================================

Nível 1 - Muito baixo (crítico)      (em vermelho)
Nível 2 - Baixo                      (em amarelo)
Nível 3 - Médio                      (em verde)
Nível 4 - Alto                       (em ciano)
Nível 5 - Muito alto (alerta)        (em azul)

❓ Qual o nível de água no reservatório? (digite de 1 a 5): 8
⚠️  Valor inválido! Digite apenas um número de 1 a 5, conforme a lista de níveis acima.
❓ Qual o nível de água no reservatório? (digite de 1 a 5): abc
⚠️  Valor inválido! Digite apenas um número de 1 a 5, conforme a lista de níveis acima.
❓ Qual o nível de água no reservatório? (digite de 1 a 5): 3

📡 Situação atual do reservatório:
Nível 3 - Médio                      (em verde)
```

## 📁 Estrutura do projeto

```
controle-niveis-agua/
├── reservatorio.py  # Script principal com a lista, a função de cores e a pergunta do nível
└── README.md        # Documentação do projeto
```

## 🚀 Melhorias futuras

- Permitir várias consultas seguidas, sem precisar executar o programa novamente.
- Simular a leitura automática de um sensor com a biblioteca `random`.
- Exibir um alerta especial quando o reservatório estiver nos níveis críticos (1 ou 5).

## 👨‍💻 Autor

Projeto desenvolvido como atividade prática de Desenvolvimento de Sistemas I em Python, com foco no uso de bibliotecas externas. 💙

---

⭐ Se este projeto foi útil, deixe uma estrela no repositório!
