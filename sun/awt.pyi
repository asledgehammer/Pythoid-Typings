from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import Button, Canvas, Checkbox, CheckboxMenuItem, Choice, Component, Desktop, Dialog, FileDialog, Frame, Label, List, Menu, MenuBar, MenuItem, Panel, PopupMenu, GraphicsDevice, ScrollPane, Scrollbar, Taskbar, TextArea, TextField, Window, AWTEvent, SecondaryLoop
from java.awt.dnd import DragGestureEvent
from java.awt.dnd.peer import DragSourceContextPeer
from java.awt.event import InvocationEvent, FocusEvent
from java.awt.peer import ButtonPeer, CanvasPeer, CheckboxPeer, CheckboxMenuItemPeer, ChoicePeer, LightweightPeer, DesktopPeer, DialogPeer, FileDialogPeer, FramePeer, LabelPeer, ListPeer, MenuPeer, MenuBarPeer, MenuItemPeer, PanelPeer, PopupMenuPeer, RobotPeer, ScrollPanePeer, ScrollbarPeer, TaskbarPeer, TextAreaPeer, TextFieldPeer, WindowPeer, FontPeer, MouseInfoPeer
from java.beans import PropertyChangeListener
from java.lang import ClassLoader, ThreadGroup, Enum, Thread, Runnable
from java.util import Set
from java.util.function import Supplier
from sun.awt.datatransfer import DataTransferer

T = TypeVar('T', default=Any)

class AppContext:

  DISPOSED_PROPERTY_NAME: str

  EVENT_QUEUE_COND_KEY: object

  EVENT_QUEUE_KEY: object

  EVENT_QUEUE_LOCK_KEY: object

  GUI_DISPOSED: str

  def addPropertyChangeListener(self, arg0: str, arg1: PropertyChangeListener) -> None: ...

  def dispose(self) -> None: ...

  def get(self, arg0: object) -> object: ...

  def getContextClassLoader(self) -> ClassLoader: ...

  @overload
  def getPropertyChangeListeners(self) -> list[PropertyChangeListener]: ...

  @overload
  def getPropertyChangeListeners(self, arg0: str) -> list[PropertyChangeListener]: ...

  def getThreadGroup(self) -> ThreadGroup: ...

  def isDisposed(self) -> bool: ...

  def put(self, arg0: object, arg1: object) -> object: ...

  def remove(self, arg0: object) -> object: ...

  def removePropertyChangeListener(self, arg0: str, arg1: PropertyChangeListener) -> None: ...

  def toString(self) -> str: ...

  @staticmethod
  def getAppContext() -> AppContext: ...

  @staticmethod
  def getAppContexts() -> Set[AppContext]: ...

  @staticmethod
  def getSoftReferenceValue(arg0: object, arg1: Supplier[T]) -> object: ...

  @staticmethod
  def isMainContext(arg0: AppContext) -> bool: ...

  class State(Enum):

    BEING_DISPOSED: AppContext.State

    DISPOSED: AppContext.State

    VALID: AppContext.State

    @staticmethod
    def valueOf(arg0: str) -> AppContext.State: ...

    @staticmethod
    def values() -> list[AppContext.State]: ...

  class PostShutdownEventRunnable:

    @overload
    def run(self) -> None: ...

    @overload
    def run(self) -> None: ...

  class CreateThreadAction:

    @overload
    def run(self) -> Thread: ...

    @overload
    def run(self) -> object: ...

    @overload
    def run(self) -> object: ...

  class GetAppContextLock: ...


class ComponentFactory:

  def createButton(self, arg0: Button) -> ButtonPeer: ...

  def createCanvas(self, arg0: Canvas) -> CanvasPeer: ...

  def createCheckbox(self, arg0: Checkbox) -> CheckboxPeer: ...

  def createCheckboxMenuItem(self, arg0: CheckboxMenuItem) -> CheckboxMenuItemPeer: ...

  def createChoice(self, arg0: Choice) -> ChoicePeer: ...

  def createComponent(self, arg0: Component) -> LightweightPeer: ...

  def createDesktopPeer(self, arg0: Desktop) -> DesktopPeer: ...

  def createDialog(self, arg0: Dialog) -> DialogPeer: ...

  def createDragSourceContextPeer(self, arg0: DragGestureEvent) -> DragSourceContextPeer: ...

  def createFileDialog(self, arg0: FileDialog) -> FileDialogPeer: ...

  def createFrame(self, arg0: Frame) -> FramePeer: ...

  def createLabel(self, arg0: Label) -> LabelPeer: ...

  def createList(self, arg0: List) -> ListPeer: ...

  def createMenu(self, arg0: Menu) -> MenuPeer: ...

  def createMenuBar(self, arg0: MenuBar) -> MenuBarPeer: ...

  def createMenuItem(self, arg0: MenuItem) -> MenuItemPeer: ...

  def createPanel(self, arg0: Panel) -> PanelPeer: ...

  def createPopupMenu(self, arg0: PopupMenu) -> PopupMenuPeer: ...

  def createRobot(self, arg0: GraphicsDevice) -> RobotPeer: ...

  def createScrollPane(self, arg0: ScrollPane) -> ScrollPanePeer: ...

  def createScrollbar(self, arg0: Scrollbar) -> ScrollbarPeer: ...

  def createTaskbarPeer(self, arg0: Taskbar) -> TaskbarPeer: ...

  def createTextArea(self, arg0: TextArea) -> TextAreaPeer: ...

  def createTextField(self, arg0: TextField) -> TextFieldPeer: ...

  def createWindow(self, arg0: Window) -> WindowPeer: ...

  def getDataTransferer(self) -> DataTransferer: ...

  def getFontPeer(self, arg0: str, arg1: int) -> FontPeer: ...

  def getMouseInfoPeer(self) -> MouseInfoPeer: ...


class ConstrainableGraphics:

  def constrain(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...


class DisplayChangedListener:

  def displayChanged(self) -> None: ...

  def paletteChanged(self) -> None: ...


class EventQueueItem:

  def __init__(self, arg0: AWTEvent):
    self.event: AWTEvent
    self.next: EventQueueItem


class FwDispatcher:

  def createSecondaryLoop(self) -> SecondaryLoop: ...

  def isDispatchThread(self) -> bool: ...

  def scheduleDispatch(self, arg0: Runnable) -> None: ...


class MostRecentKeyValue: ...


class PeerEvent(InvocationEvent):

  LOW_PRIORITY_EVENT: int

  PRIORITY_EVENT: int

  ULTIMATE_PRIORITY_EVENT: int

  def coalesceEvents(self, arg0: PeerEvent) -> PeerEvent: ...

  def getFlags(self) -> int: ...

  @overload
  def __init__(self, arg0: object, arg1: Runnable, arg2: int): ...
  @overload
  def __init__(self, arg0: object, arg1: Runnable, arg2: object, arg3: bool, arg4: int): ...


class RequestFocusController:

  def acceptRequestFocus(self, arg0: Component, arg1: Component, arg2: bool, arg3: bool, arg4: FocusEvent.Cause) -> bool: ...


class SubRegionShowable:

  def show(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def showIfNotLost(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool: ...

