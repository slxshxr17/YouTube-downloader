from pytube import YouTube
import sys
def YoutubeDownloadVideo(link, destination):
	'''Downloading the video with best resolution from YouTube.'''
	try:
		video = YouTube('{}'.format(link)).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
		print("Downloading best resolution video, please wait...")
		video.download(destination)
		print("Downloaded.")
	except:
		print("Error.")
	exit(0)
def YoutubeDownloadMusic(link, destination):
	'''Downloading the song from YouTube.'''
	try:
		video = YouTube('{}'.format(link)).streams.filter(type='audio', file_extension='mp3').first()
		print("Downloading...")
		video.download(destination)
		print("Downloaded.")
	except:
		print("Error.")
	exit(0)
def YouTubeDownloadFormat(link, destination, formatt):
	'''Downloading specific video format'''
	try:
		video = YouTube('{}'.format(link)).streams.filter(progressive=True, file_extension='mp4', res='{}p'.format(formatt)).desc().first()
		print("Downloading...")
		video.download(destination)
		print("Downloaded.")
	except:
		print("Error.")
		exit(0)
def destinationPathChange(dest):
	'''Sets user's destination folder to download videos.'''
	f = open("destination.txt", "w")
	f.write(dest)
	print("Done, new destination is: " + destinationPathGet())
	exit(0)
def destinationPathGet():
	'''Returns user's destination folder for downloading videos.'''
	f = open("destination.txt", "r")
	return f.read()
def main():
	print("Choose what you want to do/download: ")
	print("--------------------------")
	print("1. Video in best resolution.")
	print("2. Mp3 file.")
	print("3. Different video resolution.")
	print("4. Change download destination.")
	try:
		a = int(input())
	except:
		print("Error.")
		exit(0)
	if (a==4):
		print("Insert download destination, it should look like this: " + str(r'C:\Users\USERNAME\Downloads'))
		c = input()
		destinationPathChange(c)
	elif (a==1 or a==2 or a==3):
		link = input("Paste link URL: ")
		if (a==1):
			YoutubeDownloadVideo(link, destinationPathGet())
		elif (a==2):
			YoutubeDownloadMusic(link, destinationPathGet())
		elif (a==3):
			print("Choose a video resolution: ")
			print("--------------------------")
			print("1. 1080P VIDEO")
			print("2. 720P VIDEO")
			print("3. 480P VIDEO")
			print("4. 360P VIDEO")
			print("5. 144P VIDEO")
			b = int(input())
			if (b==1):
				YouTubeDownloadFormat(link, destinationPathGet(), 1080)
			elif (b==2):
				YouTubeDownloadFormat(link, destinationPathGet(), 720)
			elif (b==3):
				YouTubeDownloadFormat(link, destinationPathGet(), 480)
			elif (b==4):
				YouTubeDownloadFormat(link, destinationPathGet(), 360)
			elif (b==5):
				YouTubeDownloadFormat(link, destinationPathGet(), 144)
			else:
				print("Error.")
				exit(0)
	else:
		print("Error.")
		exit(0)
main()
	
