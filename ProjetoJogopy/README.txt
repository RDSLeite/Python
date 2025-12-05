Jogo das Naves - Entrega
Conteúdo do ficheiro zip:
- naves.py        -> contém classes NaveModelo e NaveComExtra
- funcoes.py      -> funções auxiliares (tabuleiro, guardar, carregar, etc.)
- main.py         -> programa principal (executar -> python3 main.py)
- README.txt      -> este ficheiro

Descrição rápida:
- Tabuleiro 10x10.
- 3 naves: uma NaveModelo e duas NaveComExtra (cores e símbolos diferentes).
- Jogador opta por realizar tiros aleatórios (implementado). A cada ronda são lançados 3 tiros.
- Guardar/Carregar em JSON (save_jogo.json).
- Quando total de tiros alcança 45, as naves com energia extra recebem a sua energia adicional.
- O jogo termina quando as três naves são aniquiladas ou quando se atingem 105 tiros.

Observações / melhorias possíveis:
- Permitir que o utilizador insira coordenadas dos tiros manualmente.
- Implementar um menu com escolha entre tiros aleatórios ou manuais.
- Implementar visualização colorida no terminal com a biblioteca colorama (atualmente usa códigos ANSI).
