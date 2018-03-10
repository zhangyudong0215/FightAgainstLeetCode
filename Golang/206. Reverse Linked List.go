/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode { // 4ms
    if head == nil {
        return head
    } else {
        var prev *ListNode
        node := head
        for node != nil {
            tmp := node.Next
            node.Next = prev
            prev = node
            node = tmp
        }
        return prev
    }
}
