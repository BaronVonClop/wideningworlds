def start(caller):
	caller.ndb._menutree.buildingname = "None"
	caller.ndb._menutree.buildingdesc = "None"
	caller.ndb._menutree.buildingtheme = "None"
	caller.ndb._menutree.agreestoterms = "No"
	caller.ndb._menutree.additionalnotes = "None"
	caller.ndb._menutree.buildingscope = "None"
	caller.ndb._menutree.tempticketnumber = 0
	caller.ndb._menutree.status = "none"
	caller.ndb._menutree.valid = 0
	text = \
	"""
	Welcome to the builder application review program! This is for wizards to review applications and either approve or deny them.
	"""
	
	
	options = ({"desc": "View applications.",
				"goto": "view_app"})
				
	return text, options
	
def view_app(caller):
	text = \
	"""
	|500BUILDER APPLICATIONS|n
	"""
	x = 1
	target = caller.search("builderapps", global_search=True)
	numtickets = target.db.appnum

	while (x <= numtickets - 1):
		if target.db.appdict["status%i" % x] == "OPEN":
			text +="|/#%i" % x
			x += 1
		else:
			x += 1


	text += "|/Type the number you want to see, or 'quit' to exit."
	options = ({"key": "_default",
				"exec": _save_num,
				"goto": "view_got_ticket"})
				

	return text, options
	
def view_got_ticket(caller):
	text = \
	"""
	"""
	target = caller.search("builderapps", global_search=True)
	
	text += "Applying Character: %s" % target.db.appdict["author%s" % caller.ndb._menutree.num]
	text += "|/|/|050Building Name:|n %s" % target.db.appdict["buildingname%s" % caller.ndb._menutree.num]
	text += "|/|/|050Building Theme:|n %s" % target.db.appdict["buildingtheme%s" % caller.ndb._menutree.num]
	text += "|/|/|050Building Scope:|n %s" % target.db.appdict["buildingscope%s" % caller.ndb._menutree.num]
	text += "|/|/|050Example Description:|n %s" % target.db.appdict["buildingdesc%s" % caller.ndb._menutree.num]
	text += "|/|/|050Agrees to terms:|n %s" % target.db.appdict["agreestoterms%s" % caller.ndb._menutree.num]
	text += "|/|/|050Additional Notes:|n %s" % target.db.appdict["additionalnotes%s" % caller.ndb._menutree.num]
	text += "|/|/|050Wizard Comments:|n %s" % target.db.appdict["comments%s" % caller.ndb._menutree.num]
	
	options = ({"desc": "Add comment.",
				"goto": "add_comment"},
				{"desc": "Approve request.",
				"exec": _approve_request,
				"goto": "start"},
				{"desc": "Deny request.",
				"exec": _deny_request,
				"goto": "start"})
				
	return text, options
	
def add_comment(caller):
	text = \
	"""
	Add a comment. You must add a comment before closing the ticket.
	"""
	
	options = ({"key": "_default",
				"exec": _add_comment,
				"goto": "view_got_ticket"})
	return text, options
	
def _add_comment(caller, raw_string):
	target = caller.search("builderapps", global_search=True)
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter a body!")
	else:
		target.db.appdict["comments%s" % caller.ndb._menutree.num] += ("|/COMMENT: %s" % inp + " - BY %s" % caller)
		caller.msg("Comment added.")
		caller.ndb._menutree.commadded = 1
		
def _approve_request(caller, raw_string):
	target = caller.search("builderapps", global_search=True)
	if caller.ndb._menutree.commadded != 1:
		caller.msg("You haven't added a comment.")
	else:
		target.db.appdict["status%s" % caller.ndb._menutree.num] += "APPROVED"
		caller.msg("Approved. You should now set the builder bit on the player.")
def _deny_request(caller, raw_string):
	target = caller.search("builderapps", global_search=True)
	if caller.ndb._menutree.commadded != 1:
		caller.msg("You haven't added a comment.")
	else:
		target.db.appdict["status%s" % caller.ndb._menutree.num] += "DENIED"
		caller.msg("Denied. You're finished!")
	
def _save_num(caller, raw_string):

	inp = raw_string.strip()
	
	caller.ndb._menutree.num = inp