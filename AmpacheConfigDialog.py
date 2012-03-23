import gtk, gtk.glade

class AmpacheConfigDialog(object):
	def __init__(self, glade_file, config):
		self.gladexml = gtk.glade.XML(glade_file)
		self.config = config
		self.config_dialog = self.gladexml.get_widget("preferences_dialog")

		self.url = self.gladexml.get_widget("url_entry")
		self.url.set_text(self.config.get("url"))

		self.username = self.gladexml.get_widget("username_entry")
		self.username.set_text(self.config.get("username"))

		self.password = self.gladexml.get_widget("password_entry")
		self.password.set_text(self.config.get("password"))
		self.password.set_visibility(False)

		self.config_dialog.connect("response", self.dialog_response)

	def get_dialog(self):
		return self.config_dialog

	def dialog_response(self, dialog, response):
		if response == gtk.RESPONSE_OK:
			self.config.set("url", self.url.get_text())
			self.config.set("username", self.username.get_text())
			self.config.set("password", self.password.get_text())

			self.config_dialog.hide()

		elif response == gtk.RESPONSE_CANCEL or response == gtk.RESPONSE_DELETE_EVENT:
			self.config_dialog.hide()

		else:
			print "unexpected response type in dialog_response"
			self.config_dialog.hide()
