/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    stack1 := make([]int, 0, 100)
    stack2 := make([]int, 0, 100)
    for l1 != nil {
        stack1 = append(stack1, l1.Val)
        l1 = l1.Next
    }
    for l2 != nil {
        stack2 = append(stack2, l2.Val)
        l2 = l2.Next
    }
    cur := new(ListNode)
    total := 0
    for len(stack1) > 0 || len(stack2) > 0 {
        if len(stack1) > 0 {
            total += stack1[len(stack1)-1]
            stack1 = stack1[: len(stack1)-1]
        }
        if len(stack2) > 0 {
            total += stack2[len(stack2)-1]
            stack2 = stack2[: len(stack2)-1]
        }
        cur.Val = total % 10
        total /= 10
        head := new(ListNode)
        head.Val = total
        head.Next = cur
        cur = head
    }
    if cur.Val > 0 {
        return cur
    } else {
        return cur.Next
    }
}
