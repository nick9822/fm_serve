// Copyright (c) 2018, Yumatrix Enterprise Solutions LLC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Contract', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Contract", "frequency_of_visit", function(frm, cdt, cdn) {
    var p = frm.doc;
    var d = locals[cdt][cdn];

    p.scheduled_job_visit = [];
    
    if(p.start_date){
    	var nov = p.frequency_of_visit;
    	var add_factor = 12/flt(p.frequency_of_visit);
    	var last_date = "";
    	for(var i = 0; i < nov; i++) {
    		if(i != 0){
    			last_date = frappe.datetime.add_months(last_date, add_factor);
    		}else{
    			last_date = p.start_date;
    		}
    		
    		var counter = i+1;

    		var nrow = frm.add_child("scheduled_job_visit");
	        nrow.job_visit = p.name+"-"+counter;
	        nrow.planned_date = last_date;
	        refresh_field("scheduled_job_visit")
    	}
    }else{
    	frappe.model.set_value(p.doctype, p.name,"frequency_of_visit", "");
    	frappe.throw("Please enter Start Date");
    }
});