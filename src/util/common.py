from datetime import datetime
import logging

class common():
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

            for date_string in date_strings:
                    if isinstance(date_string, str) == False:
                        continue
                    date_objs.append(datetime.strptime(date_string, '%d %b %Y'))

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

            for date_obj in date_objs:
                if isinstance(date_obj, datetime) == False:
                    continue
                date_strings.append(datetime.strftime(date_obj, '%d %b %Y'))

            return date_strings
        except Exception as e:
            logging.error(e)