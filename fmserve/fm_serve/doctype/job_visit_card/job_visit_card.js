// Copyright (c) 2018, Yumatrix Enterprise Solutions LLC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Visit Card', {
	refresh: function(frm) {
		var p = frm.doc;
		var current_date = frappe.datetime.now_datetime();
		if(p.status == "Job Scheduled"){
			frm.add_custom_button(__("Start Job"), function() {
				frappe.model.set_value(p.doctype, p.name, "job_start_time", current_date);
				frappe.model.set_value(p.doctype, p.name, "status", "Job Started");
				cur_frm.save();
			});
		}else if(p.status == "Job Started"){
			frm.add_custom_button(__("Complete Job"), function() {
				frappe.model.set_value(p.doctype, p.name, "job_end_time", current_date);
				frappe.model.set_value(p.doctype, p.name, "status", "Job Completed");
				cur_frm.save();
			});

			frm.add_custom_button(__("Pause Job"), function() {
				//frappe.model.set_value(p.doctype, p.name, "job_end_time", current_date);
				frappe.model.set_value(p.doctype, p.name, "status", "Job Paused");
				cur_frm.save();
			});
		}else if(p.status == "Job Paused"){
			frm.add_custom_button(__("Resume Job"), function() {
				frappe.model.set_value(p.doctype, p.name, "status", "Job Started");
				cur_frm.save();
			});
		}
	}
});
