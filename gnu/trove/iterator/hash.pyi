from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from gnu.trove.impl.hash import THashIterator, TObjectHash

E = TypeVar('E', default=Any)

class TObjectHashIterator[E](THashIterator):

  def __init__(self, arg0: TObjectHash[E]): ...

