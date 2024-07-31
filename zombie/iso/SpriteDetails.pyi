from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum

class IsoFlagType(Enum):

  alwaysDraw: IsoFlagType

  attachedCeiling: IsoFlagType

  attachedE: IsoFlagType

  attachedFloor: IsoFlagType

  attachedN: IsoFlagType

  attachedNW: IsoFlagType

  attachedS: IsoFlagType

  attachedSE: IsoFlagType

  attachedSurface: IsoFlagType

  attachedW: IsoFlagType

  attachtostairs: IsoFlagType

  bed: IsoFlagType

  blocksight: IsoFlagType

  blueprint: IsoFlagType

  burning: IsoFlagType

  burntOut: IsoFlagType

  canBeCut: IsoFlagType

  canBeRemoved: IsoFlagType

  canPathN: IsoFlagType

  canPathW: IsoFlagType

  CantClimb: IsoFlagType

  climbSheetE: IsoFlagType

  climbSheetN: IsoFlagType

  climbSheetS: IsoFlagType

  climbSheetTopE: IsoFlagType

  climbSheetTopN: IsoFlagType

  climbSheetTopS: IsoFlagType

  climbSheetTopW: IsoFlagType

  climbSheetW: IsoFlagType

  collideN: IsoFlagType

  collideW: IsoFlagType

  container: IsoFlagType

  cutN: IsoFlagType

  cutW: IsoFlagType

  diamondFloor: IsoFlagType

  doorN: IsoFlagType

  doorW: IsoFlagType

  DoorWallN: IsoFlagType

  DoorWallW: IsoFlagType

  exterior: IsoFlagType

  floorE: IsoFlagType

  FloorHeightOneThird: IsoFlagType

  FloorHeightTwoThirds: IsoFlagType

  FloorOverlay: IsoFlagType

  floorS: IsoFlagType

  ForceAmbient: IsoFlagType

  forceRender: IsoFlagType

  halfheight: IsoFlagType

  HasRaindrop: IsoFlagType

  HasRainSplashes: IsoFlagType

  hidewalls: IsoFlagType

  HoppableN: IsoFlagType

  HoppableW: IsoFlagType

  invisible: IsoFlagType

  makeWindowInvincible: IsoFlagType

  MAX: IsoFlagType

  noStart: IsoFlagType

  NoWallLighting: IsoFlagType

  ontable: IsoFlagType

  open: IsoFlagType

  pushable: IsoFlagType

  sheetCurtains: IsoFlagType

  shelfE: IsoFlagType

  shelfS: IsoFlagType

  smoke: IsoFlagType

  solid: IsoFlagType

  solidfloor: IsoFlagType

  solidtrans: IsoFlagType

  SpearOnlyAttackThrough: IsoFlagType

  tableE: IsoFlagType

  tableN: IsoFlagType

  tableNE: IsoFlagType

  tableNW: IsoFlagType

  tableS: IsoFlagType

  tableSE: IsoFlagType

  tableSW: IsoFlagType

  tableW: IsoFlagType

  taintedWater: IsoFlagType

  TallHoppableN: IsoFlagType

  TallHoppableW: IsoFlagType

  trans: IsoFlagType

  transparentFloor: IsoFlagType

  transparentN: IsoFlagType

  transparentW: IsoFlagType

  unflamable: IsoFlagType

  vegitation: IsoFlagType

  WallN: IsoFlagType

  WallNTrans: IsoFlagType

  WallNW: IsoFlagType

  WallOverlay: IsoFlagType

  WallSE: IsoFlagType

  WallW: IsoFlagType

  WallWTrans: IsoFlagType

  water: IsoFlagType

  waterPiped: IsoFlagType

  windowN: IsoFlagType

  windowW: IsoFlagType

  def index(self) -> int: ...

  @staticmethod
  def FromString(str: str) -> IsoFlagType: ...

  @staticmethod
  def fromIndex(value: int) -> IsoFlagType: ...

  @staticmethod
  def valueOf(arg0: str) -> IsoFlagType: ...

  @staticmethod
  def values() -> list[IsoFlagType]: ...


class IsoObjectType(Enum):

  curtainE: IsoObjectType

  curtainN: IsoObjectType

  curtainS: IsoObjectType

  curtainW: IsoObjectType

  doorFrN: IsoObjectType

  doorFrW: IsoObjectType

  doorN: IsoObjectType

  doorW: IsoObjectType

  isMoveAbleObject: IsoObjectType

  jukebox: IsoObjectType

  lightswitch: IsoObjectType

  MAX: IsoObjectType

  normal: IsoObjectType

  radio: IsoObjectType

  stairsBN: IsoObjectType

  stairsBW: IsoObjectType

  stairsMN: IsoObjectType

  stairsMW: IsoObjectType

  stairsTN: IsoObjectType

  stairsTW: IsoObjectType

  tree: IsoObjectType

  UNUSED10: IsoObjectType

  UNUSED24: IsoObjectType

  UNUSED9: IsoObjectType

  wall: IsoObjectType

  WestRoofB: IsoObjectType

  WestRoofM: IsoObjectType

  WestRoofT: IsoObjectType

  windowFN: IsoObjectType

  windowFW: IsoObjectType

  def index(self) -> int: ...

  @staticmethod
  def FromString(str: str) -> IsoObjectType: ...

  @staticmethod
  def fromIndex(value: int) -> IsoObjectType: ...

  @staticmethod
  def valueOf(arg0: str) -> IsoObjectType: ...

  @staticmethod
  def values() -> list[IsoObjectType]: ...

