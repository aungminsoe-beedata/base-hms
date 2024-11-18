/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/store/models";

//Patching Orderline to change the uom by adding a function.
patch(Orderline.prototype, {

    setup(_defaultObj, options) {
        super.setup(...arguments);
        if(options.json){
        this.employee = this.employee;
        this.physician_id = this.physician_id;
        }
    },


    export_as_JSON(){
        var json = super.export_as_JSON.call(this);
        json.employee = this.employee || false
        json.physician_id = this.physician_id || false
            return json
    },

    init_from_JSON(json){
        super.init_from_JSON(...arguments);
         this.employee = json.employee;
         this.physician_id = json.physician_id;
    },

    get_salesperson(){
        return this.sales_person , this.physician_id },
        
    getDisplayData() {
        return {
            ...super.getDisplayData(),
            employee: this.employee,
            physician_id: this.physician_id,
            
        };
    }, 
});
