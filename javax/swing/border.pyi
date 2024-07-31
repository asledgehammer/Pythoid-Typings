from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import Component, Insets, Graphics

class Border:

  def getBorderInsets(self, arg0: Component) -> Insets: ...

  def isBorderOpaque(self) -> bool: ...

  def paintBorder(self, arg0: Component, arg1: Graphics, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

