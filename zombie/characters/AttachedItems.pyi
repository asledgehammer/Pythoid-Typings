from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import ArrayList
from java.util.function import Consumer
from zombie.characterTextures import BloodBodyPartType
from zombie.characters import IsoZombie
from zombie.inventory import InventoryItem

class AttachedItem:

  def getItem(self) -> InventoryItem: ...

  def getLocation(self) -> str: ...

  def __init__(self, location: str, item: InventoryItem): ...


class AttachedItems:

  def clear(self) -> None: ...

  def contains(self, item: InventoryItem) -> bool: ...

  def copyFrom(self, other: AttachedItems) -> None: ...

  def forEach(self, c: Consumer[AttachedItem]) -> None: ...

  def get(self, index: int) -> AttachedItem: ...

  def getGroup(self) -> AttachedLocationGroup: ...

  def getItem(self, location: str) -> InventoryItem: ...

  def getItemByIndex(self, index: int) -> InventoryItem: ...

  def getLocation(self, item: InventoryItem) -> str: ...

  def isEmpty(self) -> bool: ...

  def remove(self, item: InventoryItem) -> None: ...

  def setItem(self, location: str, item: InventoryItem) -> None: ...

  def size(self) -> int: ...

  @overload
  def __init__(self, other: AttachedItems): ...
  @overload
  def __init__(self, group: AttachedLocationGroup): ...


class AttachedLocation:

  def getAttachmentName(self) -> str: ...

  def getId(self) -> str: ...

  def setAttachmentName(self, attachmentName: str) -> None: ...

  def __init__(self, group: AttachedLocationGroup, id: str): ...


class AttachedLocationGroup:

  def checkValid(self, locationId: str) -> None: ...

  def getLocation(self, locationId: str) -> AttachedLocation: ...

  def getLocationByIndex(self, index: int) -> AttachedLocation: ...

  def getOrCreateLocation(self, locationId: str) -> AttachedLocation: ...

  def indexOf(self, locationId: str) -> int: ...

  def size(self) -> int: ...

  def __init__(self, id: str): ...


class AttachedLocations:

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getGroup(id: str) -> AttachedLocationGroup: ...

  def __init__(self): ...


class AttachedModelName:

  def addChild(self, child: AttachedModelName) -> None: ...

  def getChildByIndex(self, index: int) -> AttachedModelName: ...

  def getChildCount(self) -> int: ...

  @overload
  def __init__(self, other: AttachedModelName):
    self.attachmentnameparent: str

    self.attachmentnameself: str

    self.bloodlevel: float

    self.children: ArrayList[AttachedModelName]

    self.modelname: str

  @overload
  def __init__(self, attachmentName: str, modelName: str, bloodLevel: float): ...
  @overload
  def __init__(self, attachmentNameSelf: str, attachmentNameParent: str, modelName: str, bloodLevel: float): ...


class AttachedModelNames:

  def clear(self) -> None: ...

  def copyFrom(self, other: AttachedModelNames) -> None: ...

  def get(self, index: int) -> AttachedModelName: ...

  def initFrom(self, attachedItems: AttachedItems) -> None: ...

  def size(self) -> int: ...

  def __init__(self): ...


class AttachedModels(ArrayList):

  def __init__(self): ...


class AttachedWeaponCustomOutfit:

  def __init__(self):
    self.chance: int
    self.maxitem: int
    self.outfit: str
    self.weapons: ArrayList[AttachedWeaponDefinition]


class AttachedWeaponDefinition:

  def __init__(self):
    self.addholes: bool
    self.bloodlocations: ArrayList[BloodBodyPartType]
    self.chance: int
    self.daysurvived: int
    self.ensureitem: str
    self.id: str
    self.outfit: ArrayList[str]
    self.weaponlocation: ArrayList[str]
    self.weapons: ArrayList[str]


class AttachedWeaponDefinitions:

  instance: AttachedWeaponDefinitions

  def addRandomAttachedWeapon(self, zed: IsoZombie) -> None: ...

  def checkDirty(self) -> None: ...

  def outfitHasItem(self, zombie: IsoZombie, ensureItem: str) -> bool: ...

  def __init__(self):
    self.m_chanceofattachedweapon: int
    self.m_definitions: ArrayList[AttachedWeaponDefinition]
    self.m_dirty: bool
    self.m_outfitdefinitions: ArrayList[AttachedWeaponCustomOutfit]

  class L_addRandomAttachedWeapon: ...

