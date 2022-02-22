from task_planner_main_func import *

lst_command_line = ['Command Line Interface', 'Finish work', 'Create new task', 'Review list of tasks',
                    'Review detail of task', 'Edit a task', 'Delete a task', 'Find by name', 'Sort by priority',
                    'Find overdue task', 'Save the current tasks'
                    ]

lst_keys = ['id', 'title', 'description', 'priority', 'status', 'due_date']
lst_tasks = read_file()

while True:
    print_cli(lst_command_line)
    number_function = select_function()
    if number_function == 0:
        execute_func_0(lst_tasks)
        break
    if number_function == 1:
        dict_task = create_task(lst_tasks, lst_keys)
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
        edit_task(lst_tasks)
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
