#!/usr/bin/env python2.7

import json

with open('../data.json') as f:
    data = json.load(f)

for i in data['data']:
    tooltips = "<span class='tooltip'>";
    for j in i['Locations'].split("; "):
        tooltips += j + "<br>";
    tooltips += "</span>"
    links = "";
    for k in i['Links']:
        links += "<a href=\"" + k['link_url'] + "\" target=\"_blank\">" + k['link_desc'] + "</a>";
    if i['Coupon']:
        links += "<span class=\"coupon\">'" + i['Coupon'] + "'</span>"
    if i['Note']:
        links += "<span class=\"note\">" + i['Note'] + "</span>"
    line = "<tr>\n" + \
        "\t<td><a href=\"" + i['Provider_URL'] + "\" target=\"_blank\">" + i['Provider'] + "</a></td>\n" + \
        "\t<td>" + i['Region'] + tooltips + "</td>\n" + \
        "\t<td>" + i['Space'] + "</td>\n" + \
        "\t<td>" + i['Bandwidth'] + "</td>\n" + \
        "\t<td>" + i['Port_Speed'] + "</td>\n" + \
        "\t<td>" + i['CPUs'] + "</td>\n" + \
        "\t<td>" + i['RAM'] + "</td>\n" + \
        "\t<td>" + i['IPv4'] + "</td>\n" + \
        "\t<td>" + i['IPv6'] + "</td>\n" + \
        "\t<td>" + i['VZ_Type'] + "</td>\n" + \
        "\t<td>" + i['Price'] + "</td>\n" + \
        "\t<td>" + i['Value'] + "</td>\n" + \
        "\t<td>" + links + "</td>\n" + \
        "</tr>\n";

    print line
