from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Integer
from java.util import ArrayList, Comparator
from java.util.function import Function, ToDoubleFunction, ToIntFunction, ToLongFunction
from zombie.ai import State
from zombie.characters import IsoGameCharacter, MoveDeltaModifiers, IsoLivingCharacter, IsoZombie
from zombie.core.skinnedmodel.advancedanimation import AnimEvent
from zombie.inventory.types import HandWeapon
from zombie.iso import IsoDirections, IsoObject, IsoMovingObject, Vector3, LosUtil, IsoGridSquare, Vector2
from zombie.iso.objects import IsoWindow
from zombie.network.packets.hit import AttackVars, HitInfo
from zombie.popman import ObjectPool
from zombie.vehicles import PathFindState2

U = TypeVar('U', default=Any)
T = TypeVar('T', default=Any)

class AttackNetworkState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def isAttacking(self, owner: IsoGameCharacter) -> bool: ...

  @staticmethod
  def instance() -> AttackNetworkState: ...

  def __init__(self): ...


class AttackState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def isAttacking(self, owner: IsoGameCharacter) -> bool: ...

  @staticmethod
  def instance() -> AttackState: ...

  def __init__(self): ...


class BumpedState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> BumpedState: ...

  def __init__(self): ...


class BurntToDeath(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> BurntToDeath: ...

  def __init__(self): ...


class ClimbDownSheetRopeState(State):

  CLIMB_DOWN_SPEED: float

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def getClimbDownSheetRopeSpeed(self, owner: IsoGameCharacter) -> float: ...

  @staticmethod
  def instance() -> ClimbDownSheetRopeState: ...

  def __init__(self): ...


class ClimbOverFenceState(State):

  COLLIDE_WITH_WALL: int

  TRIP_METAL_BARS: int

  TRIP_TREE: int

  TRIP_WINDOW: int

  TRIP_ZOMBIE: int

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def getDeltaModifiers(self, owner: IsoGameCharacter, modifiers: MoveDeltaModifiers) -> None: ...

  def isIgnoreCollide(self, owner: IsoGameCharacter, fromX: int, fromY: int, fromZ: int, toX: int, toY: int, toZ: int) -> bool: ...

  def setParams(self, owner: IsoGameCharacter, dir: IsoDirections) -> None: ...

  @staticmethod
  def instance() -> ClimbOverFenceState: ...

  def __init__(self): ...


class ClimbOverWallState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def isIgnoreCollide(self, owner: IsoGameCharacter, fromX: int, fromY: int, fromZ: int, toX: int, toY: int, toZ: int) -> bool: ...

  def setParams(self, owner: IsoGameCharacter, dir: IsoDirections) -> None: ...

  @staticmethod
  def instance() -> ClimbOverWallState: ...

  def __init__(self): ...


class ClimbSheetRopeState(State):

  CLIMB_SPEED: float

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def getClimbSheetRopeSpeed(self, owner: IsoGameCharacter) -> float: ...

  @staticmethod
  def instance() -> ClimbSheetRopeState: ...

  def __init__(self): ...


class ClimbThroughWindowState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def getDeltaModifiers(self, owner: IsoGameCharacter, modifiers: MoveDeltaModifiers) -> None: ...

  def getWindow(self, owner: IsoGameCharacter) -> IsoObject: ...

  def isIgnoreCollide(self, owner: IsoGameCharacter, fromX: int, fromY: int, fromZ: int, toX: int, toY: int, toZ: int) -> bool: ...

  def isPastInnerEdgeOfSquare(self, owner: IsoGameCharacter, x: int, y: int, moveDir: IsoDirections) -> bool: ...

  def isPastOuterEdgeOfSquare(self, owner: IsoGameCharacter, x: int, y: int, moveDir: IsoDirections) -> bool: ...

  def isWindowClosing(self, owner: IsoGameCharacter) -> bool: ...

  def setParams(self, owner: IsoGameCharacter, obj: IsoObject) -> None: ...

  def slideX(self, owner: IsoGameCharacter, x: float) -> None: ...

  def slideY(self, owner: IsoGameCharacter, y: float) -> None: ...

  @staticmethod
  def instance() -> ClimbThroughWindowState: ...

  def __init__(self): ...


class CloseWindowState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def getWindow(self, owner: IsoGameCharacter) -> IsoWindow: ...

  def isDoingActionThatCanBeCancelled(self) -> bool: ...

  @staticmethod
  def instance() -> CloseWindowState: ...

  def __init__(self): ...


class CollideWithWallState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> CollideWithWallState: ...

  def __init__(self): ...


class CrawlingZombieTurnState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def calculateDir(owner: IsoGameCharacter, targetDir: IsoDirections) -> bool: ...

  @staticmethod
  def instance() -> CrawlingZombieTurnState: ...

  def __init__(self): ...


class FakeDeadAttackState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> FakeDeadAttackState: ...

  def __init__(self): ...


class FakeDeadZombieState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> FakeDeadZombieState: ...

  def __init__(self): ...


class FishingState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> FishingState: ...

  def __init__(self): ...


class FitnessState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> FitnessState: ...

  def __init__(self): ...


class ForecastBeatenPlayerState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ForecastBeatenPlayerState: ...

  def __init__(self): ...


class IdleState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  @staticmethod
  def instance() -> IdleState: ...

  def __init__(self): ...


class LungeNetworkState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def isMoving(self, owner: IsoGameCharacter) -> bool: ...

  @staticmethod
  def instance() -> LungeNetworkState: ...

  def __init__(self): ...


class LungeState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, chr: IsoGameCharacter) -> None: ...

  def isMoving(self, owner: IsoGameCharacter) -> bool: ...

  @staticmethod
  def instance() -> LungeState: ...

  def __init__(self): ...


class OpenWindowState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def isDoingActionThatCanBeCancelled(self) -> bool: ...

  def setParams(self, owner: IsoGameCharacter, window: IsoWindow) -> None: ...

  @staticmethod
  def instance() -> OpenWindowState: ...

  def __init__(self): ...


class PathFindState(State):

  @staticmethod
  def instance() -> PathFindState2: ...

  def __init__(self): ...


class PlayerActionsState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerActionsState: ...

  def __init__(self): ...


class PlayerAimState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerAimState: ...

  def __init__(self): ...


class PlayerEmoteState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def isDoingActionThatCanBeCancelled(self) -> bool: ...

  @staticmethod
  def instance() -> PlayerEmoteState: ...

  def __init__(self): ...


class PlayerExtState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerExtState: ...

  def __init__(self): ...


class PlayerFallDownState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerFallDownState: ...

  def __init__(self): ...


class PlayerFallingState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerFallingState: ...

  def __init__(self): ...


class PlayerGetUpState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerGetUpState: ...

  def __init__(self): ...


class PlayerHitReactionPVPState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerHitReactionPVPState: ...

  def __init__(self): ...


class PlayerHitReactionState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerHitReactionState: ...

  def __init__(self): ...


class PlayerKnockedDown(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerKnockedDown: ...

  def __init__(self): ...


class PlayerOnGroundState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerOnGroundState: ...

  def __init__(self): ...


class PlayerSitOnGroundState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerSitOnGroundState: ...

  def __init__(self): ...


class PlayerStrafeState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> PlayerStrafeState: ...

  def __init__(self): ...


class SmashWindowState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def isDoingActionThatCanBeCancelled(self) -> bool: ...

  @staticmethod
  def instance() -> SmashWindowState: ...

  def __init__(self): ...


class StaggerBackState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> StaggerBackState: ...

  def __init__(self): ...


class SwipeStatePlayer(State):

  def CalcAttackVars(self, owner: IsoLivingCharacter, vars: AttackVars) -> None: ...

  def CalcHitChance(self, owner: IsoGameCharacter, weapon: HandWeapon, hitInfo: HitInfo) -> int: ...

  def CalcHitList(self, owner: IsoGameCharacter, extraRange: bool, attackVars: AttackVars, hitList: ArrayList[HitInfo]) -> None: ...

  def ConnectSwing(self, owner: IsoGameCharacter, weapon: HandWeapon) -> None: ...

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def calcValidTargets(self, owner: IsoLivingCharacter, weapon: HandWeapon, extraRange: bool, targetsProne: ArrayList[HitInfo], targetsStanding: ArrayList[HitInfo]) -> None: ...

  def changeWeapon(self, weapon: HandWeapon, owner: IsoGameCharacter) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def isProneTargetBetter(self, owner: IsoGameCharacter, bestStanding: HitInfo, bestProne: HitInfo) -> bool: ...

  @staticmethod
  def WeaponLowerCondition(weapon: HandWeapon, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def checkPVP(owner: IsoGameCharacter, obj: IsoMovingObject) -> bool: ...

  @staticmethod
  def getBoneWorldPos(target: IsoMovingObject, boneName: str, bonePos: Vector3) -> Vector3: ...

  @staticmethod
  def instance() -> SwipeStatePlayer: ...

  @staticmethod
  def isProne(obj: IsoMovingObject) -> bool: ...

  @staticmethod
  def isStanding(obj: IsoMovingObject) -> bool: ...

  @staticmethod
  def splash(obj: IsoMovingObject, weapon: HandWeapon, owner: IsoGameCharacter) -> None: ...

  def __init__(self):
    self.hitinfopool: ObjectPool[HitInfo]

  class WindowVisitor:

    @overload
    def getResult(self) -> LosUtil.TestResults: ...

    @overload
    def getResult(self) -> LosUtil.TestResults: ...

    @overload
    def visit(self, arg0: IsoGridSquare, arg1: IsoGridSquare) -> bool: ...

    @overload
    def visit(self, arg0: IsoGridSquare, arg1: IsoGridSquare) -> bool: ...

  class CustomComparator:

    @overload
    def compare(self, arg0: object, arg1: object) -> int: ...

    @overload
    def compare(self, arg0: object, arg1: object) -> int: ...

    @overload
    def compare(self, o1: HitInfo, o2: HitInfo) -> int: ...

    def equals(self, arg0: object) -> bool: ...

    def reversed(self) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Comparator[T]) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Function[T, U]) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

    def thenComparingDouble(self, arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

    def thenComparingInt(self, arg0: ToIntFunction[T]) -> Comparator[T]: ...

    def thenComparingLong(self, arg0: ToLongFunction[T]) -> Comparator[T]: ...

    @staticmethod
    @overload
    def comparing(arg0: Function[T, U]) -> Comparator[T]: ...

    @staticmethod
    @overload
    def comparing(arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

    @staticmethod
    def comparingDouble(arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def comparingInt(arg0: ToIntFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def comparingLong(arg0: ToLongFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def naturalOrder() -> Comparator[T]: ...

    @staticmethod
    def nullsFirst(arg0: Comparator[T]) -> Comparator[T]: ...

    @staticmethod
    def nullsLast(arg0: Comparator[T]) -> Comparator[T]: ...

    @staticmethod
    def reverseOrder() -> Comparator[T]: ...

    def __init__(self): ...

  class LOSVisitor:

    def getResult(self) -> LosUtil.TestResults: ...

    def visit(self, arg0: IsoGridSquare, arg1: IsoGridSquare) -> bool: ...


class ThumpState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def getFastForwardDamageMultiplier() -> int: ...

  @staticmethod
  def instance() -> ThumpState: ...

  def __init__(self): ...


class WalkTowardNetworkState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> WalkTowardNetworkState: ...

  def __init__(self): ...


class WalkTowardState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def calculateTargetLocation(self, zomb: IsoZombie, location: Vector2) -> bool: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def isMoving(self, owner: IsoGameCharacter) -> bool: ...

  @staticmethod
  def instance() -> WalkTowardState: ...

  def __init__(self): ...


class ZombieEatBodyState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieEatBodyState: ...

  def __init__(self): ...


class ZombieFaceTargetState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieFaceTargetState: ...

  def __init__(self): ...


class ZombieFallDownState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieFallDownState: ...

  def __init__(self): ...


class ZombieFallingState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieFallingState: ...

  def __init__(self): ...


class ZombieGetDownState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def isNearStartXY(self, owner: IsoGameCharacter) -> bool: ...

  def setParams(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieGetDownState: ...

  def __init__(self): ...


class ZombieGetUpFromCrawlState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieGetUpFromCrawlState: ...

  def __init__(self): ...


class ZombieGetUpState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieGetUpState: ...

  def __init__(self): ...


class ZombieHitReactionState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieHitReactionState: ...

  def __init__(self): ...


class ZombieIdleState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieIdleState: ...

  def __init__(self): ...


class ZombieOnGroundState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieOnGroundState: ...

  @staticmethod
  def isCharacterStandingOnOther(chrStanding: IsoGameCharacter, chrProne: IsoGameCharacter) -> bool: ...

  def __init__(self): ...


class ZombieReanimateState(State):

  def animEvent(self, owner: IsoGameCharacter, event: AnimEvent) -> None: ...

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieReanimateState: ...

  def __init__(self): ...


class ZombieSittingState(State):

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  @staticmethod
  def instance() -> ZombieSittingState: ...

  def __init__(self): ...


class ZombieTurnAlerted(State):

  PARAM_TARGET_ANGLE: Integer

  def enter(self, owner: IsoGameCharacter) -> None: ...

  def execute(self, owner: IsoGameCharacter) -> None: ...

  def exit(self, owner: IsoGameCharacter) -> None: ...

  def setParams(self, owner: IsoGameCharacter, targetAngle: float) -> None: ...

  @staticmethod
  def instance() -> ZombieTurnAlerted: ...

  def __init__(self): ...

