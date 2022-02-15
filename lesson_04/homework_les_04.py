task_text = '''
Основний рівень
1. Перерахувати особливості мови Python:
- відносно проста для вивчення;
- інтерпретована мова програмування;
- високорівнева мова програмування;
- об'єктно-орієнтована;
- з відкритим вихідним кодом;
- кросплатформенна.

2. Правила найменування змінних у Python:
- назви змінних мають складатися з літер у нижньому регістрі та цифр;
- дозволяється використовувати символ нижнього підкреслювання;
- назва змінної має відображати позначуване нею значення;
- назва змінної не може починатися з цифри.
Приклад невдалої назви змінної:
1s = 'Hello!'
Приклад вдалої назви змінної:
text = 'Hello!

3. Виправити наступний фрагмент кода, щоб не виникало помилки при виконанні:
'''

# Task 3.
major_version = 3
minor_version = .9
version = major_version + minor_version
language = 'Python'
language_version = str(language) + ' ' + str(version)

'''
4. З використанням циклу while та оператора розгалуження if (без використання range, for і т.д.) 
написати код, який обраховує суму всіх чисел, менших за 100, які діляться без залишку одночасно на 3 та 5.
'''

# Task 4.
number = 1
total_sum = 0

while number < 100:
    if number % 3 == 0 and number % 5 == 0:
        total_sum += number
    number += 1

'''
5. Факторіал числа n - добуток всіх цілих позитивних чисел, які менші або дорівнюють n.
Наприклад, 3! = 1*2*3 = 6. Знайти факторіал числа, яке дорівнює довжині прізвища студента. 
Результат вивести у вигляді рядка “5! = 120”. Реалізація з використанням циклу while.
'''

# Task 5.
multiplication = 1
number = 1
surname = 'Metlitskiy'

while number <= len(surname):
    multiplication *= number
    number += 1
print(f'{len(surname)}! = {multiplication}')

'''
6. За допомогою цикла while реалізувати код, який буде на кожному проході циклу відкидати 
останній символ із заданого рядка (наприклад, string_to_truncate = 'I have a beautiful cat!')
і виводити оновлений рядок, доки рядок не стане пустим. Коли рядок стане пустим - 
вивести повідомлення "Nothing's left here".
'''

# Task 6.
string_to_truncate = 'I have a beautiful cat!'

while len(string_to_truncate) > 1:
    string_to_truncate = string_to_truncate[:-1]
    print(string_to_truncate)
else:
    print("Nothing's left here.")

'''
Просунутий рівень
1. Які переваги і недоліки виходять з того, що Python є інтерпритованою мовою програмування?
Python не потребує компіляції в двоїчний код. Ми просто запускаємо програму безпосередньо з 
вихідного коду. Внутрішньо Python перетворює вихідний код у проміжну форму, яка називається 
байт-кодами, а потім перекладає його на рідну мову комп’ютера, а потім запускає його.
Усе це, насправді, значно полегшує використання Python, оскільки нам не потрібно турбуватися
про компіляцію програми, переконуватися, що відповідні бібліотеки пов’язані та завантажені тощо.
Це також робить наші програми Python набагато більш портативними, оскільки можна просто 
скопіювати нашу програму Python на інший комп’ютер, і вона просто запрацює!

2. Пояснити різницю між мутабельними та імутабельними типами даних.
Всі типи даних в Python відносяться до однієї з 2-х категорій: змінні (mutable) і незмінні 
(unmutable). Багато з визначених типів даних Python - це типи незмінних об'єктів: числові дані
(int, float, complex), символьні рядки (class 'str'), кортежі (tuple). Інші типи визначені як 
такі, що змінюються: списки (list), множини (set), словники (dict). Типи (класи), що визначаються 
користувачем, можуть бути визначені як незмінні або змінювані. Змінність об'єктів певного типу є 
важливою характеристикою, визначальною, чи може об'єкт такого типу виступати як ключ для словників 
(dict) чи ні. Деякі типи даних, наприклад dict або set, реалізовані як хеш-таблиці. Коли ми додаємо
елемент у множину, інтерпретатор бере хеш від цього елемента і розміщує значення за адресою, яка 
збігається з хеш. Якщо ми спробуємо покласти список у множину, то отримаємо TypeError, тому що хеш
змінився б, коли змінився б один з елементів списку. Тому мутабельні об'єкти, такі як словники чи 
списки, не можуть бути ключами у словнику або елементами множини. А ось рядки чи числа можуть.

3. Прості числа - це такі числа, які діляться без залишку тільки на 1 та самих себе. 
З використанням тільки циклу while та оператора розгалуження if (без циклу for та range), 
реалізувати код, який визначатиме чи є задане число number простим.
'''

# Task 3 (advanced).
number = int(input())
counter = 0
divider = 2

while divider <= (number // 2 + 1) and divider != number:
    if number % divider == 0:
        counter += 1
    divider += 1
if counter == 0:
    print('Number is simple.')
else:
    print('Number is composite.')

'''
4. Послідовність Фібоначчі - ряд чисел, кожен новий елемент якого визначається як сума двох попердніх 
елементів. Послідовніть Фібоначчі починається так: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89... 
З використанням тільки циклу while та оператора розгалуження if (без циклу for та range), реалізувати код, 
який знаходить суму всіх непарних чисел із послідовності Фібоначчі, що менші 100_000.
'''

num1 = 1
num2 = 1
total_sum = 0

while num1 < 100000:
    if num1 % 2 != 0:
        total_sum += num1
    num1, num2 = num2, num1 + num2

# Task, concerning BMI.
weight = 82
height = 1.74
BMI = weight / (height * height)

if BMI <= 18.5:
    print('Your BMI is less than normal')
elif 18.5 < BMI < 25:
    print('Your BMI is normal')
else:
    print('Your BMI is greater than normal')
