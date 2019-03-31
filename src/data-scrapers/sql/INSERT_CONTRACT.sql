INSERT INTO contract (
    name, commerical_name, country_code, city
)
VALUES (
    '{name}', '{commerical_name}', '{country_code}', '{city}'
)
ON CONFLICT
DO NOTHING;