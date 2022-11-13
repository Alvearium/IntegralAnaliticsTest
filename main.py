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
    workers = list()
    for i in range(1):
        work_time = input('Рабочее время ')
        worker = FreeTime(work_time)
        worker.last_name = input('Имя: ')
        worker.first_name = input('Фамилия: ')
        workers.append(worker)

    #total_time_workers(workers)

    while True:
        workers[0].take_a_slot_free_time()
        print(worker.free_time)