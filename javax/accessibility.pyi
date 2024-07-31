from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import Point, Color, Rectangle, Cursor, Font, FontMetrics, Dimension
from java.awt.event import FocusListener
from java.beans import PropertyChangeListener
from java.lang import Number
from java.util import Locale
from javax.swing.text import AttributeSet

class Accessible:

  def getAccessibleContext(self) -> AccessibleContext: ...


class AccessibleAction:

  CLICK: str

  DECREMENT: str

  INCREMENT: str

  TOGGLE_EXPAND: str

  TOGGLE_POPUP: str

  def doAccessibleAction(self, arg0: int) -> bool: ...

  def getAccessibleActionCount(self) -> int: ...

  def getAccessibleActionDescription(self, arg0: int) -> str: ...


class AccessibleBundle:

  @overload
  def toDisplayString(self) -> str: ...

  @overload
  def toDisplayString(self, arg0: Locale) -> str: ...

  def toString(self) -> str: ...

  def __init__(self): ...


class AccessibleComponent:

  def addFocusListener(self, arg0: FocusListener) -> None: ...

  def contains(self, arg0: Point) -> bool: ...

  def getAccessibleAt(self, arg0: Point) -> Accessible: ...

  def getBackground(self) -> Color: ...

  def getBounds(self) -> Rectangle: ...

  def getCursor(self) -> Cursor: ...

  def getFont(self) -> Font: ...

  def getFontMetrics(self, arg0: Font) -> FontMetrics: ...

  def getForeground(self) -> Color: ...

  def getLocation(self) -> Point: ...

  def getLocationOnScreen(self) -> Point: ...

  def getSize(self) -> Dimension: ...

  def isEnabled(self) -> bool: ...

  def isFocusTraversable(self) -> bool: ...

  def isShowing(self) -> bool: ...

  def isVisible(self) -> bool: ...

  def removeFocusListener(self, arg0: FocusListener) -> None: ...

  def requestFocus(self) -> None: ...

  def setBackground(self, arg0: Color) -> None: ...

  def setBounds(self, arg0: Rectangle) -> None: ...

  def setCursor(self, arg0: Cursor) -> None: ...

  def setEnabled(self, arg0: bool) -> None: ...

  def setFont(self, arg0: Font) -> None: ...

  def setForeground(self, arg0: Color) -> None: ...

  def setLocation(self, arg0: Point) -> None: ...

  def setSize(self, arg0: Dimension) -> None: ...

  def setVisible(self, arg0: bool) -> None: ...


class AccessibleContext:

  ACCESSIBLE_ACTION_PROPERTY: str

  ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY: str

  ACCESSIBLE_CARET_PROPERTY: str

  ACCESSIBLE_CHILD_PROPERTY: str

  ACCESSIBLE_COMPONENT_BOUNDS_CHANGED: str

  ACCESSIBLE_DESCRIPTION_PROPERTY: str

  ACCESSIBLE_HYPERTEXT_OFFSET: str

  ACCESSIBLE_INVALIDATE_CHILDREN: str

  ACCESSIBLE_NAME_PROPERTY: str

  ACCESSIBLE_SELECTION_PROPERTY: str

  ACCESSIBLE_STATE_PROPERTY: str

  ACCESSIBLE_TABLE_CAPTION_CHANGED: str

  ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED: str

  ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED: str

  ACCESSIBLE_TABLE_MODEL_CHANGED: str

  ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED: str

  ACCESSIBLE_TABLE_ROW_HEADER_CHANGED: str

  ACCESSIBLE_TABLE_SUMMARY_CHANGED: str

  ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED: str

  ACCESSIBLE_TEXT_PROPERTY: str

  ACCESSIBLE_VALUE_PROPERTY: str

  ACCESSIBLE_VISIBLE_DATA_PROPERTY: str

  def addPropertyChangeListener(self, arg0: PropertyChangeListener) -> None: ...

  def firePropertyChange(self, arg0: str, arg1: object, arg2: object) -> None: ...

  def getAccessibleAction(self) -> AccessibleAction: ...

  def getAccessibleChild(self, arg0: int) -> Accessible: ...

  def getAccessibleChildrenCount(self) -> int: ...

  def getAccessibleComponent(self) -> AccessibleComponent: ...

  def getAccessibleDescription(self) -> str: ...

  def getAccessibleEditableText(self) -> AccessibleEditableText: ...

  def getAccessibleIcon(self) -> list[AccessibleIcon]: ...

  def getAccessibleIndexInParent(self) -> int: ...

  def getAccessibleName(self) -> str: ...

  def getAccessibleParent(self) -> Accessible: ...

  def getAccessibleRelationSet(self) -> AccessibleRelationSet: ...

  def getAccessibleRole(self) -> AccessibleRole: ...

  def getAccessibleSelection(self) -> AccessibleSelection: ...

  def getAccessibleStateSet(self) -> AccessibleStateSet: ...

  def getAccessibleTable(self) -> AccessibleTable: ...

  def getAccessibleText(self) -> AccessibleText: ...

  def getAccessibleValue(self) -> AccessibleValue: ...

  def getLocale(self) -> Locale: ...

  def removePropertyChangeListener(self, arg0: PropertyChangeListener) -> None: ...

  def setAccessibleDescription(self, arg0: str) -> None: ...

  def setAccessibleName(self, arg0: str) -> None: ...

  def setAccessibleParent(self, arg0: Accessible) -> None: ...


class AccessibleEditableText:

  CHARACTER: int

  SENTENCE: int

  WORD: int

  def cut(self, arg0: int, arg1: int) -> None: ...

  def delete(self, arg0: int, arg1: int) -> None: ...

  def getAfterIndex(self, arg0: int, arg1: int) -> str: ...

  def getAtIndex(self, arg0: int, arg1: int) -> str: ...

  def getBeforeIndex(self, arg0: int, arg1: int) -> str: ...

  def getCaretPosition(self) -> int: ...

  def getCharCount(self) -> int: ...

  def getCharacterAttribute(self, arg0: int) -> AttributeSet: ...

  def getCharacterBounds(self, arg0: int) -> Rectangle: ...

  def getIndexAtPoint(self, arg0: Point) -> int: ...

  def getSelectedText(self) -> str: ...

  def getSelectionEnd(self) -> int: ...

  def getSelectionStart(self) -> int: ...

  def getTextRange(self, arg0: int, arg1: int) -> str: ...

  def insertTextAtIndex(self, arg0: int, arg1: str) -> None: ...

  def paste(self, arg0: int) -> None: ...

  def replaceText(self, arg0: int, arg1: int, arg2: str) -> None: ...

  def selectText(self, arg0: int, arg1: int) -> None: ...

  def setAttributes(self, arg0: int, arg1: int, arg2: AttributeSet) -> None: ...

  def setTextContents(self, arg0: str) -> None: ...


class AccessibleIcon:

  def getAccessibleIconDescription(self) -> str: ...

  def getAccessibleIconHeight(self) -> int: ...

  def getAccessibleIconWidth(self) -> int: ...

  def setAccessibleIconDescription(self, arg0: str) -> None: ...


class AccessibleKeyBinding:

  def getAccessibleKeyBinding(self, arg0: int) -> object: ...

  def getAccessibleKeyBindingCount(self) -> int: ...


class AccessibleRelation(AccessibleBundle):

  CHILD_NODE_OF: str

  CHILD_NODE_OF_PROPERTY: str

  CONTROLLED_BY: str

  CONTROLLED_BY_PROPERTY: str

  CONTROLLER_FOR: str

  CONTROLLER_FOR_PROPERTY: str

  EMBEDDED_BY: str

  EMBEDDED_BY_PROPERTY: str

  EMBEDS: str

  EMBEDS_PROPERTY: str

  FLOWS_FROM: str

  FLOWS_FROM_PROPERTY: str

  FLOWS_TO: str

  FLOWS_TO_PROPERTY: str

  LABEL_FOR: str

  LABEL_FOR_PROPERTY: str

  LABELED_BY: str

  LABELED_BY_PROPERTY: str

  MEMBER_OF: str

  MEMBER_OF_PROPERTY: str

  PARENT_WINDOW_OF: str

  PARENT_WINDOW_OF_PROPERTY: str

  SUBWINDOW_OF: str

  SUBWINDOW_OF_PROPERTY: str

  def getKey(self) -> str: ...

  def getTarget(self) -> list[object]: ...

  @overload
  def setTarget(self, arg0: list[object]) -> None: ...

  @overload
  def setTarget(self, arg0: object) -> None: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: list[object]): ...
  @overload
  def __init__(self, arg0: str, arg1: object): ...


class AccessibleRelationSet:

  def add(self, arg0: AccessibleRelation) -> bool: ...

  def addAll(self, arg0: list[AccessibleRelation]) -> None: ...

  def clear(self) -> None: ...

  def contains(self, arg0: str) -> bool: ...

  def get(self, arg0: str) -> AccessibleRelation: ...

  def remove(self, arg0: AccessibleRelation) -> bool: ...

  def size(self) -> int: ...

  def toArray(self) -> list[AccessibleRelation]: ...

  def toString(self) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: list[AccessibleRelation]): ...


class AccessibleRole(AccessibleBundle):

  ALERT: AccessibleRole

  AWT_COMPONENT: AccessibleRole

  CANVAS: AccessibleRole

  CHECK_BOX: AccessibleRole

  COLOR_CHOOSER: AccessibleRole

  COLUMN_HEADER: AccessibleRole

  COMBO_BOX: AccessibleRole

  DATE_EDITOR: AccessibleRole

  DESKTOP_ICON: AccessibleRole

  DESKTOP_PANE: AccessibleRole

  DIALOG: AccessibleRole

  DIRECTORY_PANE: AccessibleRole

  EDITBAR: AccessibleRole

  FILE_CHOOSER: AccessibleRole

  FILLER: AccessibleRole

  FONT_CHOOSER: AccessibleRole

  FOOTER: AccessibleRole

  FRAME: AccessibleRole

  GLASS_PANE: AccessibleRole

  GROUP_BOX: AccessibleRole

  HEADER: AccessibleRole

  HTML_CONTAINER: AccessibleRole

  HYPERLINK: AccessibleRole

  ICON: AccessibleRole

  INTERNAL_FRAME: AccessibleRole

  LABEL: AccessibleRole

  LAYERED_PANE: AccessibleRole

  LIST: AccessibleRole

  LIST_ITEM: AccessibleRole

  MENU: AccessibleRole

  MENU_BAR: AccessibleRole

  MENU_ITEM: AccessibleRole

  OPTION_PANE: AccessibleRole

  PAGE_TAB: AccessibleRole

  PAGE_TAB_LIST: AccessibleRole

  PANEL: AccessibleRole

  PARAGRAPH: AccessibleRole

  PASSWORD_TEXT: AccessibleRole

  POPUP_MENU: AccessibleRole

  PROGRESS_BAR: AccessibleRole

  PROGRESS_MONITOR: AccessibleRole

  PUSH_BUTTON: AccessibleRole

  RADIO_BUTTON: AccessibleRole

  ROOT_PANE: AccessibleRole

  ROW_HEADER: AccessibleRole

  RULER: AccessibleRole

  SCROLL_BAR: AccessibleRole

  SCROLL_PANE: AccessibleRole

  SEPARATOR: AccessibleRole

  SLIDER: AccessibleRole

  SPIN_BOX: AccessibleRole

  SPLIT_PANE: AccessibleRole

  STATUS_BAR: AccessibleRole

  SWING_COMPONENT: AccessibleRole

  TABLE: AccessibleRole

  TEXT: AccessibleRole

  TOGGLE_BUTTON: AccessibleRole

  TOOL_BAR: AccessibleRole

  TOOL_TIP: AccessibleRole

  TREE: AccessibleRole

  UNKNOWN: AccessibleRole

  VIEWPORT: AccessibleRole

  WINDOW: AccessibleRole


class AccessibleSelection:

  def addAccessibleSelection(self, arg0: int) -> None: ...

  def clearAccessibleSelection(self) -> None: ...

  def getAccessibleSelection(self, arg0: int) -> Accessible: ...

  def getAccessibleSelectionCount(self) -> int: ...

  def isAccessibleChildSelected(self, arg0: int) -> bool: ...

  def removeAccessibleSelection(self, arg0: int) -> None: ...

  def selectAllAccessibleSelection(self) -> None: ...


class AccessibleState(AccessibleBundle):

  ACTIVE: AccessibleState

  ARMED: AccessibleState

  BUSY: AccessibleState

  CHECKED: AccessibleState

  COLLAPSED: AccessibleState

  EDITABLE: AccessibleState

  ENABLED: AccessibleState

  EXPANDABLE: AccessibleState

  EXPANDED: AccessibleState

  FOCUSABLE: AccessibleState

  FOCUSED: AccessibleState

  HORIZONTAL: AccessibleState

  ICONIFIED: AccessibleState

  INDETERMINATE: AccessibleState

  MANAGES_DESCENDANTS: AccessibleState

  MODAL: AccessibleState

  MULTI_LINE: AccessibleState

  MULTISELECTABLE: AccessibleState

  OPAQUE: AccessibleState

  PRESSED: AccessibleState

  RESIZABLE: AccessibleState

  SELECTABLE: AccessibleState

  SELECTED: AccessibleState

  SHOWING: AccessibleState

  SINGLE_LINE: AccessibleState

  TRANSIENT: AccessibleState

  TRUNCATED: AccessibleState

  VERTICAL: AccessibleState

  VISIBLE: AccessibleState


class AccessibleStateSet:

  def add(self, arg0: AccessibleState) -> bool: ...

  def addAll(self, arg0: list[AccessibleState]) -> None: ...

  def clear(self) -> None: ...

  def contains(self, arg0: AccessibleState) -> bool: ...

  def remove(self, arg0: AccessibleState) -> bool: ...

  def toArray(self) -> list[AccessibleState]: ...

  def toString(self) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: list[AccessibleState]): ...


class AccessibleTable:

  def getAccessibleAt(self, arg0: int, arg1: int) -> Accessible: ...

  def getAccessibleCaption(self) -> Accessible: ...

  def getAccessibleColumnCount(self) -> int: ...

  def getAccessibleColumnDescription(self, arg0: int) -> Accessible: ...

  def getAccessibleColumnExtentAt(self, arg0: int, arg1: int) -> int: ...

  def getAccessibleColumnHeader(self) -> AccessibleTable: ...

  def getAccessibleRowCount(self) -> int: ...

  def getAccessibleRowDescription(self, arg0: int) -> Accessible: ...

  def getAccessibleRowExtentAt(self, arg0: int, arg1: int) -> int: ...

  def getAccessibleRowHeader(self) -> AccessibleTable: ...

  def getAccessibleSummary(self) -> Accessible: ...

  def getSelectedAccessibleColumns(self) -> list[int]: ...

  def getSelectedAccessibleRows(self) -> list[int]: ...

  def isAccessibleColumnSelected(self, arg0: int) -> bool: ...

  def isAccessibleRowSelected(self, arg0: int) -> bool: ...

  def isAccessibleSelected(self, arg0: int, arg1: int) -> bool: ...

  def setAccessibleCaption(self, arg0: Accessible) -> None: ...

  def setAccessibleColumnDescription(self, arg0: int, arg1: Accessible) -> None: ...

  def setAccessibleColumnHeader(self, arg0: AccessibleTable) -> None: ...

  def setAccessibleRowDescription(self, arg0: int, arg1: Accessible) -> None: ...

  def setAccessibleRowHeader(self, arg0: AccessibleTable) -> None: ...

  def setAccessibleSummary(self, arg0: Accessible) -> None: ...


class AccessibleText:

  CHARACTER: int

  SENTENCE: int

  WORD: int

  def getAfterIndex(self, arg0: int, arg1: int) -> str: ...

  def getAtIndex(self, arg0: int, arg1: int) -> str: ...

  def getBeforeIndex(self, arg0: int, arg1: int) -> str: ...

  def getCaretPosition(self) -> int: ...

  def getCharCount(self) -> int: ...

  def getCharacterAttribute(self, arg0: int) -> AttributeSet: ...

  def getCharacterBounds(self, arg0: int) -> Rectangle: ...

  def getIndexAtPoint(self, arg0: Point) -> int: ...

  def getSelectedText(self) -> str: ...

  def getSelectionEnd(self) -> int: ...

  def getSelectionStart(self) -> int: ...


class AccessibleValue:

  def getCurrentAccessibleValue(self) -> Number: ...

  def getMaximumAccessibleValue(self) -> Number: ...

  def getMinimumAccessibleValue(self) -> Number: ...

  def setCurrentAccessibleValue(self, arg0: Number) -> bool: ...

