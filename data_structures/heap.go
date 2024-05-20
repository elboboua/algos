package main

import (
    "fmt"
    "errors"
)

type MinHeap struct {
    capacity int
    size    int
    items []int
}

func (mh *MinHeap) Peek() (int, error) {
    if len(mh.items) == 0 {
        return 0, errors.New("empty")
    }
    return mh.items[0], nil}

// get index
func (mh *MinHeap) getLeftChildIndex(index int) int {
    return 2 * index + 1
}
func (mh *MinHeap) getRightChildIndex(index int) int {
    return 2 * index + 2
}
func (mh *MinHeap) getParentIndex(index int) int {
    return (index-1)/2
}
// has
func (mh*MinHeap) hasLeftChild(index int) bool {
    if mh.getLeftChildIndex(index) < mh.size {
        return true
    }
    return false
}
func (mh*MinHeap) hasRighChild(index int) bool {
    if mh.getRightChildIndex(index) < mh.size {
        return true
    }
    return false
}
func (mh *MinHeap) hasParent(index int) bool {
    if index >= 0 {
        return false
    }
    return true
}

// get item
func (mh *MinHeap) getLeftChild(index int) int {
    return mh.items[mh.getLeftChildIndex(index)]
}
func (mh *MinHeap) getRightChild(index int) int {
    return mh.items[mh.getRightChildIndex(index)]
}
func (mh *MinHeap) getParent(index int) int {
    return mh.items[mh.getParentIndex(index)]
}


func CreateMinHeap() *MinHeap { 
    return &MinHeap{ capacity: 0,
        size: 0,
        items: []int{},
    }
}


func main() {
    mh := CreateMinHeap();
    item, err := mh.Peek();
    if err != nil {
        fmt.Println(err);
    } else {
        fmt.Println(item);
    }
    fmt.Printf("%v", mh);
}

