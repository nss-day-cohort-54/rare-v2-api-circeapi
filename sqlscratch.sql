DELETE FROM rareapi_post;
DELETE FROM rareapi_comment;

UPDATE rareapi_post
SET author_id = 1
WHERE id = 1

INSERT INTO rareapi_admin 
('id', 'user_id', 'avatar')
VALUES (2,2,"")


INSERT INTO rareapi_category
('id', 'label')
VALUES (2,'abra')

INSERT INTO rareapi_category
('id', 'label')
VALUES (3,'zabra')

UPDATE auth_user
SET is_staff = 1
WHERE id = 5

UPDATE rareapi_author
SET user_id = 3
WHERE id = 3

UPDATE rareapi_author
SET user_id = 5
WHERE id = 5

UPDATE rareapi_post
SET approved = 0
WHERE id = 3