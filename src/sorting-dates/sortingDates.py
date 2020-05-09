import logging
from src.util.common import common
from src.util.exception import dateObjectIsEmpty

"""
This module is for starting the application
"""
if __name__ == '__main__':
    try:
        dates = ['01 Apr 2017', '01 Apr 2018', '01 Aug 2017', '01 Aug 2018', '01 Dec 2017', '01 Dec 2018', '01 Feb 2017', '01 Feb 2018', '01 Jan 2017', '01 Jan 2018']
        commonObj = common()
        date_objects = commonObj.stringToDate(dates)
        if not date_objects:
            raise dateObjectIsEmpty
        sortedDateObjects = sorted(date_objects)
        result = commonObj.dateToString(sortedDateObjects)
        print("Result of Sorting Dates are {} ". format(result))
    except Exception as e:
        logging.error(e)