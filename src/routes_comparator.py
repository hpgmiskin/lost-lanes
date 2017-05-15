import shapely.geometry

class ErrorCalculator:
    def __init__(self):
        pass
    def calculate_error(self,distances):
        error = sum([
            pow(distance,2)/len(distances)
            for distance in distances
        ])
        return error

class RoutesComparator:

    def __init__(self,Point=shapely.geometry.Point,Line=shapely.geometry.LineString):
        self.Point = Point
        self.Line = Line

    def compare_routes(self,route_1,route_2,error_calculator=ErrorCalculator()):
        """
        Compares two routes and returns the mean square error between them
        http://toblerity.org/shapely/manual.html#object.project
        """

        distances = []
        route_2_line = self.Line(route_2)

        for route_1_point in route_1:
            route_1_point = self.Point(route_1_point)
            distance = route_2_line.project(route_1_point)
            distances.append(distance)
            
        return error_calculator.calculate_error(distances)

if (__name__ == "__main__"):
    from route_importer import RouteImporter

    route_importer = RouteImporter()
    route_1 = route_importer.import_route('data/30WW.gpx')
    route_2 = route_importer.import_route('data/30WW.gpx')

    routes_compartor = RoutesComparator()
    error = routes_compartor.compare_routes(route_1,route_2)
    print("There was {} error between route 1 and route 2".format(error))