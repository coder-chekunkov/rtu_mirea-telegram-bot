import datetime


# Данный скрипт используется для создания логов с действиями пользователей.

# Создание лога (действия пользователя):
def make_log(message, action):
    now_date = datetime.datetime.now()
    time = f"[{now_date.day}.{now_date.month}.{now_date.year}][" \
           f"{now_date.hour}:{now_date.minute}:{now_date.second}] "

    user_id = "USER-ID: " + str(message.from_user.id) + "; "
    user_username = "USERNAME: " + message.from_user.username + "; "

    if message.from_user.first_name is not None:
        user_first_name = "NAME: " + message.from_user.first_name + "; "
    else:
        user_first_name = "NAME: null "

    if message.from_user.last_name is not None:
        user_last_name = "LASTNAME: " + message.from_user.last_name + "; "
    else:
        user_last_name = "LASTNAME: null "

    action = "ACTION: " + action + "; "
    log = time + user_id + user_username + user_first_name + user_last_name \
          + action

    write_logs_file(log)


# Создание лога (действия бота):
def make_log_bot(action):
    now_date = datetime.datetime.now()
    time = f"[{now_date.day}.{now_date.month}.{now_date.year}][" \
           f"{now_date.hour}:{now_date.minute}:{now_date.second}] "
    action = "ACTION: " + action + "; "
    log = time + "[---LOG---] " + action

    write_logs_file(log)


# Запись лога в файл:
def write_logs_file(log):
    log_file = open("log_worker/logs.txt", "a", encoding="utf-8")
    log_file.write(log + "\n")
    log_file.close()
