from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import AbstractMap, Set, Map

V = TypeVar('V', default=Any)

class PreHashedMap[V](AbstractMap):

  def entrySet(self) -> Set[Map.Entry[str, V]]: ...

  def get(self, arg0: object) -> object: ...

  def keySet(self) -> Set[str]: ...

  @overload
  def put(self, arg0: object, arg1: object) -> object: ...

  @overload
  def put(self, arg0: str, arg1: object) -> object: ...

