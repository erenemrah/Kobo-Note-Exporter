#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class OutputGenerator(object):

    def __init__(self, liste):
        self.liste = liste

    def saveAsTxt(self, outputFilePath):
        try:
            file = open(outputFilePath, "a", encoding="utf8")
            for row in self.liste:
                if None not in row:
                    file.write(row[0] + " ~ " + row[2] + "," + timeParse(row[1]))
                    file.write("\n\n")

        except Exception as txtError:
            print("Output txt record error!" + txtError.__str__())

        finally:
            file.close()
            print("txt file exported to " + outputFilePath)

    def saveAsCsv(self, outputFilePath):
        try:
            file = open(outputFilePath, "a", encoding="utf8")
            for row in self.liste:
                if None not in row:
                    file.write(row[0] + "," + row[2] + "," + timeParse(row[1]))
                    file.write("\n")

        except Exception as csvError:
            print("Output csv record error!" + csvError.__str__())

        finally:
            file.close()
            print("csv file exported to " + outputFilePath)


def timeParse(pString):
    pString = str(pString[0:10] + " " + pString[11:19])
    return pString
