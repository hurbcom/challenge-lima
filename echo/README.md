# Introducao

Este projeto "Echo" tem o objetivo de ser uma ferramenta de "simulacao" de drones e movimenta-los em um determinado espaco espaco.

## Requisitos

Os requisitos necessarios e apenas a previa instalacao de ruby 2.4.1

## Utilizacao

    $ bin/echo 10x10
    Generated new Space with 10m by 10m.

    - Menu
    - h : help
    - n : new drone
    - p : print report
    - q : exit
    n

    - Please insert position and orientation for Drone 1
    - ex.: 3 3 N
    - press enter to go menu
    - possible orientations:
      - N -> North
      - S -> South
      - O -> West
      - L -> East
    5 5 N

    Please insert movement sequence:
    - ex.: DFFFEDF
    - F -> go forward
    - D -> go right and rotate 90 degress
    - E -> go left and rotate -90 degress
    DFFFEDF


## Executar tests

    $ bundle install
    $ rspec