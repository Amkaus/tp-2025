from singleton.database_singleton import test_singleton
from factory_method.logistics_factory import test_factory_method
from abstract_factory.gui_factory import test_abstract_factory
from builder.computer_builder import test_builder


def main():
    test_singleton()
    test_factory_method()
    test_abstract_factory()
    test_builder()

if __name__ == "__main__":
    main()