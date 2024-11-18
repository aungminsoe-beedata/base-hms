/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/store/models";

//Patching Orderline to change the uom by adding a function.
patch(Orderline.prototype, {
        setup(_defaultObj, options) {
        super.setup(...arguments);
        if(options.json){
        this.physicians = this.physicians;
        this.user_id = this.user_id;
        }
    },
    export_as_JSON(){
        var json = super.export_as_JSON.call(this);
        json.physicians = this.physicians || false
        json.user_id = this.user_id || false
            return json
    },
            // Set the unit from the JSON data
    init_from_JSON(json){
        super.init_from_JSON(...arguments);
         this.physicians = json.physicians;
         this.user_id = json.user_id;
    },
    get_salesperson(){
    return this.sales_person , this.user_id },
     getDisplayData() {
        return {
            ...super.getDisplayData(),
            physicians: this.physicians,
            user_id: this.user_id,
        };
    },
});
