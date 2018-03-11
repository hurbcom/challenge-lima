package main

import (
	"log"
	"strconv"
	"strings"
)

type drone struct {
	x, y   string
	photos int
	z      rune
}

type area struct {
	x, y int
}

func NewArea(x, y int) *area {
	return &area{x, y}
}

func (d *drone) coord(x int, y int, z rune) {
	sx, _ := strconv.Atoi(d.x)
	d.x = strconv.Itoa(sx + x)

	sy, _ := strconv.Atoi(d.y)
	d.y = strconv.Itoa(sy + y)

	d.z = z
}

func (d *drone) takePhoto() {
	d.photos++
}

func (d *drone) Command(s string, a *area) {
	if len(s) < 5 {
		log.Fatal("Invalid command! It's length must be greater than 5")
	}
	s = strings.ToUpper(s)
	for i, v := range s {
		if i < 2 {
			d.x += strconv.QuoteRune(v)
		} else if i < 4 {
			d.y += strconv.QuoteRune(v)
		} else if i == 5 {
			d.z = v
		} else {
			if v != 'F' {
				d.photos++
			}
		}
	}
}

func main() {
}
