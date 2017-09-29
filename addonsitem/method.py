from __future__ import unicode_literals
import frappe

from frappe.model.document import Document

def on_price_update(doc,method):
	#if method=="on_update":
	result = frappe.db.sql("""select name from `tabItem Price` where item_code="{}" and price_list="Standard Selling" """.format(doc.name),as_list=1)
	found=0
	for row in result:
		found=1
		frappe.db.sql("""update `tabItem Price` set price_list_rate={} where item_code="{}" and price_list="{}" """.format(doc.name,"Standard Selling"),as_list=1)
	if found==0:
		gg = frappe.get_doc({
			"doctype":"Item Price",
			"item_code":doc.name,
			"price_list":"Standard Selling",
			"Selling":1,
			"price_list_rate":doc.standard_price,
			"item_name":doc.item_name,
			"item_description":doc.description
			})
		gg.insert()
