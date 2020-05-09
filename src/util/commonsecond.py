from datetime import datetime
import logging

class commonsecond():
    """
    This is class for defining all common functions

    Methods
    -------
    stringToDate()
        Converts date string list to datetime objects

    dateToString()
        Converts datetime object to date string format
    """

    def stringToDate(self, date_strings: list) -> list:
        """
        Iterate list of strings and converts into datetime objects of each date string
        :param date_strings: list of strings
        :return: list
        """
        date_objs = []
        try:
            if isinstance(date_strings, list) == False:
                return date_objs

            date_objs = list(map(lambda date_string: datetime.strptime(date_strings, '%d %b %Y'), date_strings))
            return date_objs
        except Exception as e:
            logging.error(e)

    def dateToString(self, date_objs: list) -> list:
        """
        Iterate list of datetime objects into dates of string format
        :param date_objs: list of datetime objects
        :return: list
        """
        date_strings = []
        try:
            if isinstance(date_objs, list) == False:
                return date_strings

            date_strings = list(map(lambda date_obj: datetime.strftime(date_obj, '%d %b %Y'), date_objs))
            return date_strings
        except Exception as e:
            logging.error(e)

    def sortedDates(self, date_strings: list) -> list:
        result = []
        try:
            if isinstance(date_strings, list) == False:
                return result

            result = list(map(lambda date_obj: datetime.strftime(date_obj, '%b %d %Y'), sorted(list(map(lambda date_string: datetime.strptime(date_string, '%d %b %Y'), date_strings)))))
            return result
        except Exception as e:
            logging.error(e)