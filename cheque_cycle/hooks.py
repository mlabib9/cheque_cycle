from . import __version__ as app_version

app_name = "cheque_cycle"
app_title = "Cheque Cycle"
app_publisher = "Brandimic"
app_description = "Cheque Cycle"
app_email = "support@brandimic.com"
app_license = "MIT"
required_apps = ["erpnext"]

# Includes in <head>
# ------------------
fixtures = [
    "Cheque Status"
]
# include js, css files in header of desk.html
# app_include_css = "/assets/cheque_cycle/css/cheque_cycle.css"
# app_include_js = "/assets/cheque_cycle/js/cheque_cycle.js"

# include js, css files in header of web template
# web_include_css = "/assets/cheque_cycle/css/cheque_cycle.css"
# web_include_js = "/assets/cheque_cycle/js/cheque_cycle.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cheque_cycle/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Payment Entry": "public/js/payment_entry.js",
              "Bank": "public/js/bank.js", "Mode of Payment": "public/js/mode_of_payment.js"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "cheque_cycle.utils.jinja_methods",
#	"filters": "cheque_cycle.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "cheque_cycle.install.before_install"
# after_install = "cheque_cycle.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "cheque_cycle.uninstall.before_uninstall"
# after_uninstall = "cheque_cycle.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cheque_cycle.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Payment Entry": {
        "before_validate": "cheque_cycle.controllers.payment_entry.before_validate",
        "before_submit": "cheque_cycle.controllers.payment_entry.before_submit",
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"cheque_cycle.tasks.all"
#	],
#	"daily": [
#		"cheque_cycle.tasks.daily"
#	],
#	"hourly": [
#		"cheque_cycle.tasks.hourly"
#	],
#	"weekly": [
#		"cheque_cycle.tasks.weekly"
#	],
#	"monthly": [
#		"cheque_cycle.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "cheque_cycle.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "cheque_cycle.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "cheque_cycle.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"cheque_cycle.auth.validate"
# ]
