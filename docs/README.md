
# Аннотация к проекту 
в этом проекте на языке **python** реализованы функции для вычисления 
периметра и площади разных фигур, а именно:
окружности, прямоугольника, квадрата и треугольника.

# Описание работы функций
## 1. Окружность (circle.ру)
### Площадь
#### Аргументы
```
r (int) - радиус окружности
```
#### Реализация
```python
def area(r):
    return math.pi * r * r # здесь math - это стандартная библиотека python
```
### Периметр
#### Аргументы
```
r (int) - радиус окружности
```
#### Реализация
```python
def perimetr(r):
    return 2 * math.pi * r # здесь math - это стандартная библиотека python
```
## 2. Прямоугольник (triangle.ру)
### Полупериметр
#### Аргументы 
```
a (int): длина первой стороны
b (int): длина второй стороны
с (int): длина второй стороны
```
#### Реализация 
```python
def area(a, b, c):
    return (a + b + c) / 2
```
### Периметр
#### Аргументы
```
a (int): длина первой стороны
b (int): длина второй стороны
с (int): длина второй стороны
```
#### Реализация
```python
def perimetr(a, b, c):
    return a + b + c
```
## 3. Расчёт площади и периметра фигур (круг, квадрат)
### Площадь и периметр
#### Аргументы
```
figs: список доступных фигур (circle, square).
funcs: список доступных функций (perimeter, area).
sizes: словарь для хранения параметров фигур.
```
#### Реализация
```python
figs = ['circle', 'square'] 
funcs = ['perimeter', 'area'] 
sizes = {} 

def calc(fig, func, size):
    
    assert fig in figs
    assert func in funcs

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}') 

if __name__ == "__main__":    
	             
func = ''
fig = ''
size = list()

while fig not in figs:
    fig = input(f"Enter figure name, avaliable are {figs}:\n")

while func not in funcs:
    func = input(f"Enter function name, avaliable are {funcs}:\n")

while len(size) != sizes.get(f"{func}-{fig}", 1):
    size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

calc(fig, func, size)
```
## 4. Квадрат (square.ру)
### Площадь
#### Аргументы
```
a (int): длина одной стороны
```
#### Реализация
```python
def area(a):
    return a * a
```
### Периметр
#### Аргументы
```
a (int): длина первой стороны
```
#### Реализация
```python
def perimetr(a):
    return 4 * a
```
# История коммитов
+  **8797938f448ff4e0fcd2d1202f9fccf611b7b1a2** - добавил документацию в circle.ру
+  **8ba9aeb3cea847b63a91ac378a2a6db758682460** - L-03: Circle and square added
+  **d078c8d9ee6155f3cb0e577d28d337b791de28e2** -  L-03: Docs added
+  **d080c7888b81955bad2ed78d58ad910526b5132a** - L-04: Triangle added
+  **51c40ebfd0e0b65f52fe5e54740cbb038e492db3** -  L-04: Doc updated for triangle
+  **d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71** - L-04: Add calculate.py
+  **b5b0fae727ca72c317c383b39c0af73d6adcd81c** - Update docs for calculate.py
+  **8797938f448ff4e0fcd2d1202f9fccf611b7b1a2** - добавил документацию в circle.ру
