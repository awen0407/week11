# 開新的 +程式碼 PYTHON
# week11-1py 主題 hash map, hash set (在[資料結構與演算法]教過的hash 雜湊)
table = {} #pythin用大括號代表字典 也就是 hash table (hash map, hash set)
table[9977341] = 9
table[4433997] = 4

print(table[9977341]) # 會印出 9
print(table[4433997]) # 會印出 4
# print(table[0]) # 如果沒有這個key,就會爆炸
if 0 not in table: # 如果沒有在裡面
  print("table[0]不存在")