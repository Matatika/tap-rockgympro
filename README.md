# tap-rockgympro

This is a [Singer](https://singer.io) tap that implements the [RockGymPro] API(https://api.rockgympro.com/)

This tap:
- Implements the following endpoints:
    - [Bookings](https://api.rockgympro.com/#/Bookings)
    - [Customers](https://api.rockgympro.com/#/Customers)
    - [Facilities](https://api.rockgympro.com/#/Facilities)

Caveats:
- Bookings endpoint
    - There is no way to filter by only newly updated bookings.  You can filter by when a booking was created but you can't filter by when
    a booking was cancelled so this tap will fetch all bookings looking for updated bookings based on the state.
- Customers endpoint
    - There is no way to loop through all of the customers so customers are fetched as a byproduct of other endpoints that reference customers.
    For example, bookings reference customers so we batch booking records to fetch several customers first.
- Timezones
    - I'm still not sure about timezones.  The Facilities endpoint doesn't return any timezones so this tap assumes all times are in UTC (which is probably incorrect)


## Quick Start

1. Install

    pip install git+https://github.com/cinchio/tap-rockgympro

2. Create the config file

   Create a JSON file called `config.json`. Its contents should look like:

   ```json
    {
        "api_user": "myuser",
        "api_key": "myapikey"
    }
    ```

   To generate an API key refer to the [documentation](https://support.rockgympro.com/hc/en-us/articles/360056602652-Generate-API-Key-for-RGP-Cloud)

4. Run the Tap in Discovery Mode

    tap-rockgympro -c config.json -d

   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode).

5. Run the Tap in Sync Mode

    tap-shopify -c config.json
