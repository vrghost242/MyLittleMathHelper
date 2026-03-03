from pydantic import BaseModel, Field

class FactorisedNumber(BaseModel):
    factors: list[int] = Field(default=[], description="Prime factors of the number")
    rest: int = Field(description="Left over, used for calculation")
    complex_number: bool = Field(default=True, description="Is the number a complex number or a prime")
    surd: int = 0
    surd_radical_index: int = 2
    value: int = Field(default=None, description="The value of the number with sign")




class Term(BaseModel):
    positive: bool = (Field(default=True, description="Is the term positive or negative"))
    coefficient_numerator: FactorisedNumber = Field(default=None, description="The numerator of the coefficient")
    coefficient_denominator: FactorisedNumber = Field(default=None, description="The denominator of the coefficient")
    function: str = Field(default=None, description="The function of the term")
    argument: str = Field(default=None, description="The argument of the term")


