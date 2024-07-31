from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Thread
from jdk.internal.ref import Cleaner

class DirectBuffer:

  def address(self) -> int: ...

  def attachment(self) -> object: ...

  def cleaner(self) -> Cleaner: ...


class Interruptible:

  def interrupt(self, arg0: Thread) -> None: ...

