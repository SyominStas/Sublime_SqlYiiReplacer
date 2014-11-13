import sublime, sublime_plugin

class ReplaceSqlYiiCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		text = "" # all text
		query = "" # all query
		d = {} # dictionaty

		view = self.view
		text = view.substr(sublime.Region(0, view.size())) # get all text from open tab

		selectIndex = text.index("SELECT")
		boundIndex = text.index("Bound with")
		query = text[selectIndex:boundIndex]
		toCheck = text[boundIndex:]

		while (len(toCheck) > 0): 
			ind = toCheck.index(":")
			indt = toCheck.index("=")
			try:
				indf = toCheck.index(",")
			except:
				toFind = toCheck[ind:indt]
				toRepl = toCheck[indt + 1:]
				d[toFind] = toRepl
				break
			toFind = toCheck[ind:indt]
			toRepl = toCheck[indt + 1:indf]
			toCheck = toCheck[indf + 1:]
			d[toFind] = toRepl
		l = 0;
		s = ""
		for mi in d.keys():
			for k in d.keys():
				if len(k) > l:
					l = len(k)
					s = k
			#print(s, l, d[s])
			query = query.replace(s, d[s])
			d.pop(s, None)
			s = ""
			l = 0
		#print(query)
		view.erase(edit, sublime.Region(0, view.size ())) # erase all text
		view.insert(edit, 0, query) # insert replaces query