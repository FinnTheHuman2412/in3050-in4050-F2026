"""Small plotting helpers shared by the teaching notebooks."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def plot_dataset(X, y, *, ax=None, title=None):
    """Plot a two-feature classification dataset."""
    if X.shape[1] != 2:
        raise ValueError("plot_dataset expects exactly two features")
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolor="white", s=45)
    ax.set(xlabel="$x_1$", ylabel="$x_2$", title=title)
    return ax


def plot_decision_boundary(model, X, y, *, ax=None, title=None, resolution=250):
    """Plot predictions from a fitted classifier over a two-dimensional grid."""
    ax = plot_dataset(X, y, ax=ax, title=title)
    padding = 0.6
    x1 = np.linspace(X[:, 0].min() - padding, X[:, 0].max() + padding, resolution)
    x2 = np.linspace(X[:, 1].min() - padding, X[:, 1].max() + padding, resolution)
    xx1, xx2 = np.meshgrid(x1, x2)
    grid = np.column_stack((xx1.ravel(), xx2.ravel()))
    prediction = model.predict(grid).reshape(xx1.shape)
    ax.contourf(xx1, xx2, prediction, alpha=0.18, cmap="coolwarm")
    ax.contour(xx1, xx2, prediction, levels=[0.5], colors="black", linewidths=2)
    return ax
