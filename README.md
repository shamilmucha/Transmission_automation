# Transmission_automation
Automatically check the active torrents stops seeding downloaded torrents when all downloads are finished shutting down the system

In Sri Lanka almost all the internet service providers offers night time data to use. But the night time starts at 12 AM local time and ends 6 AM. It's hard to stay awake when the torrents are downloading and shutdown the system when the downloading is finished. if you are downloading multiple downloads. This script is primarily target for those who uses linux systems (I use ubuntu) and transmission as the client for downloading torrents. this script will check if the torrents are active and downloading. if a torrent is downloaded and seeding idle, it will stop seeding the torrent also if all the torrents are downloaded then the system will shutdown. Also regardless the dowonloads if the system time exceeds 5 AM it will shutdown the system, saving you the daytime data. 

As prerequisite this script need to install the latest python version on your desktop and transmission as the default torrent client. 

In future I will extend this script to run this on all operating systems regardless whether you've installed python or not 
