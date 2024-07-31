from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Runnable
from java.util import Comparator
from java.util.function import Function, ToDoubleFunction, ToIntFunction, ToLongFunction, Consumer, Predicate
from zombie.util import PooledObject

E = TypeVar('E', default=Any)
T1 = TypeVar('T1', default=Any)
T2 = TypeVar('T2', default=Any)
U = TypeVar('U', default=Any)
T = TypeVar('T', default=Any)
T3 = TypeVar('T3', default=Any)
T4 = TypeVar('T4', default=Any)
T5 = TypeVar('T5', default=Any)
T6 = TypeVar('T6', default=Any)

class Comparators:

  def __init__(self): ...

  class Params2:

    def __init__(self): ...

    class CallbackStackItem[E, T1, T2](Comparators.Params2.StackItem):

      @overload
      def compare(self, arg0: object, arg1: object) -> int: ...

      @overload
      def compare(self, arg0: object, arg1: object) -> int: ...

      def equals(self, arg0: object) -> bool: ...

      def onReleased(self) -> None: ...

      def reversed(self) -> Comparator[T]: ...

      @overload
      def thenComparing(self, arg0: Comparator[T]) -> Comparator[T]: ...

      @overload
      def thenComparing(self, arg0: Function[T, U]) -> Comparator[T]: ...

      @overload
      def thenComparing(self, arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

      def thenComparingDouble(self, arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

      def thenComparingInt(self, arg0: ToIntFunction[T]) -> Comparator[T]: ...

      def thenComparingLong(self, arg0: ToLongFunction[T]) -> Comparator[T]: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: Comparators.Params2.ICallback) -> Comparators.Params2.CallbackStackItem: ...

      @staticmethod
      @overload
      def comparing(arg0: Function[T, U]) -> Comparator[T]: ...

      @staticmethod
      @overload
      def comparing(arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

      @staticmethod
      def comparingDouble(arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

      @staticmethod
      def comparingInt(arg0: ToIntFunction[T]) -> Comparator[T]: ...

      @staticmethod
      def comparingLong(arg0: ToLongFunction[T]) -> Comparator[T]: ...

      @staticmethod
      def naturalOrder() -> Comparator[T]: ...

      @staticmethod
      def nullsFirst(arg0: Comparator[T]) -> Comparator[T]: ...

      @staticmethod
      def nullsLast(arg0: Comparator[T]) -> Comparator[T]: ...

      @staticmethod
      def reverseOrder() -> Comparator[T]: ...

      def __init__(self): ...

    class StackItem[T1, T2](PooledObject): ...

    class ICallback[E, T1, T2]:

      def compare(self, arg0: object, arg1: object, arg2: object, arg3: object) -> int: ...

  class Params1:

    def __init__(self): ...

    class CallbackStackItem[E, T1](Comparators.Params1.StackItem):

      @overload
      def compare(self, arg0: object, arg1: object) -> int: ...

      @overload
      def compare(self, arg0: object, arg1: object) -> int: ...

      def equals(self, arg0: object) -> bool: ...

      def onReleased(self) -> None: ...

      def reversed(self) -> Comparator[T]: ...

      @overload
      def thenComparing(self, arg0: Comparator[T]) -> Comparator[T]: ...

      @overload
      def thenComparing(self, arg0: Function[T, U]) -> Comparator[T]: ...

      @overload
      def thenComparing(self, arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

      def thenComparingDouble(self, arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

      def thenComparingInt(self, arg0: ToIntFunction[T]) -> Comparator[T]: ...

      def thenComparingLong(self, arg0: ToLongFunction[T]) -> Comparator[T]: ...

      @staticmethod
      def alloc(arg0: object, arg1: Comparators.Params1.ICallback) -> Comparators.Params1.CallbackStackItem: ...

      @staticmethod
      @overload
      def comparing(arg0: Function[T, U]) -> Comparator[T]: ...

      @staticmethod
      @overload
      def comparing(arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

      @staticmethod
      def comparingDouble(arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

      @staticmethod
      def comparingInt(arg0: ToIntFunction[T]) -> Comparator[T]: ...

      @staticmethod
      def comparingLong(arg0: ToLongFunction[T]) -> Comparator[T]: ...

      @staticmethod
      def naturalOrder() -> Comparator[T]: ...

      @staticmethod
      def nullsFirst(arg0: Comparator[T]) -> Comparator[T]: ...

      @staticmethod
      def nullsLast(arg0: Comparator[T]) -> Comparator[T]: ...

      @staticmethod
      def reverseOrder() -> Comparator[T]: ...

      def __init__(self): ...

    class StackItem[T1](PooledObject): ...

    class ICallback[E, T1]:

      def compare(self, arg0: object, arg1: object, arg2: object) -> int: ...


class Consumers:

  def __init__(self): ...

  class Params5:

    def __init__(self): ...

    class CallbackStackItem[E, T1, T2, T3, T4, T5](Consumers.Params5.StackItem):

      @overload
      def accept(self, arg0: object) -> None: ...

      @overload
      def accept(self, arg0: object) -> None: ...

      def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: Consumers.Params5.ICallback) -> Consumers.Params5.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2, T3, T4, T5](PooledObject): ...

    class ICallback[E, T1, T2, T3, T4, T5]:

      def accept(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object) -> None: ...

  class Params4:

    def __init__(self): ...

    class CallbackStackItem[E, T1, T2, T3, T4](Consumers.Params4.StackItem):

      @overload
      def accept(self, arg0: object) -> None: ...

      @overload
      def accept(self, arg0: object) -> None: ...

      def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: object, arg3: object, arg4: Consumers.Params4.ICallback) -> Consumers.Params4.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2, T3, T4](PooledObject): ...

    class ICallback[E, T1, T2, T3, T4]:

      def accept(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> None: ...

  class Params3:

    def __init__(self): ...

    class CallbackStackItem[E, T1, T2, T3](Consumers.Params3.StackItem):

      @overload
      def accept(self, arg0: object) -> None: ...

      @overload
      def accept(self, arg0: object) -> None: ...

      def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: object, arg3: Consumers.Params3.ICallback) -> Consumers.Params3.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2, T3](PooledObject): ...

    class ICallback[E, T1, T2, T3]:

      def accept(self, arg0: object, arg1: object, arg2: object, arg3: object) -> None: ...

  class Params2:

    def __init__(self): ...

    class CallbackStackItem[E, T1, T2](Consumers.Params2.StackItem):

      @overload
      def accept(self, arg0: object) -> None: ...

      @overload
      def accept(self, arg0: object) -> None: ...

      def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: Consumers.Params2.ICallback) -> Consumers.Params2.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2](PooledObject): ...

    class ICallback[E, T1, T2]:

      def accept(self, arg0: object, arg1: object, arg2: object) -> None: ...

  class Params1:

    def __init__(self): ...

    class CallbackStackItem[E, T1](Consumers.Params1.StackItem):

      @overload
      def accept(self, arg0: object) -> None: ...

      @overload
      def accept(self, arg0: object) -> None: ...

      def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: Consumers.Params1.ICallback) -> Consumers.Params1.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1](PooledObject): ...

    class ICallback[E, T1]:

      def accept(self, arg0: object, arg1: object) -> None: ...


class IntSupplierFunction[E]:

  def getInt(self, arg0: object) -> int: ...


class Invokers:

  def __init__(self): ...

  class Params4:

    def __init__(self): ...

    class CallbackStackItem[T1, T2, T3, T4](Invokers.Params4.StackItem):

      def onReleased(self) -> None: ...

      @overload
      def run(self) -> None: ...

      @overload
      def run(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: object, arg3: object, arg4: Invokers.Params4.ICallback) -> Invokers.Params4.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2, T3, T4](PooledObject): ...

    class ICallback[T1, T2, T3, T4]:

      def accept(self, arg0: object, arg1: object, arg2: object, arg3: object) -> None: ...

  class Params3:

    def __init__(self): ...

    class CallbackStackItem[T1, T2, T3](Invokers.Params3.StackItem):

      def onReleased(self) -> None: ...

      @overload
      def run(self) -> None: ...

      @overload
      def run(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: object, arg3: Invokers.Params3.ICallback) -> Invokers.Params3.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2, T3](PooledObject): ...

    class ICallback[T1, T2, T3]:

      def accept(self, arg0: object, arg1: object, arg2: object) -> None: ...

  class Params2:

    def __init__(self): ...

    class CallbackStackItem[T1, T2](Invokers.Params2.StackItem):

      def onReleased(self) -> None: ...

      @overload
      def run(self) -> None: ...

      @overload
      def run(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: Invokers.Params2.ICallback) -> Invokers.Params2.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2](PooledObject): ...

    class ICallback[T1, T2]:

      def accept(self, arg0: object, arg1: object) -> None: ...

  class Params1:

    def __init__(self): ...

    class CallbackStackItem[T1](Invokers.Params1.StackItem):

      def onReleased(self) -> None: ...

      @overload
      def run(self) -> None: ...

      @overload
      def run(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: Invokers.Params1.ICallback) -> Invokers.Params1.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1](PooledObject): ...

    class ICallback[T1]:

      def accept(self, arg0: object) -> None: ...


class Predicates:

  def __init__(self): ...

  class Params3:

    def __init__(self): ...

    class CallbackStackItem[E, T1, T2, T3](Predicates.Params3.StackItem):

      def negate(self) -> Predicate[T]: ...

      def onReleased(self) -> None: ...

      @overload
      def test(self, arg0: object) -> bool: ...

      @overload
      def test(self, arg0: object) -> bool: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: object, arg3: Predicates.Params3.ICallback) -> Predicates.Params3.CallbackStackItem: ...

      @staticmethod
      def isEqual(arg0: object) -> Predicate[T]: ...

      def __init__(self): ...

    class StackItem[T1, T2, T3](PooledObject): ...

    class ICallback[E, T1, T2, T3]:

      def test(self, arg0: object, arg1: object, arg2: object, arg3: object) -> bool: ...

  class Params2:

    def __init__(self): ...

    class CallbackStackItem[E, T1, T2](Predicates.Params2.StackItem):

      def negate(self) -> Predicate[T]: ...

      def onReleased(self) -> None: ...

      @overload
      def test(self, arg0: object) -> bool: ...

      @overload
      def test(self, arg0: object) -> bool: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: Predicates.Params2.ICallback) -> Predicates.Params2.CallbackStackItem: ...

      @staticmethod
      def isEqual(arg0: object) -> Predicate[T]: ...

      def __init__(self): ...

    class StackItem[T1, T2](PooledObject): ...

    class ICallback[E, T1, T2]:

      def test(self, arg0: object, arg1: object, arg2: object) -> bool: ...

  class Params1:

    def __init__(self): ...

    class CallbackStackItem[E, T1](Predicates.Params1.StackItem):

      def negate(self) -> Predicate[T]: ...

      def onReleased(self) -> None: ...

      @overload
      def test(self, arg0: object) -> bool: ...

      @overload
      def test(self, arg0: object) -> bool: ...

      @staticmethod
      def alloc(arg0: object, arg1: Predicates.Params1.ICallback) -> Predicates.Params1.CallbackStackItem: ...

      @staticmethod
      def isEqual(arg0: object) -> Predicate[T]: ...

      def __init__(self): ...

    class StackItem[T1](PooledObject): ...

    class ICallback[E, T1]:

      def test(self, arg0: object, arg1: object) -> bool: ...


class ReturnValueContainer[T](PooledObject):

  def onReleased(self) -> None: ...

  @staticmethod
  def alloc() -> ReturnValueContainer[E]: ...

  def __init__(self):
    self.returnval: object


class ReturnValueContainerPrimitives:

  def __init__(self): ...

  class RVInt(PooledObject):

    def onReleased(self) -> None: ...

    @staticmethod
    def alloc() -> ReturnValueContainerPrimitives.RVInt: ...

    def __init__(self):
      self.returnval: int

  class RVFloat(PooledObject):

    def onReleased(self) -> None: ...

    @staticmethod
    def alloc() -> ReturnValueContainerPrimitives.RVFloat: ...

    def __init__(self):
      self.returnval: float

  class RVBoolean(PooledObject):

    def onReleased(self) -> None: ...

    @staticmethod
    def alloc() -> ReturnValueContainerPrimitives.RVBoolean: ...

    def __init__(self):
      self.returnval: bool


class Stacks:

  def __init__(self): ...

  class Params6:

    def __init__(self): ...

    class CallbackStackItem[T1, T2, T3, T4, T5, T6](Stacks.Params6.StackItem):

      def invoke(self) -> None: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: Stacks.Params6.ICallback) -> Stacks.Params6.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2, T3, T4, T5, T6](Stacks.GenericStack): ...

    class ICallback[T1, T2, T3, T4, T5, T6]:

      def accept(self, arg0: Stacks.GenericStack, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object) -> None: ...

  class Params5:

    def __init__(self): ...

    class CallbackStackItem[T1, T2, T3, T4, T5](Stacks.Params5.StackItem):

      def invoke(self) -> None: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: Stacks.Params5.ICallback) -> Stacks.Params5.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2, T3, T4, T5](Stacks.GenericStack): ...

    class ICallback[T1, T2, T3, T4, T5]:

      def accept(self, arg0: Stacks.GenericStack, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object) -> None: ...

  class Params4:

    def __init__(self): ...

    class CallbackStackItem[T1, T2, T3, T4](Stacks.Params4.StackItem):

      def invoke(self) -> None: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: object, arg3: object, arg4: Stacks.Params4.ICallback) -> Stacks.Params4.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2, T3, T4](Stacks.GenericStack): ...

    class ICallback[T1, T2, T3, T4]:

      def accept(self, arg0: Stacks.GenericStack, arg1: object, arg2: object, arg3: object, arg4: object) -> None: ...

  class Params3:

    def __init__(self): ...

    class CallbackStackItem[T1, T2, T3](Stacks.Params3.StackItem):

      def invoke(self) -> None: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: object, arg3: Stacks.Params3.ICallback) -> Stacks.Params3.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2, T3](Stacks.GenericStack): ...

    class ICallback[T1, T2, T3]:

      def accept(self, arg0: Stacks.GenericStack, arg1: object, arg2: object, arg3: object) -> None: ...

  class Params2:

    def __init__(self): ...

    class CallbackStackItem[T1, T2](Stacks.Params2.StackItem):

      def invoke(self) -> None: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: object, arg2: Stacks.Params2.ICallback) -> Stacks.Params2.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1, T2](Stacks.GenericStack): ...

    class ICallback[T1, T2]:

      def accept(self, arg0: Stacks.GenericStack, arg1: object, arg2: object) -> None: ...

  class Params1:

    def __init__(self): ...

    class CallbackStackItem[T1](Stacks.Params1.StackItem):

      def invoke(self) -> None: ...

      def onReleased(self) -> None: ...

      @staticmethod
      def alloc(arg0: object, arg1: Stacks.Params1.ICallback) -> Stacks.Params1.CallbackStackItem: ...

      def __init__(self): ...

    class StackItem[T1](Stacks.GenericStack): ...

    class ICallback[T1]:

      def accept(self, arg0: Stacks.GenericStack, arg1: object) -> None: ...

  class GenericStack(PooledObject):

    @overload
    def comparator(self, arg0: object, arg1: Comparators.Params1.ICallback) -> Comparator[E]: ...

    @overload
    def comparator(self, arg0: object, arg1: object, arg2: Comparators.Params2.ICallback) -> Comparator[E]: ...

    @overload
    def consumer(self, arg0: object, arg1: Consumers.Params1.ICallback) -> Consumer[E]: ...

    @overload
    def consumer(self, arg0: object, arg1: object, arg2: Consumers.Params2.ICallback) -> Consumer[E]: ...

    def invoke(self) -> None: ...

    def invokeAndRelease(self) -> None: ...

    @overload
    def invoker(self, arg0: object, arg1: Invokers.Params1.ICallback) -> Runnable: ...

    @overload
    def invoker(self, arg0: object, arg1: object, arg2: Invokers.Params2.ICallback) -> Runnable: ...

    @overload
    def invoker(self, arg0: object, arg1: object, arg2: object, arg3: Invokers.Params3.ICallback) -> Runnable: ...

    @overload
    def invoker(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: Invokers.Params4.ICallback) -> Runnable: ...

    def onReleased(self) -> None: ...

    @overload
    def predicate(self, arg0: object, arg1: Predicates.Params1.ICallback) -> Predicate[E]: ...

    @overload
    def predicate(self, arg0: object, arg1: object, arg2: Predicates.Params2.ICallback) -> Predicate[E]: ...

    @overload
    def predicate(self, arg0: object, arg1: object, arg2: object, arg3: Predicates.Params3.ICallback) -> Predicate[E]: ...

    def __init__(self): ...

