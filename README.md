# <img src="https://avatars1.githubusercontent.com/u/7063040?v=4&s=200.jpg" alt="HU" width="24" /> Desafio Echo

Estamos desenvolvendo um produto que basicamente usa drones para mapear uma região e tirar fotos 360º e criar um mapa de navegável, muito parecido com o Google Street View. Então o desafio é criar uma ferramenta para controlar esses drones. 🚁

Imagine que a região aonde os drones devem sobrevoar é um plano de X por Y metros e os drones só vão se locomover dentro desse plano de metro em metro (logo eles se locomovem em um grid) e a cada ponto de parada eles vão tirar uma foto 360º.

Quando eles são ligados, devem receber uma cordenada cartesiana de para onde eles vão se posicionar e para qual lado do bússula a camêra deve estar apontando, por exemplo (4, 3, N) levará o drone para as coordenadas 4metros no eixo X e 3metros no eixo Y, apontando a câmera para norte. Os pontos cardeais esperados são 4: (N)orte, (S)ul, (L)este e (O)este.

Uma vez ligados, cada drone deverá receber uma lista de comandos, em formato de string, que deverá ser executada sequencialmente e a cada comando executado uma foto 360º é tirada automaticamente. Os comandos possíveis são: (D)ireita, (E)squerda, (F)rente. A cada vez que o drone receber um comando de "D" ou "E" ele fará um giro de 90º. Ex: "DFFEEFDFE" Nesse exemplo vão ser tiradas 5 fotos.

Construa um programa de linha de comando que ao ser iniciado receberá como parâmetros o tamanho da área que deve ser fotografada e então espere receber, a cada linha, a sequência de *strings* para posicionar e movimentar cada drone. Ao final do programa deve ser exibido um simples relatório mostrando a posicão final, para qual ponto cardeal a câmera está apontando e quantas fotos foram tiradas por cada drone.

ex:
<a href="https://asciinema.org/a/n3Ufy21fz6VavHPglju9h0rEZ" target="_blank"><img src="https://asciinema.org/a/n3Ufy21fz6VavHPglju9h0rEZ.png" /></a>
Nesse exemplo, as coordenadas de inicalização do drone e para qual ponto cardeal ele deve estar apontado no início foi enviada juntamente com a sequência de comandos.

# Resposta

## Desafio Extra
**Pontos extras se você responder no README.md qual é o menor número de drones para mapear completamnente um grid de 10x10 metros com o menor número de passos possíveis!**

Resposta: Apenas 1 drone.

## Liguagem
- O Desafio foi realizado utilizando a linguagem de programação C++, devido o conhecimento prévio em na linguagem c.

## Como executar
- Requisito: gcc
- Executando:
```bash
  $> git clone https://github.com/dougrhishu/challenge-echo.git
  $> cd challenge-echo
  $> g++ algoritmo.cpp
  $> ./a.out
```

Boa sorte e boa viagem! ;)

<p align="center">
  <img src="ca.jpg" alt="Challange accepted" />
</p>
