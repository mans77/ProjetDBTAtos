{{ config(
    materialized="table"
)}}

with revenue_nuit as (
  select
    listings_id,
    listings_name,
    room_type,
    minimum_nights,
    price,
    number_of_reviews_ltm,
    last_review,
    reviews_per_month,
    availability_365,
    host_name,
    CASE
       when last_review is null then CURRENT_TIMESTAMP
       when last_review ~ '^\d{4}-\d{2}-\d{2}$' then date_trunc('month', cast(last_review as timestamp))
        else null  -- Évite la conversion des valeurs non valides en NULL
    END as review_month,
    sum(minimum_nights*availability_365/365) as estimated_nights_booked,
    sum(price*minimum_nights*availability_365/365) as estimated_revenue
  from {{ ref('source_listings_hosts') }}
  where 
    (last_review is null or last_review ~ '^\d{4}-\d{2}-\d{2}$') and
    (cast(last_review as timestamp) is null OR cast(last_review as timestamp) >= date_trunc('month', CURRENT_DATE) - interval '12 months')
  group by listings_id, listings_name, room_type, minimum_nights, price, number_of_reviews_ltm, last_review, reviews_per_month, availability_365, host_name, review_month)
  
select *
from revenue_nuit
