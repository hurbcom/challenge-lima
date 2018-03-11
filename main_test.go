package main

import (
	"strconv"
	"testing"
)

func TestValidCommand(t *testing.T) {
	d := drone{}
	a := NewArea(15, 20)
	d.Command("0112ODEDFFFEDF", a)
	if d.photos != 5 {
		t.Error("Wrong initial position. Expected 0112O, but received " + strconv.Itoa(d.photos))
	}
}

func TestValidInitialPosition(t *testing.T) {
}
