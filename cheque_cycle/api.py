# Copyright (c) 2022, Brandimic and contributors
# For license information, please see license.txt


import frappe


@frappe.whitelist()
def change_cheque_status(cheque, next_status):
    cheque = frappe.get_doc('Cheques', cheque)
    next_status = frappe.get_doc('Cheque Status', next_status)
    set_status_variables(cheque, next_status)
    update_status(cheque, next_status)


def set_status_variables(cheque, next_status):

    party_type = None
    party = None
    if next_status.destination_account_type == 'Bank Account':
        next_status_account = cheque.bank_account

    elif next_status.destination_account_type == 'First Receive/Pay Account (Not Party)':
        next_status_account = cheque.against_account

    elif next_status.destination_account_type == 'Transfer to Another Party':
        pass

    elif next_status.destination_account_type == 'Cheque Party Account':
        next_status_account = cheque.party_account
        party = cheque.party
        party_type = cheque.party_type

    else:
        next_status_account = next_status.debit_account

    if cheque.type == 'Receive':
        create_journal_entry(next_status_account, cheque.last_transaction_account, cheque.amount,
                             cheque.reference_date, cheque.doctype, cheque.name, cheque.company, party_type, party)

    elif cheque.type == 'Pay':
        create_journal_entry(cheque.last_transaction_account, next_status_account, cheque.amount,
                             cheque.reference_date, cheque.doctype, cheque.name, cheque.company, party_type, party)

    update_last_transaction_account(cheque, next_status_account)


def create_journal_entry(debit_account, credit_account, amount, reference_date, reference_type, reference_name, company, party_type, party):
    je = {
        'doctype': 'Journal Entry',
        'voucher_type': 'Journal Entry',
        'posting_date': frappe.utils.nowdate(),
        'company': company,
        'reference_doctype': reference_type,
        'reference_name': reference_name,
        'accounts': [
            {
                'account': debit_account,
                'debit_in_account_currency': amount,
                'party_type': party_type,
                'party': party
            },
            {
                'account': credit_account,
                'credit_in_account_currency': amount,
            }
        ]
    }
    je = frappe.get_doc(je)
    je.save(ignore_permissions=True)
    je.submit()


def update_status(cheque, next_status):
    # update cheque status
    frappe.db.set_value(cheque.doctype, cheque.name,
                        'cheque_status', next_status.name)
    # update cheque status in related document
    frappe.db.set_value(cheque.reference_type,
                        cheque.reference_name, 'cheque_status', next_status.name)


def update_last_transaction_account(cheque, next_status_account):
    frappe.db.set_value(cheque.doctype, cheque.name,
                        'last_transaction_account', next_status_account)


@frappe.whitelist()
def change_cheque_bank(cheque, next_status, bank):
    bank = frappe.get_doc('Bank', bank)
    if bank.account == None:
        frappe.throw('Bank Account is not set for this bank')

    cheque = frappe.get_doc('Cheques', cheque)
    next_status = frappe.get_doc('Cheque Status', next_status)
    frappe.db.set_value(cheque.doctype, cheque.name, 'bank', bank.name)
    frappe.db.set_value(cheque.doctype, cheque.name,
                        'bank_account', bank.account)


@frappe.whitelist()
def transfer_to_another_party(cheque, next_status, party_type, party):

    cheque = frappe.get_doc('Cheques', cheque)
    next_status = frappe.get_doc('Cheque Status', next_status)
    new_doc = {
        'doctype': 'Payment Entry',
        'payment_type': 'Pay',
        'party_type': party_type,
        'party': party,
        'cheque': cheque.name,
        'cheque_status': next_status.name,
        'paid_from': cheque.last_transaction_account,
        'paid_amount': 0.1,
        'received_amount': 0.1,
        'reference_date': cheque.reference_date,
        'reference_no': cheque.name,
        'clearance_date': cheque.clearance_date,
        'company': cheque.company,
        'posting_date': frappe.utils.nowdate(),
    }

    if (cheque.type == 'Receive'):
        new_doc['paid_amount'] = cheque.amount
    elif (cheque.type == 'Pay'):
        new_doc['received_amount'] = cheque.amount

    payment_entry = frappe.get_doc(new_doc)
    payment_entry.save(ignore_permissions=True)
    payment_entry.submit()

    frappe.db.set_value(cheque.doctype, cheque.name,
                        'endoresd_transaction', payment_entry.name)
    frappe.db.set_value(cheque.doctype, cheque.name,
                        'last_transaction_account', payment_entry.paid_to)
    frappe.db.set_value(cheque.doctype, cheque.name,
                        'endorsed_part_type', party_type)
    frappe.db.set_value(cheque.doctype, cheque.name, 'endoresd_party', party)
    update_status(cheque, next_status)
