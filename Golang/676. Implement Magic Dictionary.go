type MagicDictionary struct {
    wordDict map[int][]string
}


/** Initialize your data structure here. */
func Constructor() MagicDictionary {
    return MagicDictionary{wordDict: make(map[int][]string, 100)}
}


/** Build a dictionary through a list of words */
func (this *MagicDictionary) BuildDict(dict []string)  {
    for _, word := range dict {
        this.wordDict[len(word)] = append(this.wordDict[len(word)], word)
    }
}


/** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
func (this *MagicDictionary) Search(word string) bool {
    for _, item := range this.wordDict[len(word)] {
        count := 0
        for index, _ := range word {
            if item[index] != word[index] {
                count++
            }
        }
        if count == 1 {
            return true
        }
    }
    return false
}


/**
 * Your MagicDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.BuildDict(dict);
 * param_2 := obj.Search(word);
 */