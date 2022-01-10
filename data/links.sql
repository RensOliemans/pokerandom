CREATE TABLE link (
    entrance TEXT NOT NULL UNIQUE,
    destination TEXT NULL,
    one_way INTEGER NOT NULL DEFAULT 0,
    block TEXT NULL
);