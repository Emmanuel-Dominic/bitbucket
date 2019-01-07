# from flask import jsonify
# import datetime


# class Incident:
#     """docstring for Incident."""


#     def __init__(self, createdBy, locationLong, locationLat, comment, images, videos):
#         self.createdOn = datetime.datetime.today()
#         self.locationLong = locationLong
#         self.locationLat = locationLat
#         self.createdBy = createdBy
#         self.comment = comment
#         self.images = images
#         self.videos = videos
#         self.status = "draft"


#     def get_incident_details(self):
#         return {
#             "locationLong": self.locationLong,
#             "locationLat": self.locationLat,
#             "createdOn": self.createdOn,
#             "createdBy": self.createdBy,
#             "type": self.type,
#             "status": self.status,
#             "images": self.images,
#             "videos": self.videos,
#             "comment": self.comment,
#             "incidentId": self.incidentId
#         }


# class RedFlag(Incident):

#     redFlag_Id = 1

#     def __init__(self, createdBy, locationLong, locationLat, comment, images, videos):
#         Incident.__init__(self, createdBy, locationLong, locationLat, comment, images, videos)
#         self.type = 'red-flag'
#         self.incidentId = RedFlag.redFlag_Id
#         RedFlag.redFlag_Id += 1


# class Intervention(Incident):

#     intervention_Id = 1

#     def __init__(self, createdBy, locationLong, locationLat, comment, images, videos):
#         Incident.__init__(self, createdBy, locationLong, locationLat, comment, images, videos)
#         self.type = 'intervention'
#         self.incidentId = Intervention.intervention_Id
#         Intervention.intervention_Id += 1


# def intervention_table():
#     intervention_sql_command ="""
#             select * from intervention;
#             """
# 	self.cursor.execute(intervention_sql_command)
# 	intervention_rows = self.cursor.fetchall()
# 	return intervention_rows

# def redflag_table():
#     redflag_sql_command ="""
#             select * from redflag;
#             """
# 	self.cursor.execute(redflag_sql_command)
# 	redflag_rows = self.cursor.fetchall()
# 	return redflag_rows