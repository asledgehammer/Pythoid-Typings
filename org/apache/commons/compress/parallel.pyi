from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import InputStream

class InputStreamSupplier:

  def get(self) -> InputStream: ...


class ScatterGatherBackingStore:

  def close(self) -> None: ...

  def closeForWriting(self) -> None: ...

  def getInputStream(self) -> InputStream: ...

  def writeOut(self, arg0: list[int], arg1: int, arg2: int) -> None: ...


class ScatterGatherBackingStoreSupplier:

  def get(self) -> ScatterGatherBackingStore: ...

