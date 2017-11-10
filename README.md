# <img src="https://avatars1.githubusercontent.com/u/7063040?v=4&s=200.jpg" alt="HU" width="24" /> Desafio Echo

Estamos desenvolvendo um produto que basicamente usa drones para mapear uma região e tirar fotos 360º e criar um mapa de navegável, muito parecido com o Google Street View. Então o desafio é criar uma ferramenta para controlar esses drones. 🚁

Imagine que a região aonde os drones devem sobrevoar é um plano de X por Y metros e os drones só vão se locomover dentro desse plano de metro em metro (logo eles se locomovem em um grid) e a cada ponto de parada eles vão tirar uma foto 360º.

Quando eles são ligados, devem receber uma cordenada cartesiana de para onde eles vão se posicionar e para qual lado do bússula a camêra deve estar apontando, por exemplo (4, 3, N) leverá o drone para as coordenadas 4metros, 3metros e apotará a câmera para norte. Os pontos cardeais esperados são 4: (N)orte, (S)ul, (L)este e (O)este.

Uma vez ligados, cada drone deverá receber uma lista de comandos, em formato de string, que deverá ser executada sequencialmente e a cada comando executado uma foto 360º é tirada. Os comandos possíveis são: (D)ireita, (E)squerda, (F)rente. A cada vez que o drone receber um comando de "D" ou "E" ele fará um giro de 90º. Ex: "DFFEEFDFE" Nesse exemplo vão ser tiradas 5 fotos.

Construa um programa de linha de comando que ao ser iniciado receberá como parâmetros o tamanho da área que deve ser fotografada e então espere receber, a cada linha, a sequência de *strings* para posicionar e movimentar cada drone. Ao final do programa deve ser exibido um simples relatório mostrando a posicão final, para qual ponto cardeal a câmera está apontando e quantas fotos foram tiradas por cada drone.

ex:


Você pode usar qualquer linguagem de programação para o desafio. Preferencialmente esperamos que seja uma das linguagens abaixo:
- JavaScript (NodeJS)
- Go
- Kotlin
- Scala
- C++

Você pode usar qualquer _framework_. Se a sua escolhar for por um _framework_ que resulte em _boilerplate code_, por favor descreva no README qual pedaço de código foi escrito por você.

## Requisitos
- Os drones não podem voar para fora da área delimitada inicialmente. Uma vez que eles encostem em alguma borda, seu único movimento é girar
- Não deve ser tirada mais de uma foto do mesmo ponto
- Não é possível iniciar dois drones na mesma coordenada cartesiana
- Forkar esse desafio e criar o seu projeto (ou workspace) usando a sua versão desse repositório, tão logo acabe o desafio, submeta um *pull request*.
- O código precisa rodar em macOS ou Ubuntu (preferencialmente como container Docker)
- Para executar seu código, deve ser preciso apenas rodar os seguintes comandos:
  - git clone $seu-forkseu-fork
  - comando para instalar dependências
  - comando para executar a aplicação



## Critério de avaliação

- **Organização do código**: Separação de módulos, view e model, back-end e front-end
- **Clareza**: O README explica de forma resumida qual é o problema e como pode rodar a aplicação?
- **Acertividade**: A aplicação está fazendo o que é esperado? Se tem algo faltando, o README explica o porquê?
- **Legibilidade do código** (incluindo comentários)
- **Segurança**: Existe alguma vulnerabilidade clara?
- **Cobertura de testes** (Não esperamos cobertura completa)
- **Histórico de commits** (estrutura e qualidade)
- **UX**: As chamadas de coordenadas para os drones são intuítivas
- **Escolhas técnicas**: A escolha das bibliotecas, banco de dados, arquitetura, etc, é a melhor escolha para a aplicação?

## Dúvidas

Quaisquer dúvidas que você venha a ter, consulte as [_issues_](https://github.com/HotelUrbano/challenge-beta/issues) para ver se alguém já não a fez e caso você não ache sua resposta, abra você mesmo uma nova issue!

Boa sorte e boa viagem! ;)

<p align="center">
  <img src="ca.jpg" alt="Challange accepted" />
</p>
