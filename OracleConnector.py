# -*- coding: utf-8 -*-

'''
USAGE:
This returns the result as a list of dictionaries
each dictionary contain the column name and value of one row of result
compatible with python 3
__maintainer__ = 'Debaditya'
'''


import cx_Oracle


class opendb(object):

    def __init__(self,dbinfodict={'uname':'apps','password':'password','ip':'10.204.145.18','service':'ECASQAODD'}):
        self.dbinfodict = dbinfodict
        connectionString = '{username}/{password}@{ip}/{service}'.format(
            username=self.dbinfodict['uname'],
            password=self.dbinfodict['password'],
            ip=self.dbinfodict['ip'],
            service=self.dbinfodict['service'])
        self.con = cx_Oracle.connect(connectionString)

    def __enter__(self):
        return self

    def __exit__(self,exc_type, exc_value, traceback):
        if exc_type is not None:
            print(exc_type, exc_value, traceback)
        else:
            self._getresult()
            self._print_result()
            self._close_connection()


    def _getresult(self):
        _list_names = []
        #: list of table column names
        self._all = []
        #: list of all dictionaries : each dictionary is column names and one row of values 
        row = ''
        if not hasattr(self, 'result_dict'):
            self.result_dict = {}
        if self.cur.description is not None:
            for desc in self.cur.description:
                columnName = desc[0]
                _list_names.append(columnName)
            try:
                row, count = self.cur.fetchone(), 1
            except:
                print('sql script failed duet o utf-8')
            while row and count <= self.MAXROWS_TO_FETCH:
                self.result_dict = zip(_list_names,row) 
                #: create tuple of column name: value
                self._all.append(self.result_dict)
                try:
                    row = self.cur.fetchone()
                except:
                    print('this row cannot be retrieved of utf8 issue with script')
                count += 1

    def _print_result(self):
        count = 1
        for result in self._all:
            print('Fetching Result no : %d' % (count))
            print('-' * 40)
            for (k, v) in result:
                print('-' * 40)
                print('%s -> %s ' % (k, repr(v)))

            count +=1
        print('-' * 40)
        print('Total results : %d' % (count-1))
        print('-' * 40)

    def _close_connection(self):
        self.con.close()

    def commit(self):
        self.con.commit()

    def executeQuery(self, querystring, no_of_records=10):
        self.MAXROWS_TO_FETCH = no_of_records
        self.querystring = querystring
        print('Query String :::')
        print(self.querystring)
        self.cur = self.con.cursor()
        self.cur.execute(self.querystring)
        return self._all

if __name__ == "__main__":
    with opendb() as c:
        c.executeQuery("select some_col from some_table", 1)
