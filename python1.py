s = "  Hello Python  "
print(s.strip())          # 'Hello Python'  去首尾空格
print(s.lower())          # 全小写
print(s.upper())          # 全大写
print(s.replace("o","0")) # 替换
print(s.split())          # ['Hello', 'Python']  按空格分割
print("-".join(["a","b","c"]))  # a-b-c  用 - 连接
print("Python".startswith("Py"))# True
print("Python".endswith("on"))  # True
print("Python".find("th"))      # 2  找不到返回 -1
print(len("Python"))            # 6  长度