from abc import ABC, abstractmethod

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"Computer: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, GPU={self.gpu}"

class ComputerBuilder(ABC):
    def __init__(self):
        self.computer = Computer()

    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    @abstractmethod
    def build_gpu(self):
        pass

    def get_computer(self):
        return self.computer

class GamingComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel i9"

    def build_ram(self):
        self.computer.ram = "32GB DDR4"

    def build_storage(self):
        self.computer.storage = "1TB SSD + 2TB HDD"

    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4080"


class OfficeComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel i5"

    def build_ram(self):
        self.computer.ram = "16GB DDR4"

    def build_storage(self):
        self.computer.storage = "512GB SSD"

    def build_gpu(self):
        self.computer.gpu = "Integrated Graphics"

class ComputerEngineer:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_computer(self):
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_gpu()

    def get_computer(self):
        return self.builder.get_computer()

def test_builder():

    gaming_builder = GamingComputerBuilder()
    engineer = ComputerEngineer(gaming_builder)
    engineer.build_computer()
    gaming_computer = engineer.get_computer()
    print(f"Gaming Computer: {gaming_computer}")

    office_builder = OfficeComputerBuilder()
    engineer = ComputerEngineer(office_builder)
    engineer.build_computer()
    office_computer = engineer.get_computer()
    print(f"Office Computer: {office_computer}")
    print()