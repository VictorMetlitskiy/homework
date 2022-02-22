from datetime import datetime



def get_id(lst):
    """Function defines id of task.
    """
    id_task = 1
    while True:
        lst_values = [elem['id'] for elem in lst]
        if id_task not in lst_values:
            return id_task
        else:
            id_task += 1


def get_title():
    """Function defines title of task.
    """
    while True:
        try:
            title = input('Type name of the task: ')
            if 0 < len(title) <= 60:
                return title
            else:
                raise ValueError('Invalid value. Type name of task (obligatory field, up to 60 characters).')
        except ValueError as err:
            print(err)


def get_description():
    """Function define a description of task.
    """
    description = input('Type description of the task (optional field): ')
    return description


def get_priority():
    """Function sorts of tasks by key priority.
    """
    while True:
        try:
            priority_default = 1
            priority = input('Type priority of the task (from 1 to 10): ')
            if 2 <= int(priority) <= 10:
                return int(priority)
            elif len(priority) == 0 or int(priority) == 1:
                return priority_default
            else:
                raise ValueError('Invalid value. Type number in digit form (from 1 to 10)')
        except ValueError as err:
            print(err)


def get_due_date():
    """Function defines a deadline for completing a task.
    """
    while True:
        try:
            due_date = input('Type the end date of the task in format DD.MM.YYYY: ')
            date_object = datetime.strptime(due_date, '%d.%m.%Y').date()
            return date_object
        except ValueError as err:
            print(err, 'Format date must be DD.MM.YYYY')


def get_id_for_edit(lst):
    """Function defines id of editing task.
    """
    try:
        get_id_edit = int(input('Type id of task for editing: '))
        for i in range(len(lst)):
            if lst[i]['id'] == get_id_edit:
                return lst[i]
        else:
            raise KeyError('Key is invalid')
    except ValueError as err:
        print(err)
    except KeyError as err:
        print(err)


def get_edit_title(elem):
    """Function defines title of editing task.
    """
    try:
        new_title = input('Type new name of the task: ')
        if len(new_title) == 0:
            return elem
        elif 0 < len(new_title) <= 60 and new_title != elem['title']:
            elem['title'] = new_title
            return elem
        else:
            raise ValueError('Invalid value. Type name of task (obligatory field, up to 60 characters).')
    except ValueError as err:
        print(err)


def get_edit_description(elem):
    """Function defines description of editing task.
    """
    new_description = input('Type new description of the task (optional field): ')
    if len(new_description) == 0:
        return elem
    elif len(new_description) > 0 and new_description != elem['description']:
        elem['description'] = new_description
        return elem


def get_edit_priority(elem):
    """Function defines priority of editing task.
    """
    try:
        new_priority = input('Type new priority of the task (from 1 to 10): ')
        if len(new_priority) == 0:
            return elem
        elif 1 <= int(new_priority) <= 10 and int(new_priority) != elem['priority']:
            elem['priority'] = new_priority
            return elem
        else:
            raise ValueError('Invalid value. Characters must be number from 1 to 10.')
    except ValueError as err:
        print(err)


def get_edit_status(elem):
    """Function defines status of editing task.
    """
    try:
        new_status = input('Type new status of the task (in progress or done): ')
        if len(new_status) == 0:
            return elem
        elif new_status == 'in progress' or new_status == 'done':
            elem['status'] = new_status
            return elem
        else:
            raise ValueError("Value error. New meaning of status 'in progress' or 'done'.")
    except ValueError as err:
        print(err)


def get_edit_due_date(elem):
    """Function defines a deadline for completing a task, that is being edited.
    """
    try:
        new_due_date = input('Type the new end date of the task in format DD.MM.YYYY: ')
        if len(new_due_date) == 0:
            return elem
        date_object = datetime.strptime(new_due_date, '%d.%m.%Y').date()
        if date_object != elem['due_date']:
            elem['due_date'] = date_object
            return elem
    except ValueError as err:
        print(err, 'Format date must be DD.MM.YYYY')


def change_str_to_date(lst):
    """Function changes date type to str type.
    """
    for elem in lst:
        elem['due_date'] = datetime.strptime(elem['due_date'], '%d.%m.%Y').date()
    return lst


def change_date_to_str(lst):
    """Function changes date type to str type.
    """
    for elem in lst:
        elem['due_date'] = elem['due_date'].strftime('%d.%m.%Y')
    return lst
