/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { _t } from "@web/core/l10n/translation";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";

// Extend the props for Orderline to include custom fields
Orderline.props = {
    ...Orderline.props,
    line: {
        shape: {
            ...Orderline.props.line.shape,
            // employee: { type: String, optional: true },
            physician_id: { type: Number, optional: true ,default: null  },
            // state :{type: String,optional:true}
            
        }
    }
};

export class PosEmployeeButton extends Component {
    setup() {
        super.setup();
        this.pos = usePos();
        const { popup } = this.env.services;
        this.popup = popup;
    }

    get productsList() {
        let list = this.pos.db.get_product_by_category(this.pos.selectedCategoryId);
        return list.sort((a, b) => a.display_name.localeCompare(b.display_name));
    }

    async onClick() {
        const employee_list = this.pos.employee_casher_user.map((employee) => ({
            id: employee.id,
            item: employee,
            label: employee.partner_id,
            isSelected: false,
        }));

        const { confirmed, payload: employee } = await this.popup.add(SelectionPopup, {
            title: _t("Select the Salesperson"),
            list: employee_list,
        });

        if (confirmed && employee) {
            const selectedOrderline = this.pos.selectedOrder.selected_orderline;
            if (selectedOrderline) {
                selectedOrderline.employee = employee.partner_id;
                selectedOrderline.physician_id = employee.id;
                
            }
        }
    }
}

PosEmployeeButton.template = "HrEmployeeButton";

// Add the control button to ProductScreen
ProductScreen.addControlButton({
    component: PosEmployeeButton,
    condition: () => true,
});
