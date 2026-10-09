import sys
from pathlib import Path

import matplotlib.pyplot as plt
import streamlit as st

# Import your own linear algebra implementation.
sys.path.insert(
    0,
    str(Path(__file__).parent / "matrix lib")
)

from matrix_lib.Vector_Matrix_base import Matrix, Vector


st.set_page_config(
    page_title="Linear Algebra from Scratch",
    page_icon="📐",
    layout="wide",
)

st.title("Linear Algebra from Scratch")
st.markdown(
    "Explore how a matrix transforms the plane. "
    "Change its entries and watch the grid move."
)

st.sidebar.header("Transformation matrix")

a = st.sidebar.number_input(
    "a", value=1.0, min_value=-3.0, max_value=3.0, step=0.25
)
b = st.sidebar.number_input(
    "b", value=0.0, min_value=-3.0, max_value=3.0, step=0.25
)
c = st.sidebar.number_input(
    "c", value=0.0, min_value=-3.0, max_value=3.0, step=0.25
)
d = st.sidebar.number_input(
    "d", value=1.0, min_value=-3.0, max_value=3.0, step=0.25
)

A = Matrix([
    [a, b],
    [c, d],
])

st.latex(
    rf"A = \begin{{bmatrix}}"
    rf"{a:g} & {b:g} \\ {c:g} & {d:g}"
    rf"\end{{bmatrix}}"
)


def transform(x, y):
    result = A @ Vector([x, y])
    return result[0], result[1]


det = a * d - b * c
col1, col2, col3 = st.columns(3)

col1.metric("Determinant", f"{det:.2f}")
col2.metric("Area scaling", f"{abs(det):.2f}×")

if abs(det) < 1e-9:
    status = "Singular"
elif det < 0:
    status = "Invertible; orientation flips"
else:
    status = "Invertible; orientation preserved"

col3.metric("Transformation", status)


fig, ax = plt.subplots(figsize=(8, 8))
samples = [-5 + i * 0.25 for i in range(41)]

# Original grid, shown in grey.
for k in range(-5, 6):
    ax.plot(samples, [k] * len(samples),
            color="grey", alpha=0.35, linewidth=0.7)
    ax.plot([k] * len(samples), samples,
            color="grey", alpha=0.35, linewidth=0.7)

# Transform each horizontal and vertical grid line
# using your Matrix @ Vector implementation.
for k in range(-5, 6):
    horizontal = [transform(x, k) for x in samples]
    vertical = [transform(k, y) for y in samples]

    ax.plot(
        [p[0] for p in horizontal],
        [p[1] for p in horizontal],
        color="#18A1CD",
        linewidth=0.9,
    )
    ax.plot(
        [p[0] for p in vertical],
        [p[1] for p in vertical],
        color="#18A1CD",
        linewidth=0.9,
    )

# Images of the standard basis vectors.
ax.quiver(
    0, 0, a, c,
    angles="xy", scale_units="xy", scale=1,
    color="#E45756", width=0.009,
)
ax.quiver(
    0, 0, b, d,
    angles="xy", scale_units="xy", scale=1,
    color="#54A24B", width=0.009,
)

# Scale the viewing window to fit the transformed grid.
corners = [
    transform(x, y)
    for x in (-5, 5)
    for y in (-5, 5)
]
extent = max(
    5.5,
    1.1 * max(abs(v) for point in corners for v in point),
)

ax.set_xlim(-extent, extent)
ax.set_ylim(-extent, extent)
ax.set_aspect("equal", adjustable="box")
ax.axhline(0, color="black", linewidth=0.7)
ax.axvline(0, color="black", linewidth=0.7)
ax.set_title("Original grid (grey) → transformed grid (blue)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(alpha=0.15)

st.pyplot(fig)
plt.close(fig)

st.caption(
    "Red: A e₁. Green: A e₂. "
    "Every transformed grid point is calculated using your own classes."
)