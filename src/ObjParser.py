from src.CoordMatrix import CoordMatrix
from src.libs.objparser.objparser import AnalyzeObject
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