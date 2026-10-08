import matplotlib.pyplot as plt

Trans_i1 = float(input("Enter coord 1 of transformed i vector: "))
Trans_i2 = float(input("Enter coord 2 of transformed i vector: "))

Trans_j1 = float(input("Enter coord 1 of transformed j vector: "))
Trans_j2 = float(input("Enter coord 2 of transformed j vector: "))


i_new = [Trans_i1, Trans_i2]
j_new = [Trans_j1, Trans_j2]

def transform(xi, xj):
    xi_new = xi * i_new[0] + xj * j_new[0]
    xj_new = xi * i_new[1] + xj * j_new[1]

    return xi_new, xj_new



fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.grid(True)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

grid_min = -5
grid_max = 5

for x in range(grid_min, grid_max + 1):

    x_values = []
    y_values = []

    for y in range(grid_min, grid_max + 1):

        x_new, y_new = transform(x, y)

        x_values.append(x_new)
        y_values.append(y_new)

    ax.plot(x_values, y_values, linewidth=0.8)


for y in range(grid_min, grid_max + 1):

    x_values = []
    y_values = []

    for x in range(grid_min, grid_max + 1):

        x_new, y_new = transform(x, y)

        x_values.append(x_new)
        y_values.append(y_new)

    ax.plot(x_values, y_values, linewidth=0.8)

ax.quiver(
    0, 0,
    1, 0,
    angles='xy',
    scale_units='xy',
    scale=1
)

ax.quiver(
    0, 0,
    0, 1,
    angles='xy',
    scale_units='xy',
    scale=1
)

ax.quiver(
    0, 0,
    i_new[0], i_new[1],
    angles='xy',
    scale_units='xy',
    scale=1
)

ax.quiver(
    0, 0,
    j_new[0], j_new[1],
    angles='xy',
    scale_units='xy',
    scale=1
)
plt.show()