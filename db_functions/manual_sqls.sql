CREATE table "public".time_tracking_info (
    "ID" integer constraint time_tracking_pkey primary key,
    is_tracked_1min boolean not null default false,
    is_tracked_1day boolean not null default false,
    stock integer not null,
    worker_name varchar(35) not null,
    constraint stock_id foreign key (stock) references "public".stocks("ID")
);

CREATE VIEW "public".tracked_indexes AS
    SELECT
    intermediate.name as "equity_name",
    intermediate.symbol,
    m.name as "market_name",
    intermediate.is_tracked_1day,
    intermediate.is_tracked_1min,
    intermediate.worker_name
    FROM (
        SELECT s.name, s.exchange, s.symbol, t_trk.is_tracked_1min, t_trk.is_tracked_1day ,t_trk.worker_name
        FROM "public".time_tracking_info t_trk
        LEFT JOIN "public".stocks s
        on t_trk.stock = s."ID"
    ) intermediate
    LEFT JOIN "public".markets m
    on intermediate.exchange = m."ID";