from task_planner_main_func import print_cli
from task_planner_main_func import select_function
from task_planner_main_func import execute_func_0
from task_planner_main_func import review_tasks_list
from task_planner_main_func import review_task_detail
from task_planner_main_func import edit_task
from task_planner_main_func import delete_task
from task_planner_main_func import find_by_name
from task_planner_main_func import sort_by_priority
from task_planner_main_func import find_overdue_task

from task_planner_ad_func import get_id_for_edit
from task_planner_ad_func import get_id
from task_planner_ad_func import get_title
from task_planner_ad_func import get_description
from task_planner_ad_func import get_priority
from task_planner_ad_func import get_due_date

lst_command_line = ['Command Line Interface', 'Finish work', 'Create new task', 'Review list of tasks',
                    'Review detail of task', 'Edit a task', 'Delete a task', 'Find by name', 'Sort by priority',
                    'Find overdue task'
                    ]

lst_tasks = []
while True:
    print_cli(lst_command_line)
    number_function = select_function()
    if number_function == 0:
        execute_func_0()
        break
    if number_function == 1:
        lst_keys = ['id', 'title', 'description', 'priority', 'status', 'due_date']
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
            print('List of tasks is empty.')
            continue
        sorted_task_list = review_tasks_list(lst_tasks)
        for elem in sorted_task_list:
            print({'id': elem['id']}, {'title': elem['title']}, {'status': elem['status']})
    if number_function == 3:
        if len(lst_tasks) == 0:
            print('List of tasks is empty.')
            continue
        task_by_id = review_task_detail(lst_tasks)
        print(task_by_id)
    if number_function == 4:
        edit_item = get_id_for_edit(lst_tasks)
        if edit_item is None:
            continue
        edit_task(edit_item)
    if number_function == 5:
        delete_task(lst_tasks)
    if number_function == 6:
        search_task = find_by_name(lst_tasks)
        print(search_task)
    if number_function == 7:
        sorted_by_priority = sort_by_priority(lst_tasks)
        for elem in sorted_by_priority:
            print({elem['id']}, {elem['title']}, {elem['status']}, {elem['priority']})
    if number_function == 8:
        sorted_lst = find_overdue_task(lst_tasks)
        for item in sorted_lst:
            print({'id': item['id']}, {'item': item['title']}, {'status': item['status']},
                  {'item': item['due_date'].strftime('%d.%m.%Y')})
