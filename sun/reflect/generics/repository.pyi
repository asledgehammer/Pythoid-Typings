from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang.reflect import Type, TypeVariable
from sun.reflect.generics.factory import GenericsFactory

T = TypeVar('T', default=Any)
S = TypeVar('S', default=Any)

class AbstractRepository[T]: ...


class ClassRepository(GenericDeclRepository):

  NONE: ClassRepository

  def getSuperInterfaces(self) -> list[Type]: ...

  def getSuperclass(self) -> Type: ...

  @staticmethod
  def make(arg0: str, arg1: GenericsFactory) -> ClassRepository: ...


class ConstructorRepository(GenericDeclRepository):

  def getExceptionTypes(self) -> list[Type]: ...

  def getParameterTypes(self) -> list[Type]: ...

  @staticmethod
  def make(arg0: str, arg1: GenericsFactory) -> ConstructorRepository: ...


class FieldRepository(AbstractRepository):

  def getGenericType(self) -> Type: ...

  @staticmethod
  def make(arg0: str, arg1: GenericsFactory) -> FieldRepository: ...


class GenericDeclRepository[S](AbstractRepository):

  def getTypeParameters(self) -> list[TypeVariable]: ...


class MethodRepository(ConstructorRepository):

  def getReturnType(self) -> Type: ...

  @staticmethod
  def make(arg0: str, arg1: GenericsFactory) -> MethodRepository: ...

