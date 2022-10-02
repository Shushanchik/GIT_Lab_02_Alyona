def circle(r):
    s = int(3.14 * r**2)
    l = int(2 * 3.14 * r)
    return (s, l)

function = input()
if function == 'circle':
    print('Введите радиус: ')
    r = int(input())
    s, l = circle(r)
    print('s = ', s, '\nl = ', l)
