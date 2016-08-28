def start(caller):
	text = \
	"""
	Welcome to editplayer. This is a guided tool to set up your at-a-glance profile and your 'look' description.
	
	If you're a new character, this will be looked at before approval, so be sure you are putting in your best effort!
	
	What would you like to do?
	
	Your current profile:
	
	"""
	text += "%(1)s the %(2)s %(3)s" % {"1" : caller.name, "2" : caller.db.gender, "3" : caller.db.race}
	text += "|/AGE: %s" % caller.db.age
	text += "|/HEIGHT: %s" % caller.db.height
	text += "|/WEIGHT: %s" % caller.db.weight
	text += "|/COAT/SKIN: %s" % caller.db.coat
	text += "|/HAIR: %s" % caller.db.hair
	text += "|/PROFESSION: %s" % caller.db.occupation
	text += "|/Description: |/%s" % caller.db.desc
	text += "|/|/When you are complete, type 'QUIT'."
	
	
	options = ({"desc": "Edit gender.",
				"goto": "edit_gender"},
				{"desc": "Edit race.",
				"goto": "edit_race"},
				{"desc": "Edit age.",
				"goto": "edit_age"},
				{"desc": "Edit height.",
				"goto": "edit_height"},
				{"desc": "Edit weight.",
				"goto": "edit_weight"},
				{"desc": "Edit coat/skin.",
				"goto": "edit_coat"},
				{"desc": "Edit hair.",
				"goto": "edit_hair"},
				{"desc": "Edit profession.",
				"goto": "edit_profession"},
				{"desc": "Edit description.",
				"goto": "edit_desc"})
				
	return text, options
	
def edit_gender(caller):
	text = \
	"""
	Editing your gender.
	
	Type what you want your gender to appear as.
	
	Must be 20 or less characters.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_gender,
			"goto": "start"})
			
	return text, options
	
def _edit_gender(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter a body!")
	else:
		if len(inp) <= 20:
			caller.db.gender = inp
		else:
			caller.msg("Too long. Must be under 20 characters.")
			
def edit_race(caller):
	text = \
	"""
	Editing your race.
	
	Type what you want your gender to appear as.
	
	Please check the wiki for the available races if you are playing a non-standard pony. Outlandish things may result in failing approval!
	"""
	
	options = ({"key": "_default",
			"exec": _edit_race,
			"goto": "start"})
			
	return text, options
	
def _edit_race(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter anything!")
	else:
		if len(inp) <= 20:
			caller.db.race = inp
		else:
			caller.msg("Too long. Must be under 20 characters.")
			
def edit_age(caller):
	text = \
	"""
	Editing your age.
	
	Type what you want your age to appear as.
	
	Must be under 4 characters.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_age,
			"goto": "start"})
			
	return text, options
	
def _edit_age(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter anything!")
	else:
		if len(inp) <= 4:
			caller.db.age = inp
		else:
			caller.msg("Too long. Must be under 4 characters.")
			
def edit_height(caller):
	text = \
	"""
	Editing your height.
	
	Type what you want your height to appear as.
	
	Must be 20 or less characters.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_height,
			"goto": "start"})
			
	return text, options
	
def _edit_height(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter anything!")
	else:
		if len(inp) <= 20:
			caller.db.height = inp
		else:
			caller.msg("Too long. Must be under 20 characters.")
			
def edit_weight(caller):
	text = \
	"""
	Editing your weight.
	
	Type what you want your weight to appear as.
	
	Must be 20 or less characters.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_weight,
			"goto": "start"})
			
	return text, options
	
def _edit_weight(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter anything!")
	else:
		if len(inp) <= 20:
			caller.db.weight = inp
		else:
			caller.msg("Too long. Must be under 20 characters.")
			
def edit_coat(caller):
	text = \
	"""
	Editing your coat.
	
	Type what you want your coat or skin to appear as.
	
	Must be 20 or less characters.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_coat,
			"goto": "start"})
			
	return text, options
	
def _edit_coat(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter anything!")
	else:
		if len(inp) <= 20:
			caller.db.coat = inp
		else:
			caller.msg("Too long. Must be under 20 characters.")
			
def edit_hair(caller):
	text = \
	"""
	Editing your hair.
	
	Type what you want your hair to appear as.
	
	Must be 20 or less characters.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_hair,
			"goto": "start"})
			
	return text, options
	
def _edit_hair(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter anything!")
	else:
		if len(inp) <= 20:
			caller.db.hair = inp
		else:
			caller.msg("Too long. Must be under 20 characters.")
			
def edit_profession(caller):
	text = \
	"""
	Editing your profession.
	
	Type what you want your profession to appear as.
	
	Must be 20 or less characters.
	"""
	
	options = ({"key": "_default",
			"exec": _edit_profession,
			"goto": "start"})
			
	return text, options
	
def _edit_profession(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter anything!")
	else:
		if len(inp) <= 20:
			caller.db.occupation = inp
		else:
			caller.msg("Too long. Must be under 20 characters.")
			
def edit_desc(caller):
	text = \
	"""
	Editing your description.
	
	Type a nice, detailed description! You have no limits here, so go wild.
	
	To include a line break for a new paragraph, use "||/".
	"""
	
	options = ({"key": "_default",
			"exec": _edit_desc,
			"goto": "start"})
			
	return text, options
	
def _edit_desc(caller, raw_string):
	inp = raw_string.strip()
	if not inp:
		caller.msg("You didn't enter anything!")
	else:
		caller.db.desc = inp