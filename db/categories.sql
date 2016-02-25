begin;

delete from contacts;
insert into contacts (
category, email, body_id,
confirmed, deleted, editor, whenedited, note
)
select column1,
'davea@mysociety.org',       -- the email address for all contacts
body_id,                     -- the Body ID
true, false,
'Dave A (via SQL)',        -- editor
NOW(),
'initial import from SQL' -- note
from (values
  ('Put up birdbox'),
  ('Planted flowers'),
  ('Noticed a bird'),
  ('Noticed a butterfly')
) c,
(select id as body_id from body) b;

commit;