from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Integer
from java.nio import ByteBuffer, IntBuffer
from java.util.function import Consumer
from org.lwjgl.glfw import GLFWGamepadState

class Controller:

  def getAxisCount(self) -> int: ...

  def getAxisName(self, arg0: int) -> str: ...

  def getAxisValue(self, arg0: int) -> float: ...

  def getButtonCount(self) -> int: ...

  def getButtonName(self, arg0: int) -> str: ...

  def getDeadZone(self, arg0: int) -> float: ...

  def getGUID(self) -> str: ...

  def getGamepadName(self) -> str: ...

  def getHatCount(self) -> int: ...

  def getHatState(self) -> int: ...

  def getID(self) -> int: ...

  def getJoystickHats(self, arg0: int, arg1: ByteBuffer) -> ByteBuffer: ...

  def getJoystickName(self) -> str: ...

  def getPovX(self) -> float: ...

  def getPovY(self) -> float: ...

  def getXAxisValue(self) -> float: ...

  def getYAxisValue(self) -> float: ...

  def isButtonPressed(self, arg0: int) -> bool: ...

  def isButtonRelease(self, arg0: int) -> bool: ...

  def isGamepad(self) -> bool: ...

  def poll(self, arg0: GamepadState) -> None: ...

  def setDeadZone(self, arg0: int, arg1: float) -> None: ...

  def __init__(self, arg0: int):
    self.gamepadstate: GamepadState


class Controllers:

  MAX_AXES: int

  MAX_BUTTONS: int

  MAX_CONTROLLERS: int

  @staticmethod
  def create() -> None: ...

  @staticmethod
  def getController(arg0: int) -> Controller: ...

  @staticmethod
  def getControllerCount() -> int: ...

  @staticmethod
  def isCreated() -> bool: ...

  @staticmethod
  def poll(arg0: list[GamepadState]) -> None: ...

  @staticmethod
  def setControllerConnectedCallback(arg0: Consumer[Integer]) -> None: ...

  @staticmethod
  def setControllerDisconnectedCallback(arg0: Consumer[Integer]) -> None: ...

  @staticmethod
  def setDebugToggleControllerPluggedIn(arg0: int) -> None: ...

  def __init__(self): ...


class Cursor:

  CURSOR_8_BIT_ALPHA: int

  CURSOR_ANIMATION: int

  CURSOR_ONE_BIT_TRANSPARENCY: int

  def destroy(self) -> None: ...

  def getHandle(self) -> int: ...

  @staticmethod
  def getCapabilities() -> int: ...

  @staticmethod
  def getMaxCursorSize() -> int: ...

  @staticmethod
  def getMinCursorSize() -> int: ...

  def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: IntBuffer, arg6: IntBuffer): ...


class EventQueue: ...


class GamepadState:

  def quit(self) -> None: ...

  def set(self, arg0: GamepadState) -> None: ...

  def __init__(self):
    self.axesbuttons: GLFWGamepadState
    self.bpolled: bool
    self.hats: ByteBuffer
    self.hatstate: int


class KeyCodes:

  @staticmethod
  def toGlfwKey(arg0: int) -> int: ...

  @staticmethod
  def toLwjglKey(arg0: int) -> int: ...

  def __init__(self): ...


class KeyEventQueue:

  MAX_EVENTS: int

  def addCharEvent(self, arg0: str) -> None: ...

  def addKeyEvent(self, arg0: int, arg1: int) -> None: ...

  def getEventCharacter(self) -> str: ...

  def getEventKey(self) -> int: ...

  def getEventKeyState(self) -> bool: ...

  def getEventNanoseconds(self) -> int: ...

  def next(self) -> bool: ...

  def __init__(self): ...


class Keyboard:

  CHAR_NONE: int

  KEY_0: int

  KEY_1: int

  KEY_2: int

  KEY_3: int

  KEY_4: int

  KEY_5: int

  KEY_6: int

  KEY_7: int

  KEY_8: int

  KEY_9: int

  KEY_A: int

  KEY_ADD: int

  KEY_APOSTROPHE: int

  KEY_APPS: int

  KEY_AT: int

  KEY_AX: int

  KEY_B: int

  KEY_BACK: int

  KEY_BACKSLASH: int

  KEY_C: int

  KEY_CAPITAL: int

  KEY_CIRCUMFLEX: int

  KEY_CLEAR: int

  KEY_COLON: int

  KEY_COMMA: int

  KEY_CONVERT: int

  KEY_D: int

  KEY_DECIMAL: int

  KEY_DELETE: int

  KEY_DIVIDE: int

  KEY_DOWN: int

  KEY_E: int

  KEY_END: int

  KEY_EQUALS: int

  KEY_ESCAPE: int

  KEY_F: int

  KEY_F1: int

  KEY_F10: int

  KEY_F11: int

  KEY_F12: int

  KEY_F13: int

  KEY_F14: int

  KEY_F15: int

  KEY_F16: int

  KEY_F17: int

  KEY_F18: int

  KEY_F19: int

  KEY_F2: int

  KEY_F3: int

  KEY_F4: int

  KEY_F5: int

  KEY_F6: int

  KEY_F7: int

  KEY_F8: int

  KEY_F9: int

  KEY_FUNCTION: int

  KEY_G: int

  KEY_GRAVE: int

  KEY_H: int

  KEY_HOME: int

  KEY_I: int

  KEY_INSERT: int

  KEY_J: int

  KEY_K: int

  KEY_KANA: int

  KEY_KANJI: int

  KEY_L: int

  KEY_LBRACKET: int

  KEY_LCONTROL: int

  KEY_LEFT: int

  KEY_LMENU: int

  KEY_LMETA: int

  KEY_LSHIFT: int

  KEY_LWIN: int

  KEY_M: int

  KEY_MINUS: int

  KEY_MULTIPLY: int

  KEY_N: int

  KEY_NEXT: int

  KEY_NOCONVERT: int

  KEY_NONE: int

  KEY_NUMLOCK: int

  KEY_NUMPAD0: int

  KEY_NUMPAD1: int

  KEY_NUMPAD2: int

  KEY_NUMPAD3: int

  KEY_NUMPAD4: int

  KEY_NUMPAD5: int

  KEY_NUMPAD6: int

  KEY_NUMPAD7: int

  KEY_NUMPAD8: int

  KEY_NUMPAD9: int

  KEY_NUMPADCOMMA: int

  KEY_NUMPADENTER: int

  KEY_NUMPADEQUALS: int

  KEY_O: int

  KEY_P: int

  KEY_PAUSE: int

  KEY_PERIOD: int

  KEY_POWER: int

  KEY_PRIOR: int

  KEY_Q: int

  KEY_R: int

  KEY_RBRACKET: int

  KEY_RCONTROL: int

  KEY_RETURN: int

  KEY_RIGHT: int

  KEY_RMENU: int

  KEY_RMETA: int

  KEY_RSHIFT: int

  KEY_RWIN: int

  KEY_S: int

  KEY_SCROLL: int

  KEY_SECTION: int

  KEY_SEMICOLON: int

  KEY_SLASH: int

  KEY_SLEEP: int

  KEY_SPACE: int

  KEY_STOP: int

  KEY_SUBTRACT: int

  KEY_SYSRQ: int

  KEY_T: int

  KEY_TAB: int

  KEY_U: int

  KEY_UNDERLINE: int

  KEY_UNLABELED: int

  KEY_UP: int

  KEY_V: int

  KEY_W: int

  KEY_X: int

  KEY_Y: int

  KEY_YEN: int

  KEY_Z: int

  KEYBOARD_SIZE: int

  @staticmethod
  def addCharEvent(arg0: str) -> None: ...

  @staticmethod
  def addKeyEvent(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def areRepeatEventsEnabled() -> bool: ...

  @staticmethod
  def create() -> None: ...

  @staticmethod
  def destroy() -> None: ...

  @staticmethod
  def enableRepeatEvents(arg0: bool) -> None: ...

  @staticmethod
  def getEventCharacter() -> str: ...

  @staticmethod
  def getEventKey() -> int: ...

  @staticmethod
  def getEventKeyState() -> bool: ...

  @staticmethod
  def getEventNanoseconds() -> int: ...

  @staticmethod
  def getKeyIndex(arg0: str) -> int: ...

  @staticmethod
  def getKeyName(arg0: int) -> str: ...

  @staticmethod
  def initKeyNames() -> None: ...

  @staticmethod
  def isCreated() -> bool: ...

  @staticmethod
  def isKeyDown(arg0: int) -> bool: ...

  @staticmethod
  def isRepeatEvent() -> bool: ...

  @staticmethod
  def next() -> bool: ...

  @staticmethod
  def poll() -> None: ...

  def __init__(self): ...


class Mouse:

  @staticmethod
  def addButtonEvent(arg0: int, arg1: bool) -> None: ...

  @staticmethod
  def addMoveEvent(arg0: float, arg1: float) -> None: ...

  @staticmethod
  def create() -> None: ...

  @staticmethod
  def destroy() -> None: ...

  @staticmethod
  def getButtonCount() -> int: ...

  @staticmethod
  def getDWheel() -> int: ...

  @staticmethod
  def getDX() -> int: ...

  @staticmethod
  def getDY() -> int: ...

  @staticmethod
  def getEventButton() -> int: ...

  @staticmethod
  def getEventButtonState() -> bool: ...

  @staticmethod
  def getEventDWheel() -> int: ...

  @staticmethod
  def getEventDX() -> int: ...

  @staticmethod
  def getEventDY() -> int: ...

  @staticmethod
  def getEventNanoseconds() -> int: ...

  @staticmethod
  def getEventX() -> int: ...

  @staticmethod
  def getEventY() -> int: ...

  @staticmethod
  def getX() -> int: ...

  @staticmethod
  def getY() -> int: ...

  @staticmethod
  def isButtonDown(arg0: int) -> bool: ...

  @staticmethod
  def isCreated() -> bool: ...

  @staticmethod
  def isGrabbed() -> bool: ...

  @staticmethod
  def next() -> bool: ...

  @staticmethod
  def poll() -> None: ...

  @staticmethod
  def setClipMouseCoordinatesToWindow(arg0: bool) -> None: ...

  @staticmethod
  def setCursorPosition(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def setDWheel(arg0: float, arg1: float) -> None: ...

  @staticmethod
  def setGrabbed(arg0: bool) -> None: ...

  @staticmethod
  def setNativeCursor(arg0: Cursor) -> Cursor: ...

  @staticmethod
  def updateCursor() -> None: ...

  def __init__(self): ...

