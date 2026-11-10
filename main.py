import sys
from collections import deque

dados = sys.stdin.read().split()
R = int(dados[0])
C = int(dados[1])
grade = [list(linha) for linha in dados[2:2 + R]]

regioes = 0
maior = 0

for r in range(R):
    for c in range(C):
        if grade[r][c] == '1':
            regioes += 1
            grade[r][c] = '0'
            fila = deque()
            fila.append((r, c))
            tamanho = 0

            while fila:
                x, y = fila.popleft()
                tamanho += 1

                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < R and 0 <= ny < C and grade[nx][ny] == '1':
                        grade[nx][ny] = '0'
                        fila.append((nx, ny))

            if tamanho > maior:
                maior = tamanho

print(regioes, maior)