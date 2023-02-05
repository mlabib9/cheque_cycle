frappe.ui.form.on("Mode of Payment", {
  refresh: function (frm) {
    frm.set_query("payable_account", function () {
      return {
        filters: {
          account_type: ["in", ["Bank", "Cash"]],
        },
      };
    });
    frm.set_query("receivable_account", function () {
      return {
        filters: {
          account_type: ["in", ["Bank", "Cash"]],
        },
      };
    });
  },
});

