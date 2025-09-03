WITH teste_example AS (
    SELECT *
    FROM {{ ref('data_age_dbt_study') }}
)

select *
from teste_example