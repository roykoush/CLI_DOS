# Python Exercises

## Exercise 1

```bash
roykoush@Koushanis-MacBook-Air Exercises % python3
Python 3.14.8 (main, Sep 30 2026, 17:55:09) [Clang 21.0.0 (clang-2100.3.34.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1+2j
>>> b = 3+4j
>>> print(a,b)
(1+2j) (3+4j)
>>> r = a/b
>>> p = a*b.conjugate()
>>> print(r,p)
(0.44+0.08j) (11+2j)

```

## Exercise 2

```python
n = int(input('n: '))

#Left justified
for i in range(n+1):
    print(('*'*i).ljust(n))

#Right justified
for i in range(n+1):
    print(('*'*i).rjust(n))

#Centre justified
for i in range(n+1):
    print(('*'*(2*i-1)).center(2*n-1))
```

## Exercise 3

```python
n = 26
for i in range(27, 52):
    print(i%26, end=',')

```

## Exercise 4
