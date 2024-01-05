#! usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


class KoboDBConnector:
    # Kobo Db connector class
    def __init__(self, dbFile):
        self.dbFile = dbFile

    def show(self):
        print(self.dbFile)

    def getData(self, bookTitle):
        # connect db and get data
        try:
            sqliteConnection = sqlite3.connect(self.dbFile)
            cursor = sqliteConnection.cursor()
            cursor.execute('select Bookmark.Text,Bookmark.DateModified,content.BookTitle from Bookmark, content WHERE Bookmark.ContentID = content.ContentID AND content.BookTitle like "%' + bookTitle + '%" ORDER by Bookmark.DateModified;')
            data = cursor.fetchall()
            cursor.close()
            return data

        except sqlite3.Error as e:
            print("DB error!")

        finally:
            sqliteConnection.close()

    def getAllData(self):

        try:
            # connect db and get all data
            sqliteConnection = sqlite3.connect(self.dbFile)
            cursor = sqliteConnection.cursor()
            cursor.execute('select Bookmark.Text,Bookmark.DateModified,content.BookTitle from Bookmark, content WHERE Bookmark.ContentID = content.ContentID ORDER by content.BookTitle,Bookmark.DateModified;')
            data = cursor.fetchall()
            cursor.close()
            return data

        except:
            print("DB error!")

        finally:
            sqliteConnection.close()
