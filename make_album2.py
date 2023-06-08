def get_make_album(album_title, artist_name, num_song=None):
	album_info=(f"\n{album_title} by {artist_name}\n")
	return album_info.title()

while True:
	print("Enter 'q' to quit program")

	a_title=input("Album Title: ")
	if a_title=='q':
		break
	a_name=input("Artist Name: ")
	if a_name=='q':
		break

	formatted_album=get_make_album(a_title,a_name)
	print(formatted_album)

