import sublime
import sublime_plugin
import re

class FormatActivitiesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        for sel in view.sel():
            selectedText = self.view.substr(sel)
            result = self.fixActivitiesText(selectedText)

            view.replace(edit, sel, result)


    def isContainTime(self,text):
        return bool(re.search(r'([0-9:\.\-\s]+)(PM|AM)', text))

    def fixActivitiesText(self, text):

        if not text:
            return ""

        timePocket = ''
        lines = text.splitlines()

        results = []
        for line in lines:
            
            if self.isContainTime(line):
                timePocket = line
                #print "time : " + line
                continue

            results.append(line.strip())

            if not self.isContainTime(line) and line.strip() != '' and timePocket != '':
                results.append(timePocket)
                timePocket = ''

        return '\n'.join(results)
