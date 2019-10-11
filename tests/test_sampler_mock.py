"""Test cases for SamplerMock"""
import pytest
import dimod
from dimodmock import SamplerMock


EXAMPLE_CONFIGURATIONS = [
    ({}, {}),
    ({"max_num_reads": 100}, {"num_reads": ["max_num_reads"], "iterations": []}),
    ({"j_range": [-1, 1]}, {"num_reads": []})
]


@pytest.mark.parametrize("properties,parameters", EXAMPLE_CONFIGURATIONS)
def test_propagates_parameters(properties, parameters):
    """SamplerMock should correctly return dict of parameters specified during initialization."""
    mock = SamplerMock(properties, parameters)
    assert mock.parameters == parameters


@pytest.mark.parametrize("properties,parameters", EXAMPLE_CONFIGURATIONS)
def test_propagates_properties(properties, parameters):
    """SamplerMock should correctly return dict of properties specified during initialization."""
    mock = SamplerMock(properties, parameters)
    assert mock.properties == properties


def test_rejects_unknown_parameters():
    """SamplerMock should raise TypeError if uknown parameters are passed to sample* methods."""
    mock = SamplerMock({}, {"num_reads": []})

    with pytest.raises(TypeError):
        mock.sample_qubo({(0, 1): 10}, num_reads=10, annealing_time=1000)


def test_accepts_known_properties():
    """"SamplerMock should not raise if only known parameters are passed for sample* methods."""
    mock = SamplerMock({}, {"num_reads": [], "annealing_time": []})

    try:
        mock.sample_qubo({(0, 0): 5}, num_reads=5, annealing_time=10)
    except TypeError:
        pytest.fail("SamplerMock unexpectedly raised TypeError.")


@pytest.mark.parametrize(
    "vartype,random_bits,expected_variables_values",
    [
        (dimod.Vartype.SPIN, [0, 1, 0], [-1, 1, -1]),
        (dimod.Vartype.BINARY, [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0])
    ]
)
def tests_uses_get_random_bit(mock, vartype, random_bits, expected_variables_values):
    get_random_bit= mock.Mock(side_effect=random_bits)
    mock = SamplerMock({}, {}, get_random_bit=get_random_bit)
    bqm = dimod.BinaryQuadraticModel(linear={i: i for i in range(len(random_bits))}, quadratic={}, offset=0, vartype=vartype)
    result = mock.sample(bqm)
    assert all(result.first.sample[i] == expected_variables_values[i] for i in range(len(random_bits)))
