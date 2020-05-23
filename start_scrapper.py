import sys
from rightmove_webscraper import RightmoveData

RightmoveData(str(sys.argv[0]), get_date_available=True)

exit(0)