DELETE FROM rareapi_post;
DELETE FROM rareapi_comment;

UPDATE rareapi_post
SET approved = 0
WHERE id = 6

INSERT INTO rareapi_admin 
('id', 'user_id', 'avatar')
VALUES (2,2,"")


INSERT INTO rareapi_category
('id', 'label')
VALUES (2,'abra')

INSERT INTO rareapi_category
('id', 'label')
VALUES (3,'zabra')

