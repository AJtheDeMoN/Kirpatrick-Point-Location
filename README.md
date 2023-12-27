# Kirpatrick Point Location

## Description

Kirkpatrick gives a data structure for point location in triangulated subdivisions with O(n) storage space and O(log n) query time. The general idea is to build a hierarchy of triangles. To perform a query, we start by finding the top-level triangle that contains the query point.

## How it Works

1. The user is prompted to enter a region name and vertices.
2. Vertices are processed, and some may be removed based on certain conditions.
3. The program then asks the user to input coordinates for a point to check if it lies within a region.
4. The result is printed, indicating whether the point is in the region or not.
5. The user is given the option to continue or exit the program.

## Example Output

```plaintext
Enter a region name (or 'q' to quit): R1
Enter a region name (or 'q' to quit): q
Vertices: [(-100.80645161290323, 72.29437229437224), (-107.25806451612904, 37.66233766233765), (-64.9193548387097, 59.848484848484816), (-79.03225806451614, 80.9523809523809)]
Removing vertex: (-79.03225806451614, 80.9523809523809)
Independent points: [(-64.9193548387097, 59.848484848484816), (150, 0), (-150, 150), (-100.80645161290323, 72.29437229437224)]
Removing vertex: (-107.25806451612904, 37.66233766233765)
Independent points: [(-64.9193548387097, 59.848484848484816), (-100.80645161290323, 72.29437229437224), (-150, 150), (-150, -150)]
Removing vertex: (-100.80645161290323, 72.29437229437224)
Independent points: [(-64.9193548387097, 59.848484848484816), (150, 0), (-150, 150), (-150, -150)]
Enter the coordinates of the point to search: 0 1
Point lies in the region: External Region
Enter 1 to continue the program or -1 to exit: 1
Enter the coordinates of the point to search: 0 0
Point lies in the region: External Region
Enter 1 to continue the program or -1 to exit: -1
```


## Getting Started

Follow these steps to run the project on your local machine:

1. Ensure you have Python installed on your system.

2. Install the required dependencies using the following command:

   ```bash
   pip install matplotlib
   pip install copy
   pip install numpy
   ```
3. Unzip the project repository.

4. Navigate to the project directory:
   ```bash
   cd your-project
   ```
5. Run the main file:
   ```bash
   python main.py
   ```
