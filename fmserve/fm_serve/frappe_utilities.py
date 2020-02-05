# -*- coding: utf-8 -*-
# Copyright (c) 2018, Yumatrix Enterprise Solutions LLC and contributors
# For license information, please see license.txt
import frappe
import re
from frappe import _
from frappe.utils import (flt, getdate, get_first_day, get_last_day, date_diff,
	add_months, add_days, formatdate, cint)

@frappe.whitelist()
def create_scheduled_invoices():
	dt=getdate()
	for i in frappe.db.get_list("Sales Order"):
		so = frappe.get_doc("Sales Order", i.name)
		if so.docstatus	== 1:
			for f in so.payment:
				if f.next_auto_invoice_date==dt:
					if f.create_auto_invoice==1 and not f.invoice_reference:
						si= frappe.new_doc("Sales Invoice")
						si.customer=so.customer
						si.set_posting_time = 1
						si.posting_date=f.next_auto_invoice_date
						si.due_date=f.planned_invoice_date
						if so.including_tax==1:
							for i in so.taxes:
								row = si.append('taxes', {})
								row.charge_type = i.charge_type
								row.account_head= i.account_head
								row.rate = i.rate
								row.description = i.description
						else:
							si.taxes=[]
						for i in so.items:
							row = si.append('items', {})
							row.item_code = i.item_code
							row.qty = i.qty
							row.rate=i.rate*f.portion_percentage/100
						res = si.insert()
						si.submit()	               
						frappe.db.set_value("Payment",f.name, "invoice_reference", res.name) 
						frappe.db.set_value("Payment",f.name, "invoice_status", res.status) 
						frappe.db.set_value("Payment",f.name, "auto_invoice_generation_status","On")  
						frappe.db.commit()          
						frappe.msgprint("Sales Invoice is created");
	

@frappe.whitelist()
def create_manual_invoice(sodoc,lpo_n,lpo_d):
	m = frappe.get_doc("Milestones",sodoc)
	tx=frappe.get_doc("Payment Milestone",m.payment_milestone)
	if not m.invoice_reference:
		si= frappe.new_doc("Sales Invoice")
		si.from_job=m.job
		si.payment_milestone=m.payment_milestone
		si.is_paid=0
		si.customer=m.customer
		si.set_posting_time = 1
		si.posting_date=m.posting_date
		si.due_date=m.planned_invoice_date
		si.lpo_date=lpo_d
		si.lpo_number=lpo_n
		row = si.append('items', {})
		row.item_code = m.item_code
		row.qty = m.qty
		row.rate=m.portion_value
		row.description=m.item_desciption
		for i in tx.taxes:
			row = si.append('taxes', {})
			row.charge_type = i.charge_type 
			row.account_head= i.account_head 
			row.rate = i.rate 
			row.description = i.description 
		res = si.insert()              
		frappe.db.set_value("Milestones",m.name, "invoice_reference", res.name) 
		frappe.db.set_value("Milestones",m.name, "invoice_status", res.status)  
		frappe.db.commit()          
		frappe.msgprint("Sales Invoice is created");
		return si.name
					
@frappe.whitelist()
def create_customer(sodoc):
		from erpnext.crm.doctype.lead.lead import make_customer
		cust = make_customer(sodoc)     
		cust.save()	    

@frappe.whitelist()
def bring_milestones(sodoc):
	return frappe.db.get_list("Milestones", filters={"job": sodoc}, fields=["name","customer","payment_milestone", "job", "item_code", "portion_percentage","portion_value","tax_value","portion_value_with_tax","invoice_reference","invoice_status","item_desciption","item_no"])

@frappe.whitelist()
def pm_save(sodoc):
	m = frappe.get_doc("Payment Milestone",sodoc)
	for i in m.milestones:
		i.payment_milestone=sodoc
	m.save();

@frappe.whitelist()
def pay_ms_ref(rname,pm_ref,tm,tx):
	frappe.db.set_value("Job Item",rname, "payment_milestone_reference",pm_ref) 
	frappe.db.set_value("Job Item",rname, "total_amount",tm) 
	frappe.db.set_value("Job Item",rname, "tax_value",tx) 
	frappe.db.commit()  

@frappe.whitelist()
def del_doc(pmn):
	for i in frappe.db.get_list("Milestones", filters={"payment_milestone": pmn}, fields=["name"]):
		if frappe.db.exists("Milestones", i.name):
			frappe.delete_doc("Milestones",i.name)
	for i in frappe.db.get_list("Sales Invoice", filters={"payment_milestone": pmn}, fields=["name"]):
		if frappe.db.exists("Sales Invoice", i.name):
			frappe.delete_doc("Sales Invoice",i.name)
	frappe.delete_doc("Payment Milestone", pmn)	
	frappe.msgprint("Payment Milestones has been deleted");
	frappe.db.commit()
	
@frappe.whitelist()
def adrs_add(ad1,ad2,ct,cn,dn):
	ad = frappe.new_doc("Address")
	ad.address_title=cn
	ad.address_line1=ad1
	ad.address_line2=ad2
	ad.city=ct
	row = ad.append('links', {})
	row.link_doctype = "Customer"
	row.link_name=dn
	res = ad.insert()   
