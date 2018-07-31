# [LowEndStorage](https://www.lowendstorage.win)

This site compiles a list of Low End Storage solutions into a sortable table to analyze all options.

The jQuery plug-in, [DataTables](https://datatables.net/), is used to structure and sort the data.

All prices are in USD. Foreign currencies are converted to USD and may not be accurate at time of viewing.

## General Requirements

General requirements for services that are presented in this table:
1. Provider offers a plan with storage of >= 250GB
2. Price of the storage plan is <= $10/mo

## Data

Data that is used to populate the table is stored within the [data.json](data.json) file.

Due to a limitation of the DataTables plug-in, the table rows need to be generated and placed within the HTML file prior to rendering the webpage. Because of this, a Python utility dubbed, 'build_rows.py', has been created to automatically read in the data.json file and generate the HTML code for the table rows. Then the rows that are spit out can be dumped within the index.html page between the two markers.

```bash
./build_rows.py > table-rows.html
```

## How to Suggest a Change/Addition/Deletion

There are multiple ways that you can help contribute to this project to propose a change.

1. Fork the project, make your edits, and submit a Pull Request. Please conform to the json structure indicated below.
2. Open a GitHub issue with details on the edits you'd like to see incorporated. Be as specific as possible and include all relevant information (i.e. fields for the json structure if submitting an addition).
3. Email me with your proposed changes.
4. [PM me on LowEndTalk](https://www.lowendtalk.com/profile/MasonR) or post in the [LowEndStorage.win LET thread](https://www.lowendtalk.com/discussion/129707/introducing-lowendstorage-win-a-comprehensive-list-of-lowend-storage-vps-providers).

## Data json Structure

Blank structure:

```json
{
  "data": [
    {
      "Provider": "",
      "Provider_URL": "",
      "Region": "",
      "Locations": "",
      "Space": "",
      "Bandwidth": "",
      "Port_Speed": "",
      "CPUs": "",
      "RAM": "",
      "IPv4": "",
      "IPv6": "",
      "VZ_Type": "",
      "Price": "",
      "Value": "",
      "Links": [{
        "link_desc": "",
        "link_url": ""
      }],
      "Coupon": "",
      "Note": ""
    }
  ]
}
```

| Field | Required? | Description |
|---|---|---|
| Provider | Required | Name of the provider |
| Provider_URL | Required | URL to the homepage of the provider |
| Region | Required | Region that the provider offers storage within (NA, EU, APAC, etc.) |
| Locations | Required | List out all cities/countries that the provider offers the storage plan (each separated by a semicolon and space) |
| Space | Required | The amount of space (in GigaBytes) of the cheapest or best storage offer that meets the requirements posted above |
| Bandwidth | Required | The amount of bandwidth (in TeraBytes per month) of the offer |
| Port_Speed | Required | The speed of the internet connection of the plan (in Gigabits per second) |
| CPUs | Required | Number of CPUs or vCPUs that are included as part of the plan |
| RAM | Required | The amount of RAM (in GigaBytes) of the offer |
| IPv4 | Required | If any IPv4 addresses are included in the plan (possible options - Yes, NAT, No) |
| IPv6 | Required | If any IPv6 addresses are included in the plan (possible options - Yes, No, ?) |
| VZ_Type | Required | The type of virtualization of the plan (possible options - OpenVZ, KVM, Xen, LXC) |
| Price | Required | The monthly price of the plan (non-monthly plans should be the plan price divided by the number of months the period covers) |
| Value | Required | A calculation of the number of the cost per month divided by number of TeraBytes of storage space, resulting in $/TB/mo |
| Links | Required | _(1-to-many)_ Includes the link to purchase the offer, link to the LowEndTalk thread, link to the LowEndBox post, etc. |
| Coupon | Optional | Coupon code if it is required to purchase the plan at the stated price |
| Note | Optional | Notes can be included, if needed (e.g. to indicate out of stock or if the product is a pre-order deal, etc.) |

Example:

```json
{
  "data": [
    {
      "Provider": "MyFakeHost",
      "Provider_URL": "https://www.myfakehost.net",
      "Region": "EU+NA",
      "Locations": "Chicago, IL; Paris, France",
      "Space": "500",
      "Bandwidth": "5",
      "Port_Speed": "1",
      "CPUs": "2",
      "RAM": "1",
      "IPv4": "NAT",
      "IPv6": "Yes",
      "VZ_Type": "OpenVZ",
      "Price": "$2",
      "Value": "$4",
      "Links": [{
        "link_desc": "LET Offer",
        "link_url": "https://www.lowendtalk.com/link/to/offer/thread"
      }, {
        "link_desc": "Order",
        "link_url": "https://www.myfakehost.net/billing/link/to/order"
      }],
      "Coupon": "FartMother",
      "Note": "Pre-Order"
    }
  ]
}
```

## License
```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2018 Mason Rowe <mason@rowe.sh>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
```
