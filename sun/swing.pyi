from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.beans import PropertyChangeListener

class UIAction:

  ACCELERATOR_KEY: str

  ACTION_COMMAND_KEY: str

  DEFAULT: str

  DISPLAYED_MNEMONIC_INDEX_KEY: str

  LARGE_ICON_KEY: str

  LONG_DESCRIPTION: str

  MNEMONIC_KEY: str

  NAME: str

  SELECTED_KEY: str

  SHORT_DESCRIPTION: str

  SMALL_ICON: str

  @overload
  def accept(self, arg0: object) -> bool: ...

  @overload
  def accept(self, arg0: object) -> bool: ...

  @overload
  def addPropertyChangeListener(self, arg0: PropertyChangeListener) -> None: ...

  @overload
  def addPropertyChangeListener(self, arg0: PropertyChangeListener) -> None: ...

  def getName(self) -> str: ...

  @overload
  def getValue(self, arg0: str) -> object: ...

  @overload
  def getValue(self, arg0: str) -> object: ...

  @overload
  def isEnabled(self) -> bool: ...

  @overload
  def isEnabled(self) -> bool: ...

  @overload
  def putValue(self, arg0: str, arg1: object) -> None: ...

  @overload
  def putValue(self, arg0: str, arg1: object) -> None: ...

  @overload
  def removePropertyChangeListener(self, arg0: PropertyChangeListener) -> None: ...

  @overload
  def removePropertyChangeListener(self, arg0: PropertyChangeListener) -> None: ...

  @overload
  def setEnabled(self, arg0: bool) -> None: ...

  @overload
  def setEnabled(self, arg0: bool) -> None: ...

  def __init__(self, arg0: str): ...

