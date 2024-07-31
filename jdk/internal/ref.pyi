from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Runnable, Thread
from java.lang.ref import PhantomReference, Cleaner
from java.util.concurrent import ThreadFactory
from java.util.function import Function

T = TypeVar('T', default=Any)

class Cleaner(PhantomReference):

  def clean(self) -> None: ...

  @staticmethod
  def create(arg0: object, arg1: Runnable) -> Cleaner: ...


class CleanerFactory:

  @staticmethod
  def cleaner() -> Cleaner: ...

  def __init__(self): ...


class CleanerImpl:

  @overload
  def run(self) -> None: ...

  @overload
  def run(self) -> None: ...

  def start(self, arg0: Cleaner, arg1: ThreadFactory) -> None: ...

  @staticmethod
  def setCleanerImplAccess(arg0: Function[Cleaner, CleanerImpl]) -> None: ...

  def __init__(self): ...

  class PhantomCleanableRef(PhantomCleanable):

    def clear(self) -> None: ...

    def get(self) -> object: ...

    def __init__(self, arg0: object, arg1: Cleaner, arg2: Runnable): ...

  class CleanerCleanable(PhantomCleanable): ...

  class InnocuousThreadFactory:

    @overload
    def newThread(self, arg0: Runnable) -> Thread: ...

    @overload
    def newThread(self, arg0: Runnable) -> Thread: ...


class PhantomCleanable[T](PhantomReference):

  @overload
  def clean(self) -> None: ...

  @overload
  def clean(self) -> None: ...

  def clear(self) -> None: ...

  def enqueue(self) -> bool: ...

  def isEnqueued(self) -> bool: ...

  def __init__(self, arg0: object, arg1: Cleaner): ...

