from hierarchy import *
import copy

def polygen_plot(P: Polygon, ocol="k-", show=True):
    for (p1, p2) in P.E:
        plt.plot([p1.x, p2.x], [p1.y, p2.y], ocol)
    if show:
        plt.show()

def polygens_plot(T: set[Polygon], show=False):
    for poly in T:
        polygen_plot(poly, show=False)

def Algorithm(regions: list[Polygon], region_names: list[str]):
    
    H = Kirkpatrick()   #Define the hierarchy object
    tri = []    #List to store the triangulations

    for region, name in zip(regions, region_names):
        H.add_region(region, name)
    
    H.triangulate()
    tri.append(copy.deepcopy(H.delaunay))

    while (len(H.delaunay) > 3):

        tri.append(copy.deepcopy(H.delaunay))
        polygens_plot(H.delaunay)
        for polygon in H.polygons: polygen_plot(polygon, 'r-', show=False)
        plt.show()

        independent_set = H.select_independent_set()

        for vertex in independent_set:
            print(f"Removing vertex : {vertex}")
            H.remove_point(vertex)

     
    tri.append(copy.deepcopy(H.delaunay))
    tri.reverse()
    polygens_plot(H.delaunay)
    for polygon in H.polygons: polygen_plot(polygon, 'r-', show=False)
    plt.show()


    while (True):
        print("Enter the coordinates of the point to search: ")
        [x, y] = map(float,input().split())
        print("Point lies in the region: ", H.search_point(Point(x, y),tri))
        z = input("Enter 1 to continue the program or -1 to exit: ")
        if(z == '-1'):
            break
