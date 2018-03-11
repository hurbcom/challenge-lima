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

	d2 := drone{}
	d2.Command("0112NFF", a)
	if d2.photos != 0 {
		t.Errorf("Photos should't have been taken. Photos: %d", d.photos)
	}
}

func TestValidateCommand(t *testing.T) {
	d := drone{}
	a := area{}
	err := d.validateCommand("1620NDEF", &a)

	if err != nil {
		t.Error("A valid command was invalidated.", err)
	}

	err = d.validateCommand("11A5LDED", &a)

	if err == nil {
		t.Error("An invalid command was accepted: ", "11A5LDED")
	} else {
		t.Log("Error was successfully detected: ", err)
	}
}
