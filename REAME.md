# Sudoku

Utilizando algoritmo de coloração de grafos, esse projeto:

1. Modela sudoku 9x9 como um grafo em SudokuSolver.mkgraph
2. Propõe, de forma aleatória, novos jogos de sudoku em SudokuSolver.create_game
3. Lê jogos como input (arrays com 81 elementos em que os nulos são representados por -1)
3. Soluciona ou informa que o jogo não é válido em SudokuSolver.color

## Como rodar

Para rodar, basta digitar no terminal:

```sh
python3 src/main.py
```

## Especificidades

Por favor tenha paciência no gerador de jogos, ele pode gerar muitos jogos inválidos mas eventualmente ele gera alguns válidos

## Autor

Aluno: Felipe Paradas

Matricula: 170009840