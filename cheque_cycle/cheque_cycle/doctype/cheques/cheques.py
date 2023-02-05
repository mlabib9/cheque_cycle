# Copyright (c) 2022, Brandimic and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Cheques(Document):
    def before_cancel(self):
        from frappe.desk.form.linked_with import get_linked_docs, get_linked_doctypes

        linkinfo = get_linked_doctypes(self.doctype)
        docs = get_linked_docs(self.doctype, self.name, linkinfo)

        for doc in docs['Payment Entry']:
            cancel_all('Payment Entry', doc.name)

        if ('Journal Entry' in docs.keys()):
            for doc in docs['Journal Entry']:
                cancel_all('Journal Entry', doc.name)

    def on_cancel(self):
        try:
            old_cancceled = frappe.get_doc('Cheques', self.name + '-CANCELLED')
            frappe.rename_doc('Cheques', self.name, self.name +
                              '-CANCELLED', force=True, merge=True)
        except:
            merge_r = False

            frappe.rename_doc('Cheques', self.name, self.name +
                              '-CANCELLED', force=True, merge=False)


def cancel_all(doctype, docname):
    # frappe.get_doc(doctype, docname).cancel()
    frappe.db.set_value(doctype, docname, 'docstatus', 2)
