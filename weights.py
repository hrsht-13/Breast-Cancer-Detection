from google_drive_downloader import GoogleDriveDownloader as gdd
def download_weights():
    gdd.download_file_from_google_drive(file_id="1--7p9rRJy7WU4OmomkzM8i0veetZctTT",
                                        dest_path ="weights/modeldense1.h5" )
