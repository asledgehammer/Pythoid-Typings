from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from zombie.iso import BuildingDef
from zombie.randomizedWorld.randomizedBuilding import RandomizedBuildingBase

class RDSBandPractice(RandomizedDeadSurvivorBase):

  def isValid(self, arg0: BuildingDef, force: bool) -> bool: ...

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSBathroomZed(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSBedroomZed(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSBleach(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSCorpsePsycho(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSDeadDrunk(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSFootballNight(RandomizedDeadSurvivorBase):

  def isValid(self, arg0: BuildingDef, force: bool) -> bool: ...

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSGunmanInBathroom(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSGunslinger(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSHenDo(RandomizedDeadSurvivorBase):

  def isValid(self, arg0: BuildingDef, force: bool) -> bool: ...

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSHockeyPsycho(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSHouseParty(RandomizedDeadSurvivorBase):

  def isValid(self, arg0: BuildingDef, force: bool) -> bool: ...

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSPokerNight(RandomizedDeadSurvivorBase):

  def isValid(self, arg0: BuildingDef, force: bool) -> bool: ...

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSPoliceAtHouse(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSPrisonEscape(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSPrisonEscapeWithPolice(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSSkeletonPsycho(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSSpecificProfession(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSStagDo(RandomizedDeadSurvivorBase):

  def isValid(self, arg0: BuildingDef, force: bool) -> bool: ...

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSStudentNight(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSSuicidePact(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSTinFoilHat(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSZombieLockedBathroom(RandomizedDeadSurvivorBase):

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RDSZombiesEating(RandomizedDeadSurvivorBase):

  def isValid(self, arg0: BuildingDef, force: bool) -> bool: ...

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RandomizedDeadSurvivorBase(RandomizedBuildingBase):

  def isValid(self, arg0: BuildingDef, arg1: bool) -> bool: ...

  def randomizeDeadSurvivor(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...

