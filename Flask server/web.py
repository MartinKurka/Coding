from wheather_api import DayInWeek, api_req
from datetime import datetime

forecast = []
current_day = ''


def main(coordinations, city):
    global forecast
    forecast = api_req(coordinations)
    send_html = update(city)
    send_html.encode('utf-8')
    return send_html

def bot_send_forecast():
    result = ""
    city = "Milovice"
    coordinations = {"lat": 50.22622179742758, "lon": 14.870976579184042}
    forecast = api_req(coordinations)
    result += city + '\n'

    result += "Teplota: " + str(forecast["current"]["temp"])+ '\n'
    result += "Vlhkost: " + str(forecast["current"]["humidity"])+ '\n'
    result += "Tlak: " + str(forecast["current"]["pressure"])+ '\n'
    result += "Vítr, rychlost: " + str(forecast["current"]["wind_speed"])+ '\n'
    result += "Vítr, směr: " + str(forecast["current"]["wind_deg"])+ '\n'
    result += "Mraky: " + str(forecast["current"]["clouds"])+ '\n'
    result += str(forecast["current"]["weather"][0]["main"]) + " - " + str(forecast["current"]["weather"][0]["description"]) + '\n'
    return result


def update(city):
    global current_day
    current_day = int(datetime.utcfromtimestamp(forecast["current"]["dt"] + forecast["timezone_offset"]).strftime('%d'))
    str_current_day = DayInWeek[datetime.utcfromtimestamp(forecast["current"]["dt"] + forecast["timezone_offset"]).weekday()]
    str_current_time = datetime.utcfromtimestamp(forecast["current"]["dt"] + forecast["timezone_offset"]).strftime('%d-%m-%Y %H:%M')
    send_date_to_forecast = str_current_day + " - " + datetime.utcfromtimestamp(forecast["current"]["dt"] + forecast["timezone_offset"]).strftime('%d-%m-%Y')
    # print(f"current day: {current_day}")
    css_table = """<style> table, th, td {border:1px solid black;}</style>"""
    send = f"""
    <head>
        <meta charset="UTF-8">
    </head>
    {css_table}
    <body>
    <p>
    <h1>{city}</h1>
    <h2>Aktuálně</h2>
    </p>
    <table style="width:100%">
    <tr>
        <th>{str_current_day}</th>
        <th>Teplota</th>
        <th>Vlhkost</th>
        <th>Tlak</th>
        <th>Vítr, rychlost</th>
        <th>Vítr, směr</th>
        <th>Mraky</th>
        <th>Počasí</th>
        <th>Info</th>
    </tr>
    <tr>
        <td>{str_current_time}</td>
        <td>{forecast["current"]["temp"]} &#8451; </td>
        <td>{forecast["current"]["humidity"]} %</td>
        <td>{forecast["current"]["pressure"]} kPa</td>
        <td>{forecast["current"]["wind_speed"]} m/s</td>
        <td>{forecast["current"]["wind_deg"]} &#x00B0;</td>
        <td>{forecast["current"]["clouds"]} %</td>
        <td>{forecast["current"]["weather"][0]["main"]} - {forecast["current"]["weather"][0]["description"]}</td>
        <td><img src="https://icon-library.com/images/disconnect-icon/disconnect-icon-11.jpg" width="20" height="20" style="float:center"></td>
    </tr>
    </table>
    </p>
    <img src="https://cdn-icons-png.flaticon.com/512/252/252035.png" width="20" height="20">
    <br>
    <p>
    <h2>Předpověd</h2>
    </p>
    {func_forecast(send_date_to_forecast)}
    </body>
    """
    return send


def func_forecast(head_day):
    result = """"""
    offset = 7200
    i = 1
    h = []
    t = []
    global current_day
    next_day = current_day
    head_table = f"""
    <br>
    <table style="width:100%">
      <tr>
        <th>{head_day}</th>
        <th>Teplota [&#8451;]</th>
        <th>Vlhkost [%]</th>
        <th>Tlak [kPa]</th>
        <th>Vítr, rychlost [m/s]</th>
        <th>Vítr, směr [&#x00B0;]</th>
        <th>Mraky [%]</th>
        <th>Počasí</th>
      </tr>
    """
    for hour in forecast["hourly"]:
        day = int(datetime.utcfromtimestamp(hour["dt"] + offset).strftime('%d'))
        if day == next_day:
            # print(day, datetime.utcfromtimestamp(hour["dt"]))
            line = ''
        elif day != next_day:
            next_day = day
            # print(day, datetime.utcfromtimestamp(hour["dt"]))
            line = f"""            
            </table>
            <br>
            <table style="width:100%">
            <tr>
                <th>{DayInWeek[datetime.utcfromtimestamp(hour["dt"] + offset).weekday()]} - 
                {datetime.utcfromtimestamp(hour["dt"] + offset).strftime('%d-%m-%Y')}
                </th>
                <th>Teplota [&#8451;]</th>
                <th>Vlhkost [%]</th>
                <th>Tlak [kPa]</th>
                <th>Vítr, rychlost [m/s]</th>
                <th>Vítr, směr [&#x00B0;]</th>
                <th>Mraky [%]</th>
                <th>Počasí</th>
            </tr>
            """

        try:
            density = float(hour["rain"]["1h"])
        except:
            density = ""

        r = f"""
        {line}
        <tr>
            <td style="text-align:center">{datetime.utcfromtimestamp(hour["dt"] + offset).strftime('%H:%M')}</td>
            <td>{hour["temp"]}</td>
            <td>{hour["humidity"]}</td>
            <td>{hour["pressure"]}</td>
            <td>{hour["wind_speed"]}</td>
            <td>{hour["wind_deg"]}</td>
            <td>{hour["clouds"]}</td>
            <td>{hour["weather"][0]["main"]} - {hour["weather"][0]["description"]} {density}</td>
        </tr>
        """

        h.append(datetime.utcfromtimestamp(hour["dt"] + offset).strftime('%d-%m-%H:%M'))
        t.append(hour["temp"])
        result = result + r
        i += 1
    return head_table + result + '</table>'

if __name__ == "__main__":
    main()