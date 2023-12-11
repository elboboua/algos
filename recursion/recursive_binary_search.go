package main

import "fmt"

func recursiveBinarySearch(src []int, begin int, end int, target int) int {
	if begin > end {
		return -1
	}
	mid := (begin + end) / 2

	if src[mid] == target {
		return mid
	} else if src[mid] > target {
		return recursiveBinarySearch(src, begin, mid-1, target)
	} else {
		return recursiveBinarySearch(src, mid+1, end, target)
	}
}

func main() {
	src := []int{1, 2, 4, 5, 6, 7, 10}
	fmt.Println("index of 2: ", recursiveBinarySearch(src, 0, len(src)-1, 2))
	fmt.Println("index of 8: ", recursiveBinarySearch(src, 0, len(src)-1, 8))
	fmt.Println("index of 10: ", recursiveBinarySearch(src, 0, len(src)-1, 10))
}
