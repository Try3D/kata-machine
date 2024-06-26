from typing import TypeVar, Generic, Union

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Union[Node[T], None] = None
        self.prev: Union[Node[T], None] = None


class Queue(Generic[T]):
    def __init__(self):
        ...

    def enqueue(self, value: T) -> None:
        ...

    def dequeue(self) -> Union[T, None]:
        ...

    def peek(self) -> Union[T, None]:
        ...

    def is_empty(self) -> bool:
        ...
