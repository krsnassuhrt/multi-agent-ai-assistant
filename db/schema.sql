-- ==============================
-- TASKS TABLE
-- ==============================
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    task TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ==============================
-- EVENTS TABLE
-- ==============================
CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    event TEXT NOT NULL,
    event_time VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ==============================
-- NOTES TABLE
-- ==============================
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    note TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);