# Datasets

Small datasets used in the teaching notebooks. Keep this directory lightweight and document where every dataset came from.

## Included

| File | Purpose | Good for |
|---|---|---|
| `european_cities.csv` | Symmetric distance matrix for 24 European cities | Exhaustive search, hill climbing, simulated annealing and genetic algorithms |

## Generated inside notebooks

The following `scikit-learn` generators require no downloaded data and make it easy to expose one concept at a time:

- `make_blobs`: separability, overlap and multiclass classification
- `make_moons`: curved decision boundaries
- `make_circles`: strong failure case for linear classifiers
- `make_classification`: noise, class imbalance and redundant features

## Candidate real datasets

- Palmer Penguins: interpretable multiclass classification
- UCI Wine: scaling and multiclass models
- Fashion-MNIST: image classification without large compute requirements

Do not commit student data, personal data, assignment solutions, or datasets without a clear license and source.
