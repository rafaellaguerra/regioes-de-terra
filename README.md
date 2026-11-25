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
Depois, R linhas com C caracteres cada, sendo 0 ou 1, sem espaços.
Restrições: 1 ≤ R, C ≤ 1000 e R·C ≤ 10^6.

## Formato da saída

Dois números separados por espaço: quantidade de regiões e tamanho da maior.
Se não houver terra, a saída é `0 0`.

## Estratégia

O problema é contar os **componentes conexos** de um grafo em que cada
célula de terra é um vértice e há uma aresta entre células vizinhas nas
quatro direções (cima, baixo, esquerda, direita).

Usamos **busca em largura (BFS)** com fila (`deque`):

1. Percorremos a grade em ordem (linha por linha).
2. Ao encontrar uma célula `1` ainda não visitada, temos uma nova região:
   somamos 1 ao contador e rodamos uma BFS a partir dela.
3. A BFS visita todas as células de terra alcançáveis e conta quantas
   foram. Se esse tamanho for maior que o melhor até agora, ele passa a
   ser o maior.
4. Cada célula visitada é trocada de `1` para `0` **no momento em que
   entra na fila**. Assim ela não é enfileirada duas vezes e não
   precisamos de uma matriz extra de "visitados".

Por que BFS e não DFS recursiva: uma região pode ter até 10^6 células,
e uma DFS recursiva em Python estouraria o limite de recursão (cerca de
1000 por padrão) em regiões longas, como uma serpente. A BFS é iterativa
e não tem esse problema.

## Por que a resposta está correta

- **Cada região é contada uma única vez.** O contador só aumenta quando
  a varredura encontra um `1` não visitado. A BFS a partir dele visita
  **todas** as células da região (qualquer célula da região é alcançável
  por um caminho de vizinhos de terra, e a BFS explora todos os vizinhos
  de cada célula visitada). Depois disso, nenhuma célula daquela região
  continua com valor `1`, então a varredura nunca a reconta.
- **Nenhuma região é perdida.** A varredura passa por todas as células.
  Se existe uma região, sua primeira célula na ordem de varredura ainda
  está não visitada quando a varredura chega nela (só células da própria
  região a teriam marcado), então ela dispara uma BFS.
- **Regiões diferentes não se misturam.** A BFS só anda por vizinhos de
  terra nas 4 direções. Células de regiões distintas não são vizinhas,
  então uma BFS nunca atravessa para outra região.
- **O tamanho está certo.** Cada célula da região entra na fila
  exatamente uma vez (por causa da marcação na entrada) e é contada ao
  sair. O tamanho é, portanto, o número de células da região.
- **O maior é o máximo entre as regiões**, comparado ao final de cada BFS.
- **Sem terra:** nenhuma BFS roda e os valores iniciais `0 0` são
  impressos.

## Complexidade

Seja N = R·C o número de células (N ≤ 10^6).

- **Tempo: O(R·C).** Cada célula é visitada uma vez pela varredura e
  entra e sai da fila no máximo uma vez. Cada célula examina 4 vizinhos
  (trabalho constante).
- **Espaço: O(R·C).** A grade guardada em memória ocupa O(R·C). A fila
  guarda, no pior caso, uma fração das células (a "fronteira" da BFS),
  que também é O(R·C) no limite superior.

## Testes

Para conferir, cada arquivo foi rodado e a saída comparada com uma
solução independente (union-find). Todos coincidiram.

| Arquivo        | O que testa                                          | Saída esperada |
|----------------|------------------------------------------------------|----------------|
| `entrada.txt`  | exemplo do enunciado (4×5)                           | `3 4`          |
| `teste1.txt`   | **caso-limite:** sem terra (3×3 só de 0)             | `0 0`          |
| `teste2.txt`   | tudo terra (2×3), uma única região                   | `1 6`          |
| `teste3.txt`   | grade 1×1 com terra                                  | `1 1`          |
| `teste4.txt`   | só conexão diagonal: diagonais não contam            | `3 1`          |
| `teste5.txt`   | uma única linha (1×10), só 1                         | `1 10`         |
| `teste6.txt`   | uma única coluna (6×1): `1,1,0,1,1,1`                | `2 3`          |
| `teste7.txt`   | tabuleiro de xadrez 4×4: 8 regiões isoladas          | `8 1`          |
| `teste8.txt`   | região em serpente (5×4), um caminho longo           | `1 12`         |
| `teste9.txt`   | **caso-limite:** 1000×1000 todo de terra (10^6)      | `1 1000000`    |
| `teste10.txt`  | **caso-limite:** xadrez 1000×1000, máximo de regiões | `500000 1`     |
| `teste11.txt`  | 1000×1000 com uma única célula de terra              | `1 1`          |

Os testes `teste9` e `teste10` têm o tamanho máximo permitido. Em
nossa execução, cada um rodou em cerca de 1 segundo. O `teste9` é o pior
caso para a fila e o `teste10` o pior caso para o contador de regiões.
