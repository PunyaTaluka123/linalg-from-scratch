# Linear Algebra from Scratch

An educational Python project for implementing core linear algebra operations and exploring how matrices transform the plane.

The project includes a small \`Matrix\` and \`Vector\` library, a command-line Matplotlib visualizer, and a Streamlit browser interface.

## Features

### Interactive matrix visualizer

Run the Streamlit app to experiment with a \(2 \times 2\) transformation matrix.

- Change the matrix entries and see the transformed coordinate grid update.
- Visualize the images of the standard basis vectors.
- Inspect the determinant, area-scaling factor, and whether the transformation is singular or reverses orientation.
- See the transformation calculated through the project's own \`Matrix\` and \`Vector\` classes.

### Linear algebra library

Current implementations include:

**Matrices**
- Matrix–matrix and matrix–vector multiplication using \`@\`
- Transpose
- Identity matrix construction
- Frobenius norm
- Trace
- Elementary row operations: swap, scale, and add a multiple of one row to another
- An experimental row-echelon-form (\`ref\`) routine

**Vectors**
- Vector addition
- Scalar multiplication
- Dot product
- \(L_1\) and \(L_2\) norms

### Command-line visualizer

The Matplotlib script asks for the transformed images of the two standard basis vectors and plots the resulting grid.

## Run locally

Python 3.10 or newer is recommended.

1. Clone the repository and enter it:

   \`\`\`bash
   git clone https://github.com/PunyaTaluka123/linalg-from-scratch.git
   cd linalg-from-scratch
   \`\`\`

2. (Recommended) Create and activate a virtual environment:

   **macOS / Linux**
   \`\`\`bash
   python3 -m venv .venv
   source .venv/bin/activate
   \`\`\`

   **Windows PowerShell**
   \`\`\`powershell
   python -m venv .venv
   .\\.venv\\Scripts\\Activate.ps1
   \`\`\`

3. Install dependencies:

   \`\`\`bash
   python -m pip install -r requirements.txt
   \`\`\`

4. Start the interactive browser app:

   \`\`\`bash
   streamlit run app.py
   \`\`\`

   Streamlit will print a local URL, usually [http://localhost:8501](http://localhost:8501). Open it in your browser.

## Run the command-line visualizer

From the repository root:

\`\`\`bash
python matrix_lib/matrix_vis.py
\`\`\`

Enter the coordinates for the transformed \(\mathbf e_1\) and \(\mathbf e_2\) basis vectors when prompted. A Matplotlib window will display the transformed grid.

## Example: use the library

The library is in \`matrix_lib/Vector_Matrix_base.py\`.

\`\`\`python
from matrix_lib.Vector_Matrix_base import Matrix, Vector

A = Matrix([
    [2, 1],
    [0, 3],
])

v = Vector([1, 2])

print((A @ v).components)       # [4, 6]
print(A.transpose().components)
print(A.trace())                # 5
print(v.dot(Vector([3, 4])))    # 11
\`\`\`

## Deploy the browser app

The Streamlit interface can be published using [Streamlit Community Cloud](https://share.streamlit.io/):

1. Sign in with GitHub.
2. Create an app from this repository and select the \`main\` branch.
3. Set the main file path to \`app.py\`.
4. Deploy and share the URL Streamlit provides.

A public hosted URL is not listed here yet; use the local instructions above until deployment is complete.

## Project status

This is a work in progress. Some operations are still experimental. In particular, the current \`Matrix.ref()\` implementation assumes usable diagonal pivots and does not yet handle zero pivots through row pivoting, so it should not be treated as a robust general-purpose row-reduction routine.

The goal is to build the concepts from the ground up and make them easier to understand through interactive experiments.

## Contributing

Suggestions, bug reports, and improvements are welcome. Open an issue to discuss a change, or submit a pull request.

---

Built as a learning project in Python with Matplotlib and Streamlit.
