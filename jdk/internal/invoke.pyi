from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang.invoke import MethodType

class ABIDescriptorProxy:

  def shadowSpaceBytes(self) -> int: ...


class NativeEntryPoint:

  def type(self) -> MethodType: ...

  @staticmethod
  def make(arg0: str, arg1: ABIDescriptorProxy, arg2: list[VMStorageProxy], arg3: list[VMStorageProxy], arg4: bool, arg5: MethodType) -> NativeEntryPoint: ...


class VMStorageProxy:

  def index(self) -> int: ...

  def type(self) -> int: ...

