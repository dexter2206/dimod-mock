""""Test cases for StructuredMock"""
import pytest
from dimodmock import StructuredMock

EXAMPLE_CONFIGURATIONS = [
    ([0, 1, 2, 3], [(0, 2), (1, 3)], {}, {}),
    (list(range(1000)), [(0, 1), (1, 2), (0, 100)], {}, {}),
    (
        list(range(1000)),
        [(0, 1000), (10, 20)],
        {"max_num_reads": 100},
        {"num_reads": ["max_num_reads"]},
    ),
    (
        ["a", "b", "c", "d"],
        [("a", "b"), ("c", "a")],
        {"max_num_reads": 100},
        {"num_reads": ["max_num_reads"]},
    ),
]


@pytest.mark.parametrize("nodelist,edgelist,properties,parameters", EXAMPLE_CONFIGURATIONS)
def test_propagates_nodelist(nodelist, edgelist, properties, parameters):
    mock = StructuredMock(nodelist, edgelist, properties, parameters)
    assert mock.nodelist == nodelist


@pytest.mark.parametrize("nodelist,edgelist,properties,parameters", EXAMPLE_CONFIGURATIONS)
def test_propagates_edgelist(nodelist, edgelist, properties, parameters):
    mock = StructuredMock(nodelist, edgelist, properties, parameters)
    assert mock.edgelist == edgelist


@pytest.mark.parametrize("nodelist,edgelist,properties,parameters", EXAMPLE_CONFIGURATIONS)
def test_propagates_properties(nodelist, edgelist, properties, parameters):
    mock = StructuredMock(nodelist, edgelist, properties, parameters)
    assert mock.properties == properties


@pytest.mark.parametrize("nodelist,edgelist,properties,parameters", EXAMPLE_CONFIGURATIONS)
def test_propagates_parameters(nodelist, edgelist, properties, parameters):
    mock = StructuredMock(nodelist, edgelist, properties, parameters)
    assert mock.parameters == parameters
