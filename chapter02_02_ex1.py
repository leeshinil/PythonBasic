# Chapter 02-1
# Print 사용법


"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
### 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Lee'


# 출력1
ex1 = 'n = %s, s = %s, sum=%d' % (n, text, (x + y)) # %d
print(ex1)


# 출력2
ex2 = 'n = {n}, s = {serialno}, sum={sum}'.format(n=n, serialno=text, sum=x + y)
print(ex2)


# 출력3
ex3 = f'n = {n}, s = {text}, sum={x + y}' # f-String
print(ex3)

print()
print()


# 출력4(다양한 f-string 연습)

# 진수
# (2진수 : b, 8진수 : o, 16진수 : x|X)
k = 98

print(f"k 2진수: {k:b}, k 8진수: {k:o}")
print(f"k 16진수 - l:{k:x}, U:{k:X}")

print()
print()


# 구분기호
m = 10000000000

print(f"m: {m:,}")

print()
print()


# 정렬
# ^ : 가운데 , < : 왼쪽 , > : 오른쪽
t = 20

print(f"t :{t:10}")
print(f"t center: {t:^10}")
print(f"t left: {t:<10}")
print(f"t right: {t:>10}")

print()
print()


# 채우기
print(f"t:{t:-^10}")
print(f"t:{t:#^10}")