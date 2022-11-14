import re

class Worker:

    def __init__(self, first_name, last_name, post):
        self.first_name = first_name
        self.last_name = last_name
        self.post = post

class FreeTime(Worker):

    def __init__(self, work_time, worker):
        self.first_name = worker.first_name
        self.last_name = worker.last_name
        self.work_time = [work_time]
        self.free_time = {"monday": self.work_time,
                          "tuesday": self.work_time,
                          "wednesday":self.work_time,
                          "thursday": self.work_time,
                          "friday": self.work_time
        }

    def get_work_time(self):
        work_time = {}
        key = self.last_name + ' ' + self.first_name
        work_time[key] = self.work_time
        return work_time

    def get_free_time(self):
        free_time = {}
        key = self.last_name + ' ' + self.first_name
        free_time[key] = self.free_time
        return free_time

    @staticmethod
    def _search_slot(work_time, time):
        time = (re.split("-|:|\n", time))
        if int(time[0]) > 24 or int(time[0]) < 0:
            # Аналогичные проверки времени
            print('Введенное время не верное')
            return
        for slot in work_time:
            slot_sp = (re.split("-|:|\n", slot))
            if int(time[0]) >= int(slot_sp[0]) and int(time[1]) >= int(slot_sp[1]):
                if int(time[2]) == int(slot_sp[2]) and int(time[3]) <= int(slot_sp[3]):
                    return slot
                elif int(time[2]) < int(slot_sp[2]):
                    return slot
        print('Сотрудник занят в это время')
        return None



    def take_a_slot_free_time(self):
        day = input('Введите день недели monday, tuesday... : ')
        print('Свободное время в этот день: ', self.free_time[day])
        time = input('Введите интверва времени по типу 13:15-16:45: ')
        slot = self._search_slot(self.free_time[day], time)
        if slot != None:
            time = (re.split("-|:|\n", time))
            slot_sp = (re.split("-|:|\n", slot))

            if int(time[0]) == int(slot_sp[0]) and int(time[1]) == int(slot_sp[1]):

                if int(time[2]) == int(slot_sp[2]) and int(time[3]) == int(slot_sp[3]):
                    self.free_time[day].remove(slot)
                    return self.free_time[day]
                else:
                    i = self.free_time[day].index(slot)
                    new_slot = time[2] + ':' + time[3] + '-' + slot_sp[2] + ':' + slot_sp[3]
                    self.free_time[day].remove(slot)
                    self.free_time[day].insert(i, new_slot)
                    return self.free_time[day]

            elif int(time[2]) == int(slot_sp[2]) and int(time[3]) == int(slot_sp[3]):
                i = self.free_time[day].index(slot)
                new_slot = slot_sp[0] + ':' + slot_sp[1] + '-' + time[0] + ':' + time[1]
                self.free_time[day].remove(slot)
                self.free_time[day].insert(i, new_slot)
                return self.free_time[day]

            else:
                i = self.free_time[day].index(slot)
                free_time = self.free_time[day][:i]
                free_time_2 = self.free_time[day][i:]
                free_time_2.remove(slot)
                new_slot = slot_sp[0] + ':' + slot_sp[1] + '-' + time[0] + ':' + time[1]
                free_time.append(new_slot)
                new_slot_2 = time[2] + ':' + time[3] + '-' + slot_sp[2] + ':' + slot_sp[3]
                free_time.append(new_slot_2)
                self.free_time[day] = free_time + free_time_2
                return self.free_time[day]







