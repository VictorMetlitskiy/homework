import json
import os.path

from task_planner_main_func1 import print_cli
from task_planner_main_func1 import select_function
from task_planner_main_func1 import execute_func_0
from task_planner_main_func1 import review_tasks_list
from task_planner_main_func1 import review_task_detail
from task_planner_main_func1 import edit_task
from task_planner_main_func1 import delete_task
from task_planner_main_func1 import find_by_name
from task_planner_main_func1 import sort_by_priority
from task_planner_main_func1 import find_overdue_task
from task_planner_main_func1 import save_cur_tasks

from task_planner_ad_func1 import get_id_for_edit
from task_planner_ad_func1 import get_id
from task_planner_ad_func1 import get_title
from task_planner_ad_func1 import get_description
from task_planner_ad_func1 import get_priority
from task_planner_ad_func1 import get_due_date
from task_planner_ad_func1 import change_date_to_str
from task_planner_ad_func1 import change_str_to_date

lst_command_line = ['Command Line Interface', 'Finish work', 'Create new task', 'Review list of tasks',
                    'Review detail of task', 'Edit a task', 'Delete a task', 'Find by name', 'Sort by priority',
                    'Find overdue task', 'Save the current tasks'
                    ]

lst_tasks = []
lst_keys = ['id', 'title', 'description', 'priority', 'status', 'due_date']
if os.path.exists('./data/lst_tasks.json'):
    with open('./data/lst_tasks.json') as file_object:
        lst_tasks = json.load(file_object)
        lst_tasks = change_str_to_date(lst_tasks)
while True:
    print_cli(lst_command_line)
    number_function = select_function()
    if number_function == 0:
        lst_tasks = change_date_to_str(lst_tasks)
        with open('./data/lst_tasks.json', 'w') as file_object:
            json.dump(lst_tasks, file_object)
        execute_func_0()
        break
    if number_function == 1:
        task_id = get_id(lst_tasks)
        task_title = get_title()
        task_description = get_description()
        task_priority = get_priority()
        task_status = 'pending'
        task_due_date = get_due_date()
        lst_values = [task_id, task_title, task_description, task_priority, task_status, task_due_date]
        dict_task = {lst_keys[i]: lst_values[i] for i in range(len(lst_keys))}
        lst_tasks.append(dict_task)
        print('Task has been created successfully.')
    if number_function == 2:
        if len(lst_tasks) == 0:
            print('List of the tasks is empty.')
            continue
        sorted_task_list = review_tasks_list(lst_tasks)
        for elem in sorted_task_list:
            print({'id': elem['id']}, {'title': elem['title']}, {'status': elem['status']})
    if number_function == 3:
        if len(lst_tasks) == 0:
            print('List of the tasks is empty.')
            continue
        task_by_id = review_task_detail(lst_tasks)
        print(task_by_id)
    if number_function == 4:
        if len(lst_tasks) == 0:
            print('List of the tasks is empty.')
            continue
        edit_item = get_id_for_edit(lst_tasks)
        if edit_item is None:
            continue
        edit_task(edit_item)
    if number_function == 5:
        if len(lst_tasks) == 0:
            print('List of the tasks is empty.')
            continue
        delete_task(lst_tasks)
    if number_function == 6:
        if len(lst_tasks) == 0:
            print('List of the tasks is empty.')
            continue
        find_by_name(lst_tasks)
    if number_function == 7:
        if len(lst_tasks) == 0:
            print('List of the tasks is empty.')
            continue
        sorted_by_priority = sort_by_priority(lst_tasks)
        for elem in sorted_by_priority:
            print({'id': elem['id']}, {'title': elem['title']}, {'status': elem['status']},
                  {'priority': elem['priority']})
    if number_function == 8:
        if len(lst_tasks) == 0:
            print('List of the tasks is empty.')
            continue
        sorted_lst = find_overdue_task(lst_tasks)
        for item in sorted_lst:
            print({'id': item['id']}, {'item': item['title']}, {'status': item['status']},
                  {'item': item['due_date'].strftime('%d.%m.%Y')})
    if number_function == 9:
        save_cur_tasks(lst_tasks, lst_keys)
