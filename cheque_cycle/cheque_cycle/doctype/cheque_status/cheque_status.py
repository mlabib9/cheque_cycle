# Copyright (c) 2022, Brandimic and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ChequeStatus(Document):
	pass

def on_save(self):
	default = frappe.get_list('Cheque Status', filters={'default_cheque': 1})
	if not len(default) == 0:
		frappe.throw('There is already a default status for new cheques , please remove it and try again')
