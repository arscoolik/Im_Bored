package main

import (
	"fmt"
)

func Count(word string) string { //counting sort, works for O(m), where m is the size pf the word
	alph := make([]int, 26)
	for _, x := range word {
		alph[x-97]++
	}
	var ans string
	for i, v := range alph {
		for j := 0; j < v; j++{
			ans += string(i+97)
		}
	}
	return ans
}



func main() {
	strs := [...]string{"eat", "tea", "tan", "ate", "nat", "bat"}
    an := make(map[string][]string)
	for _, v := range strs {
		tmp := Count(v)
		an[tmp] = append(an[tmp], v)
	}
    fmt.Println(an)//the output could be different, but I think this way it fully demonstrates the result of the code
}
//#final complexity is O(n*m), where n is the list size and m is the words length
