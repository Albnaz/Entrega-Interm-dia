# Entrega-Intermédia

## Elementos do grupo:
- Miguel Albernaz (2024109911)
- Miguel Braz     (2024111736)

## Objetivo do jogo e especificação
- O jogo segue um modelo competitivo, no qual cada jogador tem de realizar o máximo de entregas possíveis mais rapidamente que o seu oponente. 
- O primeiro jogador a fazer 5 pontos ganha, com um ponto correspondendo a uma entrega sucedida. 
- Para completar uma entrega, o jogador tem de colocar 3 objetos sequencialmente num pacote a partir de geradores de objetos, e depois entregar este pacote ao cliente correspondente.
- Parametros do jogo (atualmente apenas alteráveis no código) incluiem fatores como o tamanho do pedido e os pontos necessários para ganhar.

## Objetos interativos 
- Jogador ([1],[2]): Não pertence muito bem a esta categoria, mas é importante mencionar. Controlado com WASD (movimento) e E (interação). Jogadores conseguem carregar um objeto de cada vez.
- Geradores de Objetos ([◦], [▵], [▫], [▪]): Geram os objetos precisos para completar pacotes. 
- Pacotes ([◼], [◧], [◫]): Conseguem receber objetos ou ter objetos removidos deles. São entregados a clientes para ganhar pontos.
- Clientes ([A:...], [B:...]): Interação com clientes enquanto está a ser-se segurado um pacote igual ao seu pedido irá entregar o pacote em troca de pontos.
- Contentores ([⛶]): Conseguem segurar objetos, permitindo planear melhor para pedidos futuros.

## Comunicação
- O jogo segue o modelo cliente-servidor, com os clientes enviando comandos por via de sockets para o servidor (ints, strings, objetos), com este alterando o estado de jogo.
- O servidor, por sua vez, irá gerir este estado interno, disponibilizando uma representação visual deste estado para os clientes.
- O jogo necessita de um servidor e dois clientes para funcionar corretamente. 
- A informação do jogo é guardada utilizando o ficheiro dados.py, que armazena os dois tipos de operações feitos no jogo, movimentações e interações com objetos. 
- Fatores a ser monitorizados em runtime incluem, por exemplo, o mapa (array 2d), com todos os objetos presentes neste, os jogadores e as suas coordenadas e pontuações e os pedidos dos clientes.
