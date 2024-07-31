from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import ArrayList

class CustomPerk:

  def __init__(self, id: str):
    self.m_bpassive: bool
    self.m_id: str
    self.m_parent: str
    self.m_translation: str
    self.m_xp: list[int]


class CustomPerks:

  instance: CustomPerks

  def init(self) -> None: ...

  def initLua(self) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  def __init__(self): ...


class PerkFactory:

  PerkList: ArrayList[PerkFactory.Perk]

  @staticmethod
  @overload
  def AddPerk(perk: PerkFactory.Perk, translation: str, xp1: int, xp2: int, xp3: int, xp4: int, xp5: int, xp6: int, xp7: int, xp8: int, xp9: int, xp10: int) -> PerkFactory.Perk: ...

  @staticmethod
  @overload
  def AddPerk(perk: PerkFactory.Perk, translation: str, xp1: int, xp2: int, xp3: int, xp4: int, xp5: int, xp6: int, xp7: int, xp8: int, xp9: int, xp10: int, passiv: bool) -> PerkFactory.Perk: ...

  @staticmethod
  @overload
  def AddPerk(perk: PerkFactory.Perk, translation: str, parent: PerkFactory.Perk, xp1: int, xp2: int, xp3: int, xp4: int, xp5: int, xp6: int, xp7: int, xp8: int, xp9: int, xp10: int) -> PerkFactory.Perk: ...

  @staticmethod
  @overload
  def AddPerk(perk: PerkFactory.Perk, translation: str, parent: PerkFactory.Perk, xp1: int, xp2: int, xp3: int, xp4: int, xp5: int, xp6: int, xp7: int, xp8: int, xp9: int, xp10: int, passiv: bool) -> PerkFactory.Perk: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getPerk(perk: PerkFactory.Perk) -> PerkFactory.Perk: ...

  @staticmethod
  def getPerkFromName(name: str) -> PerkFactory.Perk: ...

  @staticmethod
  def getPerkName(type: PerkFactory.Perk) -> str: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def initTranslations() -> None: ...

  def __init__(self): ...

  class Perk:

    def getId(self) -> str: ...

    def getName(self) -> str: ...

    def getParent(self) -> PerkFactory.Perk: ...

    def getTotalXpForLevel(self, level: int) -> float: ...

    def getType(self) -> PerkFactory.Perk: ...

    def getXp1(self) -> int: ...

    def getXp10(self) -> int: ...

    def getXp2(self) -> int: ...

    def getXp3(self) -> int: ...

    def getXp4(self) -> int: ...

    def getXp5(self) -> int: ...

    def getXp6(self) -> int: ...

    def getXp7(self) -> int: ...

    def getXp8(self) -> int: ...

    def getXp9(self) -> int: ...

    def getXpForLevel(self, level: int) -> float: ...

    def index(self) -> int: ...

    def isCustom(self) -> bool: ...

    def isPassiv(self) -> bool: ...

    def setCustom(self) -> None: ...

    def toString(self) -> str: ...

    @overload
    def __init__(self, id: str):
      self.name: str

      self.parent: PerkFactory.Perk

      self.passiv: bool

      self.translation: str

      self.xp1: int

      self.xp10: int

      self.xp2: int

      self.xp3: int

      self.xp4: int

      self.xp5: int

      self.xp6: int

      self.xp7: int

      self.xp8: int

      self.xp9: int

    @overload
    def __init__(self, id: str, parent: PerkFactory.Perk): ...

  class Perks:

    Agility: PerkFactory.Perk

    Aiming: PerkFactory.Perk

    Axe: PerkFactory.Perk

    Blacksmith: PerkFactory.Perk

    Blunt: PerkFactory.Perk

    Combat: PerkFactory.Perk

    Cooking: PerkFactory.Perk

    Crafting: PerkFactory.Perk

    Doctor: PerkFactory.Perk

    Electricity: PerkFactory.Perk

    Farming: PerkFactory.Perk

    Firearm: PerkFactory.Perk

    Fishing: PerkFactory.Perk

    Fitness: PerkFactory.Perk

    Lightfoot: PerkFactory.Perk

    LongBlade: PerkFactory.Perk

    Maintenance: PerkFactory.Perk

    MAX: PerkFactory.Perk

    Mechanics: PerkFactory.Perk

    Melee: PerkFactory.Perk

    Melting: PerkFactory.Perk

    MetalWelding: PerkFactory.Perk

    Nimble: PerkFactory.Perk

    # None: PerkFactory.Perk

    Passiv: PerkFactory.Perk

    PlantScavenging: PerkFactory.Perk

    Reloading: PerkFactory.Perk

    SmallBlade: PerkFactory.Perk

    SmallBlunt: PerkFactory.Perk

    Sneak: PerkFactory.Perk

    Spear: PerkFactory.Perk

    Sprinting: PerkFactory.Perk

    Strength: PerkFactory.Perk

    Survivalist: PerkFactory.Perk

    Tailoring: PerkFactory.Perk

    Trapping: PerkFactory.Perk

    Woodwork: PerkFactory.Perk

    @staticmethod
    def FromString(id: str) -> PerkFactory.Perk: ...

    @staticmethod
    def fromIndex(value: int) -> PerkFactory.Perk: ...

    @staticmethod
    def getMaxIndex() -> int: ...

    def __init__(self): ...

