package main

func Count(word string) string { //counting sort, works for O(m), where m is the size of the word
	alphabet := make([]int, 26)  //array for storing the number of letters
	for _, x := range word {
		alphabet[x-97]++        //counting the number of letters in the word
	}
	var answer string
	for key, value := ra nge alph {
		for tmp := 0; j < value; tmp++{
			answer += string(rune(key+97)) //joining the letters together to get the sorted word
		}
	}
	return answer
}


func anag(givenStr []string) map[string][]string{
    ans := make(map[string][]string) //a map where the key is the sorted word, and values are the words that make this sorting word
	for _, value := range givenStr {
		tmp := Count(value)
		ans[tmp] = append(ans[tmp], value)
	}
    return ans
//#final complexity is O(n*m), where n is the list size and m is the words length
