// Copyright (c) 2018, Yumatrix Enterprise Solutions LLC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Visit', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Job Visit", "job_end_time", function(frm, cdt, cdn) {
	var p = frm.doc;
    var d = locals[cdt][cdn];
    
	var d1 = new Date(p.job_start_time);
	var d2 = new Date(p.job_end_time);
	var hours = (Math.abs(d1.getTime() - d2.getTime()) / 36e5).toFixed(1);
	frappe.model.set_value(p.doctype, p.name, "ttc_in_hrs", hours);
	
});