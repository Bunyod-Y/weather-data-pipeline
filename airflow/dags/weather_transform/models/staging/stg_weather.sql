with source as (
    -- We use the source function to refer to the file we just created
    select * from {{ source('weather_source', 'raw_weather') }}
),

renamed as (
    select
        id,
        city,
        temperature as temp_celsius, -- Rename for clarity
        (temperature * 9/5) + 32 as temp_fahrenheit, -- Add a transformation!
        humidity,
        wind_speed,
        weather_description,
        ingestion_timestamp
    from source
)

select * from renamed