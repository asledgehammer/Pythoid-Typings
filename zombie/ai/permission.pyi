from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from zombie.characters import IsoGameCharacter

class DefaultStatePermissions:

  Instance: DefaultStatePermissions

  @overload
  def isDeferredMovementAllowed(self, chr: IsoGameCharacter) -> bool: ...

  @overload
  def isDeferredMovementAllowed(self, chr: IsoGameCharacter) -> bool: ...

  @overload
  def isPlayerInputAllowed(self, chr: IsoGameCharacter) -> bool: ...

  @overload
  def isPlayerInputAllowed(self, chr: IsoGameCharacter) -> bool: ...

  def __init__(self): ...


class GenericStatePermissions:

  @overload
  def isDeferredMovementAllowed(self, chr: IsoGameCharacter) -> bool: ...

  @overload
  def isDeferredMovementAllowed(self, chr: IsoGameCharacter) -> bool: ...

  @overload
  def isPlayerInputAllowed(self, chr: IsoGameCharacter) -> bool: ...

  @overload
  def isPlayerInputAllowed(self, chr: IsoGameCharacter) -> bool: ...

  def setDeferredMovementAllowed(self, val: bool) -> None: ...

  def setPlayerInputAllowed(self, val: bool) -> None: ...

  def __init__(self): ...


class IStatePermissions:

  def isDeferredMovementAllowed(self, chr: IsoGameCharacter) -> bool: ...

  def isPlayerInputAllowed(self, chr: IsoGameCharacter) -> bool: ...

