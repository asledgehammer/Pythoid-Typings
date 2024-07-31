from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import HashSet, ArrayList
from org.lwjglx.input import Controller, KeyEventQueue, Cursor

class ControllerState:

  def getController(self, index: int) -> Controller: ...

  def isCreated(self) -> bool: ...

  def poll(self) -> None: ...

  def quit(self) -> None: ...

  def reset(self) -> None: ...

  def set(self, rhs: ControllerState) -> None: ...

  def wasPolled(self) -> bool: ...


class ControllerStateCache:

  def getState(self) -> ControllerState: ...

  def poll(self) -> None: ...

  def quit(self) -> None: ...

  def swap(self) -> None: ...

  def __init__(self): ...


class GameKeyboard:

  bNoEventsWhileLoading: bool

  doLuaKeyPressed: bool

  @staticmethod
  def eatKeyPress(key: int) -> None: ...

  @staticmethod
  def getEventQueue() -> KeyEventQueue: ...

  @staticmethod
  def getEventQueuePolling() -> KeyEventQueue: ...

  @staticmethod
  def isKeyDown(key: int) -> bool: ...

  @staticmethod
  def isKeyPressed(key: int) -> bool: ...

  @staticmethod
  def poll() -> None: ...

  @staticmethod
  def setDoLuaKeyPressed(doIt: bool) -> None: ...

  @staticmethod
  def update() -> None: ...

  @staticmethod
  def wasKeyDown(key: int) -> bool: ...

  def __init__(self): ...


class JoypadManager:

  instance: JoypadManager

  def Reset(self) -> None: ...

  def addJoypad(self, controller: int, guid: str, name: str) -> JoypadManager.Joypad: ...

  def assignJoypad(self, controller: int, player: int) -> None: ...

  def getAimingAxisX(self, c: int) -> float: ...

  def getAimingAxisY(self, c: int) -> float: ...

  def getDeadZone(self, c: int, axis: int) -> float: ...

  def getFromControllerID(self, id: int) -> JoypadManager.Joypad: ...

  def getFromPlayer(self, player: int) -> JoypadManager.Joypad: ...

  def getLastActivity(self, c: int) -> int: ...

  def getMovementAxisX(self, c: int) -> float: ...

  def getMovementAxisY(self, c: int) -> float: ...

  def isAButtonReleasePress(self, c: int) -> bool: ...

  def isAButtonStartPress(self, c: int) -> bool: ...

  def isAPressed(self, c: int) -> bool: ...

  def isBButtonReleasePress(self, c: int) -> bool: ...

  def isBButtonStartPress(self, c: int) -> bool: ...

  def isBPressed(self, c: int) -> bool: ...

  def isButtonReleasePress(self, c: int, button: int) -> bool: ...

  def isButtonStartPress(self, c: int, button: int) -> bool: ...

  def isDownPressed(self, c: int) -> bool: ...

  def isJoypadConnected(self, index: int) -> bool: ...

  def isL3Pressed(self, c: int) -> bool: ...

  def isLBPressed(self, c: int) -> bool: ...

  def isLTPressed(self, c: int) -> bool: ...

  def isLeftPressed(self, c: int) -> bool: ...

  def isR3Pressed(self, c: int) -> bool: ...

  def isRBPressed(self, c: int) -> bool: ...

  def isRTPressed(self, c: int) -> bool: ...

  def isRightPressed(self, c: int) -> bool: ...

  def isUpPressed(self, c: int) -> bool: ...

  def isXButtonReleasePress(self, c: int) -> bool: ...

  def isXButtonStartPress(self, c: int) -> bool: ...

  def isXPressed(self, c: int) -> bool: ...

  def isYButtonReleasePress(self, c: int) -> bool: ...

  def isYButtonStartPress(self, c: int) -> bool: ...

  def isYPressed(self, c: int) -> bool: ...

  def onControllerConnected(self, controller: Controller) -> None: ...

  def onControllerDisconnected(self, controller: Controller) -> None: ...

  def onPressed(self, c: int, i: int) -> None: ...

  def onPressedAxis(self, c: int, i: int) -> None: ...

  def onPressedAxisNeg(self, c: int, i: int) -> None: ...

  def onPressedPov(self, c: int) -> None: ...

  def onPressedTrigger(self, c: int, i: int) -> None: ...

  def reloadControllerFiles(self) -> None: ...

  def renderUI(self) -> None: ...

  def revertToKeyboardAndMouse(self) -> None: ...

  def saveControllerSettings(self, c: int) -> None: ...

  def setControllerActive(self, guid: str, active: bool) -> None: ...

  def setDeadZone(self, c: int, axis: int, value: float) -> None: ...

  def syncActiveControllers(self) -> None: ...

  def __init__(self):
    self.activecontrollerguids: HashSet[str]
    self.joypadlist: ArrayList[JoypadManager.Joypad]
    self.joypads: list[JoypadManager.Joypad]
    self.joypadscontroller: list[JoypadManager.Joypad]

  class Joypad:

    def getAButton(self) -> int: ...

    def getAimingAxisX(self) -> float: ...

    def getAimingAxisY(self) -> float: ...

    def getBButton(self) -> int: ...

    def getBackButton(self) -> int: ...

    def getDeadZone(self, axis: int) -> float: ...

    def getID(self) -> int: ...

    def getL3(self) -> int: ...

    def getLBumper(self) -> int: ...

    def getMovementAxisX(self) -> float: ...

    def getMovementAxisY(self) -> float: ...

    def getR3(self) -> int: ...

    def getRBumper(self) -> int: ...

    def getStartButton(self) -> int: ...

    def getXButton(self) -> int: ...

    def getYButton(self) -> int: ...

    def isAPressed(self) -> bool: ...

    def isBPressed(self) -> bool: ...

    def isButtonPressed(self, button: int) -> bool: ...

    def isButtonReleasePress(self, button: int) -> bool: ...

    def isButtonStartPress(self, button: int) -> bool: ...

    def isDisabled(self) -> bool: ...

    def isDownPressed(self) -> bool: ...

    def isL3Pressed(self) -> bool: ...

    def isLBPressed(self) -> bool: ...

    def isLTPressed(self) -> bool: ...

    def isLeftPressed(self) -> bool: ...

    def isR3Pressed(self) -> bool: ...

    def isRBPressed(self) -> bool: ...

    def isRTPressed(self) -> bool: ...

    def isRightPressed(self) -> bool: ...

    def isUpPressed(self) -> bool: ...

    def isXPressed(self) -> bool: ...

    def isYPressed(self) -> bool: ...

    def onPressed(self, i: int) -> None: ...

    def onPressedAxis(self, i: int) -> None: ...

    def onPressedAxisNeg(self, i: int) -> None: ...

    def onPressedPov(self) -> None: ...

    def onPressedTrigger(self, i: int) -> None: ...

    @overload
    def setDeadZone(self, value: float) -> None: ...

    @overload
    def setDeadZone(self, axis: int, value: float) -> None: ...

    def wasButtonPressed(self, button: int) -> bool: ...

    def __init__(self): ...


class KeyboardState:

  def getEventQueue(self) -> KeyEventQueue: ...

  def getKeyCount(self) -> int: ...

  def isCreated(self) -> bool: ...

  def isKeyDown(self, button: int) -> bool: ...

  def poll(self) -> None: ...

  def reset(self) -> None: ...

  def set(self, rhs: KeyboardState) -> None: ...

  def wasPolled(self) -> bool: ...

  def __init__(self): ...


class KeyboardStateCache:

  def getState(self) -> KeyboardState: ...

  def getStatePolling(self) -> KeyboardState: ...

  def poll(self) -> None: ...

  def swap(self) -> None: ...

  def __init__(self): ...


class Mouse:

  bLeftDown: bool

  bLeftWasDown: bool

  bMiddleDown: bool

  bMiddleWasDown: bool

  bRightDown: bool

  bRightWasDown: bool

  lastActivity: int

  m_buttonDownStates: list[bool]

  UICaptured: list[bool]

  wheelDelta: int

  @staticmethod
  def UIBlockButtonDown(number: int) -> None: ...

  @staticmethod
  def getWheelState() -> int: ...

  @staticmethod
  def getX() -> int: ...

  @staticmethod
  def getXA() -> int: ...

  @staticmethod
  def getY() -> int: ...

  @staticmethod
  def getYA() -> int: ...

  @staticmethod
  def initCustomCursor() -> None: ...

  @staticmethod
  def isButtonDown(number: int) -> bool: ...

  @staticmethod
  def isButtonDownUICheck(number: int) -> bool: ...

  @staticmethod
  def isCursorVisible() -> bool: ...

  @staticmethod
  def isLeftDown() -> bool: ...

  @staticmethod
  def isLeftPressed() -> bool: ...

  @staticmethod
  def isLeftReleased() -> bool: ...

  @staticmethod
  def isLeftUp() -> bool: ...

  @staticmethod
  def isMiddleDown() -> bool: ...

  @staticmethod
  def isMiddlePressed() -> bool: ...

  @staticmethod
  def isMiddleReleased() -> bool: ...

  @staticmethod
  def isMiddleUp() -> bool: ...

  @staticmethod
  def isRightDown() -> bool: ...

  @staticmethod
  def isRightPressed() -> bool: ...

  @staticmethod
  def isRightReleased() -> bool: ...

  @staticmethod
  def isRightUp() -> bool: ...

  @staticmethod
  def loadCursor(filename: str) -> Cursor: ...

  @staticmethod
  def poll() -> None: ...

  @staticmethod
  def renderCursorTexture() -> None: ...

  @staticmethod
  def setCursorVisible(bVisible: bool) -> None: ...

  @staticmethod
  def setXY(x: int, y: int) -> None: ...

  @staticmethod
  def update() -> None: ...

  def __init__(self): ...


class MouseState:

  def getButtonCount(self) -> int: ...

  def getDWheel(self) -> int: ...

  def getX(self) -> int: ...

  def getY(self) -> int: ...

  def isButtonDown(self, button: int) -> bool: ...

  def isCreated(self) -> bool: ...

  def poll(self) -> None: ...

  def reset(self) -> None: ...

  def resetDWheel(self) -> None: ...

  def set(self, rhs: MouseState) -> None: ...

  def setCursorPosition(self, new_x: int, new_y: int) -> None: ...

  def wasPolled(self) -> bool: ...

  def __init__(self): ...


class MouseStateCache:

  def getState(self) -> MouseState: ...

  def poll(self) -> None: ...

  def swap(self) -> None: ...

  def __init__(self): ...
