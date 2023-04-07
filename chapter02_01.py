# Chapter 02-1
# Print 사용법

# 기본출력
print('a')
print('''a''')
print("a")
print("""a""")

print()

# separator 옵션
print('p','y','t','h','o','n', sep = ' ');
print('010', '1234', '1234', sep='-');

print()

# end 옵션 다음 프린트 이어준다.
print('welcom to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# File 옵션
import sys;
print('learn python', file=sys.stdout)
print()

# format 사용(d, s, f)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 2))

print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' % ('nice',)) # 10자리 
print('{:>10}'.format('nice'))

print('%-10s' % ('nice',))
print('{:10}'.format('nice'))

print('{:_<10}'.format('nice')) # _로 10자리 
print('{:^10}'.format('nice')) # 중앙정렬

print('%.5s' % ('pythonstudy',))
print('{:.5}'.format('pythonstudy'))
print('{:10.5}'.format('pythonstudy')) # 10글자공간 중 5자리만 나와라

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42,))
print('{:4d}'.format(42))

# %f
print('%f' % (3.141592653589793,))
print('{:f}'.format(3.141592653589793))

print('%06.2f' % (3.141592653589793,))
print('{:06.2f}'.format(3.141592653589793))