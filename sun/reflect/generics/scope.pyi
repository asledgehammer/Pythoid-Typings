from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class
from java.lang.reflect import TypeVariable, Constructor, Method

D = TypeVar('D', default=Any)

class AbstractScope[D]:

  @overload
  def lookup(self, arg0: str) -> TypeVariable[Any]: ...

  @overload
  def lookup(self, arg0: str) -> TypeVariable[Any]: ...


class ClassScope(AbstractScope):

  def lookup(self, arg0: str) -> TypeVariable[Any]: ...

  @staticmethod
  def make(arg0: Class[Any]) -> ClassScope: ...


class ConstructorScope(AbstractScope):

  @staticmethod
  def make(arg0: Constructor[Any]) -> ConstructorScope: ...


class MethodScope(AbstractScope):

  @staticmethod
  def make(arg0: Method) -> MethodScope: ...


class Scope:

  def lookup(self, arg0: str) -> TypeVariable[Any]: ...

