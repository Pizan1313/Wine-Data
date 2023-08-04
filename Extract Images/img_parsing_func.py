#!/usr/bin/env python
# coding: utf-8

# # Extracting Cropped Images

# ## Libraries

# In[1]:


# Import libraries
import pandas as pd
import requests
import os
from sanitize_filename import sanitize
import os.path
import warnings
warnings.filterwarnings("ignore")
from PIL import Image
import sys
import requests

from tqdm.auto import tqdm
import yadisk

# Yandex Disk token
token = ''

# Telegram API token and chat ID
tg_api_token = ''
tg_chat_id = ''


# ## Extracting, cropping and saving image

# In[2]:


def parsing(folder_from, file_name, folder_to, final_folder):
    
    # Read Excel file
    df = pd.read_excel(os.path.join(folder_from, file_name +'.xlsx'), usecols=['img_large', 'wine_id'])
    
    # Drop rows with NaN values in 'img_large' column
    df = df.dropna(subset=['img_large']).reset_index(drop=True)

    # Loop through each row in the DataFrame
    for i in tqdm(range(len(df))):
        try:
            # Get the image URL
            img_large = df['img_large'][i]

            # Get the wine ID as the filename
            directory = sanitize(str(df['wine_id'][i]))

            # Set the parent directory for the original and cropped images
            parent_dir_large = folder_to
            parent_crop_large = final_folder

            # Set the file path for the original image
            path_large = os.path.join(parent_dir_large, directory)

            # Set the file path for the original image with extension
            IMG_large = os.path.join(parent_dir_large, directory + '.png') 

            # Open a blank file to write the image content
            file_large = open(IMG_large, "wb")

            # Write the image content to the file
            file_large.write(requests.get('http:' + str(img_large)).content)
            
            # Open the image in RGB mode
            img = Image.open(os.path.join(parent_dir_large, directory + '.png'))

            # Crop the image to remove the VIVINO watermark and neck of the bottle
            width, height = img.size
            img1 = img.crop((0, 250, width, height - 55))

            # Save the cropped image
            img1.save(os.path.join(parent_crop_large, directory + '.png'))
            
        except:
            pass


# <div style='border-radius: 15px; box-shadow: 2px 2px 2px; border: 1px solid green; padding: 20px'>
# This function appears to parse image URLs from an Excel file and download and process the images using the Pillow library.
#     
# - The function reads an Excel file with a specified filename and sheet ('img_large' and 'wine_id' columns are used), drops rows with NaN values in the 'img_large' column, and then loops through each row.
# - For each row, it downloads the image from the provided URL using the 'requests' library, saves it as a PNG file in the specified 'folder_to' directory, and then crops the image to remove a watermark and neck of the bottle using the Pillow library. - The cropped image is then saved in the 'final_folder' directory with the same wine ID as the filename.
# - Any exceptions that occur during image processing are ignored ('except: pass').    
# </div>

# ## Saving to Yandex Disk

# In[3]:


def save_img_to_YDisk(final_folder,token,y_folder):
    
    y = yadisk.YaDisk(token=token)

    if y.check_token() == True:
        for filename in tqdm(os.listdir(final_folder)):
            try:
                y.upload(os.path.join(final_folder, filename), y_folder+filename)
            except: print(f'Wine photo {filename} is already on disk')
    else: print('YandexDisk token entered incorrectly, check the Token')


# <div style='border-radius: 15px; box-shadow: 2px 2px 2px; border: 1px solid green; padding: 20px'>
# This function appears to upload images to Yandex.Disk (a cloud storage service) using the 'yadisk' library.
#     
# - The function takes three arguments: 'final_folder' (the directory where the images are stored), 'token' (the Yandex.Disk access token), and 'y_folder' (the Yandex.Disk folder where the images will be uploaded).
# - It uses the 'yadisk' library to create a Yandex.Disk object with the provided access token and then checks if the token is valid using the 'check_token()' method.
# - If the token is valid, the function loops through each file in the 'final_folder' directory, and uploads the file to Yandex.Disk with the same filename in the specified 'y_folder' using the 'upload()' method.
# - If the token is invalid, it prints an error message indicating that the token is incorrect. If any exceptions occur during the file upload, it prints a message indicating that the image already exists on Yandex.Disk.    
# </div>

# ## Sending message to Telegram Bot

# In[4]:


def send_tg_message(tg_api_token,tg_chat_id,text='Parsing of photos completed.'):
    requests.post('https://api.telegram.org/' + 'bot{}/sendMessage'.format(tg_api_token),
                  params=dict(chat_id=tg_chat_id, text=text))


# <div style='border-radius: 15px; box-shadow: 2px 2px 2px; border: 1px solid green; padding: 20px'>
# This function appears to send a text message to a specified chat in Telegram using the Telegram Bot API.
# 
# - The function takes an optional argument 'text' which represents the message to be sent. The default value is 'Parsing of photos completed.' if no text is provided.
# - It uses the 'requests' library to send a POST request to the Telegram Bot API with the chat ID, text message, and bot token ('tg_api_token') as parameters.
# - The chat ID and bot token are expected to be defined elsewhere in the code.    
# </div>

# ## Final function

# In[5]:


def parsing_img(folder_from, file_name, folder_to, final_folder,token,y_folder,tg_api_token,tg_chat_id,YDisk, TG):
    parsing(folder_from, file_name, folder_to, final_folder)
    if YDisk == True:
        save_img_to_YDisk(final_folder,token,y_folder)
    else: pass
    if TG == True:
        send_tg_message(tg_api_token,tg_chat_id,text='Parsing of photos completed.')
    else: pass

