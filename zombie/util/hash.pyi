from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation

class DefaultIntHashFunction:

  INSTANCE: IntHashFunction

  @overload
  def hash(self, v: int) -> int: ...

  @overload
  def hash(self, v: int) -> int: ...


class IntHashFunction:

  def hash(self, v: int) -> int: ...


class Primes:

  @staticmethod
  def nextPrime(n: int) -> int: ...

