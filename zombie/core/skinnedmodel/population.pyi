from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Integer
from java.util import ArrayList, List
from zombie.asset import Asset, AssetType, AssetPath, AssetManager
from zombie.characters import IsoGameCharacter
from zombie.characters.WornItems import BodyLocationGroup
from zombie.core import ImmutableColor
from zombie.core.skinnedmodel import ModelManager
from zombie.core.skinnedmodel.model import CharacterMask, ModelInstance
from zombie.core.skinnedmodel.visual import ItemVisual, ItemVisuals

E = TypeVar('E', default=Any)

class BeardStyle:

  def getLevel(self) -> int: ...

  def getName(self) -> str: ...

  def getTrimChoices(self) -> ArrayList[str]: ...

  def isValid(self) -> bool: ...

  def __init__(self):
    self.growreference: bool
    self.level: int
    self.model: str
    self.name: str
    self.texture: str
    self.trimchoices: ArrayList[str]


class BeardStyles:

  instance: BeardStyles

  def FindStyle(self, name: str) -> BeardStyle: ...

  def getAllStyles(self) -> ArrayList[BeardStyle]: ...

  def getInstance(self) -> BeardStyles: ...

  def getRandomStyle(self, outfitName: str) -> str: ...

  @staticmethod
  def Parse(filename: str) -> BeardStyles: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def parse(filename: str) -> BeardStyles: ...

  def __init__(self):
    self.m_styles: ArrayList[BeardStyle]


class CarriedItem:

  def __init__(self):
    self.m_model: str
    self.m_texture: str
    self.m_twohanded: bool
    self.m_weapontype: str


class ClothingDecal:

  def isValid(self) -> bool: ...

  def __init__(self):
    self.height: int
    self.name: str
    self.texture: str
    self.width: int
    self.x: int
    self.y: int


class ClothingDecalGroup:

  def getDecals(self, decals: ArrayList[str]) -> None: ...

  def getRandomDecal(self) -> str: ...

  def __init__(self):
    self.m_decals: ArrayList[str]
    self.m_groups: ArrayList[str]
    self.m_name: str


class ClothingDecals:

  instance: ClothingDecals

  def FindGroup(self, name: str) -> ClothingDecalGroup: ...

  def getDecal(self, name: str) -> ClothingDecal: ...

  def getRandomDecal(self, groupName: str) -> str: ...

  @staticmethod
  def Parse(filename: str) -> ClothingDecals: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def parse(filename: str) -> ClothingDecals: ...

  def __init__(self):
    self.m_groups: ArrayList[ClothingDecalGroup]

  class CachedDecal: ...


class ClothingItem(Asset):

  ASSET_TYPE: AssetType

  s_masksFolderDefault: str

  def GetATexture(self) -> str: ...

  def getAllowRandomHue(self) -> bool: ...

  def getAllowRandomTint(self) -> bool: ...

  def getBaseTextures(self) -> ArrayList[str]: ...

  def getCombinedMask(self, in_out_mask: CharacterMask) -> None: ...

  def getDecalGroup(self) -> str: ...

  def getFemaleModel(self) -> str: ...

  def getMaleModel(self) -> str: ...

  def getModel(self, female: bool) -> str: ...

  def getTextureChoices(self) -> ArrayList[str]: ...

  def getType(self) -> AssetType: ...

  def hasModel(self) -> bool: ...

  def isHat(self) -> bool: ...

  def isMask(self) -> bool: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def tryGetCombinedMask(item: ClothingItem, in_out_mask: CharacterMask) -> None: ...

  @staticmethod
  @overload
  def tryGetCombinedMask(itemRef: ClothingItemReference, in_out_mask: CharacterMask) -> None: ...

  def __init__(self, path: AssetPath, assetManager: AssetManager):
    self.m_allowrandomhue: bool
    self.m_allowrandomtint: bool
    self.m_attachbone: str
    self.m_basetextures: ArrayList[str]
    self.m_decalgroup: str
    self.m_femalemodel: str
    self.m_guid: str
    self.m_hatcategory: str
    self.m_malemodel: str
    self.m_masks: ArrayList[Integer]
    self.m_masksfolder: str
    self.m_name: str
    self.m_shader: str
    self.m_static: bool
    self.m_underlaymasksfolder: str
    self.texturechoices: ArrayList[str]


class ClothingItemAssetManager(AssetManager):

  instance: ClothingItemAssetManager

  def onStateChanged(self, old_state: Asset.State, new_state: Asset.State, asset: Asset) -> None: ...

  def __init__(self): ...


class ClothingItemReference:

  @overload
  def clone(self) -> ClothingItemReference: ...

  @overload
  def clone(self) -> object: ...

  def getClothingItem(self) -> ClothingItem: ...

  def randomize(self) -> None: ...

  def setModID(self, modID: str) -> None: ...

  def __init__(self):
    self.brandomized: bool
    self.itemguid: str
    self.m_immutable: bool
    self.probability: float
    self.randomdata: ClothingItemReference.RandomData
    self.subitems: ArrayList[ClothingItemReference]

  class RandomData:

    def reset(self) -> None: ...

    def __init__(self):
      self.m_active: bool
      self.m_basetexture: str
      self.m_decal: str
      self.m_hue: float
      self.m_pickeditemref: ClothingItemReference
      self.m_texturechoice: str
      self.m_tint: ImmutableColor


class ClothingItemXML:

  def __init__(self):
    self.m_allowrandomhue: bool
    self.m_allowrandomtint: bool
    self.m_attachbone: str
    self.m_basetextures: ArrayList[str]
    self.m_decalgroup: str
    self.m_femalemodel: str
    self.m_guid: str
    self.m_hatcategory: str
    self.m_malemodel: str
    self.m_masks: ArrayList[Integer]
    self.m_masksfolder: str
    self.m_shader: str
    self.m_static: bool
    self.m_underlaymasksfolder: str
    self.texturechoices: ArrayList[str]


class DefaultClothing:

  instance: DefaultClothing

  def pickPantsHue(self) -> str: ...

  def pickPantsTexture(self) -> str: ...

  def pickPantsTint(self) -> str: ...

  def pickTShirtDecalTexture(self) -> str: ...

  def pickTShirtDecalTint(self) -> str: ...

  def pickTShirtTexture(self) -> str: ...

  def pickTShirtTint(self) -> str: ...

  def pickVestTexture(self) -> str: ...

  def pickVestTint(self) -> str: ...

  def __init__(self):
    self.m_dirty: bool
    self.pants: DefaultClothing.Clothing
    self.tshirt: DefaultClothing.Clothing
    self.tshirtdecal: DefaultClothing.Clothing
    self.vest: DefaultClothing.Clothing

  class Clothing: ...


class HairStyle:

  def getAlternate(self, category: str) -> str: ...

  def getLevel(self) -> int: ...

  def getName(self) -> str: ...

  def getTrimChoices(self) -> ArrayList[str]: ...

  def isAttachedHair(self) -> bool: ...

  def isGrowReference(self) -> bool: ...

  def isNoChoose(self) -> bool: ...

  def isValid(self) -> bool: ...

  def __init__(self):
    self.alternate: ArrayList[HairStyle.Alternate]
    self.attachedhair: bool
    self.growreference: bool
    self.level: int
    self.model: str
    self.name: str
    self.nochoose: bool
    self.texture: str
    self.trimchoices: ArrayList[str]

  class Alternate:

    def __init__(self):
      self.category: str
      self.style: str


class HairStyles:

  instance: HairStyles

  def FindFemaleStyle(self, name: str) -> HairStyle: ...

  def FindMaleStyle(self, name: str) -> HairStyle: ...

  def getAllFemaleStyles(self) -> ArrayList[HairStyle]: ...

  def getAllMaleStyles(self) -> ArrayList[HairStyle]: ...

  def getAlternateForHat(self, style: HairStyle, category: str) -> HairStyle: ...

  def getRandomFemaleStyle(self, outfitName: str) -> str: ...

  def getRandomMaleStyle(self, outfitName: str) -> str: ...

  @staticmethod
  def Parse(filename: str) -> HairStyles: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def parse(filename: str) -> HairStyles: ...

  def __init__(self):
    self.m_femalestyles: ArrayList[HairStyle]
    self.m_malestyles: ArrayList[HairStyle]


class IClothingItemListener:

  def clothingItemChanged(self, itemGuid: str) -> None: ...


class ItemManager:

  instance: ItemManager

  def GetRandomItem(self) -> CarriedItem: ...

  @staticmethod
  def Parse(filename: str) -> ItemManager: ...

  @staticmethod
  def Write(out: ItemManager, filename: str) -> None: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def parse(filename: str) -> ItemManager: ...

  @staticmethod
  def write(out: ItemManager, filename: str) -> None: ...

  def __init__(self):
    self.m_items: ArrayList[CarriedItem]


class Outfit:

  def AddItem(self, item: ClothingItemReference) -> None: ...

  def GetMask(self) -> CharacterMask: ...

  def Randomize(self) -> None: ...

  @overload
  def clone(self) -> Outfit: ...

  @overload
  def clone(self) -> object: ...

  def containsItemGuid(self, itemGuid: str) -> bool: ...

  def findHat(self) -> ClothingItemReference: ...

  def findItemByGUID(self, itemGuid: str) -> ClothingItemReference: ...

  def isEmpty(self) -> bool: ...

  def loadItems(self) -> None: ...

  def randomizeItem(self, itemGuid: str) -> None: ...

  def setModID(self, modID: str) -> None: ...

  def __init__(self):
    self.m_allowpantshue: bool
    self.m_allowpantstint: bool
    self.m_allowtoptint: bool
    self.m_allowtshirtdecal: bool
    self.m_immutable: bool
    self.m_items: ArrayList[ClothingItemReference]
    self.m_modid: str
    self.m_name: str
    self.m_pants: bool
    self.m_pantstextures: ArrayList[str]
    self.m_top: bool
    self.m_toptextures: ArrayList[str]
    self.randomdata: Outfit.RandomData

  class RandomData:

    def __init__(self):
      self.m_beardname: str
      self.m_femalehairname: str
      self.m_haircolor: ImmutableColor
      self.m_hastop: bool
      self.m_hastshirt: bool
      self.m_hastshirtdecal: bool
      self.m_malehairname: str
      self.m_pantshue: float
      self.m_pantstexture: str
      self.m_pantstint: ImmutableColor
      self.m_toptexture: str
      self.m_toptint: ImmutableColor


class OutfitManager:

  instance: OutfitManager

  def FindFemaleOutfit(self, outfitName: str) -> Outfit: ...

  def FindMaleOutfit(self, outfitName: str) -> Outfit: ...

  def GetRandomNonProfessionalOutfit(self, female: bool) -> Outfit: ...

  def GetRandomOutfit(self, female: bool) -> Outfit: ...

  def GetSpecificOutfit(self, female: bool, outfitName: str) -> Outfit: ...

  def addClothingItemListener(self, listener: IClothingItemListener) -> None: ...

  def debugOutfits(self) -> None: ...

  def getClothingItem(self, itemGUID: str) -> ClothingItem: ...

  def isLoadingClothingItems(self) -> bool: ...

  def loadAllClothingItems(self) -> None: ...

  def onClothingItemStateChanged(self, clothingItem: ClothingItem) -> None: ...

  def removeClothingItemListener(self, listener: IClothingItemListener) -> None: ...

  @staticmethod
  def Reload() -> None: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def init() -> None: ...

  def __init__(self):
    self.m_femaleoutfits: ArrayList[Outfit]
    self.m_maleoutfits: ArrayList[Outfit]

  class ClothingItemEntry: ...


class OutfitRNG:

  @staticmethod
  @overload
  def Next(max: int) -> int: ...

  @staticmethod
  @overload
  def Next(min: float, max: float) -> float: ...

  @staticmethod
  @overload
  def Next(min: int, max: int) -> int: ...

  @staticmethod
  def NextBool(invProbability: int) -> bool: ...

  @staticmethod
  def getSeed() -> int: ...

  @staticmethod
  def pickRandom(collection: List[E]) -> object: ...

  @staticmethod
  def randomImmutableColor() -> ImmutableColor: ...

  @staticmethod
  def setSeed(seed: int) -> None: ...

  def __init__(self): ...


class PopTemplateManager:

  instance: PopTemplateManager

  SKELETON_BURNED_SKIN_INDEX: int

  SKELETON_MUSCLE_SKIN_INDEX: int

  SKELETON_NORMAL_SKIN_INDEX: int

  def addClothingItem(self, chr: IsoGameCharacter, modelSlot: ModelManager.ModelSlot, itemVisual: ItemVisual, clothingItem: ClothingItem) -> ModelInstance: ...

  def init(self) -> None: ...

  def isItemModelHidden(self, bodyLocationGroup: BodyLocationGroup, visuals: ItemVisuals, visual: ItemVisual) -> bool: ...

  def populateCharacterModelSlot(self, chr: IsoGameCharacter, modelSlot: ModelManager.ModelSlot) -> None: ...

  def __init__(self):
    self.m_femaleskins: ArrayList[str]
    self.m_femaleskins_zombie1: ArrayList[str]
    self.m_femaleskins_zombie2: ArrayList[str]
    self.m_femaleskins_zombie3: ArrayList[str]
    self.m_maleskins: ArrayList[str]
    self.m_maleskins_zombie1: ArrayList[str]
    self.m_maleskins_zombie2: ArrayList[str]
    self.m_maleskins_zombie3: ArrayList[str]
    self.m_skeletonfemaleskins_zombie: ArrayList[str]
    self.m_skeletonmaleskins_zombie: ArrayList[str]

