from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import ArrayList
from zombie.iso import IsoGridSquare, IsoObject
from zombie.iso.sprite import IsoSprite, IsoSpriteInstance

class ErosionObj:

  def createObject(self, _sq: IsoGridSquare, _stage: int, _bTree: bool, _season: int) -> IsoObject: ...

  def getObject(self, _sq: IsoGridSquare, _bRemove: bool) -> IsoObject: ...

  def placeObject(self, _sq: IsoGridSquare, _stage: int, _bTree: bool, _season: int, _bloom: bool) -> bool: ...

  def removeObject(self, _sq: IsoGridSquare) -> IsoObject: ...

  def setStage(self, _sq: IsoGridSquare, _stage: int, _season: int, _bloom: bool) -> bool: ...

  def setStageObject(self, _stage: int, _object: IsoObject, _season: int, _bloom: bool) -> bool: ...

  def __init__(self, _sprites: ErosionObjSprites, _cycleTime: int, _bloomstart: float, _bloomend: float, _noSeasonBase: bool):
    self.bloomend: float
    self.bloomstart: float
    self.cycletime: int
    self.haschildsprite: bool
    self.hasflower: bool
    self.hassnow: bool
    self.name: str
    self.noseasonbase: bool
    self.stages: int


class ErosionObjOverlay:

  def removeOverlay(self, _obj: IsoObject, _id: int) -> bool: ...

  def setOverlay(self, _obj: IsoObject, _curID: int, _stage: int, _season: int, _alpha: float) -> int: ...

  def __init__(self, _sprites: ErosionObjOverlaySprites, _cycleTime: int, _applyAlpha: bool):
    self.applyalpha: bool
    self.cycletime: int
    self.name: str
    self.stages: int


class ErosionObjOverlaySprites:

  def getSprite(self, _stage: int, _season: int) -> IsoSprite: ...

  def getSpriteInstance(self, _stage: int, _season: int) -> IsoSpriteInstance: ...

  def setSprite(self, _stage: int, _sprite: str, _season: int) -> None: ...

  def __init__(self, _stages: int, _name: str):
    self.name: str
    self.stages: int

  class Stage: ...

  class Sprite:

    def getInstance(self) -> IsoSpriteInstance: ...

    def getSprite(self) -> IsoSprite: ...

    def __init__(self, arg0: str): ...


class ErosionObjSprites:

  NUM_SECTIONS: int

  SECTION_BASE: int

  SECTION_CHILD: int

  SECTION_FLOWER: int

  SECTION_SNOW: int

  def getBase(self, _stage: int, _season: int) -> str: ...

  def getChildSprite(self, _stage: int, _season: int) -> str: ...

  def getFlower(self, _stage: int) -> str: ...

  @overload
  def setBase(self, _stage: int, _sprite: str, _season: int) -> None: ...

  @overload
  def setBase(self, _stage: int, _sprites: ArrayList[str], _season: int) -> None: ...

  @overload
  def setChildSprite(self, _stage: int, _sprite: str, _season: int) -> None: ...

  @overload
  def setChildSprite(self, _stage: int, _sprites: ArrayList[str], _season: int) -> None: ...

  @overload
  def setFlower(self, _stage: int, _sprite: str) -> None: ...

  @overload
  def setFlower(self, _stage: int, _sprites: ArrayList[str]) -> None: ...

  def __init__(self, _stages: int, _name: str, _hasSnow: bool, _hasFlower: bool, _hasChildsprite: bool):
    self.cycletime: int
    self.haschildsprite: bool
    self.hasflower: bool
    self.hassnow: bool
    self.name: str
    self.noseasonbase: bool
    self.stages: int

  class Stage: ...

  class Section: ...

  class Sprites:

    def getNext(self) -> str: ...

    @overload
    def __init__(self, arg0: str):
      self.sprites: ArrayList[str]

    @overload
    def __init__(self, arg0: ArrayList[str]): ...

