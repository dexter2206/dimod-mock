[![Build Status](https://travis-ci.org/dexter2206/dimod-mock.svg?branch=master)](https://travis-ci.org/dexter2206/dimod-mock)

# dimod-mock

dimod-mock is a package for mocking dimod-based samplers, including the structured ones.
It lets you easily test your routines before trying them out on sophisticated samplers or real hardware.

# Installation

To install run

```
pip install dimodmock
```

# Usage

## Mocking simple samplers

Suppose you created some instance of your sampler (derived from `dimod.Sampler`). This is how you create its mock

```python
import dimodmock

sampler = ... # Create your sampler here
mock = dimodmock.SamplerMock.from_sampler(sampler)
```

The mock object created this way has the following properties identical to the source sampler
- `properties`
- `parameters`

The following methods are implemented:
- `sample`
- `sample_qubo`
- `sample_ising`

and have the same interface as the source sampler. In particular, call to those methods will fail
if unknown parameters are passed as keyword arguments. The returned samples are choosen randomly at uniform.
By default, the returned samplesets have one sample. See below for overriding this behaviour.

## Mocking structured samplers

You can also mock structured samplers. In this case use `dimodmock.StructuredMock.from_sampler`.
In addition to the characteristics described above, the `StructuredMock` has also the following properties, identical
to the source sampler:
- `edgelist`
- `nodelist`

Also, `sample`, `sample_qubo`, `sample_ising` methods respect the samplers structure, so trying to solve
mismatching instance will fail.

## Support for `num_reads`

By default, samplesets returned by all mocks contain only one sample. However, if the source sampler supports `num_reads`
property (which is true in particular for `DWaveSampler`), it will be respected by the mock and the correct number
of samples will be returned.

## Advanced usage
It is also possible to create mocks by specifying their properties in their initializer. For `SimpleMock` you need to specify 
`properties` and `parameters`. For `StructuredMock` you also need to specify `edgelist` and `nodelist`.

For instance, suppose you want to create a mock of a structured sampler defined on full graph of 3 nodes,
having a `max_num_reads` property and `num_reads` parameter. Here is how to do it:

```python
from dimodmock import StructuredSampler

mock = StructuredSampler(
    nodelist=[0, 1, 2], 
    edgelist=[(0, 1), (1, 2), (2, 0)], 
    properties={"max_num_reads": 10},
    parameters={"num_reads": ["max_num_reads"]},
)
```


# Caveats

Currently mocks don't validate keyword arguments passed to `sample*` methods. 
So, in the example above, mock will happily accept `num_reads=100`. In the future, additional validation might be
implemented.


# Reporting issues
Please report any issues you encounter using Github's issue tracker.
