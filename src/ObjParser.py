from CoordMatrix import CoordMatrix
from obj_parser.objParser import objFiles
class ObjParser(object):
    def __init__(self,filename):
        self.filename = filename
        self.obj_file = open(filename, "r")
    
    def _parse_header(self):
        
        pass
    def _parse_body(self):
        pass
    
    def get_coord_matrix(self) -> CoordMatrix:
        pass