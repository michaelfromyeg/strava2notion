# strava2notion

<p align="center">
  <img src="images/strava_icon.png" alt="Strava" width="32" height="32">
  <img src="images/notion_icon.png" alt="Notion" width="32" height="32">
</p>

Sync your Strava reviews to a Notion database!

Inspired by [@IVIURRAY](https://github.com/IVIURRAY/strava2notion) and [@kevinschaich](https://github.com/kevinschaich/strava-to-notion).

## Setup

1. Create an app though the [Strava API](https://strava.com/settings/api); you can use [this image](./images/notion_icon.png) for the icon
2. Insert `Client ID` and `Client Secret` into your `.env`
3. Create an app through the [Notion API](https://notion.so); you can use [this image](./images/strava_icon.png) for the icon
4. Add your secret as `TOKEN_V3` in your `.env`
5. Create a database (create this as a blank database page) in Notion and copy the ID to config file; see ["Finding your Notion database ID"](#finding-your-notion-database-id)
6. Give your Notion integration access to the database (under the `Share` button)
7. Add the relevant columns to the database; the default needs: Name, Type (select), Length (number), Time (number), Date (date), Power (number), Elevation (number), Strava Link (URL)
    - You can customize these in the `notion_api_new.py` file.

### Finding your Notion database ID

Copy the link to your database page that will look like: `https://www.notion.so/<long_hash_1>?v=<long_hash_2>` then choose `<long_hash_1>`, this is the database ID.

## Usage

1. `gh repo clone michaelfromyeg/strava2notion`
2. `cd strava2notion`
3. `python3.12 -m venv env`
4. `source env/bin/activate`
5. `pip install --upgrade pip`
6. `pip install -r requirements.txt`
7. `make run`
    - This will open a browser to ask you to authenticate the integration; if you're on WSL, I recommend using `google-chrome` via WSLg.
    - For subsequent runs set `ALL_DATA` in `config.py` to `False` to upload only new activities.
    - You can also run it via Windows Task Scheduler (use the `.bat` file) or on a related service (e.g., as a `cronjob`)

The `notion_api_test.py` file is left in for you to test adding different data to the database. See [Strava API](https://developers.strava.com/docs/reference) for what other data is taken from the API request.

## Documentation

The HTTP Requests are abstracted away by two helpful libraries: [stravio](https://github.com/sladkovm/stravaio) and [notion-sdk-py](https://github.com/ramnes/notion-sdk-py).

Their documentation coupled with the official API documentation is useful for debugging and customization.
