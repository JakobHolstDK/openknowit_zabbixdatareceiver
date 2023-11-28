SELECT
    'CREATE TABLE ' || table_name || ' (' || string_agg(column_definition, ', ') || ');'
FROM (
    SELECT
        table_name,
        column_name || ' ' || data_type ||
            CASE
                WHEN character_maximum_length IS NOT NULL THEN '(' || character_maximum_length || ')'
                ELSE ''
            END AS column_definition
    FROM information_schema.columns
    WHERE table_name = 'zabbix_data_type_2'
) AS columns_definition;
