import circle ''' circle: используется для работы с окружностью (площадь и периметр).'''
import square '''square: используется для работы с квадратом (площадь и периметр).'''


figs = ['circle', 'square'] '''figs: список доступных фигур (circle, square).'''
funcs = ['perimeter', 'area'] '''funcs: список доступных функций (perimeter, area).'''
sizes = {} '''sizes: словарь для хранения параметров фигур.'''

def calc(fig, func, size):
        '''
        Описание: Рассчитывает площадь или периметр для указанной фигуры с заданным размером.
        '''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}') '''Выводит результат вычисления.'''
        
if __name__ == "__main__":    ''' Параметры:  
                              fig: название фигуры (круг или квадрат).
                              func: операция (perimeter или area).
                              size: размер фигуры (радиус или сторона).
                              '''
        func = '' 
        fig = ''
	size = list()
        '''Запрашивает у пользователя название фигуры, операцию (площадь или периметр) и размеры.'''
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)   '''Вызывает функцию calc для выполнения вычислений.'''



