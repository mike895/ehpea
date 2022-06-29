// Copyright (c) 2022, eldx and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gender Audit Checklist IRMS part2', {
	 refresh: function(frm) {

	 frm.set_query( 'farm', () => {
   
        return {
        query: 'ehpea.ehpea.whitelist.farmfilter',
        filters: {
            email: frappe.session.user,
           }
       }

	})


	 frm.set_query( 'next_part', () => {
   
        return {
        query: 'ehpea.ehpea.whitelist.Audit_three',
        filters: {
            email: frappe.session.user,
           }
       }

        })



	 }
});
