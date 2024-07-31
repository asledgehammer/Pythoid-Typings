from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.net import InetAddress
from java.util.stream import Stream

class InetAddressResolver:

  def lookupByAddress(self, arg0: list[int]) -> str: ...

  def lookupByName(self, arg0: str, arg1: InetAddressResolver.LookupPolicy) -> Stream[InetAddress]: ...

  class LookupPolicy:

    IPV4: int

    IPV4_FIRST: int

    IPV6: int

    IPV6_FIRST: int

    def characteristics(self) -> int: ...

    @staticmethod
    def of(arg0: int) -> InetAddressResolver.LookupPolicy: ...


class InetAddressResolverProvider:

  def get(self, arg0: InetAddressResolverProvider.Configuration) -> InetAddressResolver: ...

  def name(self) -> str: ...

  class Configuration:

    def builtinResolver(self) -> InetAddressResolver: ...

    def lookupLocalHostName(self) -> str: ...

