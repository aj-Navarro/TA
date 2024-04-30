import requests
import zipfile
import io
import os

def fetch_latest_chromedriver_version():
    url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        print("Failed to fetch latest version number.")
        return None

def download_chromedriver(version):
    url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_mac64.zip"
    response = requests.get(url)
    if response.status_code == 200:
        zip_data = io.BytesIO(response.content)
        with zipfile.ZipFile(zip_data, "r") as zip_ref:
            zip_ref.extractall()
        print("ChromeDriver downloaded successfully.")
    else:
        print("Failed to download ChromeDriver.")

if __name__ == "__main__":
    latest_version = fetch_latest_chromedriver_version()
    if latest_version:
        download_chromedriver(latest_version)
    else:
        print("Script terminated.")
