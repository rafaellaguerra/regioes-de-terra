# Regiões de Terra

Programa em Python que lê uma grade de 0 (água) e 1 (terra) e informa
quantas regiões de terra existem e qual o tamanho da maior.

Duas células de terra pertencem à mesma região se estiverem lado a lado
na horizontal ou na vertical (diagonais não contam).

## Como rodar

No PowerShell, dentro da pasta do projeto:

    Get-Content entrada.txt | python main.py

## Formato da entrada

Primeira linha: número de linhas (R) e de colunas (C).
Depois, R linhas com C caracteres cada, sendo 0 ou 1.

## Formato da saída

Dois números separados por espaço: quantidade de regiões e tamanho da maior.

## Algoritmo

Busca em largura (BFS) com fila (deque). Cada célula de terra visitada
é marcada como 0 ao entrar na fila, para não ser processada duas vezes.

## Testes

Os arquivos teste1.txt a teste4.txt cobrem: sem terra, tudo terra,
uma única célula e regiões que só se tocam na diagonal.
