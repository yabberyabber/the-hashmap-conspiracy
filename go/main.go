package main;

import "os"
import "strconv"
import "math/rand"

func main() {
		size, _ := strconv.Atoi(os.Args[1])

		subject := map[int]int{}

		for i := 0; i < size; i++ {
			subject[i + (size * (rand.Int() % size))] = i
		}
}
