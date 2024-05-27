from typing import Optional
from typing_extensions import Self

from .tokens import Token

class DataType:
    '''
    `DataType` is a container class for storing relevant dataset items. As of 0.1.1-alpha, it is not
    yet supported for users to create their own `DataType` objects. Instead, currently usage is
    through the `DataTypes` module. This will change in future versions. Static objects and further
    documentation are provided in the `DataTypes` class.

    :param desc: The purpose of the DataType. This should be unique for every new object.
    :type desc: str
    :param token_type: The token type of the DataType.
    :type token_type: Token
    '''

    def __init__(self, desc: str, token_type: Token, doc: Optional[str] = None) -> None:
        self.desc: str = desc
        self.token_type: Token = token_type
        self.doc: str = doc if doc is not None else desc

    def __repr__(self) -> str:
        return f'{self.doc}'

    def __eq__(self, other: Self) -> bool:
        if self.__class__ != other.__class__:
            return False
        return self.desc == other.desc

    def __hash__(self) -> int:
        return hash(self.desc)

    def verify_token(self, value: str) -> bool:
        '''
        Verify that a given value is valid for the datatype. Calls on internal Token
        functions for validation.
        
        - `value` (`str`): the value to check if it is compatible with the DataType.
        '''
        return self.token_type.verify_token(value)