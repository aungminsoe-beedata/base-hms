/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { _t } from "@web/core/l10n/translation";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";

export class SetProductListButton1 extends Component {
    setup() {
        super.setup();
        this.pos = usePos();
        const { popup } = this.env.services;
        this.popup = popup;
    }

    get productsList() {
        let list = this.pos.db.get_product_by_category(
            this.pos.selectedCategoryId
        );

        return list.sort(function(a, b) {
            return a.display_name.localeCompare(b.display_name);
        });
    }
    
    async onClick() {
        let list = this.productsList;
        console.log("Clicked product list is:", list);

        const salespersonList = this.pos.medical_physician.map((salesperson) => {
            return {
                id: salesperson.id,
                item: salesperson,
                label: salesperson.partner_id,
                isSelected: false,
            };
        });
        console.log("Salesperson list of medical physicians:", salespersonList);
        salespersonList.forEach((salesperson) => {
            console.log("Medical Physician Name:", salesperson.label);
        });
    }
}

SetProductListButton1.template = "MedicalPhysiciansButton";

ProductScreen.addControlButton({
    component: SetProductListButton1,
    condition: function() {
        return true;
    },
});
