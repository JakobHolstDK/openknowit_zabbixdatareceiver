-- Table: public.zabbix_data_type_4

-- DROP TABLE IF EXISTS public.zabbix_data_type_4;

CREATE TABLE IF NOT EXISTS zabbix_data_type_4
(
    id SERIAL,
    clock timestamp without time zone NOT NULL,
    host_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    item_id integer NOT NULL,
    item_name character varying(255) COLLATE pg_catalog."default",
    ns bigint,
    fsname character varying(512) COLLATE pg_catalog."default" NOT NULL,
    options character varying(512) COLLATE pg_catalog."default",
    bytes_used bigint,
    bytes_free bigint,
    bytes_total bigint,
    bytes_pused double precision,
    bytes_pfred double precision,
    fstype character varying(24) COLLATE pg_catalog."default",
    inodes_used bigint,
    inodes_free bigint,
    inodes_total bigint,
    inodes_pused double precision,
    inodes_pfree double precision,
    CONSTRAINT zabbix_data_type_4_pkey PRIMARY KEY (fsname, clock, host_name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.zabbix_data_type_4
    OWNER to postgres;

GRANT ALL ON TABLE public.zabbix_data_type_4 TO dash;

GRANT ALL ON TABLE public.zabbix_data_type_4 TO grafana;

GRANT ALL ON TABLE public.zabbix_data_type_4 TO postgres;


