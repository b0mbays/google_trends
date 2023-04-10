# Google Trends Integration for Home Assistant

This custom integration for Home Assistant retrieves the top Google search trends for a specific country and displays them as individual sensor entities.

## Features

- Configurable number of search trends
- Configurable update interval
- Configurable country code for localized trends

## Installation

1. Create a `custom_components` folder in your Home Assistant's `config` directory if it doesn't already exist.
2. Clone or download this repository and copy the `google_trends` folder into the `custom_components` directory.
3. Restart Home Assistant.

## Configuration

To configure the Google Trends integration, go to the Integrations page in the Home Assistant UI, click the "+" button, and search for "Google Trends".

Fill in the following fields:

- `Country`: The country code for the country you want to retrieve trends for (e.g., "united_states" for the United States, "united_kingdom" for the United Kingdom).
- `Number of Trends`: The number of top trends you want to retrieve (e.g., 5, 10).
- `Update Interval`: The interval in minutes at which the trends should update (e.g., 60 for hourly updates).

Click "Submit" to create the integration. The Google Trends sensors will be added to Home Assistant and can be used in automations, scripts, and the UI.

## Example Lovelace Card

Here's an example of a Lovelace card configuration to display the Google Trends sensors:

```yaml
type: 'custom:auto-entities'
card:
  type: entities
  title: Google Trends
filter:
  include:
    - entity_id: sensor.google_trend_*