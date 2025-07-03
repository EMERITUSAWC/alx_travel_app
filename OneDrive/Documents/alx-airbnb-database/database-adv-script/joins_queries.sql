-- INNER JOIN: Get all bookings and the users who made them
SELECT bookings.id, users.name
FROM bookings
INNER JOIN users ON bookings.user_id = users.id;

-- LEFT JOIN: Get all properties and their reviews (including properties with no reviews)
SELECT properties.name, reviews.comment
FROM properties
LEFT JOIN reviews ON properties.id = reviews.property_id;

-- FULL OUTER JOIN: Get all users and bookings, even if there's no matching record
SELECT users.name, bookings.id
FROM users
FULL OUTER JOIN bookings ON users.id = bookings.user_id;

