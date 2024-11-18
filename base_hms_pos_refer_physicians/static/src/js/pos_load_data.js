/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
        async _processData(loadedData) {
            await super._processData(...arguments);
            this.employee_casher_user = loadedData['employee_casher_user'];
        }
    });
