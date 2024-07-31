from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum, Integer
from java.nio import ByteBuffer
from java.util import ArrayList, HashMap
from org.joml import Vector3f, Matrix4f, Quaternionf, Matrix3f
from zombie.characters import IsoPlayer
from zombie.core.textures import TextureDraw
from zombie.iso import IsoChunk, IsoMovingObject
from zombie.vehicles import BaseVehicle

class Bullet:

  cmdBuf: ByteBuffer

  TO_ACTIVATE_CHUNKMAP: int

  TO_ADD_VEHICLE: int

  TO_DEBUG_DRAW_WORLD: int

  TO_END: int

  TO_INIT_WORLD: int

  TO_SCROLL_CHUNKMAP: int

  TO_STEP_SIMULATION: int

  TO_UPDATE_CHUNK: int

  TO_UPDATE_PLAYER_LIST: int

  @staticmethod
  def CatchToBullet(bb: ByteBuffer) -> None: ...

  @staticmethod
  def activateChunkMap(playerIndex: int, wx: int, wy: int, chunkGridWidth: int) -> None: ...

  @staticmethod
  def addHingeConstraint(vidA: int, vidB: int, pivotXA: float, pivotYA: float, pivotZA: float, pivotXB: float, pivotYB: float, pivotZB: float) -> int: ...

  @staticmethod
  def addPhysicsObject(x: float, y: float) -> int: ...

  @staticmethod
  def addPointConstraint(vidA: int, vidB: int, pivotXA: float, pivotYA: float, pivotZA: float, pivotXB: float, pivotYB: float, pivotZB: float) -> int: ...

  @staticmethod
  def addRopeConstraint(vidA: int, vidB: int, pivotXA: float, pivotYA: float, pivotZA: float, pivotXB: float, pivotYB: float, pivotZB: float, linearLimit: float) -> int: ...

  @staticmethod
  def addVehicle(ID: int, x: float, y: float, z: float, qx: float, qy: float, qz: float, qw: float, scriptName: str) -> None: ...

  @staticmethod
  def applyCentralForceToVehicle(ID: int, fx: float, fy: float, fz: float) -> None: ...

  @staticmethod
  def applyTorqueToVehicle(ID: int, tx: float, ty: float, tz: float) -> None: ...

  @staticmethod
  def beginUpdateChunk(chunk: IsoChunk) -> None: ...

  @staticmethod
  def controlVehicle(ID: int, engineForce: float, brakeForce: float, steerAngle: float) -> None: ...

  @staticmethod
  def createServerCell(x: int, y: int) -> None: ...

  @staticmethod
  def deactivateChunkMap(playerIndex: int) -> None: ...

  @staticmethod
  def defineVehicleScript(name: str, params: list[float]) -> None: ...

  @staticmethod
  def destroyWorld() -> None: ...

  @staticmethod
  def endUpdateChunk() -> None: ...

  @staticmethod
  def getObjectPhysics(out: list[float]) -> int: ...

  @staticmethod
  def getOwnVehiclePhysics(vid: int, out: list[float]) -> int: ...

  @staticmethod
  def getVehicleCount() -> int: ...

  @staticmethod
  def getVehiclePhysics(offset: int, out: list[float]) -> int: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  @overload
  def initWorld(offsetX: int, offsetY: int, bServer: bool) -> None: ...

  @staticmethod
  @overload
  def initWorld(offsetX: int, offsetY: int, wx: int, wy: int, chunkGridWidth: int) -> None: ...

  @staticmethod
  def removeConstraint(id: int) -> None: ...

  @staticmethod
  def removeServerCell(x: int, y: int) -> None: ...

  @staticmethod
  def removeVehicle(ID: int) -> None: ...

  @staticmethod
  def scrollChunkMap(playerIndex: int, dir: int) -> None: ...

  @staticmethod
  def scrollChunkMapDown(playerIndex: int) -> None: ...

  @staticmethod
  def scrollChunkMapLeft(playerIndex: int) -> None: ...

  @staticmethod
  def scrollChunkMapRight(playerIndex: int) -> None: ...

  @staticmethod
  def scrollChunkMapUp(playerIndex: int) -> None: ...

  @staticmethod
  def setOwnVehiclePhysics(vid: int, data: list[float]) -> int: ...

  @staticmethod
  def setTireInflation(ID: int, wheelIndex: int, inflation: float) -> None: ...

  @staticmethod
  def setTireRemoved(ID: int, wheelIndex: int, removed: bool) -> None: ...

  @staticmethod
  @overload
  def setVehicleActive(ID: int, active: bool) -> None: ...

  @staticmethod
  @overload
  def setVehicleActive(vehicle: BaseVehicle, isActive: bool) -> None: ...

  @staticmethod
  def setVehicleMass(vid: int, mass: float) -> int: ...

  @staticmethod
  def setVehicleParams(vid: int, data: list[float]) -> int: ...

  @staticmethod
  @overload
  def setVehicleStatic(vid: int, isStatic: bool) -> int: ...

  @staticmethod
  @overload
  def setVehicleStatic(vehicle: BaseVehicle, isStatic: bool) -> int: ...

  @staticmethod
  def setVehicleVelocityMultiplier(vid: int, maxSpeed: float, multiplier: float) -> None: ...

  @staticmethod
  def stepSimulation(timeStep: float, maxSubSteps: int, fixedTimeStep: float) -> None: ...

  @staticmethod
  def teleportVehicle(ID: int, x: float, y: float, z: float, qx: float, qy: float, qz: float, qw: float) -> None: ...

  @staticmethod
  def updateChunk(x: int, y: int, z: int, numShapes: int, shapes: list[int]) -> None: ...

  @staticmethod
  def updatePlayerList(players: ArrayList[IsoPlayer]) -> None: ...

  def __init__(self): ...


class CarController:

  gears: list[CarController.GearInfo]

  def accelerator(self, apply: bool) -> None: ...

  def brake(self, apply: bool) -> None: ...

  def checkShouldBeActive(self) -> None: ...

  def control_NoControl(self) -> None: ...

  def debug(self) -> None: ...

  @overload
  def drawCircle(self, x: float, y: float, radius: float) -> None: ...

  @overload
  def drawCircle(self, x: float, y: float, radius: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def drawRect(self, vec: Vector3f, x: float, y: float, w: float, h: float) -> None: ...

  @overload
  def drawRect(self, vec: Vector3f, x: float, y: float, w: float, h: float, r: float, g: float, b: float) -> None: ...

  def findGear(self, speed: float) -> CarController.GearInfo: ...

  def getClientControls(self) -> CarController.ClientControls: ...

  def isBrakePedalPressed(self) -> bool: ...

  def isGasPedalPressed(self) -> bool: ...

  def park(self) -> None: ...

  def update(self) -> None: ...

  def updateControls(self) -> None: ...

  def updateTrailer(self) -> None: ...

  def __init__(self, vehicleObject: BaseVehicle):
    self.acceleratoron: bool
    self.brakeon: bool
    self.brakingforce: float
    self.clientcontrols: CarController.ClientControls
    self.clientforce: float
    self.engineforce: float
    self.isenable: bool
    self.speed: float
    self.vehicleobject: BaseVehicle

  class ClientControls:

    def reset(self) -> None: ...

    def __init__(self):
      self.backward: bool
      self.brake: bool
      self.forcebrake: int
      self.forward: bool
      self.shift: bool
      self.steering: float
      self.wasusingparkingbrakes: bool

  class GearInfo: ...

  class ControlState(Enum):

    Braking: CarController.ControlState

    Forward: CarController.ControlState

    NoControl: CarController.ControlState

    Reverse: CarController.ControlState

    @staticmethod
    def valueOf(arg0: str) -> CarController.ControlState: ...

    @staticmethod
    def values() -> list[CarController.ControlState]: ...

  class BulletVariables:

    def __init__(self): ...


class PhysicsDebugRenderer(TextureDraw.GenericDrawer):

  def XToScreenExact(self, objectX: float, objectY: float, objectZ: float, screenZ: int) -> float: ...

  def YToScreenExact(self, objectX: float, objectY: float, objectZ: float, screenZ: int) -> float: ...

  def drawContactPoint(self, pointOnBX: float, pointOnBY: float, pointOnBZ: float, normalOnBX: float, normalOnBY: float, normalOnBZ: float, distance: float, lifeTime: int, r: float, g: float, b: float) -> None: ...

  def drawLine(self, fromX: float, fromY: float, fromZ: float, toX: float, toY: float, toZ: float, fromR: float, fromG: float, fromB: float, toR: float, toG: float, toB: float) -> None: ...

  def drawSphere(self, pX: float, pY: float, pZ: float, radius: float, r: float, g: float, b: float) -> None: ...

  def drawTriangle(self, aX: float, aY: float, aZ: float, bX: float, bY: float, bZ: float, cX: float, cY: float, cZ: float, r: float, g: float, b: float, alpha: float) -> None: ...

  def init(self, player: IsoPlayer) -> None: ...

  def n_debugDrawWorld(self, offsetX: int, offsetY: int) -> None: ...

  def postRender(self) -> None: ...

  def release(self) -> None: ...

  def render(self) -> None: ...

  @staticmethod
  def alloc() -> PhysicsDebugRenderer: ...

  def __init__(self): ...


class Transform:

  def equals(self, obj: object) -> bool: ...

  def getMatrix(self, out: Matrix4f) -> Matrix4f: ...

  def getRotation(self, out: Quaternionf) -> Quaternionf: ...

  def hashCode(self) -> int: ...

  @overload
  def inverse(self) -> None: ...

  @overload
  def inverse(self, tr: Transform) -> None: ...

  @overload
  def set(self, mat: Matrix3f) -> None: ...

  @overload
  def set(self, mat: Matrix4f) -> None: ...

  @overload
  def set(self, tr: Transform) -> None: ...

  def setIdentity(self) -> None: ...

  def setRotation(self, q: Quaternionf) -> None: ...

  def transform(self, v: Vector3f) -> None: ...

  @overload
  def __init__(self):
    self.basis: Matrix3f

    self.origin: Vector3f

  @overload
  def __init__(self, mat: Matrix3f): ...
  @overload
  def __init__(self, mat: Matrix4f): ...
  @overload
  def __init__(self, tr: Transform): ...


class WorldSimulation:

  instance: WorldSimulation

  LEVEL_ZERO_ONLY: bool

  def activateChunkMap(self, playerIndex: int) -> None: ...

  def create(self) -> None: ...

  def deactivateChunkMap(self, playerIndex: int) -> None: ...

  def destroy(self) -> None: ...

  def scrollGroundDown(self, playerIndex: int) -> None: ...

  def scrollGroundLeft(self, playerIndex: int) -> None: ...

  def scrollGroundRight(self, playerIndex: int) -> None: ...

  def scrollGroundUp(self, playerIndex: int) -> None: ...

  def setOwnVehiclePhysics(self, vid: int, data: list[float]) -> int: ...

  def update(self) -> None: ...

  @staticmethod
  def getDrawer(playerIndex: int) -> TextureDraw.GenericDrawer: ...

  def __init__(self):
    self.created: bool
    self.offsetx: float
    self.offsety: float
    self.physicsobjectmap: HashMap[Integer, IsoMovingObject]
    self.time: int

  class s_performance: ...

