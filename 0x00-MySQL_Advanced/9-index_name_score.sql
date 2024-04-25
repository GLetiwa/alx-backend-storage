-- Creates an index on the table and the the first letter of the specified column
CREATE INDEX idx_name_first_score
ON names(name(1), score)
