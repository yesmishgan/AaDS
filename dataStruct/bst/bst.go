package bst

type Node struct {
	Key   int
	Left  *Node
	Right *Node
	P     *Node
}

func NewNode(key int) *Node {
	return &Node{Key: key}
}

type BinaryTree struct {
	Root *Node
}

func NewBinaryTree() BinaryTree {
	return BinaryTree{
		Root: nil,
	}
}

func Min(t *Node) *Node{
	x := t
	for x.Left != nil {
		x = x.Left
	}
	return x
}

func Max(t *Node) *Node{
	x := t
	for x.Right != nil {
		x = x.Right
	}
	return x
}

func (t *BinaryTree) Add(k int) {
	z := NewNode(k)
	var y *Node
	x := t.Root
	for x != nil {
		y = x
		if z.Key < x.Key {
			x = x.Left
		} else {
			x = x.Right
		}
	}
	z.P = y
	if y == nil {
		t.Root = z
	} else if z.Key < y.Key {
		y.Left = z
	} else {
		y.Right = z
	}
}