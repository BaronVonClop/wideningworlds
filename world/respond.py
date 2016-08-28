def start(caller):
	caller.ndb._menutree.title = "BLANK"
	caller.ndb._menutree.body = "BLANK"
	caller.ndb._menutree.author = "BLANK"
	caller.ndb._menutree.commadded = 0
	caller.ndb._menutree.tempticketnumber = 0
	text = \
	"""
	Welcome to the request system.
	
	What would you like to do?
	
	Type "QUIT" to exit.
	"""
	
	options = ({"desc": "View open tickets.",
				"goto": "view_open_tickets"},
				{"desc": "View closed tickets.",
				"goto": "view_closed_tickets"})
				
	return text, options
	
def view_open_tickets(caller):
	text = \
	"""
	|500OPEN TICKETS|n
	
	The following tickets are open:
	"""
	target = caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
	numtickets = target.db.requestnum
	x = 1
	while (x < numtickets):
		if target.db.requestdict["isclosed%s" % x] == 0:
			text +="|/#%i:" % x
			x += 1
		else:
			x += 1
	text += "|/Type the number you want to see, or 'quit' to exit."
	options = ({"key": "_default",
				"exec": _get_ticket,
				"goto": "view_got_ticket"})
				
	return text, options
	
def view_closed_tickets(caller):
	text = \
	"""
	|500OPEN TICKETS|n
	
	The following tickets are open:
	"""
	target = caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
	numtickets = target.db.requestnum
	x = 1
	while (x < numtickets):
		if target.db.requestdict["isclosed%s" % x] == 1:
			text +="|/#%i:" % x
			x += 1
		else:
			x += 1
	text += "|/Type the number you want to see, or 'quit' to exit."
	options = ({"key": "_default",
				"exec": _get_ticket,
				"goto": "view_got_closed_ticket"})
				
	return text, options
	
def view_got_closed_ticket(caller):
	text = \
	"""
	|500VIEW TICKET|n
	"""
	text += "|/|/Here is the status of closed ticket #%s:" % caller.ndb._menutree.tempticketnumber
	text += "|/|/This ticket's current info is:"
	text += "|/|/Title: %s" % caller.ndb._menutree.title
	text += "|/|/Body: %s" % caller.ndb._menutree.body
	text += "|/|/Type 'QUIT' to discard changes and exit."
	options = ({"key": "_default",
				"goto": "start"})
				
	return text, options
	
def view_got_ticket(caller):
	text = \
	"""
	|500VIEW TICKET|n
	"""
	text += "|/|/Here is the status of open ticket #%s:" % caller.ndb._menutree.tempticketnumber
	text += "|/|/This ticket's current info is:"
	text += "|/|/Submitted by: %s" % caller.ndb._menutree.author
	text += "|/|/Title: %s" % caller.ndb._menutree.title
	text += "|/|/Body: %s" % caller.ndb._menutree.body
	text += "|/|/Type 'QUIT' to discard changes and exit."
	options = ({"desc": "Add comment.",
				"goto": "addcomment"},
				{"desc": "Submit edits.",
				"exec": _edit_ticket,
				"goto": "start"},
				{"desc": "Close ticket.",
				"exec": _close_ticket,
				"goto": "start"})
				
	return text, options
				
def addcomment(caller):
	text = \
	"""
	|500ADD COMMENT|n
	
	This will add a comment to the ticket.
	
	To cancel, type QUIT.
	"""
	options = ({"key": "_default",
				"exec": _add_comment,
				"goto": "view_got_ticket"})
	return text, options
	
def _add_comment(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter a body!")
	else:
		caller.ndb._menutree.body += ("|/COMMENT: %s" % inp + " - BY %s" % caller)
		caller.msg("Comment added.")
		caller.ndb._menutree.commadded += 1
		
		
def _close_ticket(caller):
	#target master request item
	if caller.ndb._menutree.commadded == 0:
		caller.msg("|500!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		caller.msg("|500You need to add a comment before you close the ticket!")
		caller.msg("|500!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	else:
		target = caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
		#mark as closed
		(target.db.requestdict["isclosed%s" % caller.ndb._menutree.tempticketnumber]) = 1
		#add any comments that were made
		(target.db.requestdict["reqtext%s" % caller.ndb._menutree.tempticketnumber]) = caller.ndb._menutree.body
		#downcast number
		caller.ndb._menutree.tempticketnumber = int(caller.ndb._menutree.tempticketnumber)
		#add closed note
		(target.db.requestdict["reqtext%s" % caller.ndb._menutree.tempticketnumber]) += ("|/|/CLOSED BY %s" % caller)
		author = target.db.requestdict["reqauthor%i" % (target.db.requestnum - 1)]
		#target submitting player
		target = caller.search(author, global_search=True, typeclass="typeclasses.characters.Character")
		#move the request from their open to closed list
		target.db.requestsmade.remove(caller.ndb._menutree.tempticketnumber)
		target.db.requestsclosed.append(caller.ndb._menutree.tempticketnumber)
	
				
def _edit_ticket(caller):
	#target master request item
	target = caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
	caller.msg("Editing that ticket...")
	#save body
	(target.db.requestdict["reqtext%s" % caller.ndb._menutree.tempticketnumber]) = caller.ndb._menutree.body
	#save title
	(target.db.requestdict["reqtitle%s" % caller.ndb._menutree.tempticketnumber]) = caller.ndb._menutree.title
	
def _get_ticket(caller, raw_string):
	inp = raw_string.strip()
	target = caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
	caller.ndb._menutree.tempticketnumber = inp
	
	caller.ndb._menutree.title = (target.db.requestdict["reqtitle%s" % inp])
	caller.ndb._menutree.body = (target.db.requestdict["reqtext%s" % inp])
	caller.ndb._menutree.author = (target.db.requestdict["reqauthor%s" % inp])