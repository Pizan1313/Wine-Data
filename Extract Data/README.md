# Parsing Vivino
This is a data science project that involves web scraping data from vivino.com, a wine review website. The project collects information about wines and their bottle images, and enriches the data with additional details based on the creator's 6-year experience as a sommelier. The project is implemented in Jupyter Notebook.

## Libraries Used
The following libraries were used in this project:

- **fake_useragent** - for generating fake user agents to mimic browser requests
- **beautifulsoup4** - for parsing HTML content
- **pandas** - for data manipulation and analysis
- **requests** - for making HTTP requests
- **tqdm** - for displaying progress bars during data scraping
- **numpy** - for numerical computing
- **os** - for file and directory operations
- **sanitize_filename** - for sanitizing filenames before saving files
- **os.path** - for additional file and directory operations
- **yadisk** - for uploading files to Yandex.Disk
## Usage
The main file for running the web scraping process is called "Parsing Vivino Main.ipynb". In this file, the following parameters need to be specified:

- <code>start</code> - the starting ID for scraping
- <code>end</code> - the ending ID for scraping
- <code>path</code> - the directory path for saving scraped data
- <code>file_name</code> - the name of the file to save the scraped data as an Excel file
- <code>token</code> - the access token for Yandex.Disk for uploading files (if save_to_YD is set to True)
- <code>save_to_YD</code> - a boolean flag indicating whether to save the data to Yandex.Disk or not
- <code>tg_api_token</code> - the API token for Telegram for sending messages to a Telegram bot
- <code>tg_chat_id</code> - the chat ID of the Telegram bot for sending messages
After setting these parameters, the "Parsing Vivino Main.ipynb" file can be executed to start the web scraping process. The scraped data will be saved as an Excel file in the specified directory, and a message will be sent to the specified Telegram bot indicating that the parsing process has completed.

**Note:** If you do not want to save the data to Yandex.Disk, set save_to_YD to False.
