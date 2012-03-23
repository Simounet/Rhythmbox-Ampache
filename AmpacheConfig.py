import gconf

class AmpacheConfig(object):
	def __init__(self):
		self.gconf_keys = {
			'url'		: '/apps/rhythmbox/plugins/ampache/url',
			'username'	: '/apps/rhythmbox/plugins/ampache/username',
			'password'	: '/apps/rhythmbox/plugins/ampache/password',

			'name'		: "/apps/rhythmbox/plugins/ampache/name",
			'group'		: "/apps/rhythmbox/plugins/ampache/group",

			'icon'		: "/apps/rhythmbox/plugins/ampache/icon",
			'icon_filename'	: "/apps/rhythmbox/plugins/ampache/icon_filename",
		}

		self.gconf = gconf.client_get_default()

		# Defaults ("hidden" options)
		self.set("name", "Ampache")
		self.set("group", "Shared")

		self.set("icon", "ampache.ico")

	def get(self, key):
		if self.gconf.get_string(self.gconf_keys[key]):
			return self.gconf.get_string(self.gconf_keys[key])
		else:
			return ""

	def set(self, key, value):
		self.gconf.set_string(self.gconf_keys[key], value)

#if __name__ == "__main__":
	#config = AmpacheConfig()
	#print config.get("url")
	#config.set("password", "testing123")
	#print config.get("username")
	#print config.get("password")
	
