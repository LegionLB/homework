#1==============================================
#THE DICT
# a_dict = {
#   "type": "FeatureCollection",
#   "features": [
#     {
#       "type": "Feature",
#       "properties": {},
#       "geometry": {
#         "type": "Polygon",
#         "coordinates": [
#           [
#             [
#               69.2578125,
#               30.031055426540206
#             ],
#             [
#               72.2900390625,
#               30.031055426540206
#             ],
#             [
#               72.2900390625,
#               31.50362930577303
#             ],
#             [
#               69.2578125,
#               31.50362930577303
#             ],
#             [
#               69.2578125,
#               30.031055426540206
#             ]
#           ]
#         ]
#       }
#     },
#     {
#       "type": "Feature",
#       "properties": {},
#       "geometry": {
#         "type": "Polygon",
#         "coordinates": [
#           [
#             [
#               73.037109375,
#               31.16580958786196
#             ],
#             [
#               74.3994140625,
#               31.16580958786196
#             ],
#             [
#               74.3994140625,
#               31.87755764334002
#             ],
#             [
#               73.037109375,
#               31.87755764334002
#             ],
#             [
#               73.037109375,
#               31.16580958786196
#             ]
#           ]
#         ]
#       }
#     },
#     {
#       "type": "Feature",
#       "properties": {},
#       "geometry": {
#         "type": "Point",
#         "coordinates": [
#           73.4326171875,
#           30.600093873550072
#         ]
#       }
#     }
#   ]
# }
#
# def get(the_dict):
#     coordinates = []
#     for i in the_dict.get("features"):
#         coordinates.append(i.get('geometry').get('coordinates'))
#     return coordinates
# print(get(a_dict))

#2=================================================
#