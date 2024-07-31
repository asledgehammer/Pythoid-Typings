from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import AWTEvent, Adjustable, Component, Container, ItemSelectable, Point, Rectangle, Window
from java.awt.font import TextHitInfo
from java.lang import Enum, Exception, Throwable, Runnable
from java.text import AttributedCharacterIterator

class AWTEventListener:

  def eventDispatched(self, arg0: AWTEvent) -> None: ...


class ActionEvent(AWTEvent):

  ACTION_FIRST: int

  ACTION_LAST: int

  ACTION_PERFORMED: int

  ALT_MASK: int

  CTRL_MASK: int

  META_MASK: int

  SHIFT_MASK: int

  def getActionCommand(self) -> str: ...

  def getModifiers(self) -> int: ...

  def getWhen(self) -> int: ...

  def paramString(self) -> str: ...

  @overload
  def __init__(self, arg0: object, arg1: int, arg2: str): ...
  @overload
  def __init__(self, arg0: object, arg1: int, arg2: str, arg3: int): ...
  @overload
  def __init__(self, arg0: object, arg1: int, arg2: str, arg3: int, arg4: int): ...


class ActionListener:

  def actionPerformed(self, arg0: ActionEvent) -> None: ...


class AdjustmentEvent(AWTEvent):

  ADJUSTMENT_FIRST: int

  ADJUSTMENT_LAST: int

  ADJUSTMENT_VALUE_CHANGED: int

  BLOCK_DECREMENT: int

  BLOCK_INCREMENT: int

  TRACK: int

  UNIT_DECREMENT: int

  UNIT_INCREMENT: int

  def getAdjustable(self) -> Adjustable: ...

  def getAdjustmentType(self) -> int: ...

  def getValue(self) -> int: ...

  def getValueIsAdjusting(self) -> bool: ...

  def paramString(self) -> str: ...

  @overload
  def __init__(self, arg0: Adjustable, arg1: int, arg2: int, arg3: int): ...
  @overload
  def __init__(self, arg0: Adjustable, arg1: int, arg2: int, arg3: int, arg4: bool): ...


class AdjustmentListener:

  def adjustmentValueChanged(self, arg0: AdjustmentEvent) -> None: ...


class ComponentEvent(AWTEvent):

  COMPONENT_FIRST: int

  COMPONENT_HIDDEN: int

  COMPONENT_LAST: int

  COMPONENT_MOVED: int

  COMPONENT_RESIZED: int

  COMPONENT_SHOWN: int

  def getComponent(self) -> Component: ...

  def paramString(self) -> str: ...

  def __init__(self, arg0: Component, arg1: int): ...


class ComponentListener:

  def componentHidden(self, arg0: ComponentEvent) -> None: ...

  def componentMoved(self, arg0: ComponentEvent) -> None: ...

  def componentResized(self, arg0: ComponentEvent) -> None: ...

  def componentShown(self, arg0: ComponentEvent) -> None: ...


class ContainerEvent(ComponentEvent):

  COMPONENT_ADDED: int

  COMPONENT_REMOVED: int

  CONTAINER_FIRST: int

  CONTAINER_LAST: int

  def getChild(self) -> Component: ...

  def getContainer(self) -> Container: ...

  def paramString(self) -> str: ...

  def __init__(self, arg0: Component, arg1: int, arg2: Component): ...


class ContainerListener:

  def componentAdded(self, arg0: ContainerEvent) -> None: ...

  def componentRemoved(self, arg0: ContainerEvent) -> None: ...


class FocusEvent(ComponentEvent):

  FOCUS_FIRST: int

  FOCUS_GAINED: int

  FOCUS_LAST: int

  FOCUS_LOST: int

  def getCause(self) -> FocusEvent.Cause: ...

  def getOppositeComponent(self) -> Component: ...

  def isTemporary(self) -> bool: ...

  def paramString(self) -> str: ...

  @overload
  def __init__(self, arg0: Component, arg1: int): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: bool): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: bool, arg3: Component): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: bool, arg3: Component, arg4: FocusEvent.Cause): ...

  class Cause(Enum):

    ACTIVATION: FocusEvent.Cause

    CLEAR_GLOBAL_FOCUS_OWNER: FocusEvent.Cause

    MOUSE_EVENT: FocusEvent.Cause

    ROLLBACK: FocusEvent.Cause

    TRAVERSAL: FocusEvent.Cause

    TRAVERSAL_BACKWARD: FocusEvent.Cause

    TRAVERSAL_DOWN: FocusEvent.Cause

    TRAVERSAL_FORWARD: FocusEvent.Cause

    TRAVERSAL_UP: FocusEvent.Cause

    UNEXPECTED: FocusEvent.Cause

    UNKNOWN: FocusEvent.Cause

    @staticmethod
    def valueOf(arg0: str) -> FocusEvent.Cause: ...

    @staticmethod
    def values() -> list[FocusEvent.Cause]: ...


class FocusListener:

  def focusGained(self, arg0: FocusEvent) -> None: ...

  def focusLost(self, arg0: FocusEvent) -> None: ...


class HierarchyBoundsListener:

  def ancestorMoved(self, arg0: HierarchyEvent) -> None: ...

  def ancestorResized(self, arg0: HierarchyEvent) -> None: ...


class HierarchyEvent(AWTEvent):

  ANCESTOR_MOVED: int

  ANCESTOR_RESIZED: int

  DISPLAYABILITY_CHANGED: int

  HIERARCHY_CHANGED: int

  HIERARCHY_FIRST: int

  HIERARCHY_LAST: int

  PARENT_CHANGED: int

  SHOWING_CHANGED: int

  def getChangeFlags(self) -> int: ...

  def getChanged(self) -> Component: ...

  def getChangedParent(self) -> Container: ...

  def getComponent(self) -> Component: ...

  def paramString(self) -> str: ...

  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: Component, arg3: Container): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: Component, arg3: Container, arg4: int): ...


class HierarchyListener:

  def hierarchyChanged(self, arg0: HierarchyEvent) -> None: ...


class InputEvent(ComponentEvent):

  ALT_DOWN_MASK: int

  ALT_GRAPH_DOWN_MASK: int

  ALT_GRAPH_MASK: int

  ALT_MASK: int

  BUTTON1_DOWN_MASK: int

  BUTTON1_MASK: int

  BUTTON2_DOWN_MASK: int

  BUTTON2_MASK: int

  BUTTON3_DOWN_MASK: int

  BUTTON3_MASK: int

  CTRL_DOWN_MASK: int

  CTRL_MASK: int

  META_DOWN_MASK: int

  META_MASK: int

  SHIFT_DOWN_MASK: int

  SHIFT_MASK: int

  def consume(self) -> None: ...

  def getModifiers(self) -> int: ...

  def getModifiersEx(self) -> int: ...

  def getWhen(self) -> int: ...

  def isAltDown(self) -> bool: ...

  def isAltGraphDown(self) -> bool: ...

  def isConsumed(self) -> bool: ...

  def isControlDown(self) -> bool: ...

  def isMetaDown(self) -> bool: ...

  def isShiftDown(self) -> bool: ...

  @staticmethod
  def getMaskForButton(arg0: int) -> int: ...

  @staticmethod
  def getModifiersExText(arg0: int) -> str: ...


class InputMethodEvent(AWTEvent):

  CARET_POSITION_CHANGED: int

  INPUT_METHOD_FIRST: int

  INPUT_METHOD_LAST: int

  INPUT_METHOD_TEXT_CHANGED: int

  def consume(self) -> None: ...

  def getCaret(self) -> TextHitInfo: ...

  def getCommittedCharacterCount(self) -> int: ...

  def getText(self) -> AttributedCharacterIterator: ...

  def getVisiblePosition(self) -> TextHitInfo: ...

  def getWhen(self) -> int: ...

  def isConsumed(self) -> bool: ...

  def paramString(self) -> str: ...

  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: TextHitInfo, arg3: TextHitInfo): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: AttributedCharacterIterator, arg3: int, arg4: TextHitInfo, arg5: TextHitInfo): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: AttributedCharacterIterator, arg4: int, arg5: TextHitInfo, arg6: TextHitInfo): ...


class InputMethodListener:

  def caretPositionChanged(self, arg0: InputMethodEvent) -> None: ...

  def inputMethodTextChanged(self, arg0: InputMethodEvent) -> None: ...


class InvocationEvent(AWTEvent):

  INVOCATION_DEFAULT: int

  INVOCATION_FIRST: int

  INVOCATION_LAST: int

  @overload
  def dispatch(self) -> None: ...

  @overload
  def dispatch(self) -> None: ...

  def getException(self) -> Exception: ...

  def getThrowable(self) -> Throwable: ...

  def getWhen(self) -> int: ...

  def isDispatched(self) -> bool: ...

  def paramString(self) -> str: ...

  @overload
  def __init__(self, arg0: object, arg1: Runnable): ...
  @overload
  def __init__(self, arg0: object, arg1: Runnable, arg2: object, arg3: bool): ...
  @overload
  def __init__(self, arg0: object, arg1: Runnable, arg2: Runnable, arg3: bool): ...


class ItemEvent(AWTEvent):

  DESELECTED: int

  ITEM_FIRST: int

  ITEM_LAST: int

  ITEM_STATE_CHANGED: int

  SELECTED: int

  def getItem(self) -> object: ...

  def getItemSelectable(self) -> ItemSelectable: ...

  def getStateChange(self) -> int: ...

  def paramString(self) -> str: ...

  def __init__(self, arg0: ItemSelectable, arg1: int, arg2: object, arg3: int): ...


class ItemListener:

  def itemStateChanged(self, arg0: ItemEvent) -> None: ...


class KeyEvent(InputEvent):

  CHAR_UNDEFINED: str

  KEY_FIRST: int

  KEY_LAST: int

  KEY_LOCATION_LEFT: int

  KEY_LOCATION_NUMPAD: int

  KEY_LOCATION_RIGHT: int

  KEY_LOCATION_STANDARD: int

  KEY_LOCATION_UNKNOWN: int

  KEY_PRESSED: int

  KEY_RELEASED: int

  KEY_TYPED: int

  VK_0: int

  VK_1: int

  VK_2: int

  VK_3: int

  VK_4: int

  VK_5: int

  VK_6: int

  VK_7: int

  VK_8: int

  VK_9: int

  VK_A: int

  VK_ACCEPT: int

  VK_ADD: int

  VK_AGAIN: int

  VK_ALL_CANDIDATES: int

  VK_ALPHANUMERIC: int

  VK_ALT: int

  VK_ALT_GRAPH: int

  VK_AMPERSAND: int

  VK_ASTERISK: int

  VK_AT: int

  VK_B: int

  VK_BACK_QUOTE: int

  VK_BACK_SLASH: int

  VK_BACK_SPACE: int

  VK_BEGIN: int

  VK_BRACELEFT: int

  VK_BRACERIGHT: int

  VK_C: int

  VK_CANCEL: int

  VK_CAPS_LOCK: int

  VK_CIRCUMFLEX: int

  VK_CLEAR: int

  VK_CLOSE_BRACKET: int

  VK_CODE_INPUT: int

  VK_COLON: int

  VK_COMMA: int

  VK_COMPOSE: int

  VK_CONTEXT_MENU: int

  VK_CONTROL: int

  VK_CONVERT: int

  VK_COPY: int

  VK_CUT: int

  VK_D: int

  VK_DEAD_ABOVEDOT: int

  VK_DEAD_ABOVERING: int

  VK_DEAD_ACUTE: int

  VK_DEAD_BREVE: int

  VK_DEAD_CARON: int

  VK_DEAD_CEDILLA: int

  VK_DEAD_CIRCUMFLEX: int

  VK_DEAD_DIAERESIS: int

  VK_DEAD_DOUBLEACUTE: int

  VK_DEAD_GRAVE: int

  VK_DEAD_IOTA: int

  VK_DEAD_MACRON: int

  VK_DEAD_OGONEK: int

  VK_DEAD_SEMIVOICED_SOUND: int

  VK_DEAD_TILDE: int

  VK_DEAD_VOICED_SOUND: int

  VK_DECIMAL: int

  VK_DELETE: int

  VK_DIVIDE: int

  VK_DOLLAR: int

  VK_DOWN: int

  VK_E: int

  VK_END: int

  VK_ENTER: int

  VK_EQUALS: int

  VK_ESCAPE: int

  VK_EURO_SIGN: int

  VK_EXCLAMATION_MARK: int

  VK_F: int

  VK_F1: int

  VK_F10: int

  VK_F11: int

  VK_F12: int

  VK_F13: int

  VK_F14: int

  VK_F15: int

  VK_F16: int

  VK_F17: int

  VK_F18: int

  VK_F19: int

  VK_F2: int

  VK_F20: int

  VK_F21: int

  VK_F22: int

  VK_F23: int

  VK_F24: int

  VK_F3: int

  VK_F4: int

  VK_F5: int

  VK_F6: int

  VK_F7: int

  VK_F8: int

  VK_F9: int

  VK_FINAL: int

  VK_FIND: int

  VK_FULL_WIDTH: int

  VK_G: int

  VK_GREATER: int

  VK_H: int

  VK_HALF_WIDTH: int

  VK_HELP: int

  VK_HIRAGANA: int

  VK_HOME: int

  VK_I: int

  VK_INPUT_METHOD_ON_OFF: int

  VK_INSERT: int

  VK_INVERTED_EXCLAMATION_MARK: int

  VK_J: int

  VK_JAPANESE_HIRAGANA: int

  VK_JAPANESE_KATAKANA: int

  VK_JAPANESE_ROMAN: int

  VK_K: int

  VK_KANA: int

  VK_KANA_LOCK: int

  VK_KANJI: int

  VK_KATAKANA: int

  VK_KP_DOWN: int

  VK_KP_LEFT: int

  VK_KP_RIGHT: int

  VK_KP_UP: int

  VK_L: int

  VK_LEFT: int

  VK_LEFT_PARENTHESIS: int

  VK_LESS: int

  VK_M: int

  VK_META: int

  VK_MINUS: int

  VK_MODECHANGE: int

  VK_MULTIPLY: int

  VK_N: int

  VK_NONCONVERT: int

  VK_NUM_LOCK: int

  VK_NUMBER_SIGN: int

  VK_NUMPAD0: int

  VK_NUMPAD1: int

  VK_NUMPAD2: int

  VK_NUMPAD3: int

  VK_NUMPAD4: int

  VK_NUMPAD5: int

  VK_NUMPAD6: int

  VK_NUMPAD7: int

  VK_NUMPAD8: int

  VK_NUMPAD9: int

  VK_O: int

  VK_OPEN_BRACKET: int

  VK_P: int

  VK_PAGE_DOWN: int

  VK_PAGE_UP: int

  VK_PASTE: int

  VK_PAUSE: int

  VK_PERIOD: int

  VK_PLUS: int

  VK_PREVIOUS_CANDIDATE: int

  VK_PRINTSCREEN: int

  VK_PROPS: int

  VK_Q: int

  VK_QUOTE: int

  VK_QUOTEDBL: int

  VK_R: int

  VK_RIGHT: int

  VK_RIGHT_PARENTHESIS: int

  VK_ROMAN_CHARACTERS: int

  VK_S: int

  VK_SCROLL_LOCK: int

  VK_SEMICOLON: int

  VK_SEPARATER: int

  VK_SEPARATOR: int

  VK_SHIFT: int

  VK_SLASH: int

  VK_SPACE: int

  VK_STOP: int

  VK_SUBTRACT: int

  VK_T: int

  VK_TAB: int

  VK_U: int

  VK_UNDEFINED: int

  VK_UNDERSCORE: int

  VK_UNDO: int

  VK_UP: int

  VK_V: int

  VK_W: int

  VK_WINDOWS: int

  VK_X: int

  VK_Y: int

  VK_Z: int

  def getExtendedKeyCode(self) -> int: ...

  def getKeyChar(self) -> str: ...

  def getKeyCode(self) -> int: ...

  def getKeyLocation(self) -> int: ...

  def isActionKey(self) -> bool: ...

  def paramString(self) -> str: ...

  def setKeyChar(self, arg0: str) -> None: ...

  def setKeyCode(self, arg0: int) -> None: ...

  def setModifiers(self, arg0: int) -> None: ...

  @staticmethod
  def getExtendedKeyCodeForChar(arg0: int) -> int: ...

  @staticmethod
  def getKeyModifiersText(arg0: int) -> str: ...

  @staticmethod
  def getKeyText(arg0: int) -> str: ...

  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: str): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: str, arg6: int): ...


class KeyListener:

  def keyPressed(self, arg0: KeyEvent) -> None: ...

  def keyReleased(self, arg0: KeyEvent) -> None: ...

  def keyTyped(self, arg0: KeyEvent) -> None: ...


class MouseEvent(InputEvent):

  BUTTON1: int

  BUTTON2: int

  BUTTON3: int

  MOUSE_CLICKED: int

  MOUSE_DRAGGED: int

  MOUSE_ENTERED: int

  MOUSE_EXITED: int

  MOUSE_FIRST: int

  MOUSE_LAST: int

  MOUSE_MOVED: int

  MOUSE_PRESSED: int

  MOUSE_RELEASED: int

  MOUSE_WHEEL: int

  NOBUTTON: int

  def getButton(self) -> int: ...

  def getClickCount(self) -> int: ...

  def getLocationOnScreen(self) -> Point: ...

  def getModifiersEx(self) -> int: ...

  def getPoint(self) -> Point: ...

  def getX(self) -> int: ...

  def getXOnScreen(self) -> int: ...

  def getY(self) -> int: ...

  def getYOnScreen(self) -> int: ...

  def isPopupTrigger(self) -> bool: ...

  def paramString(self) -> str: ...

  def translatePoint(self, arg0: int, arg1: int) -> None: ...

  @staticmethod
  def getMouseModifiersText(arg0: int) -> str: ...

  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: int): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: int): ...


class MouseListener:

  def mouseClicked(self, arg0: MouseEvent) -> None: ...

  def mouseEntered(self, arg0: MouseEvent) -> None: ...

  def mouseExited(self, arg0: MouseEvent) -> None: ...

  def mousePressed(self, arg0: MouseEvent) -> None: ...

  def mouseReleased(self, arg0: MouseEvent) -> None: ...


class MouseMotionListener:

  def mouseDragged(self, arg0: MouseEvent) -> None: ...

  def mouseMoved(self, arg0: MouseEvent) -> None: ...


class MouseWheelEvent(MouseEvent):

  WHEEL_BLOCK_SCROLL: int

  WHEEL_UNIT_SCROLL: int

  def getPreciseWheelRotation(self) -> float: ...

  def getScrollAmount(self) -> int: ...

  def getScrollType(self) -> int: ...

  def getUnitsToScroll(self) -> int: ...

  def getWheelRotation(self) -> int: ...

  def paramString(self) -> str: ...

  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: int, arg9: int, arg10: int): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: int, arg11: int, arg12: int): ...
  @overload
  def __init__(self, arg0: Component, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: int, arg11: int, arg12: int, arg13: float): ...


class MouseWheelListener:

  def mouseWheelMoved(self, arg0: MouseWheelEvent) -> None: ...


class PaintEvent(ComponentEvent):

  PAINT: int

  PAINT_FIRST: int

  PAINT_LAST: int

  UPDATE: int

  def getUpdateRect(self) -> Rectangle: ...

  def paramString(self) -> str: ...

  def setUpdateRect(self, arg0: Rectangle) -> None: ...

  def __init__(self, arg0: Component, arg1: int, arg2: Rectangle): ...


class TextEvent(AWTEvent):

  TEXT_FIRST: int

  TEXT_LAST: int

  TEXT_VALUE_CHANGED: int

  def paramString(self) -> str: ...

  def __init__(self, arg0: object, arg1: int): ...


class TextListener:

  def textValueChanged(self, arg0: TextEvent) -> None: ...


class WindowAdapter:

  @overload
  def windowActivated(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowActivated(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowClosed(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowClosed(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowClosing(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowClosing(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowDeactivated(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowDeactivated(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowDeiconified(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowDeiconified(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowGainedFocus(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowGainedFocus(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowIconified(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowIconified(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowLostFocus(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowLostFocus(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowOpened(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowOpened(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowStateChanged(self, arg0: WindowEvent) -> None: ...

  @overload
  def windowStateChanged(self, arg0: WindowEvent) -> None: ...


class WindowEvent(ComponentEvent):

  WINDOW_ACTIVATED: int

  WINDOW_CLOSED: int

  WINDOW_CLOSING: int

  WINDOW_DEACTIVATED: int

  WINDOW_DEICONIFIED: int

  WINDOW_FIRST: int

  WINDOW_GAINED_FOCUS: int

  WINDOW_ICONIFIED: int

  WINDOW_LAST: int

  WINDOW_LOST_FOCUS: int

  WINDOW_OPENED: int

  WINDOW_STATE_CHANGED: int

  def getNewState(self) -> int: ...

  def getOldState(self) -> int: ...

  def getOppositeWindow(self) -> Window: ...

  def getWindow(self) -> Window: ...

  def paramString(self) -> str: ...

  @overload
  def __init__(self, arg0: Window, arg1: int): ...
  @overload
  def __init__(self, arg0: Window, arg1: int, arg2: Window): ...
  @overload
  def __init__(self, arg0: Window, arg1: int, arg2: int, arg3: int): ...
  @overload
  def __init__(self, arg0: Window, arg1: int, arg2: Window, arg3: int, arg4: int): ...


class WindowFocusListener:

  def windowGainedFocus(self, arg0: WindowEvent) -> None: ...

  def windowLostFocus(self, arg0: WindowEvent) -> None: ...


class WindowListener:

  def windowActivated(self, arg0: WindowEvent) -> None: ...

  def windowClosed(self, arg0: WindowEvent) -> None: ...

  def windowClosing(self, arg0: WindowEvent) -> None: ...

  def windowDeactivated(self, arg0: WindowEvent) -> None: ...

  def windowDeiconified(self, arg0: WindowEvent) -> None: ...

  def windowIconified(self, arg0: WindowEvent) -> None: ...

  def windowOpened(self, arg0: WindowEvent) -> None: ...


class WindowStateListener:

  def windowStateChanged(self, arg0: WindowEvent) -> None: ...

