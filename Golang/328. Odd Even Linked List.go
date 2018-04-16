/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func oddEvenList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    
    odd := head
    first_odd := head
    even := head.Next
    first_even := head.Next
    head = first_even.Next
    count := 1
    for head != nil {
        if count == 1 {
            odd.Next = head
            odd = odd.Next
            count = 0
        } else {
            even.Next = head
            even = even.Next
            count = 1
        }
        head = head.Next
    }
    even.Next = nil
    odd.Next = first_even
    return first_odd
}
