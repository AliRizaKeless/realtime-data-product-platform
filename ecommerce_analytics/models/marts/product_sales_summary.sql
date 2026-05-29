select
    product,
    count(order_id) as total_orders,
    sum(price) as total_revenue,
    avg(price) as average_price
from {{ ref('stg_orders') }}
group by product