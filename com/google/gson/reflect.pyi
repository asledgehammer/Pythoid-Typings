from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class
from java.lang.reflect import Type

T = TypeVar('T', default=Any)

class TypeToken[T]:

  def equals(self, arg0: object) -> bool: ...

  def getRawType(self) -> Class[T]: ...

  def getType(self) -> Type: ...

  def hashCode(self) -> int: ...

  @overload
  def isAssignableFrom(self, arg0: TypeToken[Any]) -> bool: ...

  @overload
  def isAssignableFrom(self, arg0: Class[Any]) -> bool: ...

  @overload
  def isAssignableFrom(self, arg0: Type) -> bool: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def get(arg0: Class[T]) -> TypeToken[T]: ...

  @staticmethod
  @overload
  def get(arg0: Type) -> TypeToken[Any]: ...

  @staticmethod
  def getArray(arg0: Type) -> TypeToken[Any]: ...

  @staticmethod
  def getParameterized(arg0: Type, arg1: list[Type]) -> TypeToken[Any]: ...

