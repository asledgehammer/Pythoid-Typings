from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import PrintStream
from java.lang import CharSequence
from java.nio import ByteBuffer, DoubleBuffer, IntBuffer, FloatBuffer, ShortBuffer
from org.lwjgl import PointerBuffer
from org.lwjgl.system import SharedLibrary, Callback, Struct, MemoryStack, StructBuffer

class Callbacks:

  @staticmethod
  def glfwFreeCallbacks(arg0: int) -> None: ...


class GLFW:

  GLFW_ACCUM_ALPHA_BITS: int

  GLFW_ACCUM_BLUE_BITS: int

  GLFW_ACCUM_GREEN_BITS: int

  GLFW_ACCUM_RED_BITS: int

  GLFW_ALPHA_BITS: int

  GLFW_ANY_RELEASE_BEHAVIOR: int

  GLFW_API_UNAVAILABLE: int

  GLFW_ARROW_CURSOR: int

  GLFW_AUTO_ICONIFY: int

  GLFW_AUX_BUFFERS: int

  GLFW_BLUE_BITS: int

  GLFW_CENTER_CURSOR: int

  GLFW_CLIENT_API: int

  GLFW_COCOA_CHDIR_RESOURCES: int

  GLFW_COCOA_FRAME_NAME: int

  GLFW_COCOA_GRAPHICS_SWITCHING: int

  GLFW_COCOA_MENUBAR: int

  GLFW_COCOA_RETINA_FRAMEBUFFER: int

  GLFW_CONNECTED: int

  GLFW_CONTEXT_CREATION_API: int

  GLFW_CONTEXT_NO_ERROR: int

  GLFW_CONTEXT_RELEASE_BEHAVIOR: int

  GLFW_CONTEXT_REVISION: int

  GLFW_CONTEXT_ROBUSTNESS: int

  GLFW_CONTEXT_VERSION_MAJOR: int

  GLFW_CONTEXT_VERSION_MINOR: int

  GLFW_CROSSHAIR_CURSOR: int

  GLFW_CURSOR: int

  GLFW_CURSOR_DISABLED: int

  GLFW_CURSOR_HIDDEN: int

  GLFW_CURSOR_NORMAL: int

  GLFW_DECORATED: int

  GLFW_DEPTH_BITS: int

  GLFW_DISCONNECTED: int

  GLFW_DONT_CARE: int

  GLFW_DOUBLEBUFFER: int

  GLFW_EGL_CONTEXT_API: int

  GLFW_FALSE: int

  GLFW_FLOATING: int

  GLFW_FOCUS_ON_SHOW: int

  GLFW_FOCUSED: int

  GLFW_FORMAT_UNAVAILABLE: int

  GLFW_GAMEPAD_AXIS_LAST: int

  GLFW_GAMEPAD_AXIS_LEFT_TRIGGER: int

  GLFW_GAMEPAD_AXIS_LEFT_X: int

  GLFW_GAMEPAD_AXIS_LEFT_Y: int

  GLFW_GAMEPAD_AXIS_RIGHT_TRIGGER: int

  GLFW_GAMEPAD_AXIS_RIGHT_X: int

  GLFW_GAMEPAD_AXIS_RIGHT_Y: int

  GLFW_GAMEPAD_BUTTON_A: int

  GLFW_GAMEPAD_BUTTON_B: int

  GLFW_GAMEPAD_BUTTON_BACK: int

  GLFW_GAMEPAD_BUTTON_CIRCLE: int

  GLFW_GAMEPAD_BUTTON_CROSS: int

  GLFW_GAMEPAD_BUTTON_DPAD_DOWN: int

  GLFW_GAMEPAD_BUTTON_DPAD_LEFT: int

  GLFW_GAMEPAD_BUTTON_DPAD_RIGHT: int

  GLFW_GAMEPAD_BUTTON_DPAD_UP: int

  GLFW_GAMEPAD_BUTTON_GUIDE: int

  GLFW_GAMEPAD_BUTTON_LAST: int

  GLFW_GAMEPAD_BUTTON_LEFT_BUMPER: int

  GLFW_GAMEPAD_BUTTON_LEFT_THUMB: int

  GLFW_GAMEPAD_BUTTON_RIGHT_BUMPER: int

  GLFW_GAMEPAD_BUTTON_RIGHT_THUMB: int

  GLFW_GAMEPAD_BUTTON_SQUARE: int

  GLFW_GAMEPAD_BUTTON_START: int

  GLFW_GAMEPAD_BUTTON_TRIANGLE: int

  GLFW_GAMEPAD_BUTTON_X: int

  GLFW_GAMEPAD_BUTTON_Y: int

  GLFW_GREEN_BITS: int

  GLFW_HAND_CURSOR: int

  GLFW_HAT_CENTERED: int

  GLFW_HAT_DOWN: int

  GLFW_HAT_LEFT: int

  GLFW_HAT_LEFT_DOWN: int

  GLFW_HAT_LEFT_UP: int

  GLFW_HAT_RIGHT: int

  GLFW_HAT_RIGHT_DOWN: int

  GLFW_HAT_RIGHT_UP: int

  GLFW_HAT_UP: int

  GLFW_HOVERED: int

  GLFW_HRESIZE_CURSOR: int

  GLFW_IBEAM_CURSOR: int

  GLFW_ICONIFIED: int

  GLFW_INVALID_ENUM: int

  GLFW_INVALID_VALUE: int

  GLFW_JOYSTICK_1: int

  GLFW_JOYSTICK_10: int

  GLFW_JOYSTICK_11: int

  GLFW_JOYSTICK_12: int

  GLFW_JOYSTICK_13: int

  GLFW_JOYSTICK_14: int

  GLFW_JOYSTICK_15: int

  GLFW_JOYSTICK_16: int

  GLFW_JOYSTICK_2: int

  GLFW_JOYSTICK_3: int

  GLFW_JOYSTICK_4: int

  GLFW_JOYSTICK_5: int

  GLFW_JOYSTICK_6: int

  GLFW_JOYSTICK_7: int

  GLFW_JOYSTICK_8: int

  GLFW_JOYSTICK_9: int

  GLFW_JOYSTICK_HAT_BUTTONS: int

  GLFW_JOYSTICK_LAST: int

  GLFW_KEY_0: int

  GLFW_KEY_1: int

  GLFW_KEY_2: int

  GLFW_KEY_3: int

  GLFW_KEY_4: int

  GLFW_KEY_5: int

  GLFW_KEY_6: int

  GLFW_KEY_7: int

  GLFW_KEY_8: int

  GLFW_KEY_9: int

  GLFW_KEY_A: int

  GLFW_KEY_APOSTROPHE: int

  GLFW_KEY_B: int

  GLFW_KEY_BACKSLASH: int

  GLFW_KEY_BACKSPACE: int

  GLFW_KEY_C: int

  GLFW_KEY_CAPS_LOCK: int

  GLFW_KEY_COMMA: int

  GLFW_KEY_D: int

  GLFW_KEY_DELETE: int

  GLFW_KEY_DOWN: int

  GLFW_KEY_E: int

  GLFW_KEY_END: int

  GLFW_KEY_ENTER: int

  GLFW_KEY_EQUAL: int

  GLFW_KEY_ESCAPE: int

  GLFW_KEY_F: int

  GLFW_KEY_F1: int

  GLFW_KEY_F10: int

  GLFW_KEY_F11: int

  GLFW_KEY_F12: int

  GLFW_KEY_F13: int

  GLFW_KEY_F14: int

  GLFW_KEY_F15: int

  GLFW_KEY_F16: int

  GLFW_KEY_F17: int

  GLFW_KEY_F18: int

  GLFW_KEY_F19: int

  GLFW_KEY_F2: int

  GLFW_KEY_F20: int

  GLFW_KEY_F21: int

  GLFW_KEY_F22: int

  GLFW_KEY_F23: int

  GLFW_KEY_F24: int

  GLFW_KEY_F25: int

  GLFW_KEY_F3: int

  GLFW_KEY_F4: int

  GLFW_KEY_F5: int

  GLFW_KEY_F6: int

  GLFW_KEY_F7: int

  GLFW_KEY_F8: int

  GLFW_KEY_F9: int

  GLFW_KEY_G: int

  GLFW_KEY_GRAVE_ACCENT: int

  GLFW_KEY_H: int

  GLFW_KEY_HOME: int

  GLFW_KEY_I: int

  GLFW_KEY_INSERT: int

  GLFW_KEY_J: int

  GLFW_KEY_K: int

  GLFW_KEY_KP_0: int

  GLFW_KEY_KP_1: int

  GLFW_KEY_KP_2: int

  GLFW_KEY_KP_3: int

  GLFW_KEY_KP_4: int

  GLFW_KEY_KP_5: int

  GLFW_KEY_KP_6: int

  GLFW_KEY_KP_7: int

  GLFW_KEY_KP_8: int

  GLFW_KEY_KP_9: int

  GLFW_KEY_KP_ADD: int

  GLFW_KEY_KP_DECIMAL: int

  GLFW_KEY_KP_DIVIDE: int

  GLFW_KEY_KP_ENTER: int

  GLFW_KEY_KP_EQUAL: int

  GLFW_KEY_KP_MULTIPLY: int

  GLFW_KEY_KP_SUBTRACT: int

  GLFW_KEY_L: int

  GLFW_KEY_LAST: int

  GLFW_KEY_LEFT: int

  GLFW_KEY_LEFT_ALT: int

  GLFW_KEY_LEFT_BRACKET: int

  GLFW_KEY_LEFT_CONTROL: int

  GLFW_KEY_LEFT_SHIFT: int

  GLFW_KEY_LEFT_SUPER: int

  GLFW_KEY_M: int

  GLFW_KEY_MENU: int

  GLFW_KEY_MINUS: int

  GLFW_KEY_N: int

  GLFW_KEY_NUM_LOCK: int

  GLFW_KEY_O: int

  GLFW_KEY_P: int

  GLFW_KEY_PAGE_DOWN: int

  GLFW_KEY_PAGE_UP: int

  GLFW_KEY_PAUSE: int

  GLFW_KEY_PERIOD: int

  GLFW_KEY_PRINT_SCREEN: int

  GLFW_KEY_Q: int

  GLFW_KEY_R: int

  GLFW_KEY_RIGHT: int

  GLFW_KEY_RIGHT_ALT: int

  GLFW_KEY_RIGHT_BRACKET: int

  GLFW_KEY_RIGHT_CONTROL: int

  GLFW_KEY_RIGHT_SHIFT: int

  GLFW_KEY_RIGHT_SUPER: int

  GLFW_KEY_S: int

  GLFW_KEY_SCROLL_LOCK: int

  GLFW_KEY_SEMICOLON: int

  GLFW_KEY_SLASH: int

  GLFW_KEY_SPACE: int

  GLFW_KEY_T: int

  GLFW_KEY_TAB: int

  GLFW_KEY_U: int

  GLFW_KEY_UNKNOWN: int

  GLFW_KEY_UP: int

  GLFW_KEY_V: int

  GLFW_KEY_W: int

  GLFW_KEY_WORLD_1: int

  GLFW_KEY_WORLD_2: int

  GLFW_KEY_X: int

  GLFW_KEY_Y: int

  GLFW_KEY_Z: int

  GLFW_LOCK_KEY_MODS: int

  GLFW_LOSE_CONTEXT_ON_RESET: int

  GLFW_MAXIMIZED: int

  GLFW_MOD_ALT: int

  GLFW_MOD_CAPS_LOCK: int

  GLFW_MOD_CONTROL: int

  GLFW_MOD_NUM_LOCK: int

  GLFW_MOD_SHIFT: int

  GLFW_MOD_SUPER: int

  GLFW_MOUSE_BUTTON_1: int

  GLFW_MOUSE_BUTTON_2: int

  GLFW_MOUSE_BUTTON_3: int

  GLFW_MOUSE_BUTTON_4: int

  GLFW_MOUSE_BUTTON_5: int

  GLFW_MOUSE_BUTTON_6: int

  GLFW_MOUSE_BUTTON_7: int

  GLFW_MOUSE_BUTTON_8: int

  GLFW_MOUSE_BUTTON_LAST: int

  GLFW_MOUSE_BUTTON_LEFT: int

  GLFW_MOUSE_BUTTON_MIDDLE: int

  GLFW_MOUSE_BUTTON_RIGHT: int

  GLFW_NATIVE_CONTEXT_API: int

  GLFW_NO_API: int

  GLFW_NO_CURRENT_CONTEXT: int

  GLFW_NO_ERROR: int

  GLFW_NO_RESET_NOTIFICATION: int

  GLFW_NO_ROBUSTNESS: int

  GLFW_NO_WINDOW_CONTEXT: int

  GLFW_NOT_INITIALIZED: int

  GLFW_OPENGL_ANY_PROFILE: int

  GLFW_OPENGL_API: int

  GLFW_OPENGL_COMPAT_PROFILE: int

  GLFW_OPENGL_CORE_PROFILE: int

  GLFW_OPENGL_DEBUG_CONTEXT: int

  GLFW_OPENGL_ES_API: int

  GLFW_OPENGL_FORWARD_COMPAT: int

  GLFW_OPENGL_PROFILE: int

  GLFW_OSMESA_CONTEXT_API: int

  GLFW_OUT_OF_MEMORY: int

  GLFW_PLATFORM_ERROR: int

  GLFW_PRESS: int

  GLFW_RAW_MOUSE_MOTION: int

  GLFW_RED_BITS: int

  GLFW_REFRESH_RATE: int

  GLFW_RELEASE: int

  GLFW_RELEASE_BEHAVIOR_FLUSH: int

  GLFW_RELEASE_BEHAVIOR_NONE: int

  GLFW_REPEAT: int

  GLFW_RESIZABLE: int

  GLFW_SAMPLES: int

  GLFW_SCALE_TO_MONITOR: int

  GLFW_SRGB_CAPABLE: int

  GLFW_STENCIL_BITS: int

  GLFW_STEREO: int

  GLFW_STICKY_KEYS: int

  GLFW_STICKY_MOUSE_BUTTONS: int

  GLFW_TRANSPARENT_FRAMEBUFFER: int

  GLFW_TRUE: int

  GLFW_VERSION_MAJOR: int

  GLFW_VERSION_MINOR: int

  GLFW_VERSION_REVISION: int

  GLFW_VERSION_UNAVAILABLE: int

  GLFW_VISIBLE: int

  GLFW_VRESIZE_CURSOR: int

  GLFW_X11_CLASS_NAME: int

  GLFW_X11_INSTANCE_NAME: int

  @staticmethod
  def getLibrary() -> SharedLibrary: ...

  @staticmethod
  def glfwCreateCursor(arg0: GLFWImage, arg1: int, arg2: int) -> int: ...

  @staticmethod
  def glfwCreateStandardCursor(arg0: int) -> int: ...

  @staticmethod
  @overload
  def glfwCreateWindow(arg0: int, arg1: int, arg2: CharSequence, arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def glfwCreateWindow(arg0: int, arg1: int, arg2: ByteBuffer, arg3: int, arg4: int) -> int: ...

  @staticmethod
  def glfwDefaultWindowHints() -> None: ...

  @staticmethod
  def glfwDestroyCursor(arg0: int) -> None: ...

  @staticmethod
  def glfwDestroyWindow(arg0: int) -> None: ...

  @staticmethod
  @overload
  def glfwExtensionSupported(arg0: CharSequence) -> bool: ...

  @staticmethod
  @overload
  def glfwExtensionSupported(arg0: ByteBuffer) -> bool: ...

  @staticmethod
  def glfwFocusWindow(arg0: int) -> None: ...

  @staticmethod
  def glfwGetClipboardString(arg0: int) -> str: ...

  @staticmethod
  def glfwGetCurrentContext() -> int: ...

  @staticmethod
  @overload
  def glfwGetCursorPos(arg0: int, arg1: list[float], arg2: list[float]) -> None: ...

  @staticmethod
  @overload
  def glfwGetCursorPos(arg0: int, arg1: DoubleBuffer, arg2: DoubleBuffer) -> None: ...

  @staticmethod
  def glfwGetError(arg0: PointerBuffer) -> int: ...

  @staticmethod
  @overload
  def glfwGetFramebufferSize(arg0: int, arg1: list[int], arg2: list[int]) -> None: ...

  @staticmethod
  @overload
  def glfwGetFramebufferSize(arg0: int, arg1: IntBuffer, arg2: IntBuffer) -> None: ...

  @staticmethod
  def glfwGetGamepadName(arg0: int) -> str: ...

  @staticmethod
  def glfwGetGamepadState(arg0: int, arg1: GLFWGamepadState) -> bool: ...

  @staticmethod
  def glfwGetGammaRamp(arg0: int) -> GLFWGammaRamp: ...

  @staticmethod
  def glfwGetInputMode(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def glfwGetJoystickAxes(arg0: int) -> FloatBuffer: ...

  @staticmethod
  def glfwGetJoystickButtons(arg0: int) -> ByteBuffer: ...

  @staticmethod
  def glfwGetJoystickGUID(arg0: int) -> str: ...

  @staticmethod
  def glfwGetJoystickHats(arg0: int) -> ByteBuffer: ...

  @staticmethod
  def glfwGetJoystickName(arg0: int) -> str: ...

  @staticmethod
  def glfwGetJoystickUserPointer(arg0: int) -> int: ...

  @staticmethod
  def glfwGetKey(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def glfwGetKeyName(arg0: int, arg1: int) -> str: ...

  @staticmethod
  def glfwGetKeyScancode(arg0: int) -> int: ...

  @staticmethod
  @overload
  def glfwGetMonitorContentScale(arg0: int, arg1: list[float], arg2: list[float]) -> None: ...

  @staticmethod
  @overload
  def glfwGetMonitorContentScale(arg0: int, arg1: FloatBuffer, arg2: FloatBuffer) -> None: ...

  @staticmethod
  def glfwGetMonitorName(arg0: int) -> str: ...

  @staticmethod
  @overload
  def glfwGetMonitorPhysicalSize(arg0: int, arg1: list[int], arg2: list[int]) -> None: ...

  @staticmethod
  @overload
  def glfwGetMonitorPhysicalSize(arg0: int, arg1: IntBuffer, arg2: IntBuffer) -> None: ...

  @staticmethod
  @overload
  def glfwGetMonitorPos(arg0: int, arg1: list[int], arg2: list[int]) -> None: ...

  @staticmethod
  @overload
  def glfwGetMonitorPos(arg0: int, arg1: IntBuffer, arg2: IntBuffer) -> None: ...

  @staticmethod
  def glfwGetMonitorUserPointer(arg0: int) -> int: ...

  @staticmethod
  @overload
  def glfwGetMonitorWorkarea(arg0: int, arg1: list[int], arg2: list[int], arg3: list[int], arg4: list[int]) -> None: ...

  @staticmethod
  @overload
  def glfwGetMonitorWorkarea(arg0: int, arg1: IntBuffer, arg2: IntBuffer, arg3: IntBuffer, arg4: IntBuffer) -> None: ...

  @staticmethod
  def glfwGetMonitors() -> PointerBuffer: ...

  @staticmethod
  def glfwGetMouseButton(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def glfwGetPrimaryMonitor() -> int: ...

  @staticmethod
  @overload
  def glfwGetProcAddress(arg0: CharSequence) -> int: ...

  @staticmethod
  @overload
  def glfwGetProcAddress(arg0: ByteBuffer) -> int: ...

  @staticmethod
  def glfwGetTime() -> float: ...

  @staticmethod
  def glfwGetTimerFrequency() -> int: ...

  @staticmethod
  def glfwGetTimerValue() -> int: ...

  @staticmethod
  @overload
  def glfwGetVersion(arg0: list[int], arg1: list[int], arg2: list[int]) -> None: ...

  @staticmethod
  @overload
  def glfwGetVersion(arg0: IntBuffer, arg1: IntBuffer, arg2: IntBuffer) -> None: ...

  @staticmethod
  def glfwGetVersionString() -> str: ...

  @staticmethod
  def glfwGetVideoMode(arg0: int) -> GLFWVidMode: ...

  @staticmethod
  def glfwGetVideoModes(arg0: int) -> GLFWVidMode.Buffer: ...

  @staticmethod
  def glfwGetWindowAttrib(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def glfwGetWindowContentScale(arg0: int, arg1: list[float], arg2: list[float]) -> None: ...

  @staticmethod
  @overload
  def glfwGetWindowContentScale(arg0: int, arg1: FloatBuffer, arg2: FloatBuffer) -> None: ...

  @staticmethod
  @overload
  def glfwGetWindowFrameSize(arg0: int, arg1: list[int], arg2: list[int], arg3: list[int], arg4: list[int]) -> None: ...

  @staticmethod
  @overload
  def glfwGetWindowFrameSize(arg0: int, arg1: IntBuffer, arg2: IntBuffer, arg3: IntBuffer, arg4: IntBuffer) -> None: ...

  @staticmethod
  def glfwGetWindowMonitor(arg0: int) -> int: ...

  @staticmethod
  def glfwGetWindowOpacity(arg0: int) -> float: ...

  @staticmethod
  @overload
  def glfwGetWindowPos(arg0: int, arg1: list[int], arg2: list[int]) -> None: ...

  @staticmethod
  @overload
  def glfwGetWindowPos(arg0: int, arg1: IntBuffer, arg2: IntBuffer) -> None: ...

  @staticmethod
  @overload
  def glfwGetWindowSize(arg0: int, arg1: list[int], arg2: list[int]) -> None: ...

  @staticmethod
  @overload
  def glfwGetWindowSize(arg0: int, arg1: IntBuffer, arg2: IntBuffer) -> None: ...

  @staticmethod
  def glfwGetWindowUserPointer(arg0: int) -> int: ...

  @staticmethod
  def glfwHideWindow(arg0: int) -> None: ...

  @staticmethod
  def glfwIconifyWindow(arg0: int) -> None: ...

  @staticmethod
  def glfwInit() -> bool: ...

  @staticmethod
  def glfwInitHint(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def glfwJoystickIsGamepad(arg0: int) -> bool: ...

  @staticmethod
  def glfwJoystickPresent(arg0: int) -> bool: ...

  @staticmethod
  def glfwMakeContextCurrent(arg0: int) -> None: ...

  @staticmethod
  def glfwMaximizeWindow(arg0: int) -> None: ...

  @staticmethod
  def glfwPollEvents() -> None: ...

  @staticmethod
  def glfwPostEmptyEvent() -> None: ...

  @staticmethod
  def glfwRawMouseMotionSupported() -> bool: ...

  @staticmethod
  def glfwRequestWindowAttention(arg0: int) -> None: ...

  @staticmethod
  def glfwRestoreWindow(arg0: int) -> None: ...

  @staticmethod
  def glfwSetCharCallback(arg0: int, arg1: GLFWCharCallbackI) -> GLFWCharCallback: ...

  @staticmethod
  def glfwSetCharModsCallback(arg0: int, arg1: GLFWCharModsCallbackI) -> GLFWCharModsCallback: ...

  @staticmethod
  @overload
  def glfwSetClipboardString(arg0: int, arg1: CharSequence) -> None: ...

  @staticmethod
  @overload
  def glfwSetClipboardString(arg0: int, arg1: ByteBuffer) -> None: ...

  @staticmethod
  def glfwSetCursor(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def glfwSetCursorEnterCallback(arg0: int, arg1: GLFWCursorEnterCallbackI) -> GLFWCursorEnterCallback: ...

  @staticmethod
  def glfwSetCursorPos(arg0: int, arg1: float, arg2: float) -> None: ...

  @staticmethod
  def glfwSetCursorPosCallback(arg0: int, arg1: GLFWCursorPosCallbackI) -> GLFWCursorPosCallback: ...

  @staticmethod
  def glfwSetDropCallback(arg0: int, arg1: GLFWDropCallbackI) -> GLFWDropCallback: ...

  @staticmethod
  def glfwSetErrorCallback(arg0: GLFWErrorCallbackI) -> GLFWErrorCallback: ...

  @staticmethod
  def glfwSetFramebufferSizeCallback(arg0: int, arg1: GLFWFramebufferSizeCallbackI) -> GLFWFramebufferSizeCallback: ...

  @staticmethod
  def glfwSetGamma(arg0: int, arg1: float) -> None: ...

  @staticmethod
  def glfwSetGammaRamp(arg0: int, arg1: GLFWGammaRamp) -> None: ...

  @staticmethod
  def glfwSetInputMode(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def glfwSetJoystickCallback(arg0: GLFWJoystickCallbackI) -> GLFWJoystickCallback: ...

  @staticmethod
  def glfwSetJoystickUserPointer(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def glfwSetKeyCallback(arg0: int, arg1: GLFWKeyCallbackI) -> GLFWKeyCallback: ...

  @staticmethod
  def glfwSetMonitorCallback(arg0: GLFWMonitorCallbackI) -> GLFWMonitorCallback: ...

  @staticmethod
  def glfwSetMonitorUserPointer(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def glfwSetMouseButtonCallback(arg0: int, arg1: GLFWMouseButtonCallbackI) -> GLFWMouseButtonCallback: ...

  @staticmethod
  def glfwSetScrollCallback(arg0: int, arg1: GLFWScrollCallbackI) -> GLFWScrollCallback: ...

  @staticmethod
  def glfwSetTime(arg0: float) -> None: ...

  @staticmethod
  def glfwSetWindowAspectRatio(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def glfwSetWindowAttrib(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def glfwSetWindowCloseCallback(arg0: int, arg1: GLFWWindowCloseCallbackI) -> GLFWWindowCloseCallback: ...

  @staticmethod
  def glfwSetWindowContentScaleCallback(arg0: int, arg1: GLFWWindowContentScaleCallbackI) -> GLFWWindowContentScaleCallback: ...

  @staticmethod
  def glfwSetWindowFocusCallback(arg0: int, arg1: GLFWWindowFocusCallbackI) -> GLFWWindowFocusCallback: ...

  @staticmethod
  def glfwSetWindowIcon(arg0: int, arg1: GLFWImage.Buffer) -> None: ...

  @staticmethod
  def glfwSetWindowIconifyCallback(arg0: int, arg1: GLFWWindowIconifyCallbackI) -> GLFWWindowIconifyCallback: ...

  @staticmethod
  def glfwSetWindowMaximizeCallback(arg0: int, arg1: GLFWWindowMaximizeCallbackI) -> GLFWWindowMaximizeCallback: ...

  @staticmethod
  def glfwSetWindowMonitor(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> None: ...

  @staticmethod
  def glfwSetWindowOpacity(arg0: int, arg1: float) -> None: ...

  @staticmethod
  def glfwSetWindowPos(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def glfwSetWindowPosCallback(arg0: int, arg1: GLFWWindowPosCallbackI) -> GLFWWindowPosCallback: ...

  @staticmethod
  def glfwSetWindowRefreshCallback(arg0: int, arg1: GLFWWindowRefreshCallbackI) -> GLFWWindowRefreshCallback: ...

  @staticmethod
  def glfwSetWindowShouldClose(arg0: int, arg1: bool) -> None: ...

  @staticmethod
  def glfwSetWindowSize(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def glfwSetWindowSizeCallback(arg0: int, arg1: GLFWWindowSizeCallbackI) -> GLFWWindowSizeCallback: ...

  @staticmethod
  def glfwSetWindowSizeLimits(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...

  @staticmethod
  @overload
  def glfwSetWindowTitle(arg0: int, arg1: CharSequence) -> None: ...

  @staticmethod
  @overload
  def glfwSetWindowTitle(arg0: int, arg1: ByteBuffer) -> None: ...

  @staticmethod
  def glfwSetWindowUserPointer(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def glfwShowWindow(arg0: int) -> None: ...

  @staticmethod
  def glfwSwapBuffers(arg0: int) -> None: ...

  @staticmethod
  def glfwSwapInterval(arg0: int) -> None: ...

  @staticmethod
  def glfwTerminate() -> None: ...

  @staticmethod
  def glfwUpdateGamepadMappings(arg0: ByteBuffer) -> bool: ...

  @staticmethod
  def glfwWaitEvents() -> None: ...

  @staticmethod
  def glfwWaitEventsTimeout(arg0: float) -> None: ...

  @staticmethod
  def glfwWindowHint(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def glfwWindowHintString(arg0: int, arg1: CharSequence) -> None: ...

  @staticmethod
  @overload
  def glfwWindowHintString(arg0: int, arg1: ByteBuffer) -> None: ...

  @staticmethod
  def glfwWindowShouldClose(arg0: int) -> bool: ...

  @staticmethod
  def nglfwCreateCursor(arg0: int, arg1: int, arg2: int) -> int: ...

  @staticmethod
  def nglfwCreateWindow(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int: ...

  @staticmethod
  def nglfwExtensionSupported(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetClipboardString(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetCursorPos(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def nglfwGetError(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetFramebufferSize(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def nglfwGetGamepadName(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetGamepadState(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwGetGammaRamp(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetJoystickAxes(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwGetJoystickButtons(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwGetJoystickGUID(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetJoystickHats(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwGetJoystickName(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetKeyName(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwGetMonitorContentScale(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def nglfwGetMonitorName(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetMonitorPhysicalSize(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def nglfwGetMonitorPos(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def nglfwGetMonitorWorkarea(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...

  @staticmethod
  def nglfwGetMonitors(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetProcAddress(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetVersion(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def nglfwGetVersionString() -> int: ...

  @staticmethod
  def nglfwGetVideoMode(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetVideoModes(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwGetWindowContentScale(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def nglfwGetWindowFrameSize(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...

  @staticmethod
  def nglfwGetWindowPos(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def nglfwGetWindowSize(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def nglfwSetCharCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetCharModsCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetClipboardString(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def nglfwSetCursorEnterCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetCursorPosCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetDropCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetErrorCallback(arg0: int) -> int: ...

  @staticmethod
  def nglfwSetFramebufferSizeCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetGammaRamp(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def nglfwSetJoystickCallback(arg0: int) -> int: ...

  @staticmethod
  def nglfwSetKeyCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetMonitorCallback(arg0: int) -> int: ...

  @staticmethod
  def nglfwSetMouseButtonCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetScrollCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetWindowCloseCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetWindowContentScaleCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetWindowFocusCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetWindowIcon(arg0: int, arg1: int, arg2: int) -> None: ...

  @staticmethod
  def nglfwSetWindowIconifyCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetWindowMaximizeCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetWindowPosCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetWindowRefreshCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetWindowSizeCallback(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def nglfwSetWindowTitle(arg0: int, arg1: int) -> None: ...

  @staticmethod
  def nglfwUpdateGamepadMappings(arg0: int) -> int: ...

  @staticmethod
  def nglfwWindowHintString(arg0: int, arg1: int) -> None: ...

  class Functions:

    CreateCursor: int

    CreateStandardCursor: int

    CreateWindow: int

    DefaultWindowHints: int

    DestroyCursor: int

    DestroyWindow: int

    ExtensionSupported: int

    FocusWindow: int

    GetClipboardString: int

    GetCurrentContext: int

    GetCursorPos: int

    GetError: int

    GetFramebufferSize: int

    GetGamepadName: int

    GetGamepadState: int

    GetGammaRamp: int

    GetInputMode: int

    GetJoystickAxes: int

    GetJoystickButtons: int

    GetJoystickGUID: int

    GetJoystickHats: int

    GetJoystickName: int

    GetJoystickUserPointer: int

    GetKey: int

    GetKeyName: int

    GetKeyScancode: int

    GetMonitorContentScale: int

    GetMonitorName: int

    GetMonitorPhysicalSize: int

    GetMonitorPos: int

    GetMonitors: int

    GetMonitorUserPointer: int

    GetMonitorWorkarea: int

    GetMouseButton: int

    GetPrimaryMonitor: int

    GetProcAddress: int

    GetTime: int

    GetTimerFrequency: int

    GetTimerValue: int

    GetVersion: int

    GetVersionString: int

    GetVideoMode: int

    GetVideoModes: int

    GetWindowAttrib: int

    GetWindowContentScale: int

    GetWindowFrameSize: int

    GetWindowMonitor: int

    GetWindowOpacity: int

    GetWindowPos: int

    GetWindowSize: int

    GetWindowUserPointer: int

    HideWindow: int

    IconifyWindow: int

    Init: int

    InitHint: int

    JoystickIsGamepad: int

    JoystickPresent: int

    MakeContextCurrent: int

    MaximizeWindow: int

    PollEvents: int

    PostEmptyEvent: int

    RawMouseMotionSupported: int

    RequestWindowAttention: int

    RestoreWindow: int

    SetCharCallback: int

    SetCharModsCallback: int

    SetClipboardString: int

    SetCursor: int

    SetCursorEnterCallback: int

    SetCursorPos: int

    SetCursorPosCallback: int

    SetDropCallback: int

    SetErrorCallback: int

    SetFramebufferSizeCallback: int

    SetGamma: int

    SetGammaRamp: int

    SetInputMode: int

    SetJoystickCallback: int

    SetJoystickUserPointer: int

    SetKeyCallback: int

    SetMonitorCallback: int

    SetMonitorUserPointer: int

    SetMouseButtonCallback: int

    SetScrollCallback: int

    SetTime: int

    SetWindowAspectRatio: int

    SetWindowAttrib: int

    SetWindowCloseCallback: int

    SetWindowContentScaleCallback: int

    SetWindowFocusCallback: int

    SetWindowIcon: int

    SetWindowIconifyCallback: int

    SetWindowMaximizeCallback: int

    SetWindowMonitor: int

    SetWindowOpacity: int

    SetWindowPos: int

    SetWindowPosCallback: int

    SetWindowRefreshCallback: int

    SetWindowShouldClose: int

    SetWindowSize: int

    SetWindowSizeCallback: int

    SetWindowSizeLimits: int

    SetWindowTitle: int

    SetWindowUserPointer: int

    ShowWindow: int

    SwapBuffers: int

    SwapInterval: int

    Terminate: int

    UpdateGamepadMappings: int

    WaitEvents: int

    WaitEventsTimeout: int

    WindowHint: int

    WindowHintString: int

    WindowShouldClose: int


class GLFWCharCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...

  def set(self, arg0: int) -> GLFWCharCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWCharCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWCharCallbackI) -> GLFWCharCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWCharCallback: ...

  class Container(GLFWCharCallback):

    def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWCharCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWCharModsCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...

  def set(self, arg0: int) -> GLFWCharModsCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWCharModsCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWCharModsCallbackI) -> GLFWCharModsCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWCharModsCallback: ...

  class Container(GLFWCharModsCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWCharModsCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWCursorEnterCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...

  def set(self, arg0: int) -> GLFWCursorEnterCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWCursorEnterCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWCursorEnterCallbackI) -> GLFWCursorEnterCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWCursorEnterCallback: ...

  class Container(GLFWCursorEnterCallback):

    def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWCursorEnterCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWCursorPosCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...

  def set(self, arg0: int) -> GLFWCursorPosCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWCursorPosCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWCursorPosCallbackI) -> GLFWCursorPosCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWCursorPosCallback: ...

  class Container(GLFWCursorPosCallback):

    def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...


class GLFWCursorPosCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...


class GLFWDropCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...

  def set(self, arg0: int) -> GLFWDropCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWDropCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWDropCallbackI) -> GLFWDropCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWDropCallback: ...

  @staticmethod
  def getName(arg0: int, arg1: int) -> str: ...

  class Container(GLFWDropCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWDropCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWErrorCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...

  def set(self) -> GLFWErrorCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWErrorCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWErrorCallbackI) -> GLFWErrorCallback: ...

  @staticmethod
  @overload
  def createPrint() -> GLFWErrorCallback: ...

  @staticmethod
  @overload
  def createPrint(arg0: PrintStream) -> GLFWErrorCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWErrorCallback: ...

  @staticmethod
  def createThrow() -> GLFWErrorCallback: ...

  @staticmethod
  def getDescription(arg0: int) -> str: ...

  class Container(GLFWErrorCallback):

    def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWErrorCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWFramebufferSizeCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...

  def set(self, arg0: int) -> GLFWFramebufferSizeCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWFramebufferSizeCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWFramebufferSizeCallbackI) -> GLFWFramebufferSizeCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWFramebufferSizeCallback: ...

  class Container(GLFWFramebufferSizeCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWFramebufferSizeCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWGamepadState(Struct):

  ALIGNOF: int

  @overload
  def axes(self) -> FloatBuffer: ...

  @overload
  def axes(self, arg0: int) -> float: ...

  @overload
  def axes(self, arg0: FloatBuffer) -> GLFWGamepadState: ...

  @overload
  def axes(self, arg0: int, arg1: float) -> GLFWGamepadState: ...

  @overload
  def buttons(self) -> ByteBuffer: ...

  @overload
  def buttons(self, arg0: int) -> int: ...

  @overload
  def buttons(self, arg0: ByteBuffer) -> GLFWGamepadState: ...

  @overload
  def buttons(self, arg0: int, arg1: int) -> GLFWGamepadState: ...

  def close(self) -> None: ...

  def free(self) -> None: ...

  @overload
  def set(self, arg0: GLFWGamepadState) -> GLFWGamepadState: ...

  @overload
  def set(self, arg0: ByteBuffer, arg1: FloatBuffer) -> GLFWGamepadState: ...

  def sizeof(self) -> int: ...

  @staticmethod
  @overload
  def calloc() -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def calloc(arg0: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def callocStack() -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def callocStack(arg0: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def callocStack(arg0: MemoryStack) -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def callocStack(arg0: int, arg1: MemoryStack) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def create() -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def createSafe(arg0: int) -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def createSafe(arg0: int, arg1: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def malloc() -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def malloc(arg0: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def mallocStack() -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def mallocStack(arg0: MemoryStack) -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int, arg1: MemoryStack) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def naxes(arg0: int) -> FloatBuffer: ...

  @staticmethod
  @overload
  def naxes(arg0: int, arg1: int) -> float: ...

  @staticmethod
  @overload
  def naxes(arg0: int, arg1: FloatBuffer) -> None: ...

  @staticmethod
  @overload
  def naxes(arg0: int, arg1: int, arg2: float) -> None: ...

  @staticmethod
  @overload
  def nbuttons(arg0: int) -> ByteBuffer: ...

  @staticmethod
  @overload
  def nbuttons(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def nbuttons(arg0: int, arg1: ByteBuffer) -> None: ...

  @staticmethod
  @overload
  def nbuttons(arg0: int, arg1: int, arg2: int) -> None: ...

  def __init__(self, arg0: ByteBuffer): ...

  class Buffer(StructBuffer):

    @overload
    def axes(self) -> FloatBuffer: ...

    @overload
    def axes(self, arg0: int) -> float: ...

    @overload
    def axes(self, arg0: FloatBuffer) -> GLFWGamepadState.Buffer: ...

    @overload
    def axes(self, arg0: int, arg1: float) -> GLFWGamepadState.Buffer: ...

    @overload
    def buttons(self) -> ByteBuffer: ...

    @overload
    def buttons(self, arg0: int) -> int: ...

    @overload
    def buttons(self, arg0: ByteBuffer) -> GLFWGamepadState.Buffer: ...

    @overload
    def buttons(self, arg0: int, arg1: int) -> GLFWGamepadState.Buffer: ...

    def close(self) -> None: ...

    def free(self) -> None: ...

    @overload
    def __init__(self, arg0: ByteBuffer): ...
    @overload
    def __init__(self, arg0: int, arg1: int): ...


class GLFWGammaRamp(Struct):

  ALIGNOF: int

  @overload
  def blue(self) -> ShortBuffer: ...

  @overload
  def blue(self, arg0: ShortBuffer) -> GLFWGammaRamp: ...

  def close(self) -> None: ...

  def free(self) -> None: ...

  @overload
  def green(self) -> ShortBuffer: ...

  @overload
  def green(self, arg0: ShortBuffer) -> GLFWGammaRamp: ...

  @overload
  def red(self) -> ShortBuffer: ...

  @overload
  def red(self, arg0: ShortBuffer) -> GLFWGammaRamp: ...

  @overload
  def set(self, arg0: GLFWGammaRamp) -> GLFWGammaRamp: ...

  @overload
  def set(self, arg0: ShortBuffer, arg1: ShortBuffer, arg2: ShortBuffer, arg3: int) -> GLFWGammaRamp: ...

  @overload
  def size(self) -> int: ...

  @overload
  def size(self, arg0: int) -> GLFWGammaRamp: ...

  def sizeof(self) -> int: ...

  @staticmethod
  @overload
  def calloc() -> GLFWGammaRamp: ...

  @staticmethod
  @overload
  def calloc(arg0: int) -> GLFWGammaRamp.Buffer: ...

  @staticmethod
  @overload
  def callocStack() -> GLFWGammaRamp: ...

  @staticmethod
  @overload
  def callocStack(arg0: int) -> GLFWGammaRamp.Buffer: ...

  @staticmethod
  @overload
  def callocStack(arg0: MemoryStack) -> GLFWGammaRamp: ...

  @staticmethod
  @overload
  def callocStack(arg0: int, arg1: MemoryStack) -> GLFWGammaRamp.Buffer: ...

  @staticmethod
  @overload
  def create() -> GLFWGammaRamp: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWGammaRamp.Buffer: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWGammaRamp: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> GLFWGammaRamp.Buffer: ...

  @staticmethod
  @overload
  def createSafe(arg0: int) -> GLFWGammaRamp: ...

  @staticmethod
  @overload
  def createSafe(arg0: int, arg1: int) -> GLFWGammaRamp.Buffer: ...

  @staticmethod
  @overload
  def malloc() -> GLFWGammaRamp: ...

  @staticmethod
  @overload
  def malloc(arg0: int) -> GLFWGammaRamp.Buffer: ...

  @staticmethod
  @overload
  def mallocStack() -> GLFWGammaRamp: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int) -> GLFWGammaRamp.Buffer: ...

  @staticmethod
  @overload
  def mallocStack(arg0: MemoryStack) -> GLFWGammaRamp: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int, arg1: MemoryStack) -> GLFWGammaRamp.Buffer: ...

  @staticmethod
  @overload
  def nblue(arg0: int) -> ShortBuffer: ...

  @staticmethod
  @overload
  def nblue(arg0: int, arg1: ShortBuffer) -> None: ...

  @staticmethod
  @overload
  def ngreen(arg0: int) -> ShortBuffer: ...

  @staticmethod
  @overload
  def ngreen(arg0: int, arg1: ShortBuffer) -> None: ...

  @staticmethod
  @overload
  def nred(arg0: int) -> ShortBuffer: ...

  @staticmethod
  @overload
  def nred(arg0: int, arg1: ShortBuffer) -> None: ...

  @staticmethod
  @overload
  def nsize(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nsize(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def validate(arg0: int) -> None: ...

  @staticmethod
  @overload
  def validate(arg0: int, arg1: int) -> None: ...

  def __init__(self, arg0: ByteBuffer): ...

  class Buffer(StructBuffer):

    @overload
    def blue(self) -> ShortBuffer: ...

    @overload
    def blue(self, arg0: ShortBuffer) -> GLFWGammaRamp.Buffer: ...

    def close(self) -> None: ...

    def free(self) -> None: ...

    @overload
    def green(self) -> ShortBuffer: ...

    @overload
    def green(self, arg0: ShortBuffer) -> GLFWGammaRamp.Buffer: ...

    @overload
    def red(self) -> ShortBuffer: ...

    @overload
    def red(self, arg0: ShortBuffer) -> GLFWGammaRamp.Buffer: ...

    @overload
    def size(self) -> int: ...

    @overload
    def size(self, arg0: int) -> GLFWGammaRamp.Buffer: ...

    @overload
    def __init__(self, arg0: ByteBuffer): ...
    @overload
    def __init__(self, arg0: int, arg1: int): ...


class GLFWImage(Struct):

  ALIGNOF: int

  def close(self) -> None: ...

  def free(self) -> None: ...

  @overload
  def height(self) -> int: ...

  @overload
  def height(self, arg0: int) -> GLFWImage: ...

  @overload
  def pixels(self, arg0: int) -> ByteBuffer: ...

  @overload
  def pixels(self, arg0: ByteBuffer) -> GLFWImage: ...

  @overload
  def set(self, arg0: GLFWImage) -> GLFWImage: ...

  @overload
  def set(self, arg0: int, arg1: int, arg2: ByteBuffer) -> GLFWImage: ...

  def sizeof(self) -> int: ...

  @overload
  def width(self) -> int: ...

  @overload
  def width(self, arg0: int) -> GLFWImage: ...

  @staticmethod
  @overload
  def calloc() -> GLFWImage: ...

  @staticmethod
  @overload
  def calloc(arg0: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def callocStack() -> GLFWImage: ...

  @staticmethod
  @overload
  def callocStack(arg0: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def callocStack(arg0: MemoryStack) -> GLFWImage: ...

  @staticmethod
  @overload
  def callocStack(arg0: int, arg1: MemoryStack) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def create() -> GLFWImage: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWImage: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def createSafe(arg0: int) -> GLFWImage: ...

  @staticmethod
  @overload
  def createSafe(arg0: int, arg1: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def malloc() -> GLFWImage: ...

  @staticmethod
  @overload
  def malloc(arg0: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def mallocStack() -> GLFWImage: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def mallocStack(arg0: MemoryStack) -> GLFWImage: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int, arg1: MemoryStack) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def nheight(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nheight(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def npixels(arg0: int, arg1: int) -> ByteBuffer: ...

  @staticmethod
  @overload
  def npixels(arg0: int, arg1: ByteBuffer) -> None: ...

  @staticmethod
  @overload
  def nwidth(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nwidth(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def validate(arg0: int) -> None: ...

  @staticmethod
  @overload
  def validate(arg0: int, arg1: int) -> None: ...

  def __init__(self, arg0: ByteBuffer): ...

  class Buffer(StructBuffer):

    def close(self) -> None: ...

    def free(self) -> None: ...

    @overload
    def height(self) -> int: ...

    @overload
    def height(self, arg0: int) -> GLFWImage.Buffer: ...

    @overload
    def pixels(self, arg0: int) -> ByteBuffer: ...

    @overload
    def pixels(self, arg0: ByteBuffer) -> GLFWImage.Buffer: ...

    @overload
    def width(self) -> int: ...

    @overload
    def width(self, arg0: int) -> GLFWImage.Buffer: ...

    @overload
    def __init__(self, arg0: ByteBuffer): ...
    @overload
    def __init__(self, arg0: int, arg1: int): ...


class GLFWJoystickCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...

  def set(self) -> GLFWJoystickCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWJoystickCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWJoystickCallbackI) -> GLFWJoystickCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWJoystickCallback: ...

  class Container(GLFWJoystickCallback):

    def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWJoystickCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWKeyCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...

  def set(self, arg0: int) -> GLFWKeyCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWKeyCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWKeyCallbackI) -> GLFWKeyCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWKeyCallback: ...

  class Container(GLFWKeyCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...


class GLFWKeyCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...


class GLFWMonitorCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...

  def set(self) -> GLFWMonitorCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWMonitorCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWMonitorCallbackI) -> GLFWMonitorCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWMonitorCallback: ...

  class Container(GLFWMonitorCallback):

    def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWMonitorCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWMouseButtonCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def set(self, arg0: int) -> GLFWMouseButtonCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWMouseButtonCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWMouseButtonCallbackI) -> GLFWMouseButtonCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWMouseButtonCallback: ...

  class Container(GLFWMouseButtonCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...


class GLFWMouseButtonCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...


class GLFWNativeCocoa:

  @staticmethod
  def glfwGetCocoaMonitor(arg0: int) -> int: ...

  @staticmethod
  def glfwGetCocoaWindow(arg0: int) -> int: ...

  class Functions:

    GetCocoaMonitor: int

    GetCocoaWindow: int


class GLFWNativeEGL:

  @staticmethod
  def glfwGetEGLContext(arg0: int) -> int: ...

  @staticmethod
  def glfwGetEGLDisplay() -> int: ...

  @staticmethod
  def glfwGetEGLSurface(arg0: int) -> int: ...

  class Functions:

    GetEGLContext: int

    GetEGLDisplay: int

    GetEGLSurface: int


class GLFWNativeGLX:

  @staticmethod
  def glfwGetGLXContext(arg0: int) -> int: ...

  @staticmethod
  def glfwGetGLXWindow(arg0: int) -> int: ...

  class Functions:

    GetGLXContext: int

    GetGLXWindow: int


class GLFWNativeNSGL:

  @staticmethod
  def glfwGetNSGLContext(arg0: int) -> int: ...

  class Functions:

    GetNSGLContext: int


class GLFWNativeWGL:

  @staticmethod
  def glfwGetWGLContext(arg0: int) -> int: ...

  class Functions:

    GetWGLContext: int


class GLFWNativeWayland:

  @staticmethod
  def glfwGetWaylandDisplay() -> int: ...

  @staticmethod
  def glfwGetWaylandMonitor(arg0: int) -> int: ...

  @staticmethod
  def glfwGetWaylandWindow(arg0: int) -> int: ...

  class Functions:

    GetWaylandDisplay: int

    GetWaylandMonitor: int

    GetWaylandWindow: int


class GLFWNativeWin32:

  @staticmethod
  def glfwAttachWin32Window(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def glfwGetWin32Adapter(arg0: int) -> str: ...

  @staticmethod
  def glfwGetWin32Monitor(arg0: int) -> str: ...

  @staticmethod
  def glfwGetWin32Window(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetWin32Adapter(arg0: int) -> int: ...

  @staticmethod
  def nglfwGetWin32Monitor(arg0: int) -> int: ...

  class Functions:

    AttachWin32Window: int

    GetWin32Adapter: int

    GetWin32Monitor: int

    GetWin32Window: int


class GLFWNativeX11:

  @staticmethod
  def glfwGetX11Adapter(arg0: int) -> int: ...

  @staticmethod
  def glfwGetX11Display() -> int: ...

  @staticmethod
  def glfwGetX11Monitor(arg0: int) -> int: ...

  @staticmethod
  def glfwGetX11SelectionString() -> str: ...

  @staticmethod
  def glfwGetX11Window(arg0: int) -> int: ...

  @staticmethod
  @overload
  def glfwSetX11SelectionString(arg0: CharSequence) -> None: ...

  @staticmethod
  @overload
  def glfwSetX11SelectionString(arg0: ByteBuffer) -> None: ...

  @staticmethod
  def nglfwGetX11SelectionString() -> int: ...

  @staticmethod
  def nglfwSetX11SelectionString(arg0: int) -> None: ...

  class Functions:

    GetX11Adapter: int

    GetX11Display: int

    GetX11Monitor: int

    GetX11SelectionString: int

    GetX11Window: int

    SetX11SelectionString: int


class GLFWScrollCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...

  def set(self, arg0: int) -> GLFWScrollCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWScrollCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWScrollCallbackI) -> GLFWScrollCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWScrollCallback: ...

  class Container(GLFWScrollCallback):

    def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...


class GLFWScrollCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...


class GLFWVidMode(Struct):

  ALIGNOF: int

  BLUEBITS: int

  GREENBITS: int

  REDBITS: int

  REFRESHRATE: int

  def blueBits(self) -> int: ...

  def greenBits(self) -> int: ...

  def height(self) -> int: ...

  def redBits(self) -> int: ...

  def refreshRate(self) -> int: ...

  def sizeof(self) -> int: ...

  def width(self) -> int: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWVidMode: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> GLFWVidMode.Buffer: ...

  @staticmethod
  @overload
  def createSafe(arg0: int) -> GLFWVidMode: ...

  @staticmethod
  @overload
  def createSafe(arg0: int, arg1: int) -> GLFWVidMode.Buffer: ...

  @staticmethod
  def nblueBits(arg0: int) -> int: ...

  @staticmethod
  def ngreenBits(arg0: int) -> int: ...

  @staticmethod
  def nheight(arg0: int) -> int: ...

  @staticmethod
  def nredBits(arg0: int) -> int: ...

  @staticmethod
  def nrefreshRate(arg0: int) -> int: ...

  @staticmethod
  def nwidth(arg0: int) -> int: ...

  def __init__(self, arg0: ByteBuffer): ...

  class Buffer(StructBuffer):

    def blueBits(self) -> int: ...

    def greenBits(self) -> int: ...

    def height(self) -> int: ...

    def redBits(self) -> int: ...

    def refreshRate(self) -> int: ...

    def width(self) -> int: ...

    @overload
    def __init__(self, arg0: ByteBuffer): ...
    @overload
    def __init__(self, arg0: int, arg1: int): ...


class GLFWWindowCloseCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int) -> None: ...

  def set(self, arg0: int) -> GLFWWindowCloseCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowCloseCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowCloseCallbackI) -> GLFWWindowCloseCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowCloseCallback: ...

  class Container(GLFWWindowCloseCallback):

    def invoke(self, arg0: int) -> None: ...


class GLFWWindowCloseCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int) -> None: ...


class GLFWWindowContentScaleCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...

  def set(self, arg0: int) -> GLFWWindowContentScaleCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowContentScaleCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowContentScaleCallbackI) -> GLFWWindowContentScaleCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowContentScaleCallback: ...

  class Container(GLFWWindowContentScaleCallback):

    def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...


class GLFWWindowContentScaleCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...


class GLFWWindowFocusCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...

  def set(self, arg0: int) -> GLFWWindowFocusCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowFocusCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowFocusCallbackI) -> GLFWWindowFocusCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowFocusCallback: ...

  class Container(GLFWWindowFocusCallback):

    def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWWindowFocusCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWWindowIconifyCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...

  def set(self, arg0: int) -> GLFWWindowIconifyCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowIconifyCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowIconifyCallbackI) -> GLFWWindowIconifyCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowIconifyCallback: ...

  class Container(GLFWWindowIconifyCallback):

    def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWWindowIconifyCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWWindowMaximizeCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...

  def set(self, arg0: int) -> GLFWWindowMaximizeCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowMaximizeCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowMaximizeCallbackI) -> GLFWWindowMaximizeCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowMaximizeCallback: ...

  class Container(GLFWWindowMaximizeCallback):

    def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWWindowMaximizeCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWWindowPosCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...

  def set(self, arg0: int) -> GLFWWindowPosCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowPosCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowPosCallbackI) -> GLFWWindowPosCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowPosCallback: ...

  class Container(GLFWWindowPosCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWWindowPosCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWWindowRefreshCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int) -> None: ...

  def set(self, arg0: int) -> GLFWWindowRefreshCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowRefreshCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowRefreshCallbackI) -> GLFWWindowRefreshCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowRefreshCallback: ...

  class Container(GLFWWindowRefreshCallback):

    def invoke(self, arg0: int) -> None: ...


class GLFWWindowRefreshCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int) -> None: ...


class GLFWWindowSizeCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...

  def set(self, arg0: int) -> GLFWWindowSizeCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowSizeCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowSizeCallbackI) -> GLFWWindowSizeCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowSizeCallback: ...

  class Container(GLFWWindowSizeCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWWindowSizeCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...

