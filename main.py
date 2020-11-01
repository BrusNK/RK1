class Driver:
    #Водитель
    def __init__(self, id, nameD, salary, carPark_id):
        self.id = id
        self.nameD = nameD
        self.salary = salary
        self.carPark_id = carPark_id


class CarPark:
    #Автопарк
    def __init__(self, id, nameCP):
        self.id = id
        self.nameCP = nameCP


class DriverToCarPark:
    #Водители автопарков
    #для реализации связи многие-ко-многим
    def __init__(self, CP_id, Dr_id):
        self.CP_id = CP_id
        self.Dr_id = Dr_id


#Водители
driver = [
    Driver(1, 'Иванов И.И.', 22000, 1),
    Driver(2, 'Александров И.В.', 25000, 1),
    Driver(3, 'Кеглин А.К.', 26000, 2),
    Driver(4, 'Алехин Т.А.', 15000, 2),
    Driver(5, 'Грибников В.В.', 18000, 1),
    Driver(6, 'Борисов К.Ю.', 21000, 3),
    Driver(7, 'Картошкин С.Б.', 19000, 3),
    Driver(8, 'Кирин В.А.', 23000, 30),
]

#Автопарки
carparks = [
    CarPark(1, '10-ый Автопарк г. Москва'),
    CarPark(2, '1-ый Автопарк г. Красногорск'),
    CarPark(3, '5-ый Автопарк г. Москва'),
    CarPark(10, 'Таксопарк №1'),
    CarPark(20, 'ООО Грузоперевозки'),
    CarPark(30, 'ОАО Автомобилькин'),
]

drive_carpsrk = [
    DriverToCarPark(1, 1),
    DriverToCarPark(1, 2),
    DriverToCarPark(2, 3),
    DriverToCarPark(2, 4),
    DriverToCarPark(2, 5),
    DriverToCarPark(3, 6),
    DriverToCarPark(3, 7),
    DriverToCarPark(3, 8),
    DriverToCarPark(30, 1),
    DriverToCarPark(30, 2),
    DriverToCarPark(30, 3),
    DriverToCarPark(20, 4),
    DriverToCarPark(20, 5),
    DriverToCarPark(20, 6),
    DriverToCarPark(10, 7),
    DriverToCarPark(10, 8),
]


def main():
    #Реализация связи один-ко-многим
    one_to_many =[(d.carPark_id, d.nameD, d.salary, c.nameCP)
                    for c in carparks
                    for d in driver if d.carPark_id == c.id]
    #Решение задания А1
    #Выберем те автопарки, у которых в названии есть "Автопарк" и выведем их наименование
    #и наименование работающих в них водителей
    print('\nЗадание А1\n')
    res_1 = ''
    for i in one_to_many:
        if "Автопарк" in i[3]:
            res_1 = res_1 + str(i[3]) + ', в котором работает водитель: ' + str(i[1]) + '\n'
    print(res_1)

    #Решение задания А2
    #Выберем для каждого водителя средний размер заработной платы
    print("\nЗадание А2:\n")
    dr_CP_all = list()
    for c in carparks:
        #Выберем всех водителей, работающих в текущем автопарке
        driveList = list(filter(lambda x: c.id == x[0], one_to_many))
        sal_dr = 0
        if len(driveList) > 0:
            #Рассматривая каждый элемент списка всех водителей автопарка
            for item in driveList:
                Dsal = item[2]
                sal_dr = sal_dr + Dsal
            #Находим среднее значение зароботной платы
            sal_dr = round(sal_dr / len(driveList), 2)
            #Добавляем найденное среднее значение в список для вывода данных
            dr_CP_all.append((c.nameCP, sal_dr))
    for item in sorted(dr_CP_all, key=lambda x: x[1]):
        print("Для автопарка: {0}, в среднем размер заработной платы водителей равен {1} у. е.".format(item[0], item[1]))



    #Реализация связи многие-ко-многим
    many_to_many_temp = [(c.nameCP, dcp.CP_id, dcp.Dr_id)
                            for c in carparks
                            for dcp in drive_carpsrk
                            if c.id == dcp.CP_id]
    many_to_many = [(d.nameD, d.salary, nameCarP)
                         for nameCarP, CarPId, DriverId in many_to_many_temp
                         for d in driver
                         if d.id == DriverId]


    #Решение задания А3:
    #Выберем данные из составленных связей многие-ко-многим, рассмотрим тех водителей,
    #фамилии которых начинается с буквы "К" и названия автопарков
    print("\nЗадание А3:\n")
    res_3 = ''
    for i in many_to_many:
        str3 = i[0]
        for k in range(len(str3)):
            if k == 0 and str3[k] == 'К':
                res_3 = res_3 + 'Водитель ' + str3 + ', работающий в автопарке: ' + str(i[2]) + '\n'
                break
            else:
                break
    print(res_3)


if __name__ == '__main__':
    main()