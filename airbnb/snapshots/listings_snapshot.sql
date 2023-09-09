{% snapshot listings_snapshot_check %}

    {{
        config(
          target_schema='airbnb',
          strategy='timestamp',
          unique_key='id',
          updated_at='last_review',
        )

    }}

    select * from {{ source('staging', 'listingsparis') }}

{% endsnapshot %}