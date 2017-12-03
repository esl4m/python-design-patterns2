import sqlite3
import types


class DefectModel:
    def getDefectList(self, component):
        query = '''select ID from defects where Component = '%s' ''' % component
        defectlist = self._dbselect(query)
        l = []
        for row in defectlist:
            l.append(row[0])
        return l

    def getSummary(self, id):
        query = '''select summary from defects where ID = '%d' ''' % id
        summary = self._dbselect(query)
        for row in summary:
            return row[0]

    def _dbselect(self, query):
        connection = sqlite3.connect('TMS')

        cursorObj = connection.cursor()
        results = cursorObj.execute(query)
        connection.commit()
        cursorObj.close()
        return results


class DefectView:
    def summary(self, summary, defectid):
        print("#### Defect Summary for defect# %d####\n%s" % (defectid,summary))

    def defectList(self, list, category):
        print ("#### Defect List for %s ####\n" % category)
        for defect in list:
            print(defect)


class Controller:
    def __init__(self):
        pass

    def getDefectSummary(self, defectid):
        model = DefectModel()
        view = DefectView()
        summary_data = model.getSummary(defectid)
        return view.summary(summary_data, defectid)

    def getDefectList(self, component):
        model = DefectModel()
        view = DefectView()
        defectlist_data = model.getDefectList(component)
        return view.defectList(defectlist_data, component)
