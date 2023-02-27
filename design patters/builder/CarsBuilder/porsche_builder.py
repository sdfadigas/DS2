from body import Body
from builder import Builder
from engine import Engine
from wheel import Wheel


class PorscheBuilder(Builder):
    def get_wheel(self) -> Wheel:
        wheel = Wheel()
        wheel.size = 30
        return wheel

    def get_engine(self) -> Engine:
        engine = Engine()
        engine.horsepower = 500 
        return engine

    def get_body(self) -> Body:
        body = Body()
        body.shape = "sedan"
        return body