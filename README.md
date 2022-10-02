# GIT_Lab_02_Alyona
## Что делает функция?
Написанная функция выполняет такой набор команд:

**rectangle -** считает периметр и площадь треугольника
**triangle -** считает периметр и площадь прямоугольника
**circle -** считает длину окружности и площадь круга

## Реализация с помощью Git Flow
Сначала подключаем Git Flow, затем создаем ветку **feature\A1** и делаем коммит на добавление функции **circle**. 
Далее сливаем ветки **feature** и **develop**, создаем ветку **release\1.1** и выпускаем версию 1.1, сливаем с веткой **main**.
Создаем вторую ветку **feature\A2**, добавляем функции **triangle** и **rectangle**. Сливаем их с **develop** и  выпускаем релиз 1.2.
Потом исправляем программу в ветке **hotfix\1.2.1** и сливаем эту ветку с **develop** и **main**. Готово:)
