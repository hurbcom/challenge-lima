# <img src="https://avatars1.githubusercontent.com/u/7063040?v=4&s=200.jpg" alt="HU" width="24" /> Lima Challenge

[[English](README.md) | [Português](README.pt.md)]

We're developing a product that basically uses drones to map a region and take 360º photos and create a navigable map, much like Google Street View. So the challenge is to create a tool to control these drones. 🚁

Imagine that the region where the drones must fly over is a plane of X by Y meters and the drones will only move within that plane from meter to meter (so they move in a grid) and at each stop point they will take a 360º photo.

When they are turned on, they should receive a Cartesian coordinate of where they will position themselves and which side of the compass the camera should be pointing to, for example (4, 3, N) will take the drone to coordinates 4 meters on the X axis and 3 meters on the Y axis, pointing the camera north. The expected cardinal points are 4: (N)orth, (S)outh, (E)ast and (W)est.

Once connected, each drone must receive a list of commands, in string format, which must be executed sequentially and for each command executed a 360º photo is taken automatically. Possible commands are: (R)ight, (L)eft, (F)orward. Each time the drone receives a command of "R" or "L" it will make a 90º turn. Ex: "RFFLLFRFL" In this example, 5 photos will be taken.

Build a command line program that when started will receive as parameters the size of the area that must be photographed and then expect to receive, on each line, the sequence of _strings_ to position and move each drone. At the end of the program, a simple report should be displayed showing the final position, which cardinal point the camera is pointing to and how many photos were taken by each drone.

ex:
<a href="https://asciinema.org/a/n3Ufy21fz6VavHPglju9h0rEZ" target="_blank"><img src="https://asciinema.org/a/n3Ufy21fz6VavHPglju9h0rEZ.png" /></a>
In this example, the drone's initialization coordinates and which cardinal point it should be pointing to at the beginning were sent along with the command sequence.

You can use any programming language for the challenge. Preferably we hope it is one of the languages ​​below:

-   JavaScript (NodeJS)
-   Go
-   Kotlin
-   Dart
-   C++

You can use any _framework_. If your choice is for a _framework_ that results in _boilerplate code_, please describe in the README which piece of code you wrote.

Extra points if you answer in README.md **which is the least number of drones to fully map a 10x10 meter grid with the fewest possible steps**!

## Requirements

-   Drones cannot fly outside the initially delimited area. Once they touch an edge, their only move is to rotate
-   A photo will not be taken if the drone passes by/stays at the same point more than once
-   It is not possible to start two drones at the same Cartesian coordinate
-   Fork this challenge and create your project (or workspace) using your version of that repository, as soon as you finish the challenge, submit a _pull request_.
    -   If you have any reason not to submit a _pull request_, create a private repository on Github, do every challenge on the **master** branch and don't forget to fill in the `pull-request.txt` file. As soon as you finish your development, add the user `automator-hurb` to your repository as a contributor and make it available for at least 30 days. **Do not add the `automator-hurb` until development is complete.**
    -   If you have any problem creating the private repository, at the end of the challenge fill in the file called `pull-request.txt`, compress the project folder - including the `.git` folder - and send it to us by email.
-   The code needs to run inside a Docker container
-   To run your code, all you need to do is run the following commands:
    -   git clone \$your-fork
    -   cd \$your-fork
    -   command to install dependencies
    -   command to run the application

## Evaluation criteria

-   **Organization of code**: Separation of modules, view and model, back-end and front-end
-   **Clarity**: Does the README explain briefly what the problem is and how can I run the application?
-   **Assertiveness**: Is the application doing what is expected? If something is missing, does the README explain why?
-   **Code readability** (including comments)
-   **Security**: Are there any clear vulnerabilities?
-   **Test coverage** (We don't expect full coverage)
-   **History of commits** (structure and quality)
-   **UX**: Is the interface user-friendly and self-explanatory? Is the API intuitive?
-   **Technical choices**: Is the choice of libraries, database, architecture, etc. the best choice for the application?

## Doubts

Any questions you may have, check the [_issues_](https://github.com/HurbCom/challenge-lima/issues) to see if someone hasn't already and if you can't find your answer, open one yourself. new issue!

Good luck and good trip! ;)

<p align="center">
  <img src="ca.jpg" alt="Challange accepted" />
</p>
