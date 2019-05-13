def quick_sort(arr : list):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        small_arr = []
        large_arr = []
        for item in arr[1:]: #범위설정 잘해주자 혼자할때 이거틀림
            if item <= pivot:
                small_arr.append(item)
            elif item > pivot:
                large_arr.append(item)
        return quick_sort(small_arr) + [pivot] + quick_sort(large_arr) #피벗도 리스트로 만들어주는거에 주의

arr = [1, 3, 5, 2, 4, 7, 9, 12 ,15]
quick_sort(arr)