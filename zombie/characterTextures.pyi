from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.util import ArrayList
from zombie.characters import IsoGameCharacter
from zombie.core.skinnedmodel.model import CharacterMask
from zombie.core.skinnedmodel.visual import HumanVisual, ItemVisual
from zombie.core.textures import SmartTexture
from zombie.inventory.types import Clothing

class BloodBodyPartType(Enum):

  Back: BloodBodyPartType

  Foot_L: BloodBodyPartType

  Foot_R: BloodBodyPartType

  ForeArm_L: BloodBodyPartType

  ForeArm_R: BloodBodyPartType

  Groin: BloodBodyPartType

  Hand_L: BloodBodyPartType

  Hand_R: BloodBodyPartType

  Head: BloodBodyPartType

  LowerLeg_L: BloodBodyPartType

  LowerLeg_R: BloodBodyPartType

  MAX: BloodBodyPartType

  Neck: BloodBodyPartType

  Torso_Lower: BloodBodyPartType

  Torso_Upper: BloodBodyPartType

  UpperArm_L: BloodBodyPartType

  UpperArm_R: BloodBodyPartType

  UpperLeg_L: BloodBodyPartType

  UpperLeg_R: BloodBodyPartType

  def getCharacterMaskParts(self) -> list[CharacterMask.Part]: ...

  def getDisplayName(self) -> str: ...

  def index(self) -> int: ...

  @staticmethod
  def FromIndex(index: int) -> BloodBodyPartType: ...

  @staticmethod
  def FromString(str: str) -> BloodBodyPartType: ...

  @staticmethod
  def ToIndex(BPT: BloodBodyPartType) -> int: ...

  @staticmethod
  def valueOf(arg0: str) -> BloodBodyPartType: ...

  @staticmethod
  def values() -> list[BloodBodyPartType]: ...


class BloodClothingType(Enum):

  Apron: BloodClothingType

  Bag: BloodClothingType

  FullHelmet: BloodClothingType

  Groin: BloodClothingType

  Hands: BloodClothingType

  Head: BloodClothingType

  Jacket: BloodClothingType

  Jumper: BloodClothingType

  JumperNoSleeves: BloodClothingType

  LongJacket: BloodClothingType

  LowerArms: BloodClothingType

  LowerBody: BloodClothingType

  LowerLegs: BloodClothingType

  Neck: BloodClothingType

  Shirt: BloodClothingType

  ShirtLongSleeves: BloodClothingType

  ShirtNoSleeves: BloodClothingType

  Shoes: BloodClothingType

  ShortsShort: BloodClothingType

  Trousers: BloodClothingType

  UpperArms: BloodClothingType

  UpperBody: BloodClothingType

  UpperLegs: BloodClothingType

  @staticmethod
  def addBasicPatch(part: BloodBodyPartType, humanVisual: HumanVisual, itemVisuals: ArrayList[ItemVisual]) -> None: ...

  @staticmethod
  @overload
  def addBlood(count: int, humanVisual: HumanVisual, itemVisuals: ArrayList[ItemVisual], allLayers: bool) -> None: ...

  @staticmethod
  @overload
  def addBlood(part: BloodBodyPartType, humanVisual: HumanVisual, itemVisuals: ArrayList[ItemVisual], allLayers: bool) -> None: ...

  @staticmethod
  @overload
  def addBlood(part: BloodBodyPartType, intensity: float, humanVisual: HumanVisual, itemVisuals: ArrayList[ItemVisual], allLayers: bool) -> None: ...

  @staticmethod
  @overload
  def addDirt(part: BloodBodyPartType, humanVisual: HumanVisual, itemVisuals: ArrayList[ItemVisual], allLayers: bool) -> None: ...

  @staticmethod
  @overload
  def addDirt(part: BloodBodyPartType, intensity: float, humanVisual: HumanVisual, itemVisuals: ArrayList[ItemVisual], allLayers: bool) -> None: ...

  @staticmethod
  @overload
  def addHole(part: BloodBodyPartType, humanVisual: HumanVisual, itemVisuals: ArrayList[ItemVisual]) -> None: ...

  @staticmethod
  @overload
  def addHole(part: BloodBodyPartType, humanVisual: HumanVisual, itemVisuals: ArrayList[ItemVisual], allLayers: bool) -> bool: ...

  @staticmethod
  def calcTotalBloodLevel(clothing: Clothing) -> None: ...

  @staticmethod
  def calcTotalDirtLevel(clothing: Clothing) -> None: ...

  @staticmethod
  def fromString(str: str) -> BloodClothingType: ...

  @staticmethod
  def getCoveredPartCount(bloodClothingType: ArrayList[BloodClothingType]) -> int: ...

  @staticmethod
  @overload
  def getCoveredParts(bloodClothingType: ArrayList[BloodClothingType]) -> ArrayList[BloodBodyPartType]: ...

  @staticmethod
  @overload
  def getCoveredParts(bloodClothingType: ArrayList[BloodClothingType], result: ArrayList[BloodBodyPartType]) -> ArrayList[BloodBodyPartType]: ...

  @staticmethod
  def valueOf(arg0: str) -> BloodClothingType: ...

  @staticmethod
  def values() -> list[BloodClothingType]: ...


class CharacterSmartTexture(SmartTexture):

  BasicPatchesMaskFiles: list[str]

  BodyCategory: int

  ClothingBottomCategory: int

  ClothingItemCategory: int

  ClothingTopCategory: int

  DecalOverlayCategory: int

  DenimPatchesMaskFiles: list[str]

  DirtOverlayCategory: int

  LeatherPatchesMaskFiles: list[str]

  MaskFiles: list[str]

  def addBlood(self, bodyPart: BloodBodyPartType, intensity: float, chr: IsoGameCharacter) -> float: ...

  def addDirt(self, bodyPart: BloodBodyPartType, intensity: float, chr: IsoGameCharacter) -> float: ...

  def addShirtDecal(self, dec: str) -> None: ...

  @overload
  def removeBlood(self) -> None: ...

  @overload
  def removeBlood(self, bodyPart: BloodBodyPartType) -> None: ...

  def setBlood(self, bodyPart: BloodBodyPartType, intensity: float) -> None: ...

  def setDirt(self, bodyPart: BloodBodyPartType, intensity: float) -> None: ...

  def __init__(self): ...


class ItemSmartTexture(SmartTexture):

  DecalOverlayCategory: int

  @overload
  def addBlood(self, tex: str, bodyPart: BloodBodyPartType, intensity: float) -> float: ...

  @overload
  def addBlood(self, tex: str, mask: str, intensity: float, category: int) -> float: ...

  @overload
  def addDirt(self, tex: str, bodyPart: BloodBodyPartType, intensity: float) -> float: ...

  @overload
  def addDirt(self, tex: str, mask: str, intensity: float, category: int) -> float: ...

  def getTexName(self) -> str: ...

  @overload
  def removeBlood(self) -> None: ...

  @overload
  def removeBlood(self, bodyPart: BloodBodyPartType) -> None: ...

  @overload
  def removeDirt(self) -> None: ...

  @overload
  def removeDirt(self, bodyPart: BloodBodyPartType) -> None: ...

  def setBasicPatches(self, bodyPart: BloodBodyPartType) -> None: ...

  @overload
  def setBlood(self, tex: str, bodyPart: BloodBodyPartType, intensity: float) -> None: ...

  @overload
  def setBlood(self, tex: str, mask: str, intensity: float, category: int) -> None: ...

  def setDenimPatches(self, bodyPart: BloodBodyPartType) -> None: ...

  def setLeatherPatches(self, bodyPart: BloodBodyPartType) -> None: ...

  @overload
  def __init__(self, tex: str): ...
  @overload
  def __init__(self, tex: str, hue: float): ...

