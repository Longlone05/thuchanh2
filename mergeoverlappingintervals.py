def merge_intervals(intervals):

    # Bước 1: Sắp xếp các khoảng theo điểm bắt đầu
    intervals.sort(key=lambda x: x[0])

    # Bước 2: Khởi tạo danh sách kết quả
    merged = []

    for interval in intervals:
        # Nếu danh sách merged rỗng hoặc không có chồng lấn, thêm khoảng hiện tại
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Nếu có chồng lấn, gộp khoảng
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged

# Tạo tuples ngẫu nhiên làm input
import random

# Số lượng tuples cần tạo và khoảng giá trị
num_tuples = int(input("Số lượng tuples: "))


# Danh sách để lưu các tuples
random_tuples = []

# Vòng lặp để tạo các tuples
for i in range(num_tuples):
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    # Tạo tuple với giá trị nhỏ trước, lớn sau
    random_tuples.append((min(a, b), max(a, b)))

# In danh sách các tuples ngẫu nhiên
print("Danh sách các tuples ngẫu nhiên:", random_tuples)

# Gọi hàm merge_intervals với input ngẫu nhiên
merged_intervals = merge_intervals(random_tuples)

# In kết quả
print("Danh sách các tuples sau khi gộp:", merged_intervals)
