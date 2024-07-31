from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Iterable
from zombie.debug import BooleanDebugOption

class Animation(OptionGroup):

  def __init__(self):
    self.allowearlytransitionout: BooleanDebugOption
    self.animlayer: Animation.AnimLayerOG
    self.animrenderpicker: BooleanDebugOption
    self.blendusefbx: BooleanDebugOption
    self.debug: BooleanDebugOption
    self.sharedskeles: Animation.SharedSkelesOG

  class AnimLayerOG(OptionGroup): ...

  class SharedSkelesOG(OptionGroup): ...


class Character(OptionGroup):

  def __init__(self):
    self.createalloutfits: BooleanDebugOption
    self.debug: Character.DebugOG

  class DebugOG(OptionGroup):

    def __init__(self, parentGroup: IDebugOptionGroup):
      self.alwaystripoverfence: BooleanDebugOption
      self.animate: Character.DebugOG.AnimateOG
      self.playsoundwheninvisible: BooleanDebugOption
      self.registerdebugvariables: BooleanDebugOption
      self.render: Character.DebugOG.RenderOG
      self.updatealpha: BooleanDebugOption
      self.updatealphaeighthspeed: BooleanDebugOption

    class RenderOG(OptionGroup):

      def __init__(self, parentGroup: IDebugOptionGroup):
        self.aimcone: BooleanDebugOption
        self.angle: BooleanDebugOption
        self.bip01: BooleanDebugOption
        self.deferredangles: BooleanDebugOption
        self.deferredmovement: BooleanDebugOption
        self.displayroomandzombieszone: BooleanDebugOption
        self.fmodroomtype: BooleanDebugOption
        self.primaryhandbone: BooleanDebugOption
        self.secondaryhandbone: BooleanDebugOption
        self.skipcharacters: BooleanDebugOption
        self.testdotside: BooleanDebugOption
        self.translationdata: BooleanDebugOption
        self.vision: BooleanDebugOption

    class AnimateOG(OptionGroup):

      def __init__(self, parentGroup: IDebugOptionGroup):
        self.deferredrotationonly: BooleanDebugOption
        self.nobonemasks: BooleanDebugOption
        self.nobonetwists: BooleanDebugOption
        self.zerocounterrotationbone: BooleanDebugOption


class IDebugOption:

  def getName(self) -> str: ...

  def getParent(self) -> IDebugOptionGroup: ...

  def setParent(self, parent: IDebugOptionGroup) -> None: ...


class IDebugOptionGroup:

  def addChild(self, childOption: IDebugOption) -> None: ...

  def getChildren(self) -> Iterable[IDebugOption]: ...

  def getName(self) -> str: ...

  def getParent(self) -> IDebugOptionGroup: ...

  def onChildAdded(self, newChild: IDebugOption) -> None: ...

  def onDescendantAdded(self, newDescendant: IDebugOption) -> None: ...

  def setParent(self, arg0: IDebugOptionGroup) -> None: ...


class IsoSprite(OptionGroup):

  def __init__(self):
    self.charactermipmapcolors: BooleanDebugOption
    self.dropshadowedges: BooleanDebugOption
    self.forcelinearmagfilter: BooleanDebugOption
    self.forcenearestmagfilter: BooleanDebugOption
    self.forcenearestmipmapping: BooleanDebugOption
    self.itemheight: BooleanDebugOption
    self.movingobjectedges: BooleanDebugOption
    self.nearestmagfilteratminzoom: BooleanDebugOption
    self.rendermodels: BooleanDebugOption
    self.rendersprites: BooleanDebugOption
    self.surface: BooleanDebugOption
    self.texturewrapclamptoedge: BooleanDebugOption
    self.texturewraprepeat: BooleanDebugOption
    self.worldmipmapcolors: BooleanDebugOption


class Network(OptionGroup):

  def __init__(self):
    self.client: Network.Client
    self.publicserverutil: Network.PublicServerUtil
    self.server: Network.Server

  class Client(OptionGroup):

    def __init__(self, arg0: Network, arg1: IDebugOptionGroup):
      self.mainloop: BooleanDebugOption
      self.syncisoobject: BooleanDebugOption
      self.updatezombiesfrompacket: BooleanDebugOption

  class Server(OptionGroup):

    def __init__(self, arg0: Network, arg1: IDebugOptionGroup):
      self.syncisoobject: BooleanDebugOption

  class PublicServerUtil(OptionGroup):

    def __init__(self, arg0: Network, arg1: IDebugOptionGroup):
      self.enabled: BooleanDebugOption


class OffscreenBuffer(OptionGroup):

  def __init__(self):
    self.render: BooleanDebugOption


class OptionGroup:

  @overload
  def addChild(self, childOption: IDebugOption) -> None: ...

  @overload
  def addChild(self, childOption: IDebugOption) -> None: ...

  @overload
  def getChildren(self) -> Iterable[IDebugOption]: ...

  @overload
  def getChildren(self) -> Iterable[IDebugOption]: ...

  def getName(self) -> str: ...

  def getParent(self) -> IDebugOptionGroup: ...

  @overload
  def onChildAdded(self, newOption: IDebugOption) -> None: ...

  @overload
  def onChildAdded(self, newOption: IDebugOption) -> None: ...

  @overload
  def onDescendantAdded(self, newOption: IDebugOption) -> None: ...

  @overload
  def onDescendantAdded(self, newOption: IDebugOption) -> None: ...

  def setParent(self, parent: IDebugOptionGroup) -> None: ...

  @staticmethod
  @overload
  def newDebugOnlyOption(name: str, defaultValue: bool) -> BooleanDebugOption: ...

  @staticmethod
  @overload
  def newDebugOnlyOption(parentGroup: IDebugOptionGroup, name: str, defaultValue: bool) -> BooleanDebugOption: ...

  @staticmethod
  @overload
  def newOption(name: str, defaultValue: bool) -> BooleanDebugOption: ...

  @staticmethod
  @overload
  def newOption(parentGroup: IDebugOptionGroup, name: str, defaultValue: bool) -> BooleanDebugOption: ...

  @overload
  def __init__(self, groupName: str):
    self.group: IDebugOptionGroup

  @overload
  def __init__(self, parentGroup: IDebugOptionGroup, groupName: str): ...


class Terrain(OptionGroup):

  def __init__(self):
    self.rendertiles: Terrain.RenderTiles

  class RenderTiles(OptionGroup):

    def __init__(self, arg0: Terrain, arg1: IDebugOptionGroup):
      self.attachedanimsprites: BooleanDebugOption
      self.attachedchildren: BooleanDebugOption
      self.attachedwallbloodsplats: BooleanDebugOption
      self.blooddecals: BooleanDebugOption
      self.enable: BooleanDebugOption
      self.highcontrastbg: BooleanDebugOption
      self.isogridsquare: Terrain.RenderTiles.IsoGridSquare
      self.lua: BooleanDebugOption
      self.minusfloorcharacters: BooleanDebugOption
      self.newrender: BooleanDebugOption
      self.overlaysprites: BooleanDebugOption
      self.rendergridsquares: BooleanDebugOption
      self.rendersprites: BooleanDebugOption
      self.shadows: BooleanDebugOption
      self.useshaders: BooleanDebugOption
      self.vegetationcorpses: BooleanDebugOption
      self.water: BooleanDebugOption
      self.waterbody: BooleanDebugOption
      self.watershore: BooleanDebugOption

    class IsoGridSquare(OptionGroup):

      def __init__(self, arg0: Terrain.RenderTiles, arg1: IDebugOptionGroup):
        self.doorsandwalls: BooleanDebugOption
        self.doorsandwalls_simplelighting: BooleanDebugOption
        self.floor: Terrain.RenderTiles.IsoGridSquare.Floor
        self.isopadding: BooleanDebugOption
        self.isopaddingattached: BooleanDebugOption
        self.isopaddingdediamond: BooleanDebugOption
        self.meshcutdown: BooleanDebugOption
        self.objects: BooleanDebugOption
        self.renderminusfloor: BooleanDebugOption
        self.shorefade: BooleanDebugOption
        self.walls: Terrain.RenderTiles.IsoGridSquare.Walls

      class Walls(OptionGroup):

        def __init__(self, arg0: Terrain.RenderTiles.IsoGridSquare, arg1: IDebugOptionGroup):
          self.attachedsprites: BooleanDebugOption
          self.lighting: BooleanDebugOption
          self.lightingdebug: BooleanDebugOption
          self.lightingolddebug: BooleanDebugOption
          self.n: BooleanDebugOption
          self.nw: BooleanDebugOption
          self.render: BooleanDebugOption
          self.w: BooleanDebugOption

      class Floor(OptionGroup):

        def __init__(self, arg0: Terrain.RenderTiles.IsoGridSquare, arg1: IDebugOptionGroup):
          self.lighting: BooleanDebugOption
          self.lightingdebug: BooleanDebugOption
          self.lightingold: BooleanDebugOption


class Weather(OptionGroup):

  def __init__(self):
    self.fx: BooleanDebugOption
    self.snow: BooleanDebugOption
    self.waterpuddles: BooleanDebugOption

