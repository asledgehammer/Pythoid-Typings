from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Runnable, Thread
from java.util.concurrent import ThreadFactory

T = TypeVar('T', default=Any)

class Cleaner:

  def register(self, arg0: object, arg1: Runnable) -> Cleaner.Cleanable: ...

  @staticmethod
  @overload
  def create() -> Cleaner: ...

  @staticmethod
  @overload
  def create(arg0: ThreadFactory) -> Cleaner: ...

  class Cleanable:

    def clean(self) -> None: ...


class FinalReference[T](Reference):

  def clear(self) -> None: ...

  def enqueue(self) -> bool: ...

  def get(self) -> object: ...

  def __init__(self, arg0: object, arg1: ReferenceQueue[T]): ...


class Finalizer(FinalReference):

  class FinalizerThread(Thread):

    def run(self) -> None: ...


class PhantomReference[T](Reference):

  def get(self) -> object: ...

  def __init__(self, arg0: object, arg1: ReferenceQueue[T]): ...


class Reference[T]:

  def clear(self) -> None: ...

  def enqueue(self) -> bool: ...

  def get(self) -> object: ...

  def isEnqueued(self) -> bool: ...

  def refersTo(self, arg0: object) -> bool: ...

  @staticmethod
  def reachabilityFence(arg0: object) -> None: ...

  class ReferenceHandler(Thread):

    def run(self) -> None: ...


class ReferenceQueue[T]:

  def poll(self) -> Reference[T]: ...

  @overload
  def remove(self) -> Reference[T]: ...

  @overload
  def remove(self, arg0: int) -> Reference[T]: ...

  def __init__(self): ...

  class Lock: ...

  class Null(ReferenceQueue): ...


class SoftReference[T](Reference):

  def get(self) -> object: ...

  @overload
  def __init__(self, arg0: object): ...
  @overload
  def __init__(self, arg0: object, arg1: ReferenceQueue[T]): ...


class WeakReference[T](Reference):

  @overload
  def __init__(self, arg0: object): ...
  @overload
  def __init__(self, arg0: object, arg1: ReferenceQueue[T]): ...

