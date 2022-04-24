package main

import (
	f "fmt"
	m "math"
)

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func findsmall(arr []int, size int) int{ //works pretty much the same as the python script
	for _, v := range arr{
		tmp := int(m.Abs(float64(v)) - 1)
		if ((0 <= tmp) && (tmp <= size)){
			arr[tmp] = min(-arr[tmp], arr[tmp])
		}
	}
	for i, _ := range arr{
		if (arr[i] > 0){
			return i + 1
		}
	}
	return size + 1

}

func main(){
	arr := []int{1, 3, 6, 1324, 5, 2, 2}
	f.Println(findsmall(arr, len(arr)))
}
