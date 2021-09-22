package main

import (
	bst "data_struct/bst"
	"fmt"
)

func main() {
	fmt.Println("Hi")
	T := bst.NewBinaryTree()
	T.Add(3)
	T.Add(8)
	T.Add(10)
	T.Add(1)
	T.Add(6)
	T.Add(4)
	fmt.Println(bst.Min(T.Root).Key)
}
