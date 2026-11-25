{% docs gross_revenue %}
**Gross revenue (EUR)** — total amount paid by the customer for an order, VAT included, shipping included, before refunds.
Owner: Head of Sales · Steward: Karim Benali · Status: approved (2026-11-10)
{% enddocs %}

{% docs active_customer %}
**Active customer** — a customer account with at least one non-cancelled order in the 12 months ending on the report date.

Rule: an order qualifies when its status is not `cancelled` and its `order_date` falls within the trailing 12 months. Sales may keep its seasonal campaign view using the same rule over six months, clearly labelled **Sales active customer (6 months)**; it is a separate view, not the company-wide KPI.

Owner: CFO / Head of Finance · Steward: Analytics engineer (Karim) · Status: approved in role-play simulation (2026-11-25; real approval required before production).
{% enddocs %}

{% docs net_revenue %}
**Net revenue (EUR)** — revenue after refunds, excluding VAT and retaining shipping fees.

Formula: `(gross_revenue_eur - refunded_eur) / 1.20` when both inputs are EUR and the applicable VAT rate is 20%; otherwise remove the applicable VAT rate after refunds. Example: `(EUR 120 gross - EUR 12 refunded) / 1.20 = EUR 90` net revenue.

Owner: CFO / Head of Finance · Steward: Finance data steward · Status: approved in role-play simulation (2026-11-25; payment-unit confirmation and real approval required before production).

The Sales memo's VAT-inclusive net figure is not the company net-revenue definition; Sales can report VAT-inclusive gross sales separately. Confirm whether the provider's payment amount is EUR or cents before applying the formula.
{% enddocs %}

{% docs churned_customer %}
**Churned customer** — a customer account with a prior non-cancelled order but no non-cancelled order in the trailing 12 months.

Rule: the account has at least one historical non-cancelled order and none in the 12-month window ending on the report date.

Owner: CFO / Head of Finance · Steward: Analytics engineer (Karim) · Status: approved in role-play simulation (2026-11-25; real approval required before production).
{% enddocs %}

{% docs customer %}
**Customer** — one ShopFast account identified by `customer_id`; it does not necessarily represent one unique person.

Rule: count distinct `customer_id` values at account grain. A person with multiple account IDs represents multiple customer accounts.

Owner: Head of Sales (Sara Martin) · Steward: Analytics engineer (Karim) · Status: approved in role-play simulation (2026-11-25; real approval required before production).
{% enddocs %}

{% docs order %}
**Order** — one ShopFast order header identified by `order_id`, regardless of its number of line items or payment events.

Rule: count distinct `order_id` values after exact duplicate order headers are removed.

Owner: Head of Sales (Sara Martin) · Steward: Analytics engineer (Karim) · Status: approved in role-play simulation (2026-11-25; real approval required before production).
{% enddocs %}
