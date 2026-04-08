# Entrega-Intermédia

## Elementos do grupo:
- Miguel Albernaz (2024109911)
- Miguel Braz     (2024111736)

## Objetivo do jogo e especificação
-O jogo segue um modelo competitivo, no qual cada jogador tem de realizar o máximo de entregas possíveis mais rapidamente que o seu oponente. \n
-O primeiro jogador a fazer 5 pontos ganha, com um ponto correspondendo a uma entrega sucedida. \n
-Para completar uma entrega, o jogador tem de colocar 3 objetos sequencialmente num pacote a partir de geradores de objetos, e depois entregar este pacote ao cliente correspondente.
-Parametros do jogo (atualmente apenas alteráveis no código) incluiem fatores como o tamanho do pedido e os pontos necessários para ganhar. 

## Comunicação
-O jogo segue o modelo cliente-servidor, com os clientes enviando comandos por via de sockets para o servidor, com este alterando o estado de jogo e retornando a representação visual deste para os clientes. \n
-A informação do jogo é guardada utilizando o ficheiro dados.py, que armazena os dois tipos de operações feitos no jogo, movimentações e interações com objetos. \n
-Fatores a ser monitorizados em runtime incluiem, por exemplo, o mapa (array 2d), com todos os objetos presentes neste, os jogadores e as suas coordenadas e pontuações e os pedidos dos clientes.
