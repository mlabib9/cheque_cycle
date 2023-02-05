function get_doc(args) {
  let response;
  frappe.call({
    method: "frappe.client.get",
    async: false,
    args: args,
    callback(r) {
      response = r.message;
    },
  });
  return response;
}
function proccess_bank_dialog_action(cheque, next_status, bank) {
  frappe.call({
    method: "cheque_cycle.api.change_cheque_bank",
    async: false,
    args: {
      cheque: cheque,
      next_status: next_status,
      bank: bank,
    },
    callback(r) {
      process_status_action(
        cheque,
        next_status
      );
    },
  });
}
function process_status_action(cheque, next_status) {
  frappe.call({
    method: "cheque_cycle.api.change_cheque_status",
    async: false,
    args: {
      cheque: cheque,
      next_status: next_status,
    },
    callback(r) {
      window.location.reload();
    },
  });
}
function party_dialog(cheque, next_status) {
  var d = new frappe.ui.Dialog({
    title: __("Cheque Details"),
    fields: [
      {
        fieldtype: "Link",
        fieldname: "party",
        label: __("Supplier"),
        options: "Supplier",
        reqd: 1,
      },
    ],
    primary_action_label: __("Submit"),
    primary_action(values) {
      frappe.call({
        method: "cheque_cycle.api.transfer_to_another_party",
        async: false,
        args: {
          cheque: cheque,
          next_status: next_status,
          party_type: "Supplier",
          party: values.party,
        },
        callback(r) {
          window.location.reload();
        },
      });
      d.hide();
    },
  });
  d.show();
}
function bank_dialog(cheque, next_status) {
  var d = new frappe.ui.Dialog({
    title: __("Cheque Details"),
    fields: [
      {
        fieldtype: "Link",
        fieldname: "cheque_bank",
        label: __("Cheque Bank"),
        options: "Bank",
        reqd: 1,
      },
    ],
    primary_action_label: __("Submit"),
    primary_action(values) {
      proccess_bank_dialog_action(cheque, next_status, values.cheque_bank);
      d.hide();
    },
  });
  d.show();
}
function change_account(frm) {
  if (frm.doc.mode_of_payment) {
    let mode_of_payment = get_doc({
      doctype: "Mode of Payment",
      name: frm.doc.mode_of_payment,
    });
    if (frm.doc.payment_type == "Pay") {
      frm.set_value("paid_from", mode_of_payment.payable_account);
    } else if (frm.doc.payment_type == "Receive") {
      frm.set_value("paid_to", mode_of_payment.receivable_account);
    }
    frm.refresh();
  }
}