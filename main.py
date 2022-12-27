from subprocess import run
import datetime

log_txt = f"{datetime.datetime.now().strftime('%d-%m-%Y-%H:%M')}-scan.txt"

result = run("ps aux", shell=True, capture_output=True).stdout.decode('utf-8').rstrip()

res_list = result.split("\n")

all_process = len(res_list) - 1
users = []
users_dict = {}
n = 1
cpu = 0
mem = 0
max_cpu = 0
max_mem = 0
max_cpu_list = [0, 0]
max_mem_list = [0, 0]
for i in res_list[1:]:
    res_list_2 = i.split()
    if res_list_2[0] in users_dict.keys():
        users_dict[res_list_2[0]] += 1
    else:
        max_cpu_list[0] = res_list_2[10]
        max_mem_list[0] = res_list_2[10]
        users_dict[res_list_2[0]] = 1
    if max_cpu < float(res_list_2[2]):
        max_cpu = float(res_list_2[2])
        max_cpu_list[0] = res_list_2[10]
        max_cpu_list[1] = max_cpu
    if max_mem < float(res_list_2[3]):
        max_mem = float(res_list_2[3])
        max_mem_list[0] = res_list_2[10]
        max_mem_list[1] = max_mem
    cpu += float(res_list_2[2])
    mem += float(res_list_2[3])
users_str = ', '.join(i for i in users_dict.keys())

users_system = f'Пользователи системы: {users_str}'
processes_started = f'Процессов запущено: {all_process}'
total_memory_used = f'Всего памяти используется: = {str(mem)[:5]}%'
total_cpu_used = f'Всего CPU используется: = {str(cpu)[:5]}%'
most_cpu_used = f'Больше всего CPU использует: = {max_cpu_list[0][:20]}'
most_memory_used = f'Больше всего памяти использует: = {max_mem_list[0][:20]}'
print("Отчёт о состоянии системы:")
print(users_system)
print(processes_started)
print("Пользовательских процессов:")
for key in users_dict:
    print(f"{key}: {users_dict[key]}")
print(total_memory_used)
print(total_cpu_used)
print(most_cpu_used)
print(most_memory_used)

with open(log_txt, 'w') as f:
    f.write("Отчёт о состоянии системы:" + '\n')
    f.write(users_system + '\n')
    f.write(processes_started + '\n')
    f.write("Пользовательских процессов:" + '\n')
    for key in users_dict:
        f.write(f"{key}: {users_dict[key]}" + '\n')
    f.write(total_memory_used + '\n')
    f.write(total_cpu_used + '\n')
    f.write(most_cpu_used + '\n')
    f.write(most_memory_used + '\n')
