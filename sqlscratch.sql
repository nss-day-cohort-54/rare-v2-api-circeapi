DELETE FROM rareapi_post;
DELETE FROM rareapi_comment;

UPDATE auth_user
SET is_staff = 1
WHERE id = 2

INSERT INTO rareapi_admin 
('id', 'user_id', 'avatar')
VALUES (2,2,"")


INSERT INTO rareapi_category
('id', 'label')
VALUES (2,'abra')

INSERT INTO rareapi_category
('id', 'label')
VALUES (3,'zabra')

