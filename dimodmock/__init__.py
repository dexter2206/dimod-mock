"""Main implementation"""
import dimod
import random
from typing import Any, Dict, List, Tuple, TypeVar

T = TypeVar("T")


def random_bit_value():
    """Returns random bit"""
    return random.randint(0, 1)


class SamplerMock(dimod.Sampler):
    """Class mocking arbitrary dimod unstructured sampler."""
    def __init__(self, properties: Dict[Any, Any], parameters: Dict[Any, List[Any]], get_random_bit=random_bit_value):
        self._properties = properties
        self._parameters = parameters
        self.get_random_bit = get_random_bit

    def sample(self, bqm: dimod.BinaryQuadraticModel, **parameters):
        for parameter in parameters:
            if parameter not in self.parameters:
                raise TypeError(f"Parameter {parameter} is not supported by this sampler.")

        if bqm.vartype == dimod.Vartype.SPIN:
            get_random_value = lambda: self.get_random_bit() * 2 - 1
        else:
            get_random_value = self.get_random_bit

        samples = [{variable: get_random_value() for variable in bqm.variables} for _ in range(parameters.get("num_reads", 1))]

        return dimod.SampleSet.from_samples_bqm(samples, bqm)

    @property
    def parameters(self) -> Dict[Any, List[Any]]:
        """Returns dict of parameters of this mock-sampler.

        See dimod's documentation for further reference on this property.
        """
        return self._parameters

    @property
    def properties(self) -> Dict[Any, Any]:
        """Returns dict of properties of this sampler.

        See dimod's documentation for further reference on this parameter.
        """
        return self._properties


class StructuredMock(SamplerMock, dimod.Structured):
    """Class mocking arbitrary-structured sampler."""

    def __init__(self, nodelist: List[T], edgelist: List[Tuple[T, T]], properties: Dict[Any, Any],
                 parameters: Dict[Any, List[Any]]):
        super().__init__(properties, parameters)
        self._nodelist = nodelist
        self._edgelist = edgelist

    def sample(self, bqm, **parameters):
        pass

    @property
    def nodelist(self) -> List[T]:
        """Returns list of all nodes of this mock sampler."""
        return self._nodelist

    @property
    def edgelist(self) -> List[Tuple[T, T]]:
        """Returns list of all edges of this mock sampler."""
        return self._edgelist
