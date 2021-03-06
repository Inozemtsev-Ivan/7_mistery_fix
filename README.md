# Решатель квадратных уравнений

Данный модуль реализует способ решения квадратных уровнений с помощью дескриминанта. 

# Как использовать

У модуля нет интерактивного интерфейса. В модуле реализована функция `get_roots(a, b, c)`, которая принимает на вход три параметра решаемого уравнения соответственно. Функция принимает параметры числовых типов `integer` и `float`. Например, для решения уравнения _-x<sup>2</sup> + 2,5x - 4_ следует вызвать функцию вида: `get_roots(-1, 2.5, -4)`.

Функция возвращает:
- `tuple` вида `(root1, root2)`, если у исходного уравнения два корня;
- `tuple` вида `(root, None)`, если у исходного уравнения один корень;
- `tuple` вида `(None, None)`, если у исходного уравнения нет корней;

Функцию необходимо импортировать из модуля перед использованием в своем коде, например:
```python
from quadratic_equation import get_roots
```
или другим удобным способом.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
