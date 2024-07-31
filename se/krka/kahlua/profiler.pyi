from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import Writer, PrintWriter
from java.util import List, Map
from se.krka.kahlua.vm import JavaFunction, Prototype, KahluaThread

class AggregatingProfiler:

  @overload
  def getSample(self, arg0: Sample) -> None: ...

  @overload
  def getSample(self, arg0: Sample) -> None: ...

  def toTree(self, arg0: int, arg1: float, arg2: int) -> StacktraceNode: ...

  def __init__(self): ...


class BufferedProfiler:

  @overload
  def getSample(self, arg0: Sample) -> None: ...

  @overload
  def getSample(self, arg0: Sample) -> None: ...

  def sendTo(self, arg0: Profiler) -> None: ...

  def __init__(self): ...


class DebugProfiler:

  @overload
  def getSample(self, arg0: Sample) -> None: ...

  @overload
  def getSample(self, arg0: Sample) -> None: ...

  def __init__(self, arg0: Writer): ...


class FakeStacktraceElement:

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  @overload
  def name(self) -> str: ...

  @overload
  def name(self) -> str: ...

  def toString(self) -> str: ...

  @overload
  def type(self) -> str: ...

  @overload
  def type(self) -> str: ...

  def __init__(self, arg0: str, arg1: str): ...


class JavaStacktraceElement:

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  @overload
  def name(self) -> str: ...

  @overload
  def name(self) -> str: ...

  @overload
  def type(self) -> str: ...

  @overload
  def type(self) -> str: ...

  def __init__(self, arg0: JavaFunction): ...


class LuaStacktraceElement:

  def equals(self, arg0: object) -> bool: ...

  def getLine(self) -> int: ...

  def getSource(self) -> str: ...

  def hashCode(self) -> int: ...

  @overload
  def name(self) -> str: ...

  @overload
  def name(self) -> str: ...

  def toString(self) -> str: ...

  @overload
  def type(self) -> str: ...

  @overload
  def type(self) -> str: ...

  def __init__(self, arg0: int, arg1: Prototype): ...


class Profiler:

  def getSample(self, arg0: Sample) -> None: ...


class Sample:

  def getList(self) -> List[StacktraceElement]: ...

  def getTime(self) -> int: ...

  def __init__(self, arg0: List[StacktraceElement], arg1: int): ...


class Sampler:

  def start(self) -> None: ...

  def stop(self) -> None: ...

  def __init__(self, arg0: KahluaThread, arg1: int, arg2: Profiler): ...


class StacktraceCounter:

  def addTime(self, arg0: int) -> None: ...

  def getChildren(self) -> Map[StacktraceElement, StacktraceCounter]: ...

  def getOrCreateChild(self, arg0: StacktraceElement) -> StacktraceCounter: ...

  def getTime(self) -> int: ...

  def __init__(self): ...


class StacktraceElement:

  def name(self) -> str: ...

  def type(self) -> str: ...


class StacktraceNode:

  @overload
  def output(self, arg0: PrintWriter) -> None: ...

  @overload
  def output(self, arg0: PrintWriter, arg1: str, arg2: int, arg3: int) -> None: ...

  @staticmethod
  def createFrom(arg0: StacktraceCounter, arg1: StacktraceElement, arg2: int, arg3: float, arg4: int) -> StacktraceNode: ...

  def __init__(self, arg0: StacktraceElement, arg1: List[StacktraceNode], arg2: int): ...

