from datetime import datetime
import os.path
import csv
import json

from task_planner_ad_func1 import get_id
from task_planner_ad_func1 import get_title
from task_planner_ad_func1 import get_description
from task_planner_ad_func1 import get_priority
from task_planner_ad_func1 import get_due_date
from task_planner_ad_func1 import get_edit_title
from task_planner_ad_func1 import get_edit_description
from task_planner_ad_func1 import get_edit_priority
from task_planner_ad_func1 import get_edit_status
from task_planner_ad_func1 import get_edit_due_date
from task_planner_ad_func1 import change_date_to_str
from task_planner_ad_func1 import change_str_to_date


def read_file():
    if os.path.exists('./data/lst_tasks.json'):
        with open('./data/lst_tasks.json') as file_object:
            lst_tasks = json.load(file_object)
            lst_tasks = change_str_to_date(lst_tasks)
            return lst_tasks
    else:
        return []


def print_cli(lst):
    """Function prints Command Line Interface
    """
    print(lst[0])
    for i in range(1, len(lst)):
        print(i - 1, lst[i])


def select_function():
    """Function defines function of Command Line Interface.
    """
    while True:
        try:
            function_answer = int(input('Type number of desirable function (from 0 to 9): '))
            if 0 <= function_answer <= 9:
                return function_answer
            else:
                raise ValueError('Invalid value. Type number in digit form (from 1 to 9).')
        except ValueError as err:
            print(err)


def execute_func_0(lst):
    """Function interrupts executing program.
    """
    lst = change_date_to_str(lst)
    with open('./data/lst_tasks.json', 'w') as file_object:
        json.dump(lst, file_object)
    print('Work is finished.')


def create_task(lst_t, lst_k):
    task_id = get_id(lst_t)
    task_title = get_title()
    task_description = get_description()
    task_priority = get_priority()
    task_status = 'pending'
    task_due_date = get_due_date()
    lst_values = [task_id, task_title, task_description, task_priority, task_status, task_due_date]
    dict_task = {lst_k[i]: lst_values[i] for i in range(len(lst_k))}
    return dict_task


def review_tasks_list(lst):
    """Function sorts the tasks by the key 'id' and prints list of tasks.
    """
    sorted_list = sorted(lst, key=lambda d: d['id'])
    return sorted_list


def review_task_detail(lst):
    """Function prints the task in details.
    """
    try:
        get_id_review = int(input('Type id of task for reviewing details: '))
        for i in range(len(lst)):
            if lst[i]['id'] == get_id_review:
                return lst[i]
        else:
            raise KeyError('Invalid key. Key is not found.')
    except ValueError as err:
        print(err)
    except KeyError as err:
        print(err)


def edit_task(elem):
    """Function edits the task or leaves the task without changes.
    """
    elem1 = get_edit_title(elem)
    if elem1 is None:
        return
    elem2 = get_edit_description(elem1)
    if elem2 is None:
        return
    elem3 = get_edit_priority(elem2)
    if elem3 is None:
        return
    elem4 = get_edit_status(elem3)
    if elem4 is None:
        return
    elem5 = get_edit_due_date(elem4)
    if elem5 is not None:
        print('Task is successfully updated.')


def delete_task(lst):
    """Function deletes the task.
    """
    try:
        get_id_delete = int(input('Type id of task for deleting: '))
        for i in range(len(lst)):
            if lst[i]['id'] == get_id_delete:
                del lst[i]
                return
        else:
            raise KeyError('Invalid key. Key is not found.')
    except ValueError as err:
        print(err)
    except KeyError as err:
        print(err)


def find_by_name(lst):
    """Function finds the task by title (part of title).
    """
    try:
        name_task = input('Type name of task for searching: ').lower()
        for i in range(len(lst)):
            if name_task in lst[i]['title'].lower():
                return print(lst[i])
        else:
            raise ValueError('Invalid value.')
    except ValueError as err:
        print(err)


def sort_by_priority(lst):
    """Function sorts the tasks by the key 'priority' and prints list of tasks.
    """
    try:
        return sorted(lst, key=lambda d: d['priority'], reverse=True)
    except TypeError as err:
        print(err)
    except ValueError as err:
        print(err)


def find_overdue_task(lst):
    """Function finds the overdue tasks and prints it.
    """
    try:
        today_date = datetime.now().date()
        lst_overdue_task = [{key: value for key, value in elem.items()} for elem in lst
                            if (elem['due_date'] - today_date).days < 0 and elem['status'] != 'done']
        return lst_overdue_task
    except TypeError as err:
        print(err)
    except ValueError as err:
        print(err)
    except KeyError as err:
        print(err)


def save_cur_tasks(lst_t, lst_k):
    """Function saves the current tasks.
        """
    try:
        get_name_file = input('Type name of file (without extension): ')
        if not os.path.exists(f'./data/{get_name_file}.csv'):
            with open(f'./data/{get_name_file}.csv', 'w') as file_object:
                writer = csv.DictWriter(file_object, fieldnames=lst_k)
                writer.writeheader()
                writer.writerows(lst_t)
                print('File is saved successfully.')
        else:
            print('A file with the same name already exists.')
            return
    except FileNotFoundError as err:
        print(err)
    except ValueError as err:
        print(err)
