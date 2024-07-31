from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.net import URL, InetAddress, InetSocketAddress
from java.security import Permission

class IPAddressUtil:

  @staticmethod
  def checkAuthority(arg0: URL) -> str: ...

  @staticmethod
  def checkExternalForm(arg0: URL) -> str: ...

  @staticmethod
  def checkHostString(arg0: str) -> str: ...

  @staticmethod
  def convertFromIPv4MappedAddress(arg0: list[int]) -> list[int]: ...

  @staticmethod
  def digit(arg0: str, arg1: int) -> int: ...

  @staticmethod
  def isBsdParsableV4(arg0: str) -> bool: ...

  @staticmethod
  def isIPv4LiteralAddress(arg0: str) -> bool: ...

  @staticmethod
  def isIPv6LiteralAddress(arg0: str) -> bool: ...

  @staticmethod
  def match(arg0: str, arg1: int, arg2: int) -> bool: ...

  @staticmethod
  @overload
  def scan(arg0: str, arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def scan(arg0: str, arg1: int, arg2: int, arg3: list[str]) -> int: ...

  @staticmethod
  def textToNumericFormatV4(arg0: str) -> list[int]: ...

  @staticmethod
  def textToNumericFormatV6(arg0: str) -> list[int]: ...

  @staticmethod
  @overload
  def toScopedAddress(arg0: InetAddress) -> InetAddress: ...

  @staticmethod
  @overload
  def toScopedAddress(arg0: InetSocketAddress) -> InetSocketAddress: ...

  @staticmethod
  def validateNumericFormatV4(arg0: str) -> list[int]: ...

  def __init__(self): ...


class URLUtil:

  @staticmethod
  def getConnectPermission(arg0: URL) -> Permission: ...

  @staticmethod
  def urlNoFragString(arg0: URL) -> str: ...

  def __init__(self): ...

