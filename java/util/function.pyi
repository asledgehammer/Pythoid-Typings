from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import Comparator

T = TypeVar('T', default=Any)
U = TypeVar('U', default=Any)
R = TypeVar('R', default=Any)
V = TypeVar('V', default=Any)

class BiConsumer[T, U]:

  def accept(self, arg0: object, arg1: object) -> None: ...

  def andThen(self, arg0: BiConsumer[T, U]) -> BiConsumer[T, U]: ...


class BiFunction[T, U, R]:

  def andThen(self, arg0: Function[R, V]) -> BiFunction[T, U, V]: ...

  def apply(self, arg0: object, arg1: object) -> object: ...


class BiPredicate[T, U]:

  def negate(self) -> BiPredicate[T, U]: ...

  def test(self, arg0: object, arg1: object) -> bool: ...


class BinaryOperator[T]:

  def andThen(self, arg0: Function[R, V]) -> BiFunction[T, U, V]: ...

  def apply(self, arg0: object, arg1: object) -> object: ...

  @staticmethod
  def maxBy(arg0: Comparator[T]) -> BinaryOperator[T]: ...

  @staticmethod
  def minBy(arg0: Comparator[T]) -> BinaryOperator[T]: ...


class BooleanSupplier:

  def getAsBoolean(self) -> bool: ...


class Consumer[T]:

  def accept(self, arg0: object) -> None: ...

  def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...


class DoubleBinaryOperator:

  def applyAsDouble(self, arg0: float, arg1: float) -> float: ...


class DoubleConsumer:

  def accept(self, arg0: float) -> None: ...

  def andThen(self, arg0: DoubleConsumer) -> DoubleConsumer: ...


class DoubleFunction[R]:

  def apply(self, arg0: float) -> object: ...


class DoublePredicate:

  def negate(self) -> DoublePredicate: ...

  def test(self, arg0: float) -> bool: ...


class DoubleSupplier:

  def getAsDouble(self) -> float: ...


class DoubleToIntFunction:

  def applyAsInt(self, arg0: float) -> int: ...


class DoubleToLongFunction:

  def applyAsLong(self, arg0: float) -> int: ...


class DoubleUnaryOperator:

  def andThen(self, arg0: DoubleUnaryOperator) -> DoubleUnaryOperator: ...

  def applyAsDouble(self, arg0: float) -> float: ...

  def compose(self, arg0: DoubleUnaryOperator) -> DoubleUnaryOperator: ...

  @staticmethod
  def identity() -> DoubleUnaryOperator: ...


class Function[T, R]:

  def andThen(self, arg0: Function[R, V]) -> Function[T, V]: ...

  def apply(self, arg0: object) -> object: ...

  def compose(self, arg0: Function[V, T]) -> Function[V, R]: ...

  @staticmethod
  def identity() -> Function[T, T]: ...


class IntBinaryOperator:

  def applyAsInt(self, arg0: int, arg1: int) -> int: ...


class IntConsumer:

  def accept(self, arg0: int) -> None: ...

  def andThen(self, arg0: IntConsumer) -> IntConsumer: ...


class IntFunction[R]:

  def apply(self, arg0: int) -> object: ...


class IntPredicate:

  def negate(self) -> IntPredicate: ...

  def test(self, arg0: int) -> bool: ...


class IntSupplier:

  def getAsInt(self) -> int: ...


class IntToDoubleFunction:

  def applyAsDouble(self, arg0: int) -> float: ...


class IntToLongFunction:

  def applyAsLong(self, arg0: int) -> int: ...


class IntUnaryOperator:

  def andThen(self, arg0: IntUnaryOperator) -> IntUnaryOperator: ...

  def applyAsInt(self, arg0: int) -> int: ...

  def compose(self, arg0: IntUnaryOperator) -> IntUnaryOperator: ...

  @staticmethod
  def identity() -> IntUnaryOperator: ...


class LongBinaryOperator:

  def applyAsLong(self, arg0: int, arg1: int) -> int: ...


class LongConsumer:

  def accept(self, arg0: int) -> None: ...

  def andThen(self, arg0: LongConsumer) -> LongConsumer: ...


class LongFunction[R]:

  def apply(self, arg0: int) -> object: ...


class LongPredicate:

  def negate(self) -> LongPredicate: ...

  def test(self, arg0: int) -> bool: ...


class LongSupplier:

  def getAsLong(self) -> int: ...


class LongToDoubleFunction:

  def applyAsDouble(self, arg0: int) -> float: ...


class LongToIntFunction:

  def applyAsInt(self, arg0: int) -> int: ...


class LongUnaryOperator:

  def andThen(self, arg0: LongUnaryOperator) -> LongUnaryOperator: ...

  def applyAsLong(self, arg0: int) -> int: ...

  def compose(self, arg0: LongUnaryOperator) -> LongUnaryOperator: ...

  @staticmethod
  def identity() -> LongUnaryOperator: ...


class ObjDoubleConsumer[T]:

  def accept(self, arg0: object, arg1: float) -> None: ...


class ObjIntConsumer[T]:

  def accept(self, arg0: object, arg1: int) -> None: ...


class ObjLongConsumer[T]:

  def accept(self, arg0: object, arg1: int) -> None: ...


class Predicate[T]:

  def negate(self) -> Predicate[T]: ...

  def test(self, arg0: object) -> bool: ...

  @staticmethod
  def isEqual(arg0: object) -> Predicate[T]: ...


class Supplier[T]:

  def get(self) -> object: ...


class ToDoubleBiFunction[T, U]:

  def applyAsDouble(self, arg0: object, arg1: object) -> float: ...


class ToDoubleFunction[T]:

  def applyAsDouble(self, arg0: object) -> float: ...


class ToIntBiFunction[T, U]:

  def applyAsInt(self, arg0: object, arg1: object) -> int: ...


class ToIntFunction[T]:

  def applyAsInt(self, arg0: object) -> int: ...


class ToLongBiFunction[T, U]:

  def applyAsLong(self, arg0: object, arg1: object) -> int: ...


class ToLongFunction[T]:

  def applyAsLong(self, arg0: object) -> int: ...


class UnaryOperator[T]:

  def andThen(self, arg0: Function[R, V]) -> Function[T, V]: ...

  def apply(self, arg0: object) -> object: ...

  def compose(self, arg0: Function[V, T]) -> Function[V, R]: ...

  @staticmethod
  @overload
  def identity() -> UnaryOperator[T]: ...

  @staticmethod
  @overload
  def identity() -> Function[T, T]: ...

