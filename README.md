This project contains a working django application where, eventually, users would be able to search for and store videos from
boilerroom. It currently consists of only two views, which are not implemented - localhost/boilerroomyoutube/, where the 
view allowing users to upload videos would exist, and the default admin page.

The admin page allows users to view and edit any of the YoutubeVideo objects that have been created in the DB, should
this be preferable over terminal use.

At present, there are just two api functions, found in api.py. The first takes a channel_id and an API token, returning the
most recent video, represented as json, for given channel_id. The second converts this response json into a YoutubeVideo object.


Given more time, the next steps in order would be:

1. Implement the view for /boilerroomyoutube in order to display the most recently entered item from the DB
2. Add user functionality in said view which would call get_latest_youtube_video for boilerroom.
3. Implement the api functions necessary for display of a page's worth of existing Youtube Videos.
4. Add these functions to the view as necessary
5. Tests

