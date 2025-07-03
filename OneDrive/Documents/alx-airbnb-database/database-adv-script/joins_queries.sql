-- 1. INNER JOIN: Get all bookings and the users who made them
SELECT bookings.id AS booking_id, users.id AS user_id, users.name, users.email
FROM bookings
INNER JOIN users ON bookings.user_id = users.id;

-- 2. LEFT JOIN: Get all properties and their reviews (including properties with no reviews)
SELECT properties.id AS property_id, properties.name AS property_name, reviews.id AS review_id, reviews.comment
FROM properties
LEFT JOIN reviews ON properties.id = reviews.property_id;

-- 3. FULL OUTER JOIN: Get all users and bookings (include unmatched records)
SELECT users.id AS user_id, bookings.id AS booking_id
FROM users
LEFT JOIN bookings ON users.id = bookings.user_id

UNION

SELECT users.id AS user_id, bookings.id AS booking_id
FROM users
RIGHT JOIN bookings ON users.id = bookings.user_id;

