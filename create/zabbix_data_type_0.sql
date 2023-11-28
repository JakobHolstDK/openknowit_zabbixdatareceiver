-- Table: public.zabbix_data_type_0

-- DROP TABLE IF EXISTS public.zabbix_data_type_0;

CREATE TABLE IF NOT EXISTS public.zabbix_data_type_0
(
    id SERIAL,
    clock timestamp without time zone NOT NULL,
    host_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    item_id integer NOT NULL,
    item_name character varying(255) COLLATE pg_catalog."default",
    ns bigint,
    value double precision,
    data_type integer,
    CONSTRAINT zabbix_data_type_0_pkey PRIMARY KEY (host_name, item_id, clock)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.zabbix_data_type_0
    OWNER to postgres;

GRANT ALL ON TABLE public.zabbix_data_type_0 TO dash;

GRANT ALL ON TABLE public.zabbix_data_type_0 TO grafana;

GRANT ALL ON TABLE public.zabbix_data_type_0 TO postgres;
