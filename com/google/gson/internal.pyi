from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from com.google.gson import InstanceCreator, Gson, TypeAdapter, ExclusionStrategy
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from java.lang import Class, Number
from java.lang.reflect import Type, Field
from java.util import Map, AbstractMap, Set, Comparator, AbstractSet, Iterator
from java.util.function import Consumer

T = TypeVar('T', default=Any)
K = TypeVar('K', default=Any)
V = TypeVar('V', default=Any)
Node_K = TypeVar('Node_K', default=Any)
Node_V = TypeVar('Node_V', default=Any)

class ConstructorConstructor:

  def get(self, arg0: TypeToken[T]) -> ObjectConstructor[T]: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: Map[Type, InstanceCreator[Any]], arg1: bool): ...


class Excluder:

  DEFAULT: Excluder

  @overload
  def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

  @overload
  def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

  def disableInnerClassSerialization(self) -> Excluder: ...

  def excludeClass(self, arg0: Class[Any], arg1: bool) -> bool: ...

  def excludeField(self, arg0: Field, arg1: bool) -> bool: ...

  def excludeFieldsWithoutExposeAnnotation(self) -> Excluder: ...

  def withExclusionStrategy(self, arg0: ExclusionStrategy, arg1: bool, arg2: bool) -> Excluder: ...

  def withModifiers(self, arg0: list[int]) -> Excluder: ...

  def withVersion(self, arg0: float) -> Excluder: ...

  def __init__(self): ...


class JsonReaderInternalAccess:

  INSTANCE: JsonReaderInternalAccess

  def promoteNameToValue(self, arg0: JsonReader) -> None: ...

  def __init__(self): ...


class LazilyParsedNumber(Number):

  def doubleValue(self) -> float: ...

  def equals(self, arg0: object) -> bool: ...

  def floatValue(self) -> float: ...

  def hashCode(self) -> int: ...

  def intValue(self) -> int: ...

  def longValue(self) -> int: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: str): ...


class LinkedTreeMap[K, V](AbstractMap):

  def clear(self) -> None: ...

  def containsKey(self, arg0: object) -> bool: ...

  def entrySet(self) -> Set[Map.Entry[K, V]]: ...

  def get(self, arg0: object) -> object: ...

  def keySet(self) -> Set[K]: ...

  def put(self, arg0: object, arg1: object) -> object: ...

  def remove(self, arg0: object) -> object: ...

  def size(self) -> int: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: Comparator[K]): ...

  class KeySet(AbstractSet):

    def clear(self) -> None: ...

    def contains(self, arg0: object) -> bool: ...

    def iterator(self) -> Iterator[K]: ...

    def remove(self, arg0: object) -> bool: ...

    def size(self) -> int: ...

  class EntrySet(AbstractSet):

    def clear(self) -> None: ...

    def contains(self, arg0: object) -> bool: ...

    def iterator(self) -> Iterator[Map.Entry[K, V]]: ...

    def remove(self, arg0: object) -> bool: ...

    def size(self) -> int: ...

  class LinkedTreeMapIterator[T]:

    def forEachRemaining(self, arg0: Consumer[E]) -> None: ...

    @overload
    def hasNext(self) -> bool: ...

    @overload
    def hasNext(self) -> bool: ...

    def next(self) -> object: ...

    @overload
    def remove(self) -> None: ...

    @overload
    def remove(self) -> None: ...

  class Node[Node_K, Node_V]:

    @overload
    def equals(self, arg0: object) -> bool: ...

    @overload
    def equals(self, arg0: object) -> bool: ...

    def first(self) -> LinkedTreeMap.Node: ...

    @overload
    def getKey(self) -> object: ...

    @overload
    def getKey(self) -> object: ...

    @overload
    def getValue(self) -> object: ...

    @overload
    def getValue(self) -> object: ...

    @overload
    def hashCode(self) -> int: ...

    @overload
    def hashCode(self) -> int: ...

    def last(self) -> LinkedTreeMap.Node: ...

    @overload
    def setValue(self, arg0: object) -> object: ...

    @overload
    def setValue(self, arg0: object) -> object: ...

    def toString(self) -> str: ...

    @staticmethod
    @overload
    def comparingByKey() -> Comparator[Map.Entry[K, V]]: ...

    @staticmethod
    @overload
    def comparingByKey(arg0: Comparator[K]) -> Comparator[Map.Entry[K, V]]: ...

    @staticmethod
    @overload
    def comparingByValue() -> Comparator[Map.Entry[K, V]]: ...

    @staticmethod
    @overload
    def comparingByValue(arg0: Comparator[V]) -> Comparator[Map.Entry[K, V]]: ...

    @staticmethod
    def copyOf(arg0: Map.Entry) -> Map.Entry: ...


class ObjectConstructor[T]:

  def construct(self) -> object: ...


class Primitives:

  @staticmethod
  def isPrimitive(arg0: Type) -> bool: ...

  @staticmethod
  def isWrapperType(arg0: Type) -> bool: ...

  @staticmethod
  def unwrap(arg0: Class[T]) -> Class[T]: ...

  @staticmethod
  def wrap(arg0: Class[T]) -> Class[T]: ...

