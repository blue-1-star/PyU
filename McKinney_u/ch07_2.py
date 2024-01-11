# p 238
import numpy as np
import pandas as pd
import re
text = "foo bar\t baz \tqux"
t2 = "Для сопоставления с одним или несколькими пробельными символами \
служит регулярное выражение \s+:"
print(re.split(r"\s+", text))
regex = re.compile(r"\s+")
print(f'regex->\n{regex.split(text)}')
print(f'regex->\n{regex.split(t2)}')
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com"""
# pattern = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"
pattern = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"
# Флаг re.IGNORECASE делает регулярное выражение нечувствительным к регистру
regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex.findall(text))
# Метод search возвращает специальный объект соответствия для первого
# встретившегося в тексте адреса
m = regex.search(text)
print(m)
print(text[m.start():m.end()])
"""
Метод regex.match возвращает None, потому что находит соответствие образцу
только в начале строки:
"""
print(regex.match(text))
"""
Метод sub возвращает новую строку, в которой вхождения образца заменены
указанной строкой:
"""
print(regex.sub("REDACTED", text))
# разбить каждый адрес на три компонента
"""
\.   - защищенная обратная косая черта перед точкой а перед какими
символами ещё употребляется \ ? 
ChatGPT
В регулярных выражениях обратная косая черта \ используется для создания 
"экранированных" символов, что означает, что следующий символ 
должен быть воспринят буквально, а не как специальный символ с определенным значением.
Вот несколько примеров использования обратной косой черты в регулярных выражениях:
\\: Экранирование для обозначения обратной косой черты как обычного символа.
\.: Экранирование для обозначения точки как обычного символа. В вашем регулярном выражении это используется, чтобы указать, что точка после \ является частью самого шаблона и не обозначает любой символ (как это было бы без экранирования).
\d: Обозначает любую цифру от 0 до 9.
\w: Обозначает любой алфавитно-цифровой символ (букву или цифру).
\s: Обозначает любой символ пробела (пробел, табуляция, новая строка).
\b: Обозначает границу слова.
\^ и \$: Обозначают начало и конец строки соответственно.
\( и \): Обозначают открывающую и закрывающую скобки.
Экранирование с помощью обратной косой черты позволяет использовать специальные символы как обычные символы в контексте регулярных выражений.
"""
pattern = r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"
regex = re.compile(pattern, flags=re.IGNORECASE)
m = regex.match("wesm@bright.net")
mm = m.groups()
print(mm)
print(regex.findall(text))
print(regex.sub(r"Username: \1, Domain: \2, Suffix: \3", text))
# 
data = {"Dave": "dave@google.com", "Steve": "steve@gmail.com",
"Rob": "rob@gmail.com", "Wes": np.nan}
data = pd.Series(data)
print(data)
print(data.isna())
print(data.str.contains("gmail"))
data_as_string_ext = data.astype('string')
print(data_as_string_ext)
print(data_as_string_ext.str.contains("gmail"))
pattern = r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"
data.str.findall(pattern, flags=re.IGNORECASE)
print(data.str.findall(pattern, flags=re.IGNORECASE))

# Расширенный тип Categorical в pandas
fruits = ['apple', 'orange', 'apple', 'apple'] * 2
N = len(fruits)
print(N)
rng = np.random.default_rng(seed=12345)
df = pd.DataFrame({'fruit': fruits,
 'basket_id': np.arange(N),
 'count': rng.integers(3, 15, size=N),
 'weight': rng.uniform(0, 4, size=N)},
 columns=['basket_id', 'fruit', 'count', 'weight'])
print(df)
# df['fruit'] – массив строковых объектов
fruit_cat = df['fruit'].astype('category')
print(fruit_cat)



