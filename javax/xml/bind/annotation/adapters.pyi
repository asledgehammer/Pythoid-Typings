from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation

ValueType = TypeVar('ValueType', default=Any)
BoundType = TypeVar('BoundType', default=Any)

class XmlAdapter[ValueType, BoundType]:

  def marshal(self, arg0: object) -> object: ...

  def unmarshal(self, arg0: object) -> object: ...

