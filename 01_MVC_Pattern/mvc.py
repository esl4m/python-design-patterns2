import sqlite3


class DefectModel:
    def get_defect_list(self, component):
        query = '''select ID from defects where Component = '%s' ''' % component
        defectlist = self._dbselect(query)
        l = []
        for row in defectlist:
            l.append(row[0])
        return l

    def get_summary(self, id):
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

    def defect_list(self, list, category):
        print ("#### Defect List for %s ####\n" % category)
        for defect in list:
            print(defect)


class Controller:
    def __init__(self):
        pass

    def get_defect_summary(self, defectid):
        model = DefectModel()
        view = DefectView()
        summary_data = model.get_summary(defectid)
        return view.summary(summary_data, defectid)

    def get_defect_list(self, component):
        model = DefectModel()
        view = DefectView()
        defectlist_data = model.get_defect_list(component)
        return view.defect_list(defectlist_data, component)
