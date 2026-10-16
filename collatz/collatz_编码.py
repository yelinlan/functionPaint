代码如下:
# cotz 编码
def encode(num):
if num <= 1:
raise ValueError("num must be positive")
return cotz(num, [], [])
def cotz(digits, code_val, detail_process):
detail_process.append(digits)
if digits == 1:
return code_val, detail_process
if digits % 2 == 0:
code_val.append('1')
return cotz(p(digits), code_val, detail_process)
else:
code_val.append('0')
return cotz(q(digits), code_val, detail_process)
def q(n):
return n * 3 + 1
def p(n):
return n // 2
def inv_p(n):
return n * 2
def inv_q(n):
return (n - 1) // 3
def decode_cotz(code_val):
if not code_val:
raise ValueError("code must not be empty")
val = 1
for i in range(len(code_val)):
if code_val[i] == '1':
val = inv_p(val)
else:
val = inv_q(val)
return val
if __name__ == '__main__':
print("*" * 50)
# num = int(input("请输入一个正整数："))
# 定义
print("Cotz编码： 【定义】：1 = //2, 0 = *3+1")
num = 100
code, detail = encode(num)
unique = ''.join(code)
unique_code = unique[::-1]
print(f"操作顺序 {num} => {unique}")
print(f"详细步骤 {" => ".join(map(str, detail))}")
print(f"编码值 => {unique_code}")
#十进制
print("编码后的十进制为", int(unique_code, 2))
print("*" * 50)
print(f"解码值 => {decode_cotz(unique_code)}")