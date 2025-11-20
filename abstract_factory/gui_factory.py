from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

class WindowsButton(Button):
    def click(self):
        return "Windows button clicked"

class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows checkbox checked"

class MacButton(Button):
    def click(self):
        return "Mac button clicked"

class MacCheckbox(Checkbox):
    def check(self):
        return "Mac checkbox checked"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def use_ui(self):
        return f"{self.button.click()}, {self.checkbox.check()}"

def test_abstract_factory():

    windows_factory = WindowsFactory()
    windows_app = Application(windows_factory)
    windows_app.create_ui()
    print(f"Windows UI: {windows_app.use_ui()}")

    mac_factory = MacFactory()
    mac_app = Application(mac_factory)
    mac_app.create_ui()
    print(f"Mac UI: {mac_app.use_ui()}")
    print()