// Copyright (c) 2018, Yumatrix Enterprise Solutions LLC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Worksite', {
	refresh: function(frm) {
		frm.add_custom_button(__('Equipments'), function() {
			frappe.set_route('Report/Equipment', 'Equipments', {installed_at: frm.doc.name});
		});	
	}
});
