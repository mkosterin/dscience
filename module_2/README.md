## Что нужно сделать:
1. Загрузить датасет, содержащий данные условий жизни учащихся
2. Выполнить предобработку данных, заполнив (обработав) пропуски
3. Оценить наличие выбросов, обработать
4. Выполнить корреляционный анализ, избавится от избыточности в датасете
5. Оценить номитативные переменные, устранить те, которые не влияют на результат
6. Сформулировать выводы
7. Выполнить проект и загрузить его на git.
8. Сдать свой ноутбук с решением на проверку ментору.
9. Получить обратную связь от ментора.


## Задание выполнено
1. Ноутбук написан
2. Исходный код проверен линтером
3. Выводы написаны

## Выводы
1. Проведена первичная обработка данных. Большинство строк удалось сохранить, заменив отсутствующие значения средним или медианным значениями.
2. Выбросы и очевидно неверные значения были обработаны
3. Корреляционный анализ показал, что имеющиеся числовые столбцы слабо коррелируют друг с другом, следовательно все данные можно использовать для построения модели. Возможно, можно использовать одно из двух значений Fedu или Medu, так как коэффициент корреляции составляет 0.6. Кроме того, не документированный столбец granular по модулю имеет полную корреляцию с studytime, соответственно может быть удален из модели.
4. Анализ номинативных переменных показал значимость стобцов sex, address, Mjob, higher, romantic. Остальные при построении модели можно исключить.