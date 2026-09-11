# Gramik Accounting Custom

Odoo 19 custom module for adding a Business Segment field to customer invoices.

## Business Segment values
- B2B – Distributor
- B2B – Retailer
- B2C

## Features
- Adds Business Segment to customer invoice form.
- Adds Business Segment to customer invoice list/tree view.

## Installation
1. Copy `gramik_accounting_custom` into the Odoo addons directory.
2. Restart the Odoo server.
3. Update the Apps list.
4. Install **Gramik Accounting Custom**.

## Technical note
The field is added to `account.move`, which is the model used for invoices in Odoo.
