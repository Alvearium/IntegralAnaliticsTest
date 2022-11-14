from FreeTime import Worker, FreeTime

def total_time_workers(workers):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    print(days)
    day = int(input('Выберите день недели 1,2,3,4,5: ')) - 1
    try:
        total_free_time = list()
        for worker in workers:
            total_free_time += worker.free_time[days[day]]

        counter = {}
        for elem in total_free_time:
            counter[elem] = counter.get(elem, 0) + 1

        doubles = {element: count for element, count in counter.items() if count > 1}
        print(doubles)
    except:
        print('Скорее всего вы ошиблись при вводе, попробуйте еще раз')


if __name__ == '__main__':
    lst = list()
    worker_1 = Worker('Иван', 'Иванов', 'Программист')
    worker_2 = Worker('Петр', 'Петров', 'Cис.Админ')
    worker_3 = Worker('Роман', 'Романов', 'Дизайнер')

    lst.append(FreeTime('9:00-16:00', worker_1))
    lst.append(FreeTime('9:00-18:00', worker_2))
    lst.append(FreeTime('9:00-16:00', worker_3))

    # Нахождение общих слотов
    total_time_workers(lst)

    # Получение рабочего времени первого сотрудника:
    print(lst[0].get_work_time())

    # Получение свободных слотов времени второго сотрудника:
    print(lst[1].get_free_time())

    # Забить слот времени у третьего сотрудника
    print(lst[2].take_a_slot_free_time())
