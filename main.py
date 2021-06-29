# Find Closest Number
A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]

def find_closest_num(A, target):
    min_diff = float("inf") # Минимальная разница
    low = 0
    high = len(A) - 1
    closest_num = None

    # Частные случаи с пустым списком и со списком с одним элементом
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high) // 2
        if mid+1 < len(A):
            min_diff_right = abs(A[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid-1] - target)


        # Проверяем на наличие наименьшей разницы слева и справа
        # Если такие есть обновляем минимальную разницу и ближайшее число
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]

        # Перемещаем среднюю точку как это сделано в бинарном поиске
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
            if high < 0:
                return A[mid]
        else:
            # Если целью является сам элемент, вернуть число
            return A[mid]
        return closest_num        
            