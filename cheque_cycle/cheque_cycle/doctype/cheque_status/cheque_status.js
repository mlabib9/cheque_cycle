// Copyright (c) 2022, Brandimic and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cheque Status', {
	refresh: function(frm) {
		cur_frm.set_query("debit_account", function () {
			return {
				"filters": {
					"is_group": 0,
					"account_type": ["not in", ["Payable", "Receivable"]],
				}
			}
		})
	}
});
