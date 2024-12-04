import random

def largest_sum_subarray(arr):
    max_sum = float('-inf')  # Khởi tạo tổng lớn nhất là một giá trị nhỏ
    current_sum = 0          # Tổng hiện tại
    start = end = temp_start = 0  # Các chỉ số cho mảng con

    for i in range(len(arr)):
        current_sum += arr[i]

        # Cập nhật tổng lớn nhất nếu cần
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        # Nếu tổng hiện tại âm, đặt lại tổng hiện tại và cập nhật vị trí bắt đầu
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return max_sum, arr[start:end + 1]

# Tạo mảng ngẫu nhiên
size = 10          
min_value = int(input("Nhập giá trị nhỏ nhất:"))  
max_value = int(input("Nhập giá trị lớn nhất:"))   

random_array = [random.randint(min_value, max_value) for _ in range(size)]

# Gọi hàm largest_sum_subarray và in kết quả
max_sum, subarray = largest_sum_subarray(random_array)
# In kết quả
print("Mảng ngẫu nhiên:", random_array)
print("Tổng lớn nhất:", max_sum)
print("Mảng con có tổng lớn nhất:", subarray)

