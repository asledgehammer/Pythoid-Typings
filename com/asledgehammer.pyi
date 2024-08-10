from typing import Any

class Pythoid:

    @staticmethod
    def expose(clazz: Any) -> None: ...

    @staticmethod
    def invoke(instance: object, methodName: str, *args) -> Any: ...

    @staticmethod
    def invokeStatic(clazz: object, methodName: str, *args) -> Any: ...

    @staticmethod
    def getField(instance: object, fieldName: str) -> Any: ...

    @staticmethod
    def setField(instance: object, fieldName: str, value: Any) -> None: ...

    @staticmethod
    def getStaticField(clazz: object, fieldName: str) -> Any: ... 

    @staticmethod
    def setStaticField(clazz: object, fieldName: str, value: Any) -> None: ...
