from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from fmod.fmod import FMODSoundEmitter
from java.lang import Enum
from zombie.audio import FMODGlobalParameter, FMODLocalParameter
from zombie.characters import IsoGameCharacter, IsoPlayer, IsoZombie
from zombie.iso import IsoObject
from zombie.vehicles import BaseVehicle

class ParameterCameraZoom(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterCharacterInside(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, character: IsoGameCharacter): ...


class ParameterCharacterMovementSpeed(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def setMovementType(self, movementType: ParameterCharacterMovementSpeed.MovementType) -> None: ...

  def __init__(self, character: IsoGameCharacter): ...

  class MovementType(Enum):

    Run: ParameterCharacterMovementSpeed.MovementType

    SneakRun: ParameterCharacterMovementSpeed.MovementType

    SneakWalk: ParameterCharacterMovementSpeed.MovementType

    Sprint: ParameterCharacterMovementSpeed.MovementType

    Strafe: ParameterCharacterMovementSpeed.MovementType

    Walk: ParameterCharacterMovementSpeed.MovementType

    @staticmethod
    def valueOf(arg0: str) -> ParameterCharacterMovementSpeed.MovementType: ...

    @staticmethod
    def values() -> list[ParameterCharacterMovementSpeed.MovementType]: ...


class ParameterClosestWallDistance(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterCurrentZone(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, object: IsoObject): ...

  class Zone(Enum):

    DeepForest: ParameterCurrentZone.Zone

    Farm: ParameterCurrentZone.Zone

    Forest: ParameterCurrentZone.Zone

    Nav: ParameterCurrentZone.Zone

    # None: ParameterCurrentZone.Zone

    Town: ParameterCurrentZone.Zone

    TrailerPark: ParameterCurrentZone.Zone

    Vegetation: ParameterCurrentZone.Zone

    @staticmethod
    def valueOf(arg0: str) -> ParameterCurrentZone.Zone: ...

    @staticmethod
    def values() -> list[ParameterCurrentZone.Zone]: ...


class ParameterEquippedBaggageContainer(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  @overload
  def setContainerType(self, containerType: str) -> None: ...

  @overload
  def setContainerType(self, containerType: ParameterEquippedBaggageContainer.ContainerType) -> None: ...

  def __init__(self, character: IsoGameCharacter): ...

  class ContainerType(Enum):

    DuffleBag: ParameterEquippedBaggageContainer.ContainerType

    GarbageBag: ParameterEquippedBaggageContainer.ContainerType

    HikingBag: ParameterEquippedBaggageContainer.ContainerType

    # None: ParameterEquippedBaggageContainer.ContainerType

    PlasticBag: ParameterEquippedBaggageContainer.ContainerType

    SchoolBag: ParameterEquippedBaggageContainer.ContainerType

    ToteBag: ParameterEquippedBaggageContainer.ContainerType

    @staticmethod
    def valueOf(arg0: str) -> ParameterEquippedBaggageContainer.ContainerType: ...

    @staticmethod
    def values() -> list[ParameterEquippedBaggageContainer.ContainerType]: ...


class ParameterFireSize(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def setSize(self, size: int) -> None: ...

  def __init__(self): ...


class ParameterFogIntensity(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterFootstepMaterial(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, character: IsoGameCharacter): ...

  class FootstepMaterial(Enum):

    BrokenGlass: ParameterFootstepMaterial.FootstepMaterial

    Carpet: ParameterFootstepMaterial.FootstepMaterial

    Ceramic: ParameterFootstepMaterial.FootstepMaterial

    Concrete: ParameterFootstepMaterial.FootstepMaterial

    Dirt: ParameterFootstepMaterial.FootstepMaterial

    Grass: ParameterFootstepMaterial.FootstepMaterial

    Gravel: ParameterFootstepMaterial.FootstepMaterial

    Metal: ParameterFootstepMaterial.FootstepMaterial

    Puddle: ParameterFootstepMaterial.FootstepMaterial

    Sand: ParameterFootstepMaterial.FootstepMaterial

    Snow: ParameterFootstepMaterial.FootstepMaterial

    Upstairs: ParameterFootstepMaterial.FootstepMaterial

    Wood: ParameterFootstepMaterial.FootstepMaterial

    @staticmethod
    def valueOf(arg0: str) -> ParameterFootstepMaterial.FootstepMaterial: ...

    @staticmethod
    def values() -> list[ParameterFootstepMaterial.FootstepMaterial]: ...


class ParameterFootstepMaterial2(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, character: IsoGameCharacter): ...

  class FootstepMaterial2(Enum):

    BrokenGlass: ParameterFootstepMaterial2.FootstepMaterial2

    # None: ParameterFootstepMaterial2.FootstepMaterial2

    PuddleDeep: ParameterFootstepMaterial2.FootstepMaterial2

    PuddleShallow: ParameterFootstepMaterial2.FootstepMaterial2

    @staticmethod
    def valueOf(arg0: str) -> ParameterFootstepMaterial2.FootstepMaterial2: ...

    @staticmethod
    def values() -> list[ParameterFootstepMaterial2.FootstepMaterial2]: ...


class ParameterHardOfHearing(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterInside(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterLocalPlayer(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, player: IsoPlayer): ...


class ParameterMeleeHitSurface(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def setMaterial(self, material: ParameterMeleeHitSurface.Material) -> None: ...

  def __init__(self, character: IsoGameCharacter): ...

  class Material(Enum):

    Body: ParameterMeleeHitSurface.Material

    Default: ParameterMeleeHitSurface.Material

    Fabric: ParameterMeleeHitSurface.Material

    GarageDoor: ParameterMeleeHitSurface.Material

    Glass: ParameterMeleeHitSurface.Material

    Head: ParameterMeleeHitSurface.Material

    Metal: ParameterMeleeHitSurface.Material

    MetalDoor: ParameterMeleeHitSurface.Material

    MetalGate: ParameterMeleeHitSurface.Material

    Plastic: ParameterMeleeHitSurface.Material

    PrisonMetalDoor: ParameterMeleeHitSurface.Material

    SlidingGlassDoor: ParameterMeleeHitSurface.Material

    Stone: ParameterMeleeHitSurface.Material

    Tree: ParameterMeleeHitSurface.Material

    Wood: ParameterMeleeHitSurface.Material

    WoodDoor: ParameterMeleeHitSurface.Material

    WoodGate: ParameterMeleeHitSurface.Material

    @staticmethod
    def valueOf(arg0: str) -> ParameterMeleeHitSurface.Material: ...

    @staticmethod
    def values() -> list[ParameterMeleeHitSurface.Material]: ...


class ParameterMoodlePanic(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterMusicActionStyle(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...

  class State(Enum):

    Legacy: ParameterMusicActionStyle.State

    Official: ParameterMusicActionStyle.State

    @staticmethod
    def valueOf(arg0: str) -> ParameterMusicActionStyle.State: ...

    @staticmethod
    def values() -> list[ParameterMusicActionStyle.State]: ...


class ParameterMusicLibrary(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...

  class Library(Enum):

    EarlyAccess: ParameterMusicLibrary.Library

    Official: ParameterMusicLibrary.Library

    Random: ParameterMusicLibrary.Library

    @staticmethod
    def valueOf(arg0: str) -> ParameterMusicLibrary.Library: ...

    @staticmethod
    def values() -> list[ParameterMusicLibrary.Library]: ...


class ParameterMusicState(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def setState(self, state: ParameterMusicState.State) -> None: ...

  def __init__(self): ...

  class State(Enum):

    InGame: ParameterMusicState.State

    Loading: ParameterMusicState.State

    MainMenu: ParameterMusicState.State

    PauseMenu: ParameterMusicState.State

    Tutorial: ParameterMusicState.State

    @staticmethod
    def valueOf(arg0: str) -> ParameterMusicState.State: ...

    @staticmethod
    def values() -> list[ParameterMusicState.State]: ...


class ParameterMusicWakeState(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def setState(self, player: IsoPlayer, state: ParameterMusicWakeState.State) -> None: ...

  def __init__(self): ...

  class State(Enum):

    Awake: ParameterMusicWakeState.State

    Sleeping: ParameterMusicWakeState.State

    WakeNightmare: ParameterMusicWakeState.State

    WakeNormal: ParameterMusicWakeState.State

    WakeZombies: ParameterMusicWakeState.State

    @staticmethod
    def valueOf(arg0: str) -> ParameterMusicWakeState.State: ...

    @staticmethod
    def values() -> list[ParameterMusicWakeState.State]: ...


class ParameterMusicZombiesTargeting(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterMusicZombiesVisible(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterOcclusion(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def resetToDefault(self) -> None: ...

  def __init__(self, emitter: FMODSoundEmitter): ...


class ParameterPlayerDistance(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, zombie: IsoZombie): ...


class ParameterPlayerHealth(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, player: IsoPlayer): ...


class ParameterPowerSupply(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterRainIntensity(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterRoomSize(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterRoomType(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  @staticmethod
  def render(player: IsoPlayer) -> None: ...

  @staticmethod
  def setRoomType(roomType: int) -> None: ...

  def __init__(self): ...

  class RoomType(Enum):

    Barn: ParameterRoomType.RoomType

    Church: ParameterRoomType.RoomType

    Factory: ParameterRoomType.RoomType

    Generic: ParameterRoomType.RoomType

    Mall: ParameterRoomType.RoomType

    Office: ParameterRoomType.RoomType

    Prison: ParameterRoomType.RoomType

    Warehouse: ParameterRoomType.RoomType

    @staticmethod
    def valueOf(arg0: str) -> ParameterRoomType.RoomType: ...

    @staticmethod
    def values() -> list[ParameterRoomType.RoomType]: ...


class ParameterSeason(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterShoeType(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def setShoeType(self, shoeType: ParameterShoeType.ShoeType) -> None: ...

  def __init__(self, character: IsoGameCharacter): ...

  class ShoeType(Enum):

    Barefoot: ParameterShoeType.ShoeType

    Boots: ParameterShoeType.ShoeType

    FlipFlops: ParameterShoeType.ShoeType

    Shoes: ParameterShoeType.ShoeType

    Slippers: ParameterShoeType.ShoeType

    Sneakers: ParameterShoeType.ShoeType

    @staticmethod
    def valueOf(arg0: str) -> ParameterShoeType.ShoeType: ...

    @staticmethod
    def values() -> list[ParameterShoeType.ShoeType]: ...


class ParameterSnowIntensity(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterStorm(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterTemperature(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterTimeOfDay(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterVehicleBrake(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, vehicle: BaseVehicle): ...


class ParameterVehicleEngineCondition(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, vehicle: BaseVehicle): ...


class ParameterVehicleGear(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, vehicle: BaseVehicle): ...


class ParameterVehicleHitLocation(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def setLocation(self, location: ParameterVehicleHitLocation.HitLocation) -> None: ...

  @staticmethod
  def calculateLocation(vehicle: BaseVehicle, x: float, y: float, z: float) -> ParameterVehicleHitLocation.HitLocation: ...

  def __init__(self): ...

  class HitLocation(Enum):

    Front: ParameterVehicleHitLocation.HitLocation

    Rear: ParameterVehicleHitLocation.HitLocation

    Side: ParameterVehicleHitLocation.HitLocation

    @staticmethod
    def valueOf(arg0: str) -> ParameterVehicleHitLocation.HitLocation: ...

    @staticmethod
    def values() -> list[ParameterVehicleHitLocation.HitLocation]: ...


class ParameterVehicleLoad(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, vehicle: BaseVehicle): ...


class ParameterVehicleRPM(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, vehicle: BaseVehicle): ...


class ParameterVehicleRoadMaterial(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, vehicle: BaseVehicle): ...

  class Material(Enum):

    Carpet: ParameterVehicleRoadMaterial.Material

    Concrete: ParameterVehicleRoadMaterial.Material

    Dirt: ParameterVehicleRoadMaterial.Material

    Grass: ParameterVehicleRoadMaterial.Material

    Gravel: ParameterVehicleRoadMaterial.Material

    Puddle: ParameterVehicleRoadMaterial.Material

    Sand: ParameterVehicleRoadMaterial.Material

    Snow: ParameterVehicleRoadMaterial.Material

    Wood: ParameterVehicleRoadMaterial.Material

    @staticmethod
    def valueOf(arg0: str) -> ParameterVehicleRoadMaterial.Material: ...

    @staticmethod
    def values() -> list[ParameterVehicleRoadMaterial.Material]: ...


class ParameterVehicleSkid(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, vehicle: BaseVehicle): ...


class ParameterVehicleSpeed(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, vehicle: BaseVehicle): ...


class ParameterVehicleSteer(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, vehicle: BaseVehicle): ...


class ParameterVehicleTireMissing(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, vehicle: BaseVehicle): ...


class ParameterWaterSupply(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterWeatherEvent(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...

  class Event(Enum):

    FreshSnow: ParameterWeatherEvent.Event

    # None: ParameterWeatherEvent.Event

    @staticmethod
    def valueOf(arg0: str) -> ParameterWeatherEvent.Event: ...

    @staticmethod
    def values() -> list[ParameterWeatherEvent.Event]: ...


class ParameterWindIntensity(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...


class ParameterZombieState(FMODLocalParameter):

  def calculateCurrentValue(self) -> float: ...

  def isState(self, state: ParameterZombieState.State) -> bool: ...

  def setState(self, state: ParameterZombieState.State) -> None: ...

  def __init__(self, zombie: IsoZombie): ...

  class State(Enum):

    Attack: ParameterZombieState.State

    AttackBite: ParameterZombieState.State

    AttackLacerate: ParameterZombieState.State

    AttackScratch: ParameterZombieState.State

    Death: ParameterZombieState.State

    Eating: ParameterZombieState.State

    GettingUp: ParameterZombieState.State

    Hit: ParameterZombieState.State

    Idle: ParameterZombieState.State

    LockTarget: ParameterZombieState.State

    Pushed: ParameterZombieState.State

    Reanimate: ParameterZombieState.State

    RunOver: ParameterZombieState.State

    SearchTarget: ParameterZombieState.State

    @staticmethod
    def valueOf(arg0: str) -> ParameterZombieState.State: ...

    @staticmethod
    def values() -> list[ParameterZombieState.State]: ...


class ParameterZone(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self, name: str, zoneName: str): ...


class ParameterZoneWaterSide(FMODGlobalParameter):

  def calculateCurrentValue(self) -> float: ...

  def __init__(self): ...

