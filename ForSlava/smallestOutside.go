package main

import (
	m "math"
)

func min(a, b int) int { //своя функция для нахождения минимума
    if a < b {
        return a
    }
    return b
}


//Суть алгоритма: 
//Если в массиве длиной n, есть все числа от одного до n, то нужно вывести n+1
//Задача, посмотреть какие числа от 1 до n есть, если какого-то нет, то вывести первое которого не встречается
//Проходом по массиву просматриваем каждый элемент, проверяем если он является индексом(=это число от 1 до n), и если это выполняется
//То, элемент массива с данным индексом делаем отрицательным. То есть, для хранения наличия того или иного числа будем хранить минус в ячейке с таким индексом
//В конце, проходясь по массиву, ищем первый положительный элемент, его индекс(+1) - ответ
//Сложность: O(n)

//Пример:
//Рассотрим массив []int{1, 3, 6, 1324, 5, 2, 2}
//size=7
//Походимся
//curValue = 1, value = 0, 0<=value<=size  => givenArray[0] = -1 
//Массив теперь выглядит как []int{-1, 3, 6, 1324, 5, 2, 2}
//Дальше на каждой итерации:
//[]int{-1, 3, -6, 1324, 5, 2, 2}
//[]int{-1, 3, -6, 1324, 5, -2, 2}
//[]int{-1, 3, -6, 1324, 5, -2, 2}
//[]int{-1, -3, -6, 1324, 5, -2, 2}
//[]int{-1, -3, -6, 1324, 5, -2, 2}
//Первый элемент который положительный это 1324, у него индекс 3, тогда ответ: 3+1=4

func findsmall(givenArray []int) int{ 
	size := len(givenArray)													//размер массива
	for _, curValue := range givenArray{									//проходим по массиву, рассматриваем только значения
		value := int(m.Abs(float64(curValue)) - 1)							//для того, чтобы перейти к индексам в будущем, уменьшаем на единицу
		if ((0 <= value) && (value < size)){								//проверяем, что данный индекс находится между 0 и размером массива
			givenArray[value] = min(-givenArray[value], givenArray[value])	//если это так, и значение положительно, меняем его на отрицательное
		}
	}
	for i, _ := range givenArray{
		if (givenArray[i] > 0){												//выводим первое число которое не является отрицательным
			return i + 1
		}
	}
	return size + 1 														//если все числа есть, то выводим большее на один

}
