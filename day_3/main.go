package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

const width int = 31

func main() {
	input, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(input), "\n")

	fmt.Printf("Hit trees on the way down (%d right, %d down): %d \n", 1, 1, calcHits(1, 1, lines))
	fmt.Printf("Hit trees on the way down (%d right, %d down): %d \n", 3, 1, calcHits(3, 1, lines))
	fmt.Printf("Hit trees on the way down (%d right, %d down): %d \n", 5, 1, calcHits(5, 1, lines))
	fmt.Printf("Hit trees on the way down (%d right, %d down): %d \n", 7, 1, calcHits(7, 1, lines))
	fmt.Printf("Hit trees on the way down (%d right, %d down): %d \n", 1, 2, calcHits(1, 2, lines))
}

func calcHits(rightSteps int, downSteps int, lines []string) int {
	rightPos := rightSteps
	downPos := downSteps
	treesHit := 0

	for downPos < len(lines) {
		if lines[downPos][rightPos] == '#' {
			treesHit++
		}

		downPos += downSteps
		rightPos = (rightPos + rightSteps) % width
	}

	return treesHit
}
