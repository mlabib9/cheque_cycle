frappe.require("assets/cheque_cycle/js/utilities.js");

frappe.ui.form.on("Payment Entry", {
  refresh: function (frm) {
    // Validators
    frm.set_query("cheque_bank", function () {
      return {
        filters: {
          account: ["!=", ""],
        },
      };
    });

    if (frm.doc.docstatus != 1) {
      return;
    }

    // Set cheque actions
    var workflows = get_doc({
      doctype: "Cheque Settings",
    }).workflow;
    for (var wokflow_step of workflows) {
      if (
        wokflow_step.status == frm.doc.cheque_status &&
        wokflow_step.cheque_type == frm.doc.payment_type
      ) {
        let workflow_details = wokflow_step;
        frm.add_custom_button(
          __(wokflow_step.action_name),
          function () {
            let next_status = get_doc({
              doctype: "Cheque Status",
              name: workflow_details.next_status,
            });
            let cheque = get_doc({
              doctype: "Cheques",
              name: frm.doc.cheque,
            });
            if (
              (next_status.with_bank_selection ||
                next_status.destination_account_type == "Bank Account") &&
              !cheque.bank
            ) {
              bank_dialog(frm.doc.cheque, workflow_details.next_status);
            } else if (
              next_status.destination_account_type ==
              "Transfer to Another Party"
            ) {
              party_dialog(frm.doc.cheque, workflow_details.next_status);
            } else {
              process_status_action(
                frm.doc.cheque,
                workflow_details.next_status
              );
            }
          },
          __("Actions")
        );
      }
    }
  },
  mode_of_payment: function (frm) {
    change_account(frm);
  },
  payment_type: function (frm) {
    change_account(frm);
  },
});
