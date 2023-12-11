package main

import "fmt"

func recursiveSum(src []int) int {
	if len(src) == 1 {
		return src[0]
	}

	return src[0] + recursiveSum(src[1:])
}

func main() {
	src := []int{1, 2, 3, 4, 5, 6}
	sum := recursiveSum(src)
	fmt.Println("Total sum: ", sum)
}
