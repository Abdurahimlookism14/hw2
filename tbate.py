
class Computer:
    def init(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f"Выполняются вычисления с параметрами: CPU = {self.cpu}, Память = {self.memory}."

    def str(self):
        return f"Компьютер: CPU = {self.cpu}, Память = {self.memory}."

    def eq(self, other):
        return self.__memory == other.memory

    def ne(self, other):
        return self.__memory != other.memory

    def lt(self, other):
        return self.__memory < other.memory

    def le(self, other):
        return self.__memory <= other.memory

    def gt(self, other):
        return self.__memory > other.memory

    def ge(self, other):
        return self.__memory >= other.memory


class Phone:
    def init(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list


    @property
    def sim_cards_list(self):
        return self.__sim_cards_list


    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        print(f"Идет звонок на номер {call_to_number} с SIM-карты-{sim_card_number} - {sim_card}.")

    def str(self):
        return f"Телефон с SIM-картами: {', '.join(self.__sim_cards_list)}."


class SmartPhone(Computer, Phone):
    def init(self, cpu, memory, sim_cards_list):
        Computer.init(self, cpu, memory)
        Phone.init(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Строится маршрут до локации {location}.")

    def str(self):
        return f"Смартфон: CPU = {self.cpu}, Память = {self.memory}, SIM-карты: {', '.join(self.sim_cards_list)}."


computer = Computer("Intel i7", "16GB")
phone = Phone(["Beeline", "MegaCom"])
smartphone1 = SmartPhone("Snapdragon 888", "8GB", ["Beeline", "MegaCom"])
smartphone2 = SmartPhone("Apple A14", "4GB", ["O!", "Beeline"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print(computer.make_computations())
phone.call(1, "+99600343039")
smartphone1.use_gps("Бишкек, площадь Ала-Тоо")

print(smartphone1 > smartphone2)
































