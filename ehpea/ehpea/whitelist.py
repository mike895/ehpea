
import frappe


@frappe.whitelist()
def farmfilter(doctype, txt, searchfield, start, page_len,filters):

	if filters['email'] != 'Administrator':
		perm = frappe.db.get_list('Ehpea Permission',filters={'user': filters['email']}, fields=['all_farm'])
		values = {'company': filters['email']}
		data = frappe.db.sql(""" SELECT farm FROM `tabSelected Farm` WHERE parent = %(company)s """, values=values, as_dict=0)
	else:
		perm = 'admin'

	if perm == 'admin' or perm[0]['all_farm'] == 1:
		list = frappe.db.sql(""" SELECT farm FROM `tabFarm Profile`""", as_dict=0)
		filtered_list = list
		
	else:
		
		filtered_list =  data

	return filtered_list



@frappe.whitelist()
def Audit_two(doctype, txt, searchfield, start, page_len,filters):
	if filters['email'] != 'Administrator':
		perm = frappe.db.get_list('Ehpea Permission',filters={'user': filters['email']}, fields=['all_farm'])
		value = {'user':filters['email']}
		farm_data = frappe.db.sql(""" SELECT farm FROM `tabSelected Farm` WHERE parent = %(user)s """, values=value, as_dict=0)
		values = {'farms':farm_data,'company': 'Gender Audit Checklist IRMS part2'}
		data = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s AND farm IN %(farms)s """, values=values, as_dict=0)
	else:
                perm = 'admin'

	if perm == 'admin' or perm[0]['all_farm'] == 1:
                list = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s`""", as_dict=0)
                filtered_list = list
                
	else:
                
                filtered_list =  data

	return filtered_list







@frappe.whitelist()
def Audit_three(doctype, txt, searchfield, start, page_len,filters):
        if filters['email'] != 'Administrator':
                perm = frappe.db.get_list('Ehpea Permission',filters={'user': filters['email']}, fields=['all_farm'])
                value = {'user':filters['email']}
                farm_data = frappe.db.sql(""" SELECT farm FROM `tabSelected Farm` WHERE parent = %(user)s """, values=value, as_dict=0)
                values = {'farms':farm_data,'company': 'Gender Audit Checklist IRMS part3'}
                data = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s AND farm IN %(farms)s """, values=values, as_dict=0)
        else:
                perm = 'admin'

        if perm == 'admin' or perm[0]['all_farm'] == 1:
                list = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s`""", as_dict=0)
                filtered_list = list
                
        else:
                
                filtered_list =  data

        return filtered_list






@frappe.whitelist()
def worker_two(doctype, txt, searchfield, start, page_len,filters):
        if filters['email'] != 'Administrator':
                perm = frappe.db.get_list('Ehpea Permission',filters={'user': filters['email']}, fields=['all_farm'])
                value = {'user':filters['email']}
                farm_data = frappe.db.sql(""" SELECT farm FROM `tabSelected Farm` WHERE parent = %(user)s """, values=value, as_dict=0)
                values = {'farms':farm_data,'company': 'Workers Walfare OSH part 2'}
                data = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s AND farm IN %(farms)s """, values=values, as_dict=0)
        else:
                perm = 'admin'

        if perm == 'admin' or perm[0]['all_farm'] == 1:
                list = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s`""", as_dict=0)
                filtered_list = list
                
        else:
                
                filtered_list =  data

        return filtered_list






@frappe.whitelist()
def worker_three(doctype, txt, searchfield, start, page_len,filters):
        if filters['email'] != 'Administrator':
                perm = frappe.db.get_list('Ehpea Permission',filters={'user': filters['email']}, fields=['all_farm'])
                value = {'user':filters['email']}
                farm_data = frappe.db.sql(""" SELECT farm FROM `tabSelected Farm` WHERE parent = %(user)s """, values=value, as_dict=0)
                values = {'farms':farm_data,'company': 'Workers Walfare OSH part 3'}
                data = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s AND farm IN %(farms)s """, values=values, as_dict=0)
        else:
                perm = 'admin'

        if perm == 'admin' or perm[0]['all_farm'] == 1:
                list = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s`""", as_dict=0)
                filtered_list = list
                
        else:
                
                filtered_list =  data

        return filtered_list




@frappe.whitelist()
def liquid_two(doctype, txt, searchfield, start, page_len,filters):
        if filters['email'] != 'Administrator':
                perm = frappe.db.get_list('Ehpea Permission',filters={'user': filters['email']}, fields=['all_farm'])
                value = {'user':filters['email']}
                farm_data = frappe.db.sql(""" SELECT farm FROM `tabSelected Farm` WHERE parent = %(user)s """, values=value, as_dict=0)
                values = {'farms':farm_data,'company': 'Liquid Waste Management Part2'}
                data = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s AND farm IN %(farms)s """, values=values, as_dict=0)
        else:
                perm = 'admin'

        if perm == 'admin' or perm[0]['all_farm'] == 1:
                list = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s`""", as_dict=0)
                filtered_list = list
                
        else:
                
                filtered_list =  data

        return filtered_list







@frappe.whitelist()
def pest_two(doctype, txt, searchfield, start, page_len,filters):
        if filters['email'] != 'Administrator':
                perm = frappe.db.get_list('Ehpea Permission',filters={'user': filters['email']}, fields=['all_farm'])
                value = {'user':filters['email']}
                farm_data = frappe.db.sql(""" SELECT farm FROM `tabSelected Farm` WHERE parent = %(user)s """, values=value, as_dict=0)
                values = {'farms':farm_data,'company': 'Implementation of pest management part 2'}
                data = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s AND farm IN %(farms)s """, values=values, as_dict=0)
        else:
                perm = 'admin'

        if perm == 'admin' or perm[0]['all_farm'] == 1:
                list = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s`""", as_dict=0)
                filtered_list = list
                
        else:
                
                filtered_list =  data

        return filtered_list






@frappe.whitelist()
def pest_three(doctype, txt, searchfield, start, page_len,filters):
        if filters['email'] != 'Administrator':
                perm = frappe.db.get_list('Ehpea Permission',filters={'user': filters['email']}, fields=['all_farm'])
                value = {'user':filters['email']}
                farm_data = frappe.db.sql(""" SELECT farm FROM `tabSelected Farm` WHERE parent = %(user)s """, values=value, as_dict=0)
                values = {'farms':farm_data,'company': 'Implementation of pest management part 3'}
                data = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s AND farm IN %(farms)s """, values=values, as_dict=0)
        else:
                perm = 'admin'

        if perm == 'admin' or perm[0]['all_farm'] == 1:
                list = frappe.db.sql(""" SELECT parent FROM `tabSelected Farm` WHERE parenttype = %(company)s`""", as_dict=0)
                filtered_list = list
                
        else:
                
                filtered_list =  data

        return filtered_list


