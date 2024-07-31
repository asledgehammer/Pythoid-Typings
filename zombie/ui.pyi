from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from gnu.trove.list.array import TIntArrayList
from java.awt import Rectangle
from java.lang import Boolean, Enum, CharSequence, Double
from java.util import HashMap, Stack, ArrayList, Collection, Vector
from org.lwjgl.util import Rectangle
from se.krka.kahlua.vm import KahluaTable, KahluaThread
from zombie.characters import IsoGameCharacter, IsoSurvivor, SurvivorDesc
from zombie.characters.BodyDamage import BodyPartType
from zombie.characters.Moodles import MoodleType
from zombie.core import Color
from zombie.core.fonts import AngelCodeFont
from zombie.core.textures import Texture, TextureDraw, TextureFBO, ColorInfo
from zombie.inventory import InventoryItem
from zombie.iso import IsoObject, IsoDirections, IsoObjectPicker, Vector2
from zombie.iso.areas import IsoBuilding
from zombie.iso.objects import IsoStove

class ActionProgressBar(UIElement):

  def getValue(self) -> float: ...

  def render(self) -> None: ...

  def setValue(self, delta: float) -> None: ...

  def update(self, nPlayer: int) -> None: ...

  def __init__(self, x: int, y: int):
    self.delayhide: int


class Clock(UIElement):

  instance: Clock

  def isDateVisible(self) -> bool: ...

  def onMouseDown(self, x: float, y: float) -> Boolean: ...

  def render(self) -> None: ...

  def resize(self) -> None: ...

  def __init__(self, x: int, y: int):
    self.digital: bool
    self.isalarmringing: bool
    self.isalarmset: bool


class DialogButton(UIElement):

  def onMouseDown(self, x: float, y: float) -> Boolean: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def onMouseUp(self, x: float, y: float) -> Boolean: ...

  def render(self) -> None: ...

  @overload
  def __init__(self, messages: UIElement, x: float, y: float, text: str, name: str):
    self.clicked: bool

    self.messagetarget: UIElement

    self.mouseover: bool

    self.name: str

    self.text: str

  @overload
  def __init__(self, messages: UIEventHandler, x: int, y: int, text: str, name: str): ...


class FPSGraph(UIElement):

  instance: FPSGraph

  def addLighting(self, time: int) -> None: ...

  def addRender(self, time: int) -> None: ...

  def addUI(self, time: int) -> None: ...

  def addUpdate(self, time: int) -> None: ...

  def render(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self): ...

  class Graph:

    def add(self, arg0: int) -> None: ...

    def render(self, arg0: float, arg1: float, arg2: float) -> None: ...


class FontsFile:

  def read(self, path: str, fonts: HashMap[str, FontsFileFont]) -> bool: ...

  def __init__(self): ...


class FontsFileFont:

  def __init__(self):
    self.fnt: str
    self.id: str
    self.img: str


class GenericButton(UIElement):

  def onMouseDown(self, x: float, y: float) -> Boolean: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def onMouseUp(self, x: float, y: float) -> Boolean: ...

  def render(self) -> None: ...

  @overload
  def __init__(self, messages: UIElement, x: float, y: float, width: float, height: float, name: str, text: str, UpTex: Texture, DownTex: Texture):
    self.clicked: bool

    self.messagetarget: UIElement

    self.mouseover: bool

    self.name: str

    self.text: str

  @overload
  def __init__(self, messages: UIEventHandler, x: float, y: float, width: float, height: float, name: str, text: str, UpTex: Texture, DownTex: Texture): ...


class HUDButton(UIElement):

  def onMouseDown(self, x: float, y: float) -> Boolean: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def onMouseUp(self, x: float, y: float) -> Boolean: ...

  def render(self) -> None: ...

  def update(self) -> None: ...

  @overload
  def __init__(self, name: str, x: float, y: float, texture: str, highlight: str, display: UIElement):
    self.clickedalpha: float

    self.notclickedalpha: float

  @overload
  def __init__(self, name: str, x: float, y: float, texture: str, highlight: str, handler: UIEventHandler): ...
  @overload
  def __init__(self, name: str, x: float, y: float, texture: str, highlight: str, overicon: str, display: UIElement): ...
  @overload
  def __init__(self, name: str, x: float, y: float, texture: str, highlight: str, overicon: str, handler: UIEventHandler): ...


class LoadingQueueUI(UIElement):

  def onresize(self) -> None: ...

  def render(self) -> None: ...

  def setPlaceInQueue(self, placeInQueue: int) -> None: ...

  def update(self) -> None: ...

  def __init__(self): ...


class ModalDialog(NewWindow):

  def ButtonClicked(self, name: str) -> None: ...

  def Clicked(self, name: str) -> None: ...

  def __init__(self, name: str, help: str, bYesNo: bool):
    self.byes: bool
    self.clicked: bool
    self.name: str


class MoodlesUI(UIElement):

  chevronDown: Texture

  chevronDownBorder: Texture

  chevronUp: Texture

  chevronUpBorder: Texture

  minusGreen: Texture

  minusRed: Texture

  plusGreen: Texture

  plusRed: Texture

  def CurrentlyAnimating(self) -> bool: ...

  def Nest(self, el: UIElement, t: int, r: int, b: int, l: int) -> None: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def render(self) -> None: ...

  def setCharacter(self, chr: IsoGameCharacter) -> None: ...

  def update(self) -> None: ...

  def wiggle(self, Moodle: MoodleType) -> None: ...

  @staticmethod
  def getInstance() -> MoodlesUI: ...

  def __init__(self):
    self.clienth: float
    self.clientw: float
    self.movable: bool
    self.ncclienth: int
    self.ncclientw: int
    self.nesteditems: Stack[Rectangle]


class NewHealthPanel(NewWindow):

  instance: NewHealthPanel

  def SetCharacter(self, chr: IsoGameCharacter) -> None: ...

  def getDamageStatusString(self) -> str: ...

  def render(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self, x: int, y: int, ParentCharacter: IsoGameCharacter):
    self.bodyoutline: Texture
    self.foot_l: UI_BodyPart
    self.foot_r: UI_BodyPart
    self.forearm_l: UI_BodyPart
    self.forearm_r: UI_BodyPart
    self.groin: UI_BodyPart
    self.hand_l: UI_BodyPart
    self.hand_r: UI_BodyPart
    self.head: UI_BodyPart
    self.healthbar: Texture
    self.healthbarback: Texture
    self.healthicon: Texture
    self.lowerleg_l: UI_BodyPart
    self.lowerleg_r: UI_BodyPart
    self.neck: UI_BodyPart
    self.torso_lower: UI_BodyPart
    self.torso_upper: UI_BodyPart
    self.upperarm_l: UI_BodyPart
    self.upperarm_r: UI_BodyPart
    self.upperleg_l: UI_BodyPart
    self.upperleg_r: UI_BodyPart


class NewWindow(UIElement):

  def ButtonClicked(self, name: str) -> None: ...

  def Nest(self, el: UIElement, t: int, r: int, b: int, l: int) -> None: ...

  def onMouseDown(self, x: float, y: float) -> Boolean: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def onMouseUp(self, x: float, y: float) -> Boolean: ...

  def render(self) -> None: ...

  def setMovable(self, bMoveable: bool) -> None: ...

  def update(self) -> None: ...

  def __init__(self, x: int, y: int, width: int, height: int, bHasClose: bool):
    self.clickx: int
    self.clicky: int
    self.clienth: int
    self.clientw: int
    self.movable: bool
    self.moving: bool
    self.ncclienth: int
    self.ncclientw: int
    self.nesteditems: Stack[Rectangle]
    self.resizetofity: bool


class ObjectTooltip(UIElement):

  alphaStep: float

  def DrawProgressBar(self, x: int, y: int, w: int, h: int, f: float, r: float, g: float, b: float, a: float) -> None: ...

  def DrawText(self, font: UIFont, text: str, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  def DrawTextCentre(self, font: UIFont, text: str, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  def DrawTextRight(self, font: UIFont, text: str, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  def DrawTextureScaled(self, tex: Texture, x: float, y: float, width: float, height: float, alpha: float) -> None: ...

  def DrawTextureScaledAspect(self, tex: Texture, x: float, y: float, width: float, height: float, r: float, g: float, b: float, alpha: float) -> None: ...

  def DrawValueRight(self, value: int, x: int, y: int, highGood: bool) -> None: ...

  @overload
  def DrawValueRightNoPlus(self, value: float, x: int, y: int) -> None: ...

  @overload
  def DrawValueRightNoPlus(self, value: int, x: int, y: int) -> None: ...

  def adjustWidth(self, textX: int, text: str) -> None: ...

  def beginLayout(self) -> ObjectTooltip.Layout: ...

  def endLayout(self, layout: ObjectTooltip.Layout) -> None: ...

  def getCharacter(self) -> IsoGameCharacter: ...

  def getFont(self) -> UIFont: ...

  def getLineSpacing(self) -> int: ...

  def getTexture(self) -> Texture: ...

  def getWeightOfStack(self) -> float: ...

  def hide(self) -> None: ...

  def isMeasureOnly(self) -> bool: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def render(self) -> None: ...

  def setCharacter(self, chr: IsoGameCharacter) -> None: ...

  def setMeasureOnly(self, b: bool) -> None: ...

  def setWeightOfStack(self, weight: float) -> None: ...

  def show(self, obj: IsoObject, x: float, y: float) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def checkFont() -> None: ...

  def __init__(self):
    self.bisitem: bool
    self.item: InventoryItem
    self.object: IsoObject
    self.padbottom: int
    self.padright: int

  class Layout:

    def addItem(self) -> ObjectTooltip.LayoutItem: ...

    def free(self) -> None: ...

    def render(self, left: int, top: int, ui: ObjectTooltip) -> int: ...

    def setMinLabelWidth(self, minWidth: int) -> None: ...

    def setMinValueWidth(self, minWidth: int) -> None: ...

    def __init__(self):
      self.items: ArrayList[ObjectTooltip.LayoutItem]
      self.minlabelwidth: int
      self.minvaluewidth: int
      self.next: ObjectTooltip.Layout
      self.nextpady: int

  class LayoutItem:

    def calcSizes(self) -> None: ...

    def render(self, x: int, y: int, mid: int, right: int, ui: ObjectTooltip) -> None: ...

    def reset(self) -> None: ...

    def setLabel(self, label: str, r: float, g: float, b: float, a: float) -> None: ...

    def setProgress(self, fraction: float, r: float, g: float, b: float, a: float) -> None: ...

    def setValue(self, label: str, r: float, g: float, b: float, a: float) -> None: ...

    def setValueRight(self, value: int, highGood: bool) -> None: ...

    @overload
    def setValueRightNoPlus(self, value: float) -> None: ...

    @overload
    def setValueRightNoPlus(self, value: int) -> None: ...

    def __init__(self):
      self.a0: float
      self.a1: float
      self.b0: float
      self.b1: float
      self.g0: float
      self.g1: float
      self.hasvalue: bool
      self.height: int
      self.label: str
      self.labelwidth: int
      self.progressfraction: float
      self.progresswidth: int
      self.r0: float
      self.r1: float
      self.rightjustify: bool
      self.value: str
      self.valuewidth: int
      self.valuewidthright: int


class RadarPanel(UIElement):

  def render(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self, playerIndex: int): ...

  class ZombiePosPool:

    def alloc(self, arg0: float, arg1: float) -> RadarPanel.ZombiePos: ...

    def release(self, arg0: Collection[RadarPanel.ZombiePos]) -> None: ...

  class ZombiePos:

    def set(self, arg0: float, arg1: float) -> RadarPanel.ZombiePos: ...

    def __init__(self, arg0: float, arg1: float):
      self.x: float
      self.y: float


class RadialMenu(UIElement):

  def addSlice(self, text: str, texture: Texture) -> None: ...

  def clear(self) -> None: ...

  def getSliceIndexFromJoypad(self, joypad: int) -> int: ...

  def getSliceIndexFromMouse(self, mx: int, my: int) -> int: ...

  def render(self) -> None: ...

  def setJoypad(self, joypad: int) -> None: ...

  def setSliceText(self, sliceIndex: int, text: str) -> None: ...

  def setSliceTexture(self, sliceIndex: int, texture: Texture) -> None: ...

  def update(self) -> None: ...

  def __init__(self, x: int, y: int, innerRadius: int, outerRadius: int): ...

  class Slice: ...


class RadialProgressBar(UIElement):

  def getTexture(self) -> Texture: ...

  def getValue(self) -> float: ...

  def render(self) -> None: ...

  def setTexture(self, texture: Texture) -> None: ...

  def setValue(self, delta: float) -> None: ...

  def update(self) -> None: ...

  def __init__(self, table: KahluaTable, tex: Texture): ...

  class RadSegment: ...


class ScrollBar(UIElement):

  def SetParentTextBox(self, Parent: UITextBox2) -> None: ...

  def onMouseDown(self, x: float, y: float) -> Boolean: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def onMouseUp(self, x: float, y: float) -> Boolean: ...

  def render(self) -> None: ...

  def scrollToBottom(self) -> None: ...

  def setHeight(self, height: float) -> None: ...

  def update(self) -> None: ...

  def __init__(self, name: str, messages: UIEventHandler, x_pos: int, y_pos: int, Length: int, IsVertical: bool):
    self.backgroundcolour: Color
    self.buttoncolour: Color
    self.buttonhighlightcolour: Color
    self.isverticle: bool


class SpeedControls(UIElement):

  FasterForward: HUDButton

  FastForward: HUDButton

  instance: SpeedControls

  Pause: HUDButton

  Play: HUDButton

  Wait: HUDButton

  def ButtonClicked(self, name: str) -> None: ...

  def SetCorrectIconStates(self) -> None: ...

  def SetCurrentGameSpeed(self, NewSpeed: int) -> None: ...

  def getCurrentGameSpeed(self) -> int: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def render(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self):
    self.currentspeed: int
    self.multibeforepause: float
    self.speedbeforepause: int

  class SCButton(HUDButton):

    def render(self) -> None: ...

    def __init__(self, name: str, x: float, y: float, texture: str, highlight: str, display: UIElement): ...


class TextBox(UIElement):

  def SetText(self, text: str) -> None: ...

  def onresize(self) -> None: ...

  def render(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self, font: UIFont, x: int, y: int, width: int, text: str):
    self.centred: bool
    self.resizeparent: bool


class TextDrawHorizontal(Enum):

  Center: TextDrawHorizontal

  Left: TextDrawHorizontal

  Right: TextDrawHorizontal

  @staticmethod
  def valueOf(arg0: str) -> TextDrawHorizontal: ...

  @staticmethod
  def values() -> list[TextDrawHorizontal]: ...


class TextDrawObject:

  @overload
  def AddBatchedDraw(self, x: float, y: float) -> None: ...

  @overload
  def AddBatchedDraw(self, x: float, y: float, drawOutlines: bool) -> None: ...

  @overload
  def AddBatchedDraw(self, x: float, y: float, drawOutlines: bool, alpha: float) -> None: ...

  @overload
  def AddBatchedDraw(self, x: float, y: float, r: float, g: float, b: float, a: float, drawOutlines: bool) -> None: ...

  @overload
  def AddBatchedDraw(self, horz: TextDrawHorizontal, x: float, y: float, r: float, g: float, b: float, a: float, drawOutlines: bool) -> None: ...

  def Clear(self) -> None: ...

  @overload
  def Draw(self, x: float, y: float) -> None: ...

  @overload
  def Draw(self, x: float, y: float, drawOutlines: bool) -> None: ...

  @overload
  def Draw(self, x: float, y: float, drawOutlines: bool, alpha: float) -> None: ...

  @overload
  def Draw(self, x: float, y: float, r: float, g: float, b: float, a: float, drawOutlines: bool) -> None: ...

  @overload
  def Draw(self, horz: TextDrawHorizontal, x: float, y: float, r: float, g: float, b: float, a: float, drawOutlines: bool) -> None: ...

  def DrawRaw(self, horz: TextDrawHorizontal, x: float, y: float, r: float, g: float, b: float, a: float, drawOutlines: bool) -> None: ...

  @overload
  def ReadString(self, str: str) -> None: ...

  @overload
  def ReadString(self, str: str, maxLineWidth: int) -> None: ...

  @overload
  def ReadString(self, font: UIFont, str: str, maxLineWidth: int) -> None: ...

  def calculateDimensions(self) -> None: ...

  def getCustomTag(self) -> str: ...

  def getDefaultFontEnum(self) -> UIFont: ...

  def getEnabled(self) -> bool: ...

  def getHearRange(self) -> int: ...

  def getHeight(self) -> int: ...

  def getHorizontalAlign(self) -> TextDrawHorizontal: ...

  def getInternalClock(self) -> float: ...

  def getOriginal(self) -> str: ...

  def getScrambleVal(self) -> float: ...

  def getUnformatted(self) -> str: ...

  def getVisibleRadius(self) -> int: ...

  def getWidth(self) -> int: ...

  def isNullOrZeroLength(self) -> bool: ...

  def setAllowAnyImage(self, allowAnyImage: bool) -> None: ...

  def setAllowBBcode(self, allowBBcode: bool) -> None: ...

  def setAllowChatIcons(self, allowChatIcons: bool) -> None: ...

  def setAllowColors(self, allowColors: bool) -> None: ...

  def setAllowFonts(self, allowFonts: bool) -> None: ...

  def setAllowImages(self, allowImages: bool) -> None: ...

  def setAllowLineBreaks(self, allowLineBreaks: bool) -> None: ...

  def setCustomImageMaxDimensions(self, dim: int) -> None: ...

  def setCustomTag(self, tag: str) -> None: ...

  @overload
  def setDefaultColors(self, r: float, g: float, b: float) -> None: ...

  @overload
  def setDefaultColors(self, r: int, g: int, b: int) -> None: ...

  @overload
  def setDefaultColors(self, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def setDefaultColors(self, r: int, g: int, b: int, a: int) -> None: ...

  def setDefaultFont(self, f: UIFont) -> None: ...

  def setDrawBackground(self, draw: bool) -> None: ...

  def setEnabled(self, enabled: bool) -> None: ...

  def setEqualizeLineHeights(self, equalizeLineHeights: bool) -> None: ...

  def setHearRange(self, range: int) -> None: ...

  @overload
  def setHorizontalAlign(self, horz: str) -> None: ...

  @overload
  def setHorizontalAlign(self, horz: TextDrawHorizontal) -> None: ...

  def setInternalTickClock(self, ticks: float) -> None: ...

  def setMaxCharsPerLine(self, charsperline: int) -> None: ...

  @overload
  def setOutlineColors(self, r: float, g: float, b: float) -> None: ...

  @overload
  def setOutlineColors(self, r: int, g: int, b: int) -> None: ...

  @overload
  def setOutlineColors(self, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def setOutlineColors(self, r: int, g: int, b: int, a: int) -> None: ...

  def setScrambleVal(self, value: float) -> None: ...

  def setSettings(self, allowBBcode: bool, allowImages: bool, allowChatIcons: bool, allowColors: bool, allowFonts: bool, equalizeLineHeights: bool) -> None: ...

  def setValidFonts(self, list: list[str]) -> None: ...

  def setValidImages(self, list: list[str]) -> None: ...

  def setVisibleRadius(self, radius: int) -> None: ...

  @overload
  def updateInternalTickClock(self) -> float: ...

  @overload
  def updateInternalTickClock(self, delta: float) -> float: ...

  @staticmethod
  def NoRender(playerNum: int) -> None: ...

  @staticmethod
  def RenderBatch(playerNum: int) -> None: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, r: int, g: int, b: int, allowBBcode: bool): ...
  @overload
  def __init__(self, r: int, g: int, b: int, allowBBcode: bool, allowImages: bool, allowChatIcons: bool, allowColors: bool, allowFonts: bool, equalizeLineHeights: bool): ...

  class DrawLine: ...

  class DrawElement: ...

  class RenderBatch: ...


class TextManager:

  instance: TextManager

  @overload
  def DrawString(self, x: float, y: float, str: str) -> None: ...

  @overload
  def DrawString(self, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def DrawString(self, font: UIFont, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def DrawString(self, font: UIFont, x: float, y: float, zoom: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  def DrawStringBBcode(self, font: UIFont, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def DrawStringCentre(self, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def DrawStringCentre(self, font: UIFont, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  def DrawStringCentreDefered(self, font: UIFont, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def DrawStringRight(self, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def DrawStringRight(self, font: UIFont, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  def DrawStringUntrimmed(self, font: UIFont, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  def DrawTextFromGameWorld(self) -> None: ...

  def DrawTextObject(self, x: float, y: float, td: TextDrawObject) -> None: ...

  def GetDrawTextObject(self, str: str, maxLineWidth: int, restrictImages: bool) -> TextDrawObject: ...

  def Init(self) -> None: ...

  def MeasureFont(self, font: UIFont) -> int: ...

  def MeasureStringX(self, font: UIFont, str: str) -> int: ...

  def MeasureStringY(self, font: UIFont, str: str) -> int: ...

  def getFontFromEnum(self, font: UIFont) -> AngelCodeFont: ...

  def getFontHeight(self, fontID: UIFont) -> int: ...

  def getNormalFromFontSize(self, points: int) -> AngelCodeFont: ...

  def __init__(self):
    self.codetext: AngelCodeFont
    self.debugconsole: AngelCodeFont
    self.enumtofont: list[AngelCodeFont]
    self.font: AngelCodeFont
    self.font2: AngelCodeFont
    self.font3: AngelCodeFont
    self.font4: AngelCodeFont
    self.handwritten: AngelCodeFont
    self.intro: AngelCodeFont
    self.main1: AngelCodeFont
    self.main2: AngelCodeFont
    self.normal: list[AngelCodeFont]
    self.todotextlist: ArrayList[TextManager.DeferedTextDraw]
    self.zombiefontcredits1: AngelCodeFont
    self.zombiefontcredits2: AngelCodeFont
    self.zombienew1: AngelCodeFont
    self.zombienew2: AngelCodeFont
    self.zombienew3: AngelCodeFont
    self.zomboiddialogue: AngelCodeFont

  class DeferedTextDraw:

    def __init__(self, font: UIFont, x: float, y: float, str: str, r: float, g: float, b: float, a: float):
      self.a: float
      self.b: float
      self.font: UIFont
      self.g: float
      self.r: float
      self.str: str
      self.x: float
      self.y: float

  class StringDrawer:

    def draw(self, font: UIFont, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...


class TutorialManager:

  Debug: bool

  instance: TutorialManager

  def AllowUse(self, Object: IsoObject) -> bool: ...

  def CheckWake(self) -> None: ...

  def CreateQuests(self) -> None: ...

  def init(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self):
    self.active: bool
    self.activecontrolzombies: bool
    self.alarmticktime: int
    self.alarmtime: int
    self.allowsleep: bool
    self.barricadecount: int
    self.candragwife: bool
    self.donefirstsleep: bool
    self.doorslocked: bool
    self.gunnut: IsoSurvivor
    self.millingtune: str
    self.prefmusic: str
    self.profanityfilter: bool
    self.skipped: bool
    self.stage: TutorialManager.Stage
    self.stealcontrol: bool
    self.targetzombies: float
    self.timer: int
    self.triggerfire: bool
    self.tutbuilding: IsoBuilding
    self.tutorialstove: IsoStove
    self.warnedhammer: bool
    self.wife: IsoSurvivor
    self.wifekilledbyearl: bool

  class Stage(Enum):

    Alarm: TutorialManager.Stage

    Apply: TutorialManager.Stage

    BoardUpHouse: TutorialManager.Stage

    BreakBarricade: TutorialManager.Stage

    Distraction: TutorialManager.Stage

    EquipHammer: TutorialManager.Stage

    Escape: TutorialManager.Stage

    ExploreHouse: TutorialManager.Stage

    FindFood: TutorialManager.Stage

    FindShed: TutorialManager.Stage

    getBelt: TutorialManager.Stage

    getShedItems: TutorialManager.Stage

    getSoupIngredients: TutorialManager.Stage

    InHouseFood: TutorialManager.Stage

    InvestigateSound: TutorialManager.Stage

    KillZombie: TutorialManager.Stage

    LightStove: TutorialManager.Stage

    MakeSoupPot: TutorialManager.Stage

    Mouseover: TutorialManager.Stage

    RipSheet: TutorialManager.Stage

    ShouldBeOk: TutorialManager.Stage

    StockUp: TutorialManager.Stage

    @staticmethod
    def valueOf(arg0: str) -> TutorialManager.Stage: ...

    @staticmethod
    def values() -> list[TutorialManager.Stage]: ...


class UI3DModel(UIElement):

  @overload
  def clothingItemChanged(self, itemGuid: str) -> None: ...

  @overload
  def clothingItemChanged(self, itemGuid: str) -> None: ...

  def getDirection(self) -> IsoDirections: ...

  def render(self) -> None: ...

  def reportEvent(self, event: str) -> None: ...

  def setAnimSetName(self, name: str) -> None: ...

  def setAnimate(self, animate: bool) -> None: ...

  def setCharacter(self, character: IsoGameCharacter) -> None: ...

  def setDirection(self, dir: IsoDirections) -> None: ...

  def setDoRandomExtAnimations(self, doExt: bool) -> None: ...

  def setIsometric(self, iso: bool) -> None: ...

  def setOutfitName(self, outfitName: str, female: bool, zombie: bool) -> None: ...

  def setState(self, state: str) -> None: ...

  def setSurvivorDesc(self, survivorDesc: SurvivorDesc) -> None: ...

  def setXOffset(self, newXOffset: float) -> None: ...

  def setYOffset(self, newYOffset: float) -> None: ...

  def setZoom(self, newZoom: float) -> None: ...

  def __init__(self, table: KahluaTable): ...

  class Drawer(TextureDraw.GenericDrawer):

    def init(self, arg0: int, arg1: int) -> None: ...

    def postRender(self) -> None: ...

    def render(self) -> None: ...


class UIDebugConsole(NewWindow):

  instance: UIDebugConsole

  def ProcessCommand(self) -> None: ...

  def addOutput(self, b: list[int], __off__: int, len: int) -> None: ...

  def levenshteinDistance(self, lhs: CharSequence, rhs: CharSequence) -> int: ...

  def onOtherKey(self, key: int) -> None: ...

  def render(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self, x: int, y: int):
    self.bdebouncedown: bool
    self.bdebounceup: bool
    self.commandline: UITextBox2
    self.previousindex: int

  class CommandEntry(UITextBox2):

    def onOtherKey(self, arg0: int) -> None: ...

    def onPressDown(self) -> None: ...

    def onPressUp(self) -> None: ...

    def __init__(self, arg0: UIDebugConsole, arg1: UIFont, arg2: int, arg3: int, arg4: int, arg5: int, arg6: str, arg7: bool): ...


class UIDialoguePanel(UIElement):

  def Nest(self, el: UIElement, t: int, r: int, b: int, l: int) -> None: ...

  def render(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self, x: float, y: float, width: float, height: float):
    self.clienth: float
    self.clientw: float
    self.nesteditems: Stack[Rectangle]


class UIElement:

  def AddChild(self, el: UIElement) -> None: ...

  def BringToTop(self, el: UIElement) -> None: ...

  def ButtonClicked(self, name: str) -> None: ...

  def ClearChildren(self) -> None: ...

  def DrawSubTextureRGBA(self, tex: Texture, subX: float, subY: float, subW: float, subH: float, x: float, y: float, w: float, h: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def DrawText(self, text: str, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  @overload
  def DrawText(self, font: UIFont, text: str, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  @overload
  def DrawText(self, text: str, x: float, y: float, width: float, height: float, r: float, g: float, b: float, alpha: float) -> None: ...

  @overload
  def DrawText(self, font: UIFont, text: str, x: float, y: float, zoom: float, r: float, g: float, b: float, alpha: float) -> None: ...

  @overload
  def DrawTextCentre(self, text: str, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  @overload
  def DrawTextCentre(self, font: UIFont, text: str, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  @overload
  def DrawTextRight(self, text: str, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  @overload
  def DrawTextRight(self, font: UIFont, text: str, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  def DrawTextUntrimmed(self, font: UIFont, text: str, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  @overload
  def DrawTexture(self, tex: Texture, x: float, y: float, alpha: float) -> None: ...

  @overload
  def DrawTexture(self, tex: Texture, tlx: float, tly: float, trx: float, try2: float, brx: float, bry: float, blx: float, bly: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def DrawTextureAngle(self, tex: Texture, centerX: float, centerY: float, angle: float) -> None: ...

  @overload
  def DrawTextureAngle(self, tex: Texture, centerX: float, centerY: float, angle: float, r: float, g: float, b: float, a: float) -> None: ...

  def DrawTextureCol(self, tex: Texture, x: float, y: float, col: Color) -> None: ...

  def DrawTextureColor(self, tex: Texture, x: float, y: float, r: float, g: float, b: float, a: float) -> None: ...

  def DrawTextureIgnoreOffset(self, tex: Texture, x: float, y: float, width: int, height: int, col: Color) -> None: ...

  def DrawTextureScaled(self, tex: Texture, x: float, y: float, width: float, height: float, alpha: float) -> None: ...

  def DrawTextureScaledAspect(self, tex: Texture, x: float, y: float, width: float, height: float, r: float, g: float, b: float, alpha: float) -> None: ...

  def DrawTextureScaledAspect2(self, tex: Texture, x: float, y: float, width: float, height: float, r: float, g: float, b: float, alpha: float) -> None: ...

  @overload
  def DrawTextureScaledCol(self, tex: Texture, x: float, y: float, width: float, height: float, col: Color) -> None: ...

  @overload
  def DrawTextureScaledCol(self, tex: Texture, x: float, y: float, width: float, height: float, r: float, g: float, b: float, a: float) -> None: ...

  def DrawTextureScaledColor(self, tex: Texture, x: Double, y: Double, width: Double, height: Double, r: Double, g: Double, b: Double, a: Double) -> None: ...

  def DrawTextureScaledUniform(self, tex: Texture, x: float, y: float, scale: float, r: float, g: float, b: float, alpha: float) -> None: ...

  def DrawTextureTiled(self, tex: Texture, x: float, y: float, w: float, h: float, r: float, g: float, b: float, a: float) -> None: ...

  def DrawTextureTiledX(self, tex: Texture, x: float, y: float, w: float, h: float, r: float, g: float, b: float, a: float) -> None: ...

  def DrawTextureTiledY(self, tex: Texture, x: float, y: float, w: float, h: float, r: float, g: float, b: float, a: float) -> None: ...

  def DrawTexture_FlippedX(self, tex: Texture, x: float, y: float, width: int, height: int, col: Color) -> None: ...

  def DrawTexture_FlippedXIgnoreOffset(self, tex: Texture, x: float, y: float, width: int, height: int, col: Color) -> None: ...

  def DrawUVSliceTexture(self, tex: Texture, x: float, y: float, width: float, height: float, col: Color, xStart: float, yStart: float, xEnd: float, yEnd: float) -> None: ...

  def RemoveChild(self, el: UIElement) -> None: ...

  def RemoveControl(self, el: UIElement) -> None: ...

  def backMost(self) -> None: ...

  def bringToTop(self) -> None: ...

  def clampToParentX(self, x: float) -> Double: ...

  def clampToParentY(self, y: float) -> Double: ...

  def clearMaxDrawHeight(self) -> None: ...

  def clearStencilRect(self) -> None: ...

  def getAbsoluteX(self) -> Double: ...

  def getAbsoluteY(self) -> Double: ...

  def getClickedValue(self) -> str: ...

  def getControls(self) -> ArrayList[UIElement]: ...

  def getHeight(self) -> Double: ...

  def getMaxDrawHeight(self) -> Double: ...

  def getParent(self) -> UIElement: ...

  def getPlayerContext(self) -> int: ...

  def getRenderThisPlayerOnly(self) -> int: ...

  def getScrollChildren(self) -> Boolean: ...

  def getScrollHeight(self) -> Double: ...

  def getScrollWithParent(self) -> Boolean: ...

  def getTable(self) -> KahluaTable: ...

  def getUIName(self) -> str: ...

  def getWidth(self) -> Double: ...

  def getX(self) -> Double: ...

  def getXScroll(self) -> Double: ...

  def getXScrolled(self, parent: UIElement) -> Double: ...

  def getY(self) -> Double: ...

  def getYScroll(self) -> Double: ...

  def getYScrolled(self, parent: UIElement) -> Double: ...

  def ignoreHeightChange(self) -> None: ...

  def ignoreWidthChange(self) -> None: ...

  def isAnchorBottom(self) -> Boolean: ...

  def isAnchorLeft(self) -> Boolean: ...

  def isAnchorRight(self) -> Boolean: ...

  def isAnchorTop(self) -> bool: ...

  def isCapture(self) -> Boolean: ...

  def isConsumeMouseEvents(self) -> bool: ...

  def isDefaultDraw(self) -> Boolean: ...

  def isEnabled(self) -> bool: ...

  def isFollowGameWorld(self) -> Boolean: ...

  def isForceCursorVisible(self) -> bool: ...

  def isIgnoreLossControl(self) -> Boolean: ...

  def isKeyConsumed(self, key: int) -> bool: ...

  def isMouseOver(self) -> Boolean: ...

  def isPointOver(self, screenX: float, screenY: float) -> Boolean: ...

  def isVisible(self) -> Boolean: ...

  def isWantKeyEvents(self) -> bool: ...

  def onKeyPress(self, key: int) -> None: ...

  def onKeyRelease(self, key: int) -> None: ...

  def onKeyRepeat(self, key: int) -> None: ...

  def onMouseDown(self, x: float, y: float) -> Boolean: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def onMouseUp(self, x: float, y: float) -> Boolean: ...

  def onMouseUpOutside(self, x: float, y: float) -> None: ...

  def onMouseWheel(self, arg0: float) -> Boolean: ...

  def onResize(self) -> None: ...

  def onRightMouseDown(self, x: float, y: float) -> Boolean: ...

  def onRightMouseUp(self, x: float, y: float) -> Boolean: ...

  def onresize(self) -> None: ...

  def render(self) -> None: ...

  def repaintStencilRect(self, x: float, y: float, width: float, height: float) -> None: ...

  def resumeStencil(self) -> None: ...

  def setAlwaysOnTop(self, b: bool) -> None: ...

  def setAnchorBottom(self, anchorBottom: bool) -> None: ...

  def setAnchorLeft(self, anchorLeft: bool) -> None: ...

  def setAnchorRight(self, anchorRight: bool) -> None: ...

  def setAnchorTop(self, anchorTop: bool) -> None: ...

  def setCapture(self, capture: bool) -> None: ...

  def setClickedValue(self, clickedValue: str) -> None: ...

  def setConsumeMouseEvents(self, bConsume: bool) -> None: ...

  def setControls(self, Controls: Vector[UIElement]) -> None: ...

  def setDefaultDraw(self, defaultDraw: bool) -> None: ...

  def setEnabled(self, en: bool) -> None: ...

  def setFollowGameWorld(self, followGameWorld: bool) -> None: ...

  def setForceCursorVisible(self, force: bool) -> None: ...

  def setHeight(self, height: float) -> None: ...

  def setHeightOnly(self, height: float) -> None: ...

  def setHeightSilent(self, height: float) -> None: ...

  def setIgnoreLossControl(self, IgnoreLossControl: bool) -> None: ...

  def setMaxDrawHeight(self, height: float) -> None: ...

  def setParent(self, Parent: UIElement) -> None: ...

  def setPlayerContext(self, nPlayer: int) -> None: ...

  def setRenderClippedChildren(self, b: bool) -> None: ...

  def setRenderThisPlayerOnly(self, playerIndex: int) -> None: ...

  def setScrollChildren(self, bScroll: bool) -> None: ...

  def setScrollHeight(self, h: float) -> None: ...

  def setScrollWithParent(self, bScroll: bool) -> None: ...

  def setStencilRect(self, x: float, y: float, width: float, height: float) -> None: ...

  def setTable(self, table: KahluaTable) -> None: ...

  def setUIName(self, name: str) -> None: ...

  def setVisible(self, visible: bool) -> None: ...

  def setWantKeyEvents(self, want: bool) -> None: ...

  def setWidth(self, width: float) -> None: ...

  def setWidthOnly(self, width: float) -> None: ...

  def setWidthSilent(self, width: float) -> None: ...

  def setX(self, x: float) -> None: ...

  def setXScroll(self, x: float) -> None: ...

  def setY(self, y: float) -> None: ...

  def setYScroll(self, y: float) -> None: ...

  def suspendStencil(self) -> None: ...

  def update(self) -> None: ...

  @overload
  def __init__(self):
    self.alwaysback: bool

    self.anchorbottom: bool

    self.anchorleft: bool

    self.anchorright: bool

    self.anchortop: bool

    self.bscrollchildren: bool

    self.bscrollwithparent: bool

    self.capture: bool

    self.clickedvalue: str

    self.controls: ArrayList[UIElement]

    self.defaultdraw: bool

    self.followgameworld: bool

    self.height: float

    self.ignorelosscontrol: bool

    self.parent: UIElement

    self.playercontext: int

    self.table: KahluaTable

    self.visible: bool

    self.width: float

    self.x: float

    self.y: float

  @overload
  def __init__(self, table: KahluaTable): ...


class UIEventHandler:

  def DoubleClick(self, name: str, x: int, y: int) -> None: ...

  def ModalClick(self, name: str, chosen: str) -> None: ...

  def Selected(self, name: str, Selected: int, LastSelected: int) -> None: ...


class UIFont(Enum):

  AutoNormLarge: UIFont

  AutoNormMedium: UIFont

  AutoNormSmall: UIFont

  Code: UIFont

  Cred1: UIFont

  Cred2: UIFont

  DebugConsole: UIFont

  Dialogue: UIFont

  Handwritten: UIFont

  Intro: UIFont

  Large: UIFont

  MainMenu1: UIFont

  MainMenu2: UIFont

  Massive: UIFont

  Medium: UIFont

  MediumNew: UIFont

  NewLarge: UIFont

  NewMedium: UIFont

  NewSmall: UIFont

  Small: UIFont

  Title: UIFont

  @staticmethod
  def FromString(str: str) -> UIFont: ...

  @staticmethod
  def valueOf(arg0: str) -> UIFont: ...

  @staticmethod
  def values() -> list[UIFont]: ...


class UIManager:

  bFadeBeforeUI: bool

  black: Texture

  bSuspend: bool

  clock: Clock

  DebugConsole: UIDebugConsole

  defaultthread: KahluaThread

  DoneTutorials: ArrayList[str]

  doTick: bool

  FadeAlpha: float

  FadeInTime: int

  FadeInTimeMax: int

  FadingOut: bool

  KeyDownZoomIn: bool

  KeyDownZoomOut: bool

  lastAlpha: float

  lastMouseTexture: Texture

  lastMouseX: int

  lastMouseY: int

  lastOffX: float

  lastOffY: float

  LastPicked: IsoObject

  luaDebuggerAction: str

  Modal: ModalDialog

  MoodleUI: list[MoodlesUI]

  mouseArrow: Texture

  mouseAttack: Texture

  mouseExamine: Texture

  mouseGrab: Texture

  Picked: IsoObjectPicker.ClickObject

  PickedTile: Vector2

  PickedTileLocal: Vector2

  previousThread: KahluaThread

  ProgressBar: list[ActionProgressBar]

  RightDownObject: IsoObject

  ServerToolbox: UIServerToolbox

  speedControls: SpeedControls

  toolTip: ObjectTooltip

  toTop: ArrayList[UIElement]

  UI: ArrayList[UIElement]

  UIFBO: TextureFBO

  uiRenderIntervalMS: int

  uiRenderTimeMS: int

  uiUpdateIntervalMS: int

  uiUpdateTimeMS: int

  useUIFBO: bool

  VisibleAllUI: bool

  @staticmethod
  def AddUI(el: UIElement) -> None: ...

  @staticmethod
  def CloseContainers() -> None: ...

  @staticmethod
  def CreateFBO(width: int, height: int) -> None: ...

  @staticmethod
  @overload
  def DrawTexture(tex: Texture, x: float, y: float) -> None: ...

  @staticmethod
  @overload
  def DrawTexture(tex: Texture, x: float, y: float, width: float, height: float, alpha: float) -> None: ...

  @staticmethod
  @overload
  def FadeIn(seconds: float) -> None: ...

  @staticmethod
  @overload
  def FadeIn(playerIndex: float, seconds: float) -> None: ...

  @staticmethod
  @overload
  def FadeOut(seconds: float) -> None: ...

  @staticmethod
  @overload
  def FadeOut(playerIndex: float, seconds: float) -> None: ...

  @staticmethod
  def RemoveElement(el: UIElement) -> None: ...

  @staticmethod
  def clearArrays() -> None: ...

  @staticmethod
  def closeContainers() -> None: ...

  @staticmethod
  def createTexture(x: float, y: float, test: bool) -> TextureFBO: ...

  @staticmethod
  def debugBreakpoint(filename: str, pc: int) -> None: ...

  @staticmethod
  def getBlack() -> Texture: ...

  @staticmethod
  def getClock() -> Clock: ...

  @staticmethod
  def getDebugConsole() -> UIDebugConsole: ...

  @staticmethod
  def getDefaultThread() -> KahluaThread: ...

  @staticmethod
  def getDoneTutorials() -> ArrayList[str]: ...

  @staticmethod
  def getDoubleClickDist() -> Double: ...

  @staticmethod
  def getDoubleClickInterval() -> Double: ...

  @staticmethod
  @overload
  def getFadeAlpha() -> Double: ...

  @staticmethod
  @overload
  def getFadeAlpha(playerIndex: float) -> float: ...

  @staticmethod
  def getFadeInTime() -> Double: ...

  @staticmethod
  def getFadeInTimeMax() -> Double: ...

  @staticmethod
  def getLastAlpha() -> float: ...

  @staticmethod
  def getLastMouseTexture() -> Texture: ...

  @staticmethod
  def getLastMouseX() -> Double: ...

  @staticmethod
  def getLastMouseY() -> Double: ...

  @staticmethod
  def getLastOffX() -> float: ...

  @staticmethod
  def getLastOffY() -> float: ...

  @staticmethod
  def getLastPicked() -> IsoObject: ...

  @staticmethod
  def getMillisSinceLastRender() -> float: ...

  @staticmethod
  def getMillisSinceLastUpdate() -> float: ...

  @staticmethod
  def getModal() -> ModalDialog: ...

  @staticmethod
  def getMoodleUI(index: float) -> MoodlesUI: ...

  @staticmethod
  def getMouseArrow() -> Texture: ...

  @staticmethod
  def getMouseAttack() -> Texture: ...

  @staticmethod
  def getMouseExamine() -> Texture: ...

  @staticmethod
  def getMouseGrab() -> Texture: ...

  @staticmethod
  def getPicked() -> IsoObjectPicker.ClickObject: ...

  @staticmethod
  def getPickedTile() -> Vector2: ...

  @staticmethod
  def getPickedTileLocal() -> Vector2: ...

  @staticmethod
  def getProgressBar(index: float) -> ActionProgressBar: ...

  @staticmethod
  def getRightDownObject() -> IsoObject: ...

  @staticmethod
  def getSecondsSinceLastRender() -> float: ...

  @staticmethod
  def getSecondsSinceLastUpdate() -> float: ...

  @staticmethod
  def getServerToolbox() -> UIServerToolbox: ...

  @staticmethod
  def getSpeedControls() -> SpeedControls: ...

  @staticmethod
  def getTileFromMouse(mx: float, my: float, z: float) -> Vector2: ...

  @staticmethod
  def getToolTip() -> ObjectTooltip: ...

  @staticmethod
  def getUI() -> ArrayList[UIElement]: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def isDoubleClick(x1: float, y1: float, x2: float, y2: float, clickTime: float) -> Boolean: ...

  @staticmethod
  def isFBOActive() -> bool: ...

  @staticmethod
  def isFadingOut() -> Boolean: ...

  @staticmethod
  def isForceCursorVisible() -> bool: ...

  @staticmethod
  def isMouseOverInventory() -> bool: ...

  @staticmethod
  def isShowLuaDebuggerOnError() -> bool: ...

  @staticmethod
  def isShowPausedMessage() -> bool: ...

  @staticmethod
  def isbFadeBeforeUI() -> bool: ...

  @staticmethod
  def onKeyPress(key: int) -> bool: ...

  @staticmethod
  def onKeyRelease(key: int) -> bool: ...

  @staticmethod
  def onKeyRepeat(key: int) -> bool: ...

  @staticmethod
  def render() -> None: ...

  @staticmethod
  def resize() -> None: ...

  @staticmethod
  def setBlack(aBlack: Texture) -> None: ...

  @staticmethod
  def setClock(aClock: Clock) -> None: ...

  @staticmethod
  def setDebugConsole(aDebugConsole: UIDebugConsole) -> None: ...

  @staticmethod
  def setDoneTutorials(aDoneTutorials: ArrayList[str]) -> None: ...

  @staticmethod
  def setFadeAlpha(aFadeAlpha: float) -> None: ...

  @staticmethod
  def setFadeBeforeUI(playerIndex: int, bFadeBeforeUI: bool) -> None: ...

  @staticmethod
  def setFadeInTime(aFadeInTime: float) -> None: ...

  @staticmethod
  def setFadeInTimeMax(aFadeInTimeMax: float) -> None: ...

  @staticmethod
  def setFadeTime(playerIndex: float, FadeTime: float) -> None: ...

  @staticmethod
  def setFadingOut(aFadingOut: bool) -> None: ...

  @staticmethod
  def setLastAlpha(aLastAlpha: float) -> None: ...

  @staticmethod
  def setLastMouseTexture(aLastMouseTexture: Texture) -> None: ...

  @staticmethod
  def setLastMouseX(aLastMouseX: float) -> None: ...

  @staticmethod
  def setLastMouseY(aLastMouseY: float) -> None: ...

  @staticmethod
  def setLastOffX(aLastOffX: float) -> None: ...

  @staticmethod
  def setLastOffY(aLastOffY: float) -> None: ...

  @staticmethod
  def setLastPicked(aLastPicked: IsoObject) -> None: ...

  @staticmethod
  def setModal(aModal: ModalDialog) -> None: ...

  @staticmethod
  def setMoodleUI(index: float, aMoodleUI: MoodlesUI) -> None: ...

  @staticmethod
  def setMouseArrow(aMouseArrow: Texture) -> None: ...

  @staticmethod
  def setMouseAttack(aMouseAttack: Texture) -> None: ...

  @staticmethod
  def setMouseExamine(aMouseExamine: Texture) -> None: ...

  @staticmethod
  def setMouseGrab(aMouseGrab: Texture) -> None: ...

  @staticmethod
  def setPicked(aPicked: IsoObjectPicker.ClickObject) -> None: ...

  @staticmethod
  def setPickedTile(aPickedTile: Vector2) -> None: ...

  @staticmethod
  def setPickedTileLocal(aPickedTileLocal: Vector2) -> None: ...

  @staticmethod
  def setPlayerInventory(playerIndex: int, inventory: UIElement, loot: UIElement) -> None: ...

  @staticmethod
  def setPlayerInventoryTooltip(playerIndex: int, inventory: UIElement, loot: UIElement) -> None: ...

  @staticmethod
  def setProgressBar(index: float, aProgressBar: ActionProgressBar) -> None: ...

  @staticmethod
  def setRightDownObject(aRightDownObject: IsoObject) -> None: ...

  @staticmethod
  def setServerToolbox(aServerToolbox: UIServerToolbox) -> None: ...

  @staticmethod
  def setShowLuaDebuggerOnError(show: bool) -> None: ...

  @staticmethod
  def setShowPausedMessage(showPausedMessage: bool) -> None: ...

  @staticmethod
  def setSpeedControls(aSpeedControls: SpeedControls) -> None: ...

  @staticmethod
  def setToolTip(aToolTip: ObjectTooltip) -> None: ...

  @staticmethod
  def setUI(aUI: ArrayList[UIElement]) -> None: ...

  @staticmethod
  def setVisibleAllUI(visible: bool) -> None: ...

  @staticmethod
  def setbFadeBeforeUI(abFadeBeforeUI: bool) -> None: ...

  @staticmethod
  def update() -> None: ...

  @staticmethod
  def updateBeforeFadeOut() -> None: ...

  def __init__(self): ...

  class FadeInfo:

    def FadeIn(self, arg0: int) -> None: ...

    def FadeOut(self, arg0: int) -> None: ...

    def getFadeAlpha(self) -> float: ...

    def getFadeTime(self) -> int: ...

    def getFadeTimeMax(self) -> int: ...

    def isFadeBeforeUI(self) -> bool: ...

    def isFadingOut(self) -> bool: ...

    def render(self) -> None: ...

    def setFadeAlpha(self, arg0: float) -> None: ...

    def setFadeBeforeUI(self, arg0: bool) -> None: ...

    def setFadeTime(self, arg0: int) -> None: ...

    def setFadeTimeMax(self, arg0: int) -> None: ...

    def setFadingOut(self, arg0: bool) -> None: ...

    def update(self) -> None: ...

    def __init__(self, arg0: int):
      self.bfadebeforeui: bool
      self.fadealpha: float
      self.fadetime: int
      self.fadetimemax: int
      self.fadingout: bool
      self.playerindex: int

  class Sync: ...


class UINineGrid(UIElement):

  def Nest(self, el: UIElement, t: int, r: int, b: int, l: int) -> None: ...

  def getAlpha(self) -> float: ...

  def render(self) -> None: ...

  def setAlpha(self, alpha: float) -> None: ...

  def update(self) -> None: ...

  def __init__(self, x: int, y: int, width: int, height: int, TopWidth: int, LeftWidth: int, RightWidth: int, BottomWidth: int, TL_Tex: str, T_Tex: str, TR_Tex: str, L_Tex: str, C_Tex: str, R_Tex: str, BL_Tex: str, B_Tex: str, BR_Tex: str):
    self.clienth: int
    self.clientw: int
    self.colour: Color
    self.nesteditems: Stack[Rectangle]


class UIServerToolbox(NewWindow):

  instance: UIServerToolbox

  @overload
  def DoubleClick(self, name: str, x: int, y: int) -> None: ...

  @overload
  def DoubleClick(self, name: str, x: int, y: int) -> None: ...

  @overload
  def ModalClick(self, name: str, chosen: str) -> None: ...

  @overload
  def ModalClick(self, name: str, chosen: str) -> None: ...

  @overload
  def OnCoopServerMessage(self, tag: str, cookie: str, payload: str) -> None: ...

  @overload
  def OnCoopServerMessage(self, tag: str, cookie: str, payload: str) -> None: ...

  @overload
  def Selected(self, name: str, Selected: int, LastSelected: int) -> None: ...

  @overload
  def Selected(self, name: str, Selected: int, LastSelected: int) -> None: ...

  def render(self) -> None: ...

  def shutdown(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self, x: int, y: int):
    self.autoaccept: bool


class UITextBox2(UIElement):

  ConsoleHasFocus: bool

  def ClearHighlights(self) -> None: ...

  def SetText(self, text: str) -> None: ...

  def clearInput(self) -> None: ...

  def focus(self) -> None: ...

  def getCursorLine(self) -> int: ...

  def getCursorPos(self) -> int: ...

  def getForceUpperCase(self) -> bool: ...

  def getFrameAlpha(self) -> float: ...

  def getInset(self) -> int: ...

  def getInternalText(self) -> str: ...

  def getMaxLines(self) -> int: ...

  def getMaxTextLength(self) -> int: ...

  def getText(self) -> str: ...

  def ignoreFirstInput(self) -> None: ...

  def isEditable(self) -> bool: ...

  def isFocused(self) -> bool: ...

  def isMasked(self) -> bool: ...

  def isMultipleLine(self) -> bool: ...

  def isOnlyNumbers(self) -> bool: ...

  def isSelectable(self) -> bool: ...

  def onCommandEntered(self) -> None: ...

  def onMouseDown(self, x: float, y: float) -> Boolean: ...

  def onMouseMove(self, dx: float, dy: float) -> Boolean: ...

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def onMouseUp(self, x: float, y: float) -> Boolean: ...

  def onMouseUpOutside(self, x: float, y: float) -> None: ...

  def onOtherKey(self, key: int) -> None: ...

  def onPressDown(self) -> None: ...

  def onPressUp(self) -> None: ...

  def onTextChange(self) -> None: ...

  def onresize(self) -> None: ...

  def render(self) -> None: ...

  def resetBlink(self) -> None: ...

  def selectAll(self) -> None: ...

  def setClearButton(self, hasButton: bool) -> None: ...

  def setCursorLine(self, line: int) -> None: ...

  def setCursorPos(self, charIndex: int) -> None: ...

  def setEditable(self, b: bool) -> None: ...

  def setForceUpperCase(self, forceUpperCase: bool) -> None: ...

  def setFrameAlpha(self, alpha: float) -> None: ...

  def setHasFrame(self, hasFrame: bool) -> None: ...

  def setMasked(self, b: bool) -> None: ...

  def setMaxLines(self, maxLines: int) -> None: ...

  def setMaxTextLength(self, maxtextLength: int) -> None: ...

  def setMultipleLine(self, multiple: bool) -> None: ...

  def setOnlyNumbers(self, onlyNumbers: bool) -> None: ...

  def setSelectable(self, b: bool) -> None: ...

  def setTextColor(self, newColor: ColorInfo) -> None: ...

  def toDisplayLine(self, textOffset: int) -> int: ...

  def unfocus(self) -> None: ...

  def update(self) -> None: ...

  def updateText(self) -> None: ...

  def __init__(self, font: UIFont, x: int, y: int, width: int, height: int, text: str, HasFrame: bool):
    self.badcolour: Color
    self.balwayspaginate: bool
    self.bmask: bool
    self.btextchanged: bool
    self.centred: bool
    self.cursorline: int
    self.doingtextentry: bool
    self.frame: UINineGrid
    self.goodcolour: Color
    self.ignorefirst: bool
    self.internaltext: str
    self.iseditable: bool
    self.isselectable: bool
    self.lines: Stack[str]
    self.maskchr: str
    self.multipleline: bool
    self.nuetralcolour: Color
    self.nuetralcolour2: Color
    self.standardframecolour: Color
    self.text: str
    self.textentrycursorcolour: Color
    self.textentrycursorcolour2: Color
    self.textentrycursorpos: int
    self.textentryframecolour: Color
    self.textentrymaxlength: int
    self.textoffsetoflinestart: TIntArrayList
    self.toselectionindex: int


class UITransition:

  def fraction(self) -> float: ...

  def getElapsed(self) -> float: ...

  def init(self, duration: float, fadeOut: bool) -> None: ...

  def reset(self) -> None: ...

  def setElapsed(self, elapsed: float) -> None: ...

  def setFadeIn(self, fadeIn: bool) -> None: ...

  def setIgnoreUpdateTime(self, ignore: bool) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def UpdateAll() -> None: ...

  def __init__(self): ...


class UI_BodyPart(UIElement):

  def onMouseMoveOutside(self, dx: float, dy: float) -> None: ...

  def render(self) -> None: ...

  def __init__(self, type: BodyPartType, x: int, y: int, part: str, character: IsoGameCharacter, RenderFlipped: bool):
    self.alpha: float
    self.bodyparttype: BodyPartType
    self.color: Color
    self.isflipped: bool
    self.maxoscilatorrate: float
    self.minoscilatorrate: float
    self.oscilator: float
    self.oscilatorrate: float
    self.oscilatorstep: float


class VehicleGauge(UIElement):

  def render(self) -> None: ...

  def setNeedleWidth(self, newSize: int) -> None: ...

  def setTexture(self, newText: Texture) -> None: ...

  def setValue(self, value: float) -> None: ...

  def __init__(self, texture: Texture, needleX: int, needleY: int, minAngle: float, maxAngle: float): ...

