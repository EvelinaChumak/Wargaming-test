# Wargaming-test
Данная приложение - решение тестового задания для Wargaming St. Petersburg
## Структура
### framework
Предназначен для базовой работы с базой данных и вспомагательными ко всему приложению функциями
### tests
Описана сама работа с конкретной базой данных
#### config
Содержит изменяемую информацию, такую как имена файлов и данные для заполения базы данных
#### database
Содержит запросы к бд и класс с функциями по созданию, изменению и получению информации
#### test_functional.py
Автотесты с использованием pytest