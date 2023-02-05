frappe.ui.form.on("Bank", {
    refresh: function (frm) {
        cur_frm.set_query("account", function () {
            return {
                "filters": {
                    "account_type": "Bank",
                    "is_group": 0,
                }
            }
        });
    }
})