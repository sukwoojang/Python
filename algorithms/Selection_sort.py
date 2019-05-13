def find_smallest(arr): #arr : 최소값을 찾을 리스트
    smallest = arr[0] #리스트 내 첫번째 값
    smallest_index = 0 #리스트 내 첫번째 값의 인덱스
    for i in range(1,len(arr)): #for문 i의 범위는 1부터 arr의 길이까지(즉, 리스트 내 두번 째 원소부터 마지막 원소까지 반복한다)
        if smallest > arr[i]: #smallest는 arr리스트 내 첫번 째 값, 조건문을 통해 smallest값보다 작은 값이 있다면
            smallest = arr[i] #그 원소가 smallest에 저장된다
            smallest_index = i #또한 그 원소의 index 값이 smallest_index에 저장된다
    return smallest_index #리스트 내 최소값인 원소의 index 값인 smallest_index 값을 반환한다

def selection_sort(arr): # 입력값 : 선택정렬을 진행할 리스트
    newArr = [] #빈 리스트를 생성
    for i in range(len(arr)): #i의 범위는 0 부터 arr의 길이까지,즉,원소 개수의 횟수만큼 반복한다
        smallest = find_smallest(arr) #arr내의 가장 작은 원소의 index 값을 smallest 변수에 저장합니다
        newArr.append(arr.pop(smallest)) #위의 index값을 이용하여 arr내 해당위치의 값을 pop하여 newArr리스트에 append한다
    return newArr #반복문을 모두 수행하여 가장작은값부터 차례대로 정렬된 새로운 리스트 newArr을 반환한다


my_Arr = [1,18,2,9,14,5,11]
selection_sort(my_Arr)