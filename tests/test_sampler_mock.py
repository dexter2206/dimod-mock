"""Test cases for SamplerMock"""
import pytest
from dimodmock import SamplerMock


EXAMPLE_CONFIGURATIONS = [
    ({}, {}),
    ({"max_num_reads": 100}, {"num_reads": ["max_num_reads"], "iterations": []}),
    ({"j_range": [-1, 1]}, {"num_reads": []})
]


@pytest.mark.parametrize("properties,parameters", EXAMPLE_CONFIGURATIONS)
def test_propagates_parameters(properties, parameters):
    mock = SamplerMock(properties, parameters)
    assert mock.parameters == parameters


@pytest.mark.parametrize("properties,parameters", EXAMPLE_CONFIGURATIONS)
def test_propagates_properties(properties, parameters):
    mock = SamplerMock(properties, parameters)
    assert mock.properties == properties
