package main

import (
	"bufio"
	"challenge-echo/drone"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	var command string
	var drones []drone.Drone
	count := 1
	reader := bufio.NewReader(os.Stdin)

	args := os.Args[1:]
	if len(args) != 1 {
		log.Fatal("You must inform the grid dimension. Ex.: 10x20")
	}
	args = strings.Split(args[0], "x")
	fmt.Printf("Generating flying grid with dimensions of %sm by %sm.\n\n", args[0], args[1])
	x, _ := strconv.Atoi(args[0])
	y, _ := strconv.Atoi(args[1])
	a := drone.NewArea(x, y)

	for {
		fmt.Printf("Please inform the command sequence for drone %d or leave empty to exit: ", count)
		command, _ = reader.ReadString('\n')
		if command == "\n" {
			break
		}
		d := drone.NewDrone()
		err := d.Command(strings.TrimSuffix(command, "\n"), a)
		if err != nil {
			log.Fatal(err)
		}
		drones = append(drones, *d)
		count++
	}

	for i, v := range drones {
		fmt.Printf("Drone %d\n", i+1)
		report(v)
		fmt.Println()
	}
}

func report(d drone.Drone) {
	var direction string
	x, y, photosTaken, camOrient := d.GetInfo()
	switch camOrient {
	case "N":
		direction = "Norte"
	case "S":
		direction = "Sul"
	case "L":
		direction = "Leste"
	case "O":
		direction = "Oeste"
	}
	fmt.Printf("- Final position: [%d, %d]\n- Direction: %s\n- Pictures taken: %d\n", x, y, direction, photosTaken)
}
