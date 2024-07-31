from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Exception, Class
from java.security import BasicPermission, Principal, PrivilegedAction, PrivilegedExceptionAction, AccessControlContext
from java.util import Set, Collection, Iterator, Spliterator, AbstractSet
from java.util.concurrent import Callable

T = TypeVar('T', default=Any)
E = TypeVar('E', default=Any)

class AuthPermission(BasicPermission):

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: str): ...


class DestroyFailedException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class Destroyable:

  def destroy(self) -> None: ...

  def isDestroyed(self) -> bool: ...


class Subject:

  def equals(self, arg0: object) -> bool: ...

  @overload
  def getPrincipals(self) -> Set[Principal]: ...

  @overload
  def getPrincipals(self, arg0: Class[T]) -> Set[T]: ...

  @overload
  def getPrivateCredentials(self) -> Set[object]: ...

  @overload
  def getPrivateCredentials(self, arg0: Class[T]) -> Set[T]: ...

  @overload
  def getPublicCredentials(self) -> Set[object]: ...

  @overload
  def getPublicCredentials(self, arg0: Class[T]) -> Set[T]: ...

  def hashCode(self) -> int: ...

  def isReadOnly(self) -> bool: ...

  def setReadOnly(self) -> None: ...

  def toString(self) -> str: ...

  @staticmethod
  def callAs(arg0: Subject, arg1: Callable[T]) -> object: ...

  @staticmethod
  def current() -> Subject: ...

  @staticmethod
  @overload
  def doAs(arg0: Subject, arg1: PrivilegedAction[T]) -> object: ...

  @staticmethod
  @overload
  def doAs(arg0: Subject, arg1: PrivilegedExceptionAction[T]) -> object: ...

  @staticmethod
  @overload
  def doAsPrivileged(arg0: Subject, arg1: PrivilegedAction[T], arg2: AccessControlContext) -> object: ...

  @staticmethod
  @overload
  def doAsPrivileged(arg0: Subject, arg1: PrivilegedExceptionAction[T], arg2: AccessControlContext) -> object: ...

  @staticmethod
  def getSubject(arg0: AccessControlContext) -> Subject: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: bool, arg1: Set[Principal], arg2: Set[Any], arg3: Set[Any]): ...

  class SecureSet[E]:

    @overload
    def add(self, arg0: object) -> bool: ...

    @overload
    def add(self, arg0: object) -> bool: ...

    @overload
    def addAll(self, arg0: Collection[E]) -> bool: ...

    @overload
    def addAll(self, arg0: Collection[E]) -> bool: ...

    @overload
    def clear(self) -> None: ...

    @overload
    def clear(self) -> None: ...

    @overload
    def contains(self, arg0: object) -> bool: ...

    @overload
    def contains(self, arg0: object) -> bool: ...

    @overload
    def containsAll(self, arg0: Collection[Any]) -> bool: ...

    @overload
    def containsAll(self, arg0: Collection[Any]) -> bool: ...

    @overload
    def equals(self, arg0: object) -> bool: ...

    @overload
    def equals(self, arg0: object) -> bool: ...

    @overload
    def hashCode(self) -> int: ...

    @overload
    def hashCode(self) -> int: ...

    @overload
    def isEmpty(self) -> bool: ...

    @overload
    def isEmpty(self) -> bool: ...

    @overload
    def iterator(self) -> Iterator[E]: ...

    @overload
    def iterator(self) -> Iterator[E]: ...

    @overload
    def remove(self, arg0: object) -> bool: ...

    @overload
    def remove(self, arg0: object) -> bool: ...

    @overload
    def removeAll(self, arg0: Collection[Any]) -> bool: ...

    @overload
    def removeAll(self, arg0: Collection[Any]) -> bool: ...

    @overload
    def retainAll(self, arg0: Collection[Any]) -> bool: ...

    @overload
    def retainAll(self, arg0: Collection[Any]) -> bool: ...

    @overload
    def size(self) -> int: ...

    @overload
    def size(self) -> int: ...

    def spliterator(self) -> Spliterator[E]: ...

    @overload
    def toArray(self) -> list[object]: ...

    @overload
    def toArray(self) -> list[object]: ...

    @overload
    def toArray(self, arg0: list[object]) -> list[object]: ...

    @overload
    def toArray(self, arg0: list[object]) -> list[object]: ...

    @staticmethod
    def copyOf(arg0: Collection[E]) -> Set[E]: ...

    @staticmethod
    @overload
    def of() -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: list[object]) -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: object) -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object) -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object, arg3: object) -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object) -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object) -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object) -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object, arg8: object) -> Set[E]: ...

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object, arg8: object, arg9: object) -> Set[E]: ...

  class AuthPermissionHolder: ...

  class ClassSet[T](AbstractSet):

    def add(self, arg0: object) -> bool: ...

    def iterator(self) -> Iterator[T]: ...

    def size(self) -> int: ...

