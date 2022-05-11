![Alt text](/cdci.png?raw=true "Title")

# CDCI - Causality

Implementation of the CDCI algorithm from the [Bivariate Causal Discovery via Conditional Divergence](https://openreview.net/forum?id=8X6cWIvY_2v) paper. The algorithm is a simple, yet effective, method to identify causal direction between two variables.

The main idea relies on the assumption that the conditional distribution of the effect given the cause has the same shape for any value of the cause (despite locations and scales can differ). On the other hand, conditioning the cause on the effect does not usually show this property.

## Install

```bash
$ pip install cdci-causality
```

[![PyPI - Python Version](https://img.shields.io/pypi/v/cdci-causality?style=flat&colorA=0f0f0f&colorB=0f0f0f)](https://pypi.org/project/cdci-causality/)

## Usage

```python
import numpy as np
from scipy.stats import entropy
from cdci_causality import CDCI

model = CDCI(entropy)
mu = 5
sigma = 9
n_samples = 1000
X = np.random.normal(mu, sigma, n_samples)
Y = X ** 2 + np.random.normal(0, 1, n_samples) * X
causal_direction = model(X, Y)
print(causal_direction)
```

Where `causal_direction` is a value representing the model's confidence of the causal direction. A positive value indicates that `X -> Y`, while a negative value indicates that `Y -> X`. Using CDCI, the identifiability of the causal direction is ensured if exactly one of `P[Y|X]` and `P[X|Y]` is invariant in shape. Section 4 of [the paper](https://openreview.net/forum?id=8X6cWIvY_2v) presents partial theoretical guarantees, and give in-depth explanations on why CDCI can correctly predict the causal direction in many situations, even in presence of (non-causal) confounders.

## Citation

```bibtex
@inproceedings{
  duong2022bivariate,
  title={Bivariate Causal Discovery via Conditional Divergence},
  author={Bao Duong and Thin Nguyen},
  booktitle={First Conference on Causal Learning and Reasoning},
  year={2022},
  url={https://openreview.net/forum?id=8X6cWIvY_2v}
}
```
