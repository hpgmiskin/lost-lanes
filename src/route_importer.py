import gpxpy

class RouteImporter:

    def __init__(self,parser=gpxpy.parse,debug=False):
        self.parser = parser
        self.debug = debug

    def import_route(self,filename):

        gpx_file = open(filename, 'r')
        gpx = gpxpy.parse(gpx_file)
        if (self.debug): self.print_information(gpx)
        points = [
            ( point.latitude, point.longitude )
            for point,_,_,index in gpx.walk()
        ]
        return points

    def print_information(self,gpx):

        print(dir(gpx))
        for point in gpx.walk():
            print(point,len(point))
        return
        print("There are {} tracks, {} waypoints and {} routes".format(len(gpx.tracks),len(gpx.waypoints),len(gpx.routes)))

        for track in gpx.tracks:
            print('There are {} segments'.format(len(track.segments)))
            for segment in track.segments:
                print('There are {} points'.format(len(segment.points)))
                for point in segment.points:
                    print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

        for waypoint in gpx.waypoints:
            print('waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude))
            
        for route in gpx.routes:
            print('Route:')
            for point in route.points:
                print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))


if (__name__ == "__main__"):
    route_importer = RouteImporter()
    route = route_importer.import_route('data/30WW.gpx')
    print(route)