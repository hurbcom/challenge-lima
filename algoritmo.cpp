#include <iostream>
#include <string>
#include<bits/stdc++.h>
#include <ctype.h>
using namespace std;

int main(){
  //Declaração de Variáveis
  string posicionamento, comandos, m, mm, instrucoes = "1", resultados[1] = "1";
  int cont = 0, fotos = 1, x, y, position, mx, my, qtdeDrone = 0;
  //Solicitando o tamanho da matriz para o usuário
  cout << "Informe a area como no exemplo a seguir: 10x20"  << endl << "Informe a Area:";
  getline(cin, m);
  //Usando o substr para selecionar uma parte da string e o istringstream convertendo para inteiro
  istringstream(m.substr(0,2)) >> my;
  istringstream(m.substr(3,2)) >> mx;
  //Usando o substr para selecionar uma parte da string
  mm = m.substr(2,1);
  //Verificando se a entrada para a definição da matriz é válida
  if(mm != "x" || mx == 0 || my == 0){
    cout << "A entrada informada é inválida"<< endl;
    exit(0); //Parando a execução do algoritmo
  }
  //Declaração de variáveL, sendo que a "partidaDrone" é para definir a posição inicial de todos os
  //drones para que não inicie outro na mesma posição
  string partidaDrone[mx][my];
  //Declaração de variável, definindo o tamanho da matriz usada pela navegação do drone
  string matriz[my][mx];
  //Laço de repetição será executado enquando o usuário inserir não inserir uma informação vazia.
  while(instrucoes != ""){
    //Solicitando os comandos a serem executados pelo drone
    cout << "Please inform the command sequence for drone " << qtdeDrone << " or leave empty to exit: ";
    getline(cin, instrucoes);
    //Se o usuário digitar uma informação em branco não irá executar os comandos dentro do if
    if(instrucoes != ""){
      fotos = 1;
      cont = 0;
      //Usando o substr para selecionar uma parte da string e o istringstream convertendo para inteiro
      istringstream(instrucoes.substr(2,-1)) >> x;
      istringstream(instrucoes.substr(0,2)) >> y;

      posicionamento = instrucoes.substr(4,1);
      comandos = instrucoes.substr(5);
      //Se não tiver nenhum drone iniciado na localização
      if(partidaDrone[x][y] != "D"){
        //Defininco o ponto inicial de um novo drone
        partidaDrone[x][y] = "D";
        //Executando a sequencia de comandos
        qtdeDrone++;
        while(comandos[cont]){
          //Verifica se os caracteres do comando passado são válidos
          if(comandos[cont] != 'F' && comandos[cont] != 'E' && comandos[cont] != 'D'){
            cout << "A entrada de comando é inválida"<< endl;
            exit(0);
          }
          //Se a posição estiver para o norte
          if(posicionamento == "N"){
            if(comandos[cont]=='F' && x > 0){ //Se o comando for para frente e a coluna for maior que 0
              posicionamento = "N";
              if(matriz[y][x-1] != "*"){ //Verificando se o drone não passou na posição
                fotos++; //tirando foto
              }
              x--; //movendo entre colunas
              matriz[y][x] = "*"; //Marcando a posição passada pelo drone
            }else{
              if(comandos[cont]=='D'){
                posicionamento = "O";
              }else{
                posicionamento = "L";
              }
            }
          }else if(posicionamento == "S"){ //Se a posição estiver para o sul
            if(comandos[cont]=='F' && x < mx){ //Verificando se o comando é para frente e se pode mover na coluna
              posicionamento = "S";
              if(matriz[y][x+1] != "*"){ //Verificando se o drone não passou na posição
                fotos++; //tirando foto
              }
              x++; //movendo entre colunas
              matriz[y][x] = "*"; //Marcando que o drone passou na posição
            }else{
              if(comandos[cont]=='D'){
                posicionamento = "L";
              }else{
                posicionamento = "O";
              }
            }
          }else if(posicionamento == "L"){ //Se a posição estiver para o leste
            if(comandos[cont]=='F' && y < my){ //Verificando se o comando é para frente e se pode mover na linha
              posicionamento = "L";
              if(matriz[y+1][x] != "*"){ //Verificando se o drone não passou na posição
                fotos++; //tirando foto
              }
              y++; //movendo entre linhas
              matriz[y][x] = "*";
            }else{
              if(comandos[cont]=='D'){
                posicionamento = "N";
              }else{
                posicionamento = "S";
              }
            }
          }else if(posicionamento == "O"){ //Se a posição estiver para o oeste
            if(comandos[cont]=='F' && y > 0){ //Verificando se o comando é para frente e se pode mover na linha
              posicionamento = "O";
              if(matriz[y-1][x] != "*"){ //Verificando se o drone não passou na posição
                fotos++; //tirando foto
              }
              y--; //movendo entre linhas
              matriz[y][x] = "*"; //Marcando que o drone passou na posição
            }else{
              if(comandos[cont]=='D'){
                posicionamento = "S";
              }else{
                posicionamento = "N";
              }
            }
          }
          cont++;
        }

        cout << "Posição Final: ["<<y << "," << x <<"]" << endl;
        cout << "Direção: "<<posicionamento << endl;
        cout << "Fotos: "<<fotos << endl << endl;

      }else{ //Caso a posição já tenha se iniciado com outro drone
        cout << "Entrada Inválida dois drones não podem iniciar na mesma localização"<< endl;
      }
    }
  }
  return 0;
}
