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
	Welcome to the builder application! This is a short application that will grant you a builder bit to build your own location if approved.
	
	Take this seriously! If we feel your descriptions are too lacking, your bit will |500not be granted.|n Have a unique idea, and put your best effort into it!
	
	Be sure to review the building application guidelines on the wiki!
	
	http://wiki.wideningworlds.com/index.php?title=Builder_Application_Guidelines
	"""
	
	
	options = ({"desc": "Open new builder application.",
				"goto": "open_app"},
				{"desc": "View an application.",
				"goto": "view_app"})
				
	return text, options

def open_app(caller):
	text = \
	"""
	|500BUILDER APPLICATION|n
	"""

	text += "Character: %s" % caller.name
	text += "|/|/|050Building Name:|n %s" % caller.ndb._menutree.buildingname
	text += "|/|/|050Building Theme:|n %s" % caller.ndb._menutree.buildingtheme
	text += "|/|/|050Building Scope:|n %s" % caller.ndb._menutree.buildingscope
	text += "|/|/|050Example Description:|n %s" % caller.ndb._menutree.buildingdesc
	text += "|/|/|050Agrees to terms:|n %s" % caller.ndb._menutree.agreestoterms
	text += "|/|/|050Additional Notes:|n %s" % caller.ndb._menutree.additionalnotes
	
	options = ({"desc": "Edit name.",
				"goto": "edit_name"},
				{"desc": "Edit theme.",
				"goto": "edit_theme"},
				{"desc": "Edit scope.",
				"goto": "edit_scope"},
				{"desc": "Edit description.",
				"goto": "edit_desc"},
				{"desc": "Edit additional notes.",
				"goto": "edit_notes"},
				{"desc": "Review terms.",
				"goto": "review_terms"},
				{"desc": "Submit application!",
				"goto": "submit_app"})

	return text, options
	
	
def view_app(caller):
	text = \
	"""
	|500BUILDER APPLICATIONS|n
	
	You own the following applications:
	"""
	x = 1
	
	numtickets = len(caller.db.buildingappsopen)
	try:
		while (x <= numtickets):
			text +="|/#%i: |/" % caller.db.buildingappsopen[x-1]
			x += 1
		text += "|/Type the number you want to see, or 'quit' to exit."
		options = ({"key": "_default",
					"exec": _get_ticket,
					"goto": "view_got_ticket"})
				
	except TypeError:
		text+= "You have no submitted tickets."
		options = ({"desc": "Go back.",
					"goto": "start"})

	return text, options
	
def _get_ticket(caller, raw_string):
	inp = raw_string.strip()
	target = caller.search("builderapps", global_search=True)
	caller.ndb._menutree.tempticketnumber = inp
	
	try:
		caller.ndb._menutree.status = target.db.appdict["status%s" % inp]
		caller.ndb._menutree.additionalnotes = target.db.appdict["comments%s" % inp]
		caller.ndb._menutree.valid = 1
		return
	except KeyError:
		caller.msg("That isn't a valid number.")

def view_got_ticket(caller):
	text = \
	"""
	|500BUILDER APPLICATIONS|n
	"""
	if caller.ndb._menutree.valid == 1:
		text += "|/Status of application #%s: " % caller.ndb._menutree.tempticketnumber + "%s" % caller.ndb._menutree.status
		text += "|/|/Comments made: %s" % caller.ndb._menutree.additionalnotes
		options = ({"desc": "Go back.",
					"goto": "start"})
	if caller.ndb._menutree.valid == 0:
		text+= "That isn't a valid number."
		options = ({"desc": "Go back.",
					"goto": "start"})

	return text, options
	
	
def edit_name(caller):
	text = \
	"""
	What are you going to name your new location?
	"""
	
	options = ({"key": "_default",
			"exec": _edit_name,
			"goto": "open_app"})
			
	return text, options
			
def _edit_name(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("|500You didn't enter anything!")
	else:
		caller.ndb._menutree.buildingname = inp
		
def edit_theme(caller):
	text = \
	"""
	Describe the theme of your new location. Discuss the focus of the building's roleplay, as well as the asthetic of the area.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_theme,
			"goto": "open_app"})
			
	return text, options
			
def _edit_theme(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("|500You didn't enter anything!")
	else:
		caller.ndb._menutree.buildingtheme = inp
		
def edit_scope(caller):
	text = \
	"""
	Describe the scope of your location. How many rooms is this going to be? Is it just a single business, just a home for yourself, or an entire area? A whole town?
	"""
	
	options = ({"key": "_default",
			"exec": _edit_scope,
			"goto": "open_app"})
			
	return text, options
			
def _edit_scope(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("|500You didn't enter anything!")
	else:
		caller.ndb._menutree.buildingscope = inp
		
def edit_desc(caller):
	text = \
	"""
	This is arguably the most important part of your application! Put a good amount effort into this.
	
	Describe the "main" room of your building. This will be either the main hang-out room for people IC, or if there isn't one, a room of your choice.
	
	Remember, we are not judging on |500length|n, we are judging on |500quality|n. Someone who writes one well-done paragraph will have a much better chance of approval than someone who writes six long paragraphs of nothing but purple prose.
	
	Don't forget, use "||/" for a line break if needed!
	"""
	
	options = ({"key": "_default",
			"exec": _edit_desc,
			"goto": "open_app"})
			
	return text, options
			
def _edit_desc(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("|500You didn't enter anything!")
	else:
		caller.ndb._menutree.buildingdesc = inp
		
def edit_notes(caller):
	text = \
	"""
	If you have additional notes that you would like us to consider when reviewing your app, post them here.
	
	This field is optional.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_notes,
			"goto": "open_app"})
			
	return text, options
			
def _edit_notes(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("|500You didn't enter anything!")
	else:
		caller.ndb._menutree.additionalnotes = inp
		
def review_terms(caller):
	text = \
	"""
	Please review the builder rules and terms.
	
	http://wiki.wideningworlds.com/index.php?title=Builder_Rules
	
	To agree to these terms, enter the passphrase.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_terms,
			"goto": "open_app"})
			
	return text, options
			
def _edit_terms(caller, raw_string):
	inp = raw_string.strip()
	if inp != "nanners":
		caller.msg("|500Incorrect passphrase. Please review the builder rules and terms for the passphrase and try again.")
	else:
		caller.ndb._menutree.agreestoterms = "YES"
		
def submit_app(caller):
	text = \
	"""
	Are you ready to submit?
	"""
	
	options = ({"desc": "Yes",
			"exec": _submit_app,
			"goto": "start"},
			{"desc": "No",
			"goto": "open_app"})
			
	return text, options
	
def _submit_app(caller, raw_string):
	caller.msg("Submitting your application.")
	target = caller.search("builderapps", global_search=True)
	num = target.db.appnum
	target.db.appdict["buildingname%i" % num] = caller.ndb._menutree.buildingname
	target.db.appdict["buildingdesc%i" % num] = caller.ndb._menutree.buildingdesc
	target.db.appdict["buildingtheme%i" % num] = caller.ndb._menutree.buildingtheme
	target.db.appdict["agreestoterms%i" % num] = caller.ndb._menutree.agreestoterms
	target.db.appdict["additionalnotes%i" % num] = caller.ndb._menutree.additionalnotes
	target.db.appdict["buildingscope%i" % num] = caller.ndb._menutree.buildingscope
	target.db.appdict["status%i" % num] = "OPEN"
	target.db.appdict["author%i" % num] = caller
	target.db.appdict["comments%i" % num] = ""
	target.db.appnum += 1
	caller.db.buildingappsopen.append(num)
	caller.msg("Your builder application has been submitted as #%i." % num)