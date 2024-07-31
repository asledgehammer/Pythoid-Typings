from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Runnable, Class
from zombie.util.lambda import Invokers

T1 = TypeVar('T1', default=Any)
T2 = TypeVar('T2', default=Any)
Probe = TypeVar('Probe', default=Any)
Constructor_Probe = TypeVar('Constructor_Probe', default=Any)

class AbstractPerformanceProfileProbe:

  def end(self) -> None: ...

  @overload
  def invokeAndMeasure(self, invoke: Runnable) -> None: ...

  @overload
  def invokeAndMeasure(self, arg0: object, arg1: Invokers.Params1.ICallback) -> None: ...

  @overload
  def invokeAndMeasure(self, arg0: object, arg1: object, arg2: Invokers.Params2.ICallback) -> None: ...

  def isEnabled(self) -> bool: ...

  def setEnabled(self, val: bool) -> None: ...

  def start(self) -> None: ...


class PerformanceProfileFrameProbe(PerformanceProfileProbe):

  def __init__(self, name: str): ...


class PerformanceProfileProbe(AbstractPerformanceProfileProbe):

  @overload
  def __init__(self, name: str): ...
  @overload
  def __init__(self, name: str, isEnabled: bool): ...


class PerformanceProfileProbeList[Probe]:

  def at(self, layerIdx: int) -> Probe: ...

  def count(self) -> int: ...

  def start(self, layerIdx: int) -> Probe: ...

  @staticmethod
  @overload
  def construct(prefix: str, count: int) -> PerformanceProfileProbeList[PerformanceProfileProbe]: ...

  @staticmethod
  @overload
  def construct(prefix: str, count: int, type: Class[Probe], ctor: PerformanceProfileProbeList.Constructor) -> PerformanceProfileProbeList[Probe]: ...

  class Constructor[Constructor_Probe]:

    def get(self, title: str) -> Probe: ...


class TriggerGameProfilerFile:

  def __init__(self):
    self.discard: bool
    self.isrecording: bool

