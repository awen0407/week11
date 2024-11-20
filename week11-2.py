# week11-2.py leetcode 2461
nums = [1,1,1,2,3] #輸入資料
from collections import Counter # 進階資料結構 hash map 用來計算出現幾次
counter = Counter() # 左邊小寫 右邊大寫
for num in nums:
  counter[num] += 1

print(counter) #印出統計的結果