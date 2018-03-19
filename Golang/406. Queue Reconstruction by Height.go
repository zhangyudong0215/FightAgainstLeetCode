func reconstructQueue(people [][]int) [][]int { // 48ms
    res := make([][]int, 0, len(people))

    // 按照 persons 的排序方式，对 people 进行排序
    sort.Sort(persons(people))

    // 把 person 插入到 res[idx] 上
    insert := func(idx int, person []int) {
        res = append(res, person)
        // 插入到末尾
        if len(res)-1 == idx {
            return
        }
        // 插入到中间位置
        copy(res[idx+1:], res[idx:])
        res[idx] = person
    }

    for _, p := range people {
        insert(p[1], p)
    }

    return res
}

// persons 实现了 sort.Interface 接口
type persons [][]int

func (p persons) Len() int { return len(p) }

// 以 h 的降序为主
// 以 k 的升序为辅
func (p persons) Less(i, j int) bool {
    if p[i][0] == p[j][0] {
        return p[i][1] < p[j][1]
    }
    return p[i][0] > p[j][0]
}

func (p persons) Swap(i, j int) { p[i], p[j] = p[j], p[i] }