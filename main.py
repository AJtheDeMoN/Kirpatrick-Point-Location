from algorithm import *
import matplotlib.pyplot as plt

def create_regions():
    regions = []
    region_names = []

    # Define the enclosing triangle
    super_triangle = Polygon((150, 0), (-150, 150), (-150, -150))

    # List to store previously drawn polygons
    drawn_polygons = []

    while True:
        region_name = input("Enter a region name (or 'q' to quit): ")
        if region_name == 'q':
            break

        # Assuming each region is defined as a list of (x, y) points
        points = []

        def onclick(event):
            # Get the x and y coordinates of the click
            x = event.xdata
            y = event.ydata
            if x is not None and y is not None:
                # Append the vertex to the list
                points.append((x, y))

                # Plot the vertex
                plt.plot(x, y, 'bo')
                plt.draw()

        fig, ax = plt.subplots()
        ax.set_title('Click to add polygon vertices')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_xlim(-150, 150)  # Set x-axis limits
        ax.set_ylim(-150, 150)  # Set y-axis limits

        # Plot previously drawn polygons in grey
        for polygon in drawn_polygons:
            for (p1, p2) in polygon.E:
                plt.plot([p1.x, p2.x], [p1.y, p2.y], 'grey')

        # Plot the enclosing triangle by specifying its vertices
        vertices = [(150, 0), (-150, 150), (-150, -150), (150, 0)]
        x, y = zip(*vertices)
        plt.plot(x, y, 'ro-')  # Red line for the enclosing triangle

        # Connect the callback function to the plot
        cid = fig.canvas.mpl_connect('button_press_event', onclick)

        # Show the plot and wait for the user to finish adding vertices
        plt.show()

        if points:
            if len(points) < 3:
                print("A polygon must have at least 3 vertices")
                continue
            new_polygon = Polygon(*points)
            regions.append(new_polygon)
            region_names.append(region_name)
            drawn_polygons.append(new_polygon)
        else:
            break
    return regions, region_names

if __name__ == "__main__":
    regions, region_names = create_regions()
    Algorithm(regions, region_names)
