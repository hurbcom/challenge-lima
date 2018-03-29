
# Desafio Echo

	Este projeto é um simulador para controle de drones que tiram fotos 360º de uma área previamente delimitada desenvolvido em Python3 . 	

## Executando o Projeto
	É necessário ter instalado: Python3.
	Alternativamente é possivel o uso do [Docker](https://www.docker.com/).

### Executando com Python
	Instalar [Python](https://www.python.org/downloads/) 3.X
	Executar o comando:
	`python ./DesafioEcho/main.py`

### Executando com Docker
	Instalar [Docker](https://docs.docker.com/install/)
	Executar os comandos:
	`docker build -t desafio-echo .`
	`docker run --rm -it desafio-echo python3 main.py`

	Também há a opção de executar um arquivo Shell Script executando o comando:
	`sh start.sh`

## Executando Testes
	O projeto também contem alguns testes automatizados.
	Os testes podem ser executados utilizando  Python3 através do comando:
	`python ./DesafioEcho/Testes/testesDrone.py`

## Utilizando o Simulador
	Um breve tutorial de como um usuário pode utilizar o simulador.

### Inicializando a Área
	Ao executar o projeto o usuário deverá informar qual a Largura e a Altura que ele deseja que a área a ser fotografada possua. A área deve ter sempre altura e largura maiores do que 0. Caso números válidos sejam informados, uma mensagem de confirmação irá surgir.
### Inicializando os Drones
	Uma vez que a área esteja criada é necessário posicionar os drones e indicar qual  será sua lista de comandos. Para isso é utilizada uma única sequência de caracteres que indicará qual a coordenada cartesiana que o drone será iniciado, em que direção dos pontos cardeais a câmera do drone está virada e por fim a lista de comandos daquele drone.

	A maneira como as coordenadas cartesianas são indicas mudam de acordo com o tamanho da área delimitada. Em uma área 300x20 a coordenada [3,2] seria indicada "00302" enquanto em uma área 15X2 a mesma coordenada seria "032".
	As direções possiveis para inicializar um drone são N, S, L e O que simbolizam respectivamente os pontos cardeais Norte, Sul, Leste e Oeste.
	Os comandos possiveis para a lista de comandos do drone são F, D e E que simbolizam respectivamente Frente, Direita e Esquerda.

	Uma sequência que não esteja de acordo com essas regras irá emitir um erro e a sequência deverá ser digitada novamente.
	Um exemplo de uma sequência válida: dada uma área 20x20, ao passar a sequência "0403NDFFEEFDFE" o drone será inicializado na posição [4,3], virado para o Norte e com a lista de comandos "DFFEEFDFE".

### Finalizando Execução
	No final da execução do simulador um relatório é impresso na tela. Neste relatório é indicada a numeração do drone e abaixo dela a posição final do drone, a direção final em que a câmera do drone ficou e quantas fotos ele tirou.
	Caso a área não possua drones inicializados será impresso uma mensagem avisando que nenhum drone fora adicionado.

