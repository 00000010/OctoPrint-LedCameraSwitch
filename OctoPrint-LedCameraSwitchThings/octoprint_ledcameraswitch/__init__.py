# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class LedCameraSwitchPlugin(octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin,
                            octoprint.plugin.SettingsPlugin):
    def on_after_startup(self):
        #self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))
	self._logger.info("led plugin loaded")
        self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(
	    url = "https://en.wikipedia.org/wiki/Hello_world"
	)

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

'''
    def get_settings_defaults(self):
        return dict(
	    url = "https://en.wikipedia.org/wiki/Hello_world"
        )

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]
'''

__plugin_name__ = "Led Camera Switch"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = LedCameraSwitchPlugin()
