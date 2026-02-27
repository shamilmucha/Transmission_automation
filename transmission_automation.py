from itertools import count
from transmission_rpc import Client
from transmission_rpc.error import TransmissionError
import os
from datetime import datetime

def has_active_torrents(client):
    torrents = client.get_torrents()

    return any(
        t.rate_download > 0 or t.rate_upload > 0
        for t in torrents
    )


def shutdown_now():
    os.system('shutdown -h now')
    #print('Shutting down now...')



def stop_seeding_torrents(client):
    torrents = client.get_torrents()
    seeding = [t for t in torrents if t.status == "seeding"]

    if not seeding:
        print("No seeding torrents found.")
        return

    for t in seeding:
        client.stop_torrent(t.id)
        print(f"Stopped: {t.name}")


def all_downloaded(client):
    torrents = client.get_torrents()
    downloading = [t for t in torrents if t.status == "downloading"]

    if not downloading:
        shutdown_now()
    else:
        return
    

def main():
    try:
        client = Client(
            host="localhost",
            port=9091,
            #if uses authentication
            username="UserName",
            password="Password"
        )

        #print("Connected to Transmission RPC")

        if has_active_torrents(client):
            all_downloaded(client)
            stop_seeding_torrents(client)
            currnt_time = datetime.now().time()
            #print(currnt_time)
            if currnt_time.hour >= 5 and currnt_time.hour < 6:
                shutdown_now()
            else:
                return
            
        else:
            return

    except TransmissionError as e:
        print("Transmission RPC error")
        print(e)
    except Exception as e:
        print("Unexpected error")
        print(e)


if __name__ == "__main__":
    main()
