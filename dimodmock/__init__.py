"""Main implementation"""
import dimod
from typing import Any, Dict, List, Tuple, TypeVar

T = TypeVar("T")


class StructuredMock(dimod.Sampler, dimod.Structured):
    """Class mocking arbitrary-structured sampler."""

    def __init__(self, nodelist: List[T], edgelist: List[Tuple[T, T]], properties: Dict[Any, Any], parameters: Dict[Any, List[Any]]):
        self._nodelist = nodelist
        self._edgelist = edgelist
        self._properties = properties
        self._parameters = parameters

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
