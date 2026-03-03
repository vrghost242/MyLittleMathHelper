from fractions import Fraction
from timeit import default_timer as timer
from include.logger import Logger
from include.generators.roots import Root
from include.generators.factorize_smarter import FactorisedNumber, FactorizeSmarter
from pydantic import BaseModel, Field, field_validator
import math


log = Logger("squares")
LOG_LEVEL = "INFO"
fz = FactorizeSmarter()
root = Root()

class coordinate(BaseModel):
    x_coordinate: Fraction = Field(default=0)
    y_coordinate: Fraction = Field(default=0)

    @field_validator('x_coordinate', 'y_coordinate', mode='before')
    @classmethod
    def convert_to_fraction(cls, v):
        """Converts int or float to Fraction before assignment."""
        if isinstance(v, Fraction):
            return v
        elif isinstance(v, (int, float)):
            return Fraction(v).limit_denominator()
        else:
            raise ValueError(f"Expected int, float, or Fraction, got {type(v)}")


class Geometry:
    pass
    def line_gradient(self, point1: coordinate, point2: coordinate):
        return (point2.y_coordinate - point1.y_coordinate) / (point2.x_coordinate - point1.x_coordinate)
    def inverse(self, gradient: Fraction):
        return Fraction(-1,gradient)
    def midpoint(self, point1: coordinate, point2: coordinate):
        return coordinate(x_coordinate=(point1.x_coordinate + point2.x_coordinate)/2, y_coordinate=(point1.y_coordinate + point2.y_coordinate)/2)



if __name__ == "__main__":
    log.debug("Hello World")
    geo = Geometry()
    geo.line_gradient(coordinate(x_coordinate=1, y_coordinate=1), coordinate(x_coordinate=2, y_coordinate=2))
    for i in [(-3,1,1,-1),(1,-1,-3,1),(1,-1,4,8),(4,8,1,-1)]:
        log.info(f"Testing line gradient for {i[0]},{i[1]} and {i[2]},{i[3]}")
        log.info(f"Gradient is {geo.line_gradient(coordinate(x_coordinate=i[0],y_coordinate=i[1]), coordinate(x_coordinate=i[2],y_coordinate=i[3]))}")
        log.info(f"Inverse is {geo.inverse(geo.line_gradient(coordinate(x_coordinate=i[0],y_coordinate=i[1]), coordinate(x_coordinate=i[2],y_coordinate=i[3])))}")
        log.info(f"Midpoint is {geo.midpoint(coordinate(x_coordinate=i[0],y_coordinate=i[1]), coordinate(x_coordinate=i[2],y_coordinate=i[3]))}")