# Copyright (c) 2022, brandimic.com and contributors
# For license information, please see license.txt

import frappe


def before_validate(self, method):
    if self.with_cheque_management == 1:
        self.cheque = ''


def before_submit(self, method):

    if self.with_cheque_management == 1:
        statuses = frappe.get_list(
            'Cheque Status', filters={'default_cheque': 1})
        if len(statuses) == 0:
            frappe.throw(
                'No default cheque status found, please create one and try again')
        else:
            self.cheque_status = statuses[0].name
            cheque_name = create_cheque(self)
            self.cheque = cheque_name


def create_cheque(payment_entry):
    cheque = frappe.new_doc('Cheques')
    cheque.number = payment_entry.reference_no
    cheque.cheque_status = payment_entry.cheque_status
    cheque.type = payment_entry.payment_type
    cheque.transaction_date = payment_entry.posting_date
    cheque.reference_date = payment_entry.reference_date
    cheque.clearance_date = payment_entry.clearance_date
    if payment_entry.payment_type == 'Receive':
        cheque.issuer_bank = payment_entry.issuer_bank
    elif payment_entry.payment_type == 'Pay':
        cheque.bank = payment_entry.cheque_bank
        cheque.bank_account = payment_entry.cheque_bank_account

    cheque.last_transaction_account = payment_entry.paid_to if (
        payment_entry.payment_type == 'Receive') else payment_entry.paid_from
    cheque.amount = payment_entry.paid_amount if (
        payment_entry.payment_type == 'Pay') else payment_entry.received_amount
    cheque.party_type = payment_entry.party_type
    cheque.party = payment_entry.party
    cheque.against_account = payment_entry.paid_to if (
        payment_entry.payment_type == 'Receive') else payment_entry.paid_from
    cheque.party_account = payment_entry.paid_to if (
        payment_entry.payment_type == 'Pay') else payment_entry.paid_from
    cheque.reference_type = "Payment Entry"
    cheque.reference_name = payment_entry.name
    cheque.company = payment_entry.company
    cheque.save(ignore_permissions=True)
    cheque.submit()

    return cheque.name
