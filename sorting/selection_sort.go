package main

import "fmt"

func SelectionSort(src []int) []int {
	src_copy := make([]int, len(src))
	copy(src_copy, src)
	dst := []int{}
	for len(src_copy) > 0 {
		var smallest_index int = 0
		for index, val := range src_copy {
			if val < src_copy[smallest_index] {
				smallest_index = index
			}
		}
		dst = append(dst, src_copy[smallest_index])
		src_copy = append(src_copy[0:smallest_index], src_copy[smallest_index+1:]...)
	}

	return dst
}

func SelectionSortInPlace(src []int) {
	for i := 0; i < len(src)-1; i++ {
		smallest_index := i
		for j := i + 1; j < len(src); j++ {
			if src[j] < src[smallest_index] {
				smallest_index = j
			}
		}
		src[smallest_index], src[i] = src[i], src[smallest_index]
	}
}

func main() {
	src := []int{5, 6, 10, 500, 1, -1}
	fmt.Println("Original slice: ", src)
	dst := SelectionSort(src)
	fmt.Println("Sorted not in place slice: ", dst)
	SelectionSortInPlace(src)
	fmt.Println("Sorted in place slice: ", src)
}
