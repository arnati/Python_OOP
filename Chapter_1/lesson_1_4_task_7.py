class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = []
        if len(mem_slots) <= self.total_mem_slots:
            self.mem_slots = mem_slots

    def get_config(self):
        m = ''
        for i in range(len(self.mem_slots)):
            if i == len(self.mem_slots) - 1:
                m += f"{self.mem_slots[i].name} - {self.mem_slots[i].volume}"
            else:
                m += f"{self.mem_slots[i].name} - {self.mem_slots[i].volume}; "

        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {m}']


cpu = CPU('asus', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, [mem1, mem2])

# print(mb.get_config())
# for i in mb.get_config():
#     print(i)
