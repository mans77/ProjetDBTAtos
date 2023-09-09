{% snapshot host_snapshot_check %}

    {{
        config(
          target_schema='airbnb',
          strategy='timestamp',
          unique_key='host_id',
          updated_at='host_id',
        )
    }}

    select * from  {{ source('staging', 'hostsparis') }}

{% endsnapshot %}