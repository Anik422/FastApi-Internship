from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return 5


print(say_hello("John Doe"))