from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import AWTEvent, Container, Component
from java.awt.event import MouseEvent, KeyEvent
from java.lang import Class
from java.util import EventObject, EventListener
from javax.swing import JComponent, MenuSelectionManager, MenuElement

T = TypeVar('T', default=Any)

class AncestorEvent(AWTEvent):

  ANCESTOR_ADDED: int

  ANCESTOR_MOVED: int

  ANCESTOR_REMOVED: int

  def getAncestor(self) -> Container: ...

  def getAncestorParent(self) -> Container: ...

  def getComponent(self) -> JComponent: ...

  def __init__(self, arg0: JComponent, arg1: int, arg2: Container, arg3: Container): ...


class AncestorListener:

  def ancestorAdded(self, arg0: AncestorEvent) -> None: ...

  def ancestorMoved(self, arg0: AncestorEvent) -> None: ...

  def ancestorRemoved(self, arg0: AncestorEvent) -> None: ...


class ChangeEvent(EventObject):

  def __init__(self, arg0: object): ...


class ChangeListener:

  def stateChanged(self, arg0: ChangeEvent) -> None: ...


class EventListenerList:

  def add(self, arg0: Class[T], arg1: T) -> None: ...

  @overload
  def getListenerCount(self) -> int: ...

  @overload
  def getListenerCount(self, arg0: Class[Any]) -> int: ...

  def getListenerList(self) -> list[object]: ...

  def getListeners(self, arg0: Class[T]) -> list[EventListener]: ...

  def remove(self, arg0: Class[T], arg1: T) -> None: ...

  def toString(self) -> str: ...

  def __init__(self): ...


class MenuDragMouseEvent(MouseEvent):

  def getMenuSelectionManager(self) -> MenuSelectionManager: ...

  def getPath(self) -> list[MenuElement]: ...

  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: list[MenuElement], arg9: MenuSelectionManager): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: list[MenuElement], arg11: MenuSelectionManager): ...


class MenuDragMouseListener:

  def menuDragMouseDragged(self, arg0: MenuDragMouseEvent) -> None: ...

  def menuDragMouseEntered(self, arg0: MenuDragMouseEvent) -> None: ...

  def menuDragMouseExited(self, arg0: MenuDragMouseEvent) -> None: ...

  def menuDragMouseReleased(self, arg0: MenuDragMouseEvent) -> None: ...


class MenuEvent(EventObject):

  def __init__(self, arg0: object): ...


class MenuKeyEvent(KeyEvent):

  def getMenuSelectionManager(self) -> MenuSelectionManager: ...

  def getPath(self) -> list[MenuElement]: ...

  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: str, arg6: list[MenuElement], arg7: MenuSelectionManager): ...


class MenuKeyListener:

  def menuKeyPressed(self, arg0: MenuKeyEvent) -> None: ...

  def menuKeyReleased(self, arg0: MenuKeyEvent) -> None: ...

  def menuKeyTyped(self, arg0: MenuKeyEvent) -> None: ...


class MenuListener:

  def menuCanceled(self, arg0: MenuEvent) -> None: ...

  def menuDeselected(self, arg0: MenuEvent) -> None: ...

  def menuSelected(self, arg0: MenuEvent) -> None: ...


class PopupMenuEvent(EventObject):

  def __init__(self, arg0: object): ...


class PopupMenuListener:

  def popupMenuCanceled(self, arg0: PopupMenuEvent) -> None: ...

  def popupMenuWillBecomeInvisible(self, arg0: PopupMenuEvent) -> None: ...

  def popupMenuWillBecomeVisible(self, arg0: PopupMenuEvent) -> None: ...

