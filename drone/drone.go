package drone

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

type Drone struct {
	x, y   int
	photos int
	z      string
}

type area struct {
	x, y int
}

func NewArea(x, y int) *area {
	return &area{x, y}
}

func NewDrone() *Drone {
	return &Drone{}
}

//gets x, y, photos, z
func (d *Drone) GetInfo() (int, int, int, string) {
	return d.x, d.y, d.photos, d.z
}

func (d *Drone) updateDronePos(c string) (int, int, error) {
	switch c {
	case "D":
		if d.z == "N" {
			d.z = "L"
		} else if d.z == "L" {
			d.z = "S"
		} else if d.z == "S" {
			d.z = "O"
		} else if d.z == "O" {
			d.z = "N"
		}
		return 1, 0, nil
	case "E":
		if d.z == "N" {
			d.z = "O"
		} else if d.z == "O" {
			d.z = "S"
		} else if d.z == "S" {
			d.z = "L"
		} else if d.z == "L" {
			d.z = "N"
		}
		return -1, 0, nil
	case "F":
		if d.z == "N" {
			return 0, 1, nil
		} else if d.z == "S" {
			return 0, -1, nil
		} else if d.z == "L" {
			return 1, 0, nil
		} else if d.z == "O" {
			return -1, 0, nil
		}
		return 0, 0, errors.New("Invalid drone state!")
	default:
		return 0, 0, errors.New("Invalid command " + c)
	}
}
func (d *Drone) updateCoord(x, y int, a *area) error {
	if (d.x+x > a.x) || (d.y+y > a.y) || (d.y+y < 0) || (d.x+x < 0) {
		return errors.New("Invalid command. Drone location is out of range.")
	}
	d.x += x
	d.y += y
	return nil
}

func (d *Drone) takePhoto() {
	d.photos++
}
func readRune(r rune) string {
	return fmt.Sprintf("%c", r)
}

func (d *Drone) validateCommand(s string) error {
	if len(s) < 5 {
		return errors.New("Invalid command! It's length must be greater than 5")
	}
	for i, v := range s {
		if i > 4 {
			if readRune(v) != "D" && readRune(v) != "E" && readRune(v) != "F" {
				return errors.New(fmt.Sprintf("Invalid command. '%s' was found and it's not valid.", readRune(v)))
			}
		} else if i < 4 {
			if !unicode.IsNumber(v) {
				return errors.New(fmt.Sprintf("Invalid initial position. '%c' isn't valid.", v))
			}
		} else if i == 4 && readRune(v) != "N" && readRune(v) != "S" && readRune(v) != "L" && readRune(v) != "O" {
			return errors.New(fmt.Sprintf("Invalid orientation '%c'.", v))
		}
	}
	return nil
}
func (d *Drone) Command(s string, a *area) error {
	s = strings.ToUpper(s)
	err := d.validateCommand(s)
	if err != nil {
		return err
	}
	var sx, sy string
	for i, v := range s {
		if i < 2 {
			sx += readRune(v)
		} else if i < 4 {
			sy += readRune(v)
		} else if i == 4 {
			d.z = readRune(v)
			d.x, _ = strconv.Atoi(sx)
			d.y, _ = strconv.Atoi(sy)
			if d.x > a.x || d.y > a.y {
				return errors.New("Invalid initial position. It is out of range.")
			}
		} else {
			if readRune(v) != "F" {
				d.photos++
			}
			x, y, err := d.updateDronePos(readRune(v))
			if err != nil {
				return err
			}
			err = d.updateCoord(x, y, a)
			if err != nil {
				return err
			}
		}
	}
	return nil
}

func (d *Drone) Report() {
	var direction string
	switch d.z {
	case "N":
		direction = "Norte"
	case "S":
		direction = "Sul"
	case "L":
		direction = "Leste"
	case "O":
		direction = "Oeste"
	}
	fmt.Printf("- Final position: [%d, %d]\n- Direction: %s\n- Pictures taken: %d\n", d.x, d.y, direction, d.photos)
}
