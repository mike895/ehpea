// Copyright (c) 2022, eldx and contributors
// For license information, please see license.txt

frappe.ui.form.on('Liquid Waste Management', {
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
        query: 'ehpea.ehpea.whitelist.liquid_two',
        filters: {
            email: frappe.session.user,
           }
       }

                })





	 }
});
