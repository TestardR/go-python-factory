from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class AK47Creator(Creator):
    def factory_method(self) -> Gun:
        return AK47()


class MusketCreator(Creator):
    def factory_method(self) -> Gun:
        return Musket()


class Gun(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class AK47(Gun):
    def operation(self) -> str:
        return "{Result of AK47}"


class Musket(Gun):
    def operation(self) -> str:
        return "{Result of Musket}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with AK47Creator.")
    client_code(AK47Creator())
    print("\n")

    print("App: Launched with the MusketCreator.")
    client_code(MusketCreator())
