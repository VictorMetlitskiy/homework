from datetime import datetime

from task_planner_ad_func import get_edit_title
from task_planner_ad_func import get_edit_description
from task_planner_ad_func import get_edit_priority
from task_planner_ad_func import get_edit_status
from task_planner_ad_func import get_edit_due_date


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
            function_answer = int(input('Type number of desirable function (from 0 to 8): '))
            if 0 <= function_answer <= 8:
                return function_answer
            else:
                raise ValueError('Invalid value. Type number in digit form (from 1 to 8).')
        except ValueError as err:
            print(err)


def execute_func_0():
    """Function interrupts executing program.
    """
    print('Work is finished.')


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
