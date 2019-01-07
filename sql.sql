SELECT * FROM users

SELECT user_Id,first_Name,last_Name,other_Name,email,
	user_Name,phone_Number,passwd,isAdmin,join_Date FROM users;

-- UPDATE users SET * = '' WHERE user_Id = user_Id;
-- DELETE FROM users WHERE user_Id = user_Id;

SELECT * FROM redflag

SELECT (incident_Id,created_By,incident_Type,comment,status_View,
	images,videos,created_On,latitude,longititude) FROM redflag;

-- UPDATE redflag SET (latitude,longititude) = ('','') WHERE incident_Id = incident_Id;
-- UPDATE redflag SET comment = '' WHERE incident_Id = incident_Id;
-- UPDATE redflag SET status_View = '' WHERE incident_Id = incident_Id;
-- DELETE FROM redflag WHERE incident_Id = incident_Id;



-- UPDATE intervention SET (latitude,longititude) = ('','') WHERE incident_Id = incident_Id;
-- UPDATE intervention SET comment = '' WHERE incident_Id = incident_Id;
-- UPDATE intervention SET status_View = '' WHERE incident_Id = incident_Id;
-- DELETE FROM intervention WHERE incident_Id = incident_Id;

SELECT * FROM intervention

SELECT (incident_Id,created_By,incident_Type,comment,status_View,
	images,videos,created_On,latitude,longititude) FROM intervention;


   SELECT  user_Id,first_Name,last_Name,other_Name,email,
   user_Name,phone_Number,passwd,isAdmin,join_Date
   FROM users
   LEFT JOIN redflag
   ON users.user_Id = redflag.created_By
EXCEPT
   SELECT  user_Id,first_Name,last_Name,other_Name,email,
   user_Name,phone_Number,passwd,isAdmin,join_Date
   FROM users
   RIGHT JOIN redflag
   ON users.user_Id = redflag.created_By;


   SELECT  user_Id,first_Name,last_Name,other_Name,email,
   user_Name,phone_Number,passwd,isAdmin,join_Date
   FROM users
   LEFT JOIN intervention
   ON users.user_Id = intervention.created_By
EXCEPT
   SELECT  user_Id,first_Name,last_Name,other_Name,email,
   user_Name,phone_Number,passwd,isAdmin,join_Date
   FROM users
   RIGHT JOIN intervention
   ON users.user_Id = intervention.created_By;

