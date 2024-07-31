from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from de.btobastian.javacord.entities import Server, Channel
from java.lang import Enum

class RateLimitManager:

  @overload
  def addRateLimit(self, arg0: RateLimitType, arg1: int) -> None: ...

  @overload
  def addRateLimit(self, arg0: RateLimitType, arg1: Server, arg2: Channel, arg3: int) -> None: ...

  @overload
  def getRateLimit(self, arg0: RateLimitType) -> int: ...

  @overload
  def getRateLimit(self, arg0: RateLimitType, arg1: Server, arg2: Channel) -> int: ...

  @overload
  def isRateLimited(self, arg0: RateLimitType) -> bool: ...

  @overload
  def isRateLimited(self, arg0: RateLimitType, arg1: Channel) -> bool: ...

  @overload
  def isRateLimited(self, arg0: RateLimitType, arg1: Server) -> bool: ...

  @overload
  def isRateLimited(self, arg0: RateLimitType, arg1: Server, arg2: Channel) -> bool: ...

  def __init__(self): ...


class RateLimitType(Enum):

  NAME_CHANGE: RateLimitType

  PRIVATE_MESSAGE: RateLimitType

  PRIVATE_MESSAGE_DELETE: RateLimitType

  SERVER_MESSAGE: RateLimitType

  SERVER_MESSAGE_DELETE: RateLimitType

  UNKNOWN: RateLimitType

  @staticmethod
  def valueOf(arg0: str) -> RateLimitType: ...

  @staticmethod
  def values() -> list[RateLimitType]: ...

