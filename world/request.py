from evennia.utils.evtable import EvTable
from time import gmtime, strftime

def start(caller):
	caller.ndb._menutree.title = "BLANK"
	caller.ndb._menutree.body = "BLANK"
	caller.ndb._menutree.time = "BLANK"
	caller.ndb._menutree.valid = "No"
	caller.ndb._menutree.tempticketnumber = 0
	text = \
	"""
	Welcome to the request system.
	
	This is used to submit trouble or issue tickets to wizards, who can then address the problem you're having.
	
	What would you like to do?
	
	Type "QUIT" to exit.
	"""
	
	options = ({"desc": "Open a new ticket.",
				"goto": "open_ticket"},
				{"desc": "View, edit or close one of my open tickets.",
				"goto": "view_open_tickets"},
				{"desc": "View my closed tickets.",
				"goto": "view_closed_tickets"})
				
	return text, options
	
def view_open_tickets(caller):
	text = \
	"""
	|500OPEN TICKETS|n
	
	You currently have the following tickets open:
	"""
	numtickets = len(caller.db.requestsmade)
	x = 1
	
	while (x <= numtickets):
		text +="|/#%i:" % caller.db.requestsmade[x-1]
		x += 1
	text += "|/Type the number you want to see, or 'quit' to exit."
	options = ({"key": "_default",
				"exec": _get_ticket,
				"goto": "view_got_ticket"})
				
	return text, options
	
def view_closed_tickets(caller):
	text = \
	"""
	|500CLOSED TICKETS|n
	
	Your following tickets have been closed:
	"""
	numtickets = len(caller.db.requestsclosed)
	x = 1
	
	while (x <= numtickets):
		text +="|/#%s:" % caller.db.requestsclosed[x-1]
		x += 1
	text += "|/Type the number you want to see, or 'quit' to exit."
	options = ({"key": "_default",
				"exec": _get_ticket,
				"goto": "view_got_closed_ticket"})
				
	return text, options
	
def open_ticket(caller):
	text = \
	"""
	|500OPEN NEW TICKET|n
	
	Alright! Let's open a ticket, then.
	
	Type "QUIT" to exit without submitting and discard changes.
	"""
	
	text += "|/Your ticket's current info is:"
	text += "|/|/Title: %s" % caller.ndb._menutree.title
	text += "|/|/Body: %s" % caller.ndb._menutree.body
	options = ({"desc": "Edit Title.",
				"goto": "edittitle"},
				{"desc": "Edit body.",
				"goto": "editbody"},
				{"desc": "Submit ticket.",
				"exec": _create_ticket,
				"goto": "start"})
				
	return text, options
	
def view_got_ticket(caller):
	text = \
	"""
	|500VIEW TICKET|n
	"""
	if caller.ndb._menutree.valid == "Yes":
		text += "|/|/Here is the status of your open ticket, #%s:" %caller.ndb._menutree.tempticketnumber
		text += "|/|/Your ticket's current info is:"
		text += "|/|/Title: %s" % caller.ndb._menutree.title
		text += "|/|/Body: %s" % caller.ndb._menutree.body
		text += "|/|/Time submitted: %s" % caller.ndb._menutree.time
		text += "|/|/Type 'QUIT' to discard changes and exit."
		options = ({"desc": "Edit Title.",
					"goto": "editopentitle"},
					{"desc": "Add comment.",
					"goto": "addcomment"},
					{"desc": "Submit edits.",
					"exec": _edit_ticket,
					"goto": "start"},
					{"desc": "Close ticket.",
					"exec": _close_ticket,
					"goto": "start"})
	if caller.ndb._menutree.valid == "No":
		text += "|/|/That ticket number isn't valid. Please try again."
		text += "|/|/Press any key to continue."
		options = ({"key": "_default",
					"goto": "view_open_tickets"})
				
	return text, options
	
def view_got_closed_ticket(caller):
	text = \
	"""
	|500VIEW TICKET|n
	"""
	text += "|/|/Here was the info of your closed ticket, #%s:" %caller.ndb._menutree.tempticketnumber
	text += "|/|/Title: %s" % caller.ndb._menutree.title
	text += "|/|/Body: %s" % caller.ndb._menutree.body
	options = ({"desc": "Back.",
				"goto": "start"})
				
	return text, options
	
#add comment to open ticket
def addcomment(caller):
	text = \
	"""
	|500ADD COMMENT|n
	
	This will add a comment to your ticket.
	
	Use this for things like new info, or if you've been asked to by a Wizard.
	
	To cancel, type QUIT.
	"""
	options = ({"key": "_default",
				"exec": _add_comment,
				"goto": "view_got_ticket"})
	return text, options
	
	
#edit an open ticket's title
def editopentitle(caller):
	text = \
	"""
	Enter the title for your ticket.
	
	Be clear and concice on what your issue is.
	
	This is only a TITLE; save the details for the description!
	"""
	
	options = ({"key": "_default",
				"exec": _set_title,
				"goto": "view_got_ticket"})
	return text, options
	
	
#edit a new ticket's title
def edittitle(caller):
	text = \
	"""
	Enter the title for your ticket.
	
	Be clear and concice on what your issue is.
	
	This is only a TITLE; save the details for the description!
	"""
	
	options = ({"key": "_default",
				"exec": _set_title,
				"goto": "open_ticket"})
	return text, options
	
#edit a new ticket's body
def editbody(caller):
	text = \
	"""
	Enter the body for your ticket.
	
	Here you can give as much detail as you like! Screenshots, etc.
	
	Please note that if you are reporting a bug in code, you should submit an issue on github instead.
	"""
	
	options = ({"key": "_default",
				"exec": _set_body,
				"goto": "open_ticket"})
	return text, options
	
#pull info for ticket from view
def _get_ticket(caller, raw_string):
	inp = raw_string.strip()
	target = caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
	caller.ndb._menutree.tempticketnumber = inp

	#check if player is ticket owner, if not then reject
	try:
		if not caller == target.db.requestdict["reqauthor%s" % inp]:
			caller.msg("That's not your ticket! Only wizards can see other player's tickets.")
			caller.ndb._menutree.valid == "No"
			
	except KeyError:
		caller.msg("That's not a valid ticket number.")
		caller.ndb._menutree.valid = "No"
		return
		
	#if player is ticket owner, pull the info for it
	if caller == target.db.requestdict["reqauthor%s" % inp]:
		caller.ndb._menutree.valid = "Yes"
		caller.ndb._menutree.title = (target.db.requestdict["reqtitle%s" % inp])
		caller.ndb._menutree.body = (target.db.requestdict["reqtext%s" % inp])
		caller.ndb._menutree.time = (target.db.requestdict["reqtime%s" % inp])
		
	
#set the title
def _set_title(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter a title!")
	else:
		caller.ndb._menutree.title = "%s" % inp
		caller.msg("Title set to %s." % caller.ndb._menutree.title)
		
#set body
def _set_body(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter a body!")
	else:
		caller.ndb._menutree.body = "%s" % inp
		caller.msg("Title set to %s." % caller.ndb._menutree.body)
		
def _add_comment(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter a body!")
	else:
		caller.ndb._menutree.body += ("|/COMMENT: %s" % inp + " - BY %s" % caller)
		caller.msg("Comment added.")
		
#the Big Shit, creating the ticket
def _create_ticket(caller):
	#target master request item
	target = caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
	caller.msg("Submitting your ticket...")
	#If the user tried to submit a ticket with no title or body, reject it
	if caller.ndb._menutree.body == "BLANK" or caller.ndb._menutree.title == "BLANK":
		caller.msg("You tried to submit an unfinished ticket! Try again.")
		return
	else:
		#save body
		(target.db.requestdict["reqtext%i" % target.db.requestnum]) = caller.ndb._menutree.body
		#save title
		(target.db.requestdict["reqtitle%i" % target.db.requestnum]) = caller.ndb._menutree.title
		#set author to the submitter
		(target.db.requestdict["reqauthor%i" % target.db.requestnum]) = caller
		(target.db.requestdict["isclosed%i" % target.db.requestnum]) = 0
		(target.db.requestdict["reqtime%i" % target.db.requestnum]) = strftime("%d %b %H:%M", gmtime())
		#add the ticket number to the author's profile for viewing later
		caller.db.requestsmade.append(target.db.requestnum)
		caller.msg("Your ticket has been submitted as #%i" % target.db.requestnum)
		#increase the number for the next ticket
		target.db.requestnum += 1
		
		
def _edit_ticket(caller):
	#target master request item
	target = caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
	caller.msg("Editing your ticket...")
	#If the user tried to submit a ticket with no title or body, reject it
	if caller.ndb._menutree.body == "BLANK" or caller.ndb._menutree.title == "BLANK":
		caller.msg("You tried to submit an unfinished ticket! Try again.")
		return
	else:
		#save body
		(target.db.requestdict["reqtext%s" % caller.ndb._menutree.tempticketnumber]) = caller.ndb._menutree.body
		#save title
		(target.db.requestdict["reqtitle%s" % caller.ndb._menutree.tempticketnumber]) = caller.ndb._menutree.title
		
def _close_ticket(caller):
	#target master request item
	target = caller.search("request", global_search=True, typeclass="typeclasses.requests.request")
	(target.db.requestdict["isclosed%s" % caller.ndb._menutree.tempticketnumber]) = 1
	caller.ndb._menutree.tempticketnumber = int(caller.ndb._menutree.tempticketnumber)
	caller.db.requestsmade.remove(caller.ndb._menutree.tempticketnumber)
	caller.db.requestsclosed.append(caller.ndb._menutree.tempticketnumber)
	(target.db.requestdict["reqtext%s" % caller.ndb._menutree.tempticketnumber]) += (("|/|/CLOSED BY %s" % caller) + (" ON %s" % strftime("%d %b %H:%M", gmtime())))