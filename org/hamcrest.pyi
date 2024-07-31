from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Iterable

T = TypeVar('T', default=Any)

class Description:

  NONE: Description

  def appendDescriptionOf(self, arg0: SelfDescribing) -> Description: ...

  def appendList(self, arg0: str, arg1: str, arg2: str, arg3: Iterable[SelfDescribing]) -> Description: ...

  def appendText(self, arg0: str) -> Description: ...

  def appendValue(self, arg0: object) -> Description: ...

  @overload
  def appendValueList(self, arg0: str, arg1: str, arg2: str, arg3: list[object]) -> Description: ...

  @overload
  def appendValueList(self, arg0: str, arg1: str, arg2: str, arg3: Iterable[T]) -> Description: ...

  class NullDescription:

    NONE: Description

    @overload
    def appendDescriptionOf(self, arg0: SelfDescribing) -> Description: ...

    @overload
    def appendDescriptionOf(self, arg0: SelfDescribing) -> Description: ...

    @overload
    def appendList(self, arg0: str, arg1: str, arg2: str, arg3: Iterable[SelfDescribing]) -> Description: ...

    @overload
    def appendList(self, arg0: str, arg1: str, arg2: str, arg3: Iterable[SelfDescribing]) -> Description: ...

    @overload
    def appendText(self, arg0: str) -> Description: ...

    @overload
    def appendText(self, arg0: str) -> Description: ...

    @overload
    def appendValue(self, arg0: object) -> Description: ...

    @overload
    def appendValue(self, arg0: object) -> Description: ...

    @overload
    def appendValueList(self, arg0: str, arg1: str, arg2: str, arg3: list[object]) -> Description: ...

    @overload
    def appendValueList(self, arg0: str, arg1: str, arg2: str, arg3: list[object]) -> Description: ...

    @overload
    def appendValueList(self, arg0: str, arg1: str, arg2: str, arg3: Iterable[T]) -> Description: ...

    @overload
    def appendValueList(self, arg0: str, arg1: str, arg2: str, arg3: Iterable[T]) -> Description: ...

    def toString(self) -> str: ...

    def __init__(self): ...


class Matcher[T]:

  def _dont_implement_Matcher___instead_extend_BaseMatcher_(self) -> None: ...

  def describeMismatch(self, arg0: object, arg1: Description) -> None: ...

  def describeTo(self, arg0: Description) -> None: ...

  def matches(self, arg0: object) -> bool: ...


class SelfDescribing:

  def describeTo(self, arg0: Description) -> None: ...

