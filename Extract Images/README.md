# Image Parsing with Telegram Notification

This repository contains Python code for image parsing and sending a Telegram notification. It includes two functions:

1. `parsing_img(folder_from, file_name, folder_to, final_folder)`: This function reads an Excel file (`file_name.xlsx`) from a specified folder (`folder_from`) and parses image URLs from the 'img_large' column. It then downloads the images, crops them, and saves them to a different folder (`folder_to`) with a modified filename. The cropped images are also saved to a final folder (`final_folder`).

2. `save_img_to_YDisk(final_folder, token, y_folder)`: This function uploads the cropped images from the `final_folder` to a specified folder on Yandex.Disk (a cloud storage service) using a provided access token (`token`). It uses the `yadisk` library to interact with the Yandex.Disk API.

## Prerequisites

Before using these functions, please make sure you have the following:

- Python 3.x installed
- Required libraries: `pandas`, `requests`, `os`, `sanitize_filename`, `PIL`, `sys`, `tqdm`, and `yadisk`
- Telegram bot and chat ID: You need to create a Telegram bot, obtain the bot token, and get the chat ID where you want to send notifications. Update the code with the bot token and chat ID.

## Usage

1. Clone the repository to your local machine.
2. Import the functions `parsing_img` and `save_img_to_YDisk` in your Python script.
3. Use the functions in your code by providing the required arguments.
4. Make sure to update the bot token, chat ID, and other necessary parameters as needed.
5. Run your Python script to execute the image parsing and Telegram notification.

Example usage:

```python
# Import the functions
from image_parser import parsing_img, save_img_to_YDisk

# Call the image parsing function
parsing_img(folder_from, file_name, folder_to, final_folder)

# Call the image upload function
save_img_to_YDisk(final_folder, token, y_folder)

# Call the Telegram notification function (if desired)
send_tg_message(text='Parsing of photos completed.')
```

Note: You may need to install the required libraries using pip or conda before running the code.

## Contributing
If you wish to contribute to this project, feel free to submit a pull request with your changes. You can also open issues for bug reports, feature requests, or general feedback.
