# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "fmserve"
app_title = "FM Serve"
app_publisher = "Yumatrix Enterprise Solutions LLC"
app_description = "Facility Management"
app_icon = "octicon octicon-package"
app_color = "blue"
app_email = "nickesh@yumatrix.com"
app_license = "EULA"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fmserve/css/fmserve.css"
# app_include_js = "/assets/fmserve/js/fmserve.js"

# include js, css files in header of web template
# web_include_css = "/assets/fmserve/css/fmserve.css"
# web_include_js = "/assets/fmserve/js/fmserve.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "fmserve.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "fmserve.install.before_install"
# after_install = "fmserve.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fmserve.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"fmserve.tasks.all"
# 	],
# 	"daily": [
# 		"fmserve.tasks.daily"
# 	],
# 	"hourly": [
# 		"fmserve.tasks.hourly"
# 	],
# 	"weekly": [
# 		"fmserve.tasks.weekly"
# 	]
# 	"monthly": [
# 		"fmserve.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "fmserve.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "fmserve.event.get_events"
# }

