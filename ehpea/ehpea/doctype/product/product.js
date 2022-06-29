// Copyright (c) 2022, eldx and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product', {
	 refresh: function(frm) {

	 frm.set_query( 'farm', () => {
   
        return {
        query: 'ehpea.ehpea.whitelist.farmfilter',
        filters: {
            email: frappe.session.user,
           }
       }

	})

	 }
});
