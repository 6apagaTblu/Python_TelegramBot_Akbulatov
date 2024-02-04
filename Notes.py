import os

def build_note(note_text, note_name):
    """Создание заметки, на вход: текст и название заметки, на выход: файл созданной заметки"""
    try:
        with open(f'notes/{note_name}.txt', 'w') as f:
            f.write(note_text)
        print(f'Заметка {note_name} создана')
    except:
        print('Произошла ошибка при вызове функции создания заметки')

def create_note():
    """Запрос создания заметки, запрашивает данные у пользователя и вызывает build_note"""
    try:
        note_name = input('Введите название новой заметки: ')
        note_text = input('Введите текст новой заметки: ')
        build_note(note_text, note_name)
    except:
        print('Произошла ошибка при вызове функции создания заметки')

def read_note():
    """Чтение заметки, запрашивает данные у пользователя и открывает файл заметки"""

    try:
        note_name = input('Введите название заметки для чтения: ')
        if os.path.isfile(f'notes/{note_name}.txt'):
            with open(f'notes/{note_name}.txt', 'r') as f:
                print(f.read())
        else:
            print('Заметка с таким названием не найдена')
    except:
        print('Произошла ошибка при вызове функции чтения заметки')

def edit_note():
    """Редактирование заметки, запрашивает данные у пользователя и вносит корректировки в файл заметки"""

    try:
        note_name = input('Введите название редактируемой заметки: ')
        if os.path.isfile(f'notes/{note_name}.txt'):
            with open(f'notes/{note_name}.txt', 'r') as f:
                print(f.read())
            note_text = input('Введите новый текст заметки: ')
            with open(f'notes/{note_name}.txt', 'w') as f:
                f.write(note_text)
            print(f'Изменения в заметку {note_name} внесены')
        else:
            print('Заметка с таким названием не найдена')
    except:
        print('Произошла ошибка при вызове функции редактирования заметки')

def delete_note():
    """Удаление заметки, запрашивает даныне у пользователя и удаляет файл заметки"""

    try:
        note_name = input('Введите название планируемой к удалению заметки: ')
        if os.path.isfile(f'notes/{note_name}.txt'):
            os.remove(f'notes/{note_name}.txt')
            print(f'Заметка {note_name} удалена')
        else:
            print('Заметка с таким названием не найдена')
    except:
        print('Произошла ошибка при вызове функции удаления заметки')

def display_sorted_notes(rev=False):
    """Вывод всех заметок в порядке, указанном пользователем"""

    try:
        ls_notes = [f for f in os.listdir(os.path.join(os.getcwd(), 'notes'))
                    if f.endswith('.txt')] #список всех txt-файлов
        d_notes = {}

        for note in ls_notes: #создаем словарь с длиной заметок
            with open(f'notes/{note}', 'r') as file:
                d_notes[note] = file.read()

        d_notes = sorted(d_notes.items(),
                         key=lambda x: len(x[1]), reverse=rev) #превращаем словарь в сортированный список кортежей

        for note in d_notes:
            print(f'Заметка "{note[0][:-4]}"') #печатаем название заметки без расширения
            print(f'Содержание: {note[1]}', end='\n\n') #печатаем содержание заметки
    except:
        print('Произошла ошибка при вызове функции создания списка заметок')

def main():
    """Основной код, запрашивает код команды и вызывает соответствующую функцию"""

    try:
        while True:
            act = input('''Выберите действие:
            1. Создать заметку (C)
            2. Прочитать заметку (R)
            3. Редактировать заметку (E)
            4. Удалить заметку (D)
            5. Вывести все заметки (DA)
            ''')
            if act.lower() == 'c':
                create_note()
            elif act.lower() == 'r':
                read_note()
            elif act.lower() == 'e':
                edit_note()
            elif act.lower() == 'd':
                delete_note()
            elif act.lower() == 'da':
                act = input('Прямая сортировка? (y/n)')  # определяем направление сортировки
                display_sorted_notes(False if act.lower() == 'y' else True)
            else:
                print('Вы ввели некорректную команду')
            act = input('Хотите продолжить? (y/n) ')
            if act.lower() == 'n':
                break
    except:
        print('Произошла ошибка при вызове основной функции')