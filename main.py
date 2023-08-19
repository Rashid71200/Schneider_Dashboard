from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="$n200000G",
        database="power_meter"
    )

@app.route("/", methods=["GET"])
def home():
    connection = create_connection()
    cursor = connection.cursor()
#Power Factor Total
    list_value = [
        '`Current Avg`',
        '`Voltage L-N Avg`',
        '`Active Power Total`',
        '`Apparent Power C`'
    ]
    current='nan'
    voltage='nan'
    active='nan'
    frequency='nan'
    data = []

    try:
        for value in list_value:
            query = f"SELECT {value} FROM POWER_METER_4 ORDER BY timestamp DESC LIMIT 1"
            cursor.execute(query)
            data1 = cursor.fetchone()
            data.append(data1)
        # Retrieve the most recent row from table_1


    except mysql.connector.Error as err:
        print("Error: ", err)
        recent_data = None
    finally:
        cursor.close()
        connection.close()

    #current, voltage, active, frequency = data
    print(data)
    current, voltage, active, frequency = data

    return render_template("home.html", total_energy_usage=current, total_voltage=voltage, total_load=active, total_power_factor=frequency)

@app.route('/dashboards')
def dashboards_dash():
    return render_template("dashboards_dash.html" )

@app.route('/dashboards1')
def dashboards_dash1():
    return render_template("chart3.html" )

@app.route('/dashboards2')
def dashboards_dash3():
    return render_template("dashboards_dash3.html" )

@app.route('/dashboards3')
def dashboards_dash2():
    return render_template("dashboards_dash4.html" )

@app.route('/dashboards4')
def dashboards_dash4():
    return render_template("dashboards_dash5.html" )

@app.route('/dashboards5')
def dashboards_dash5():
    return render_template("dashboards_dash6.html" )

@app.route('/dashboards6')
def dashboards_dash6():
    return render_template("dashboards_dash7.html" )

@app.route('/dashboards7')
def dashboards_dash7():
    return render_template("dashboards_dash8.html" )

@app.route('/tables')
def tables_dash():
    return render_template("tables_dash.html" )

@app.route('/alarms')
def alarms_dash():
    return render_template("alarms_dash.html" )

@app.route('/cost')
def cost_dash():
    return render_template("cost_dash.html" )

@app.route('/reports_dash')
def reports_dash():
    return render_template("reports_dash.html" )

#   '''    < Top Page Button >   '''



#   '''   <Diagram Page >  '''

@app.route('/home', methods=['GET', 'POST'])
def redirect_home():
    connection = create_connection()
    cursor = connection.cursor()
    # Power Factor Total
    list_value = [
        '`Current Avg`',
        '`Voltage L-N Avg`',
        '`Active Power Total`',
        '`Apparent Power C`'
    ]
    current = 'nan'
    voltage = 'nan'
    active = 'nan'
    frequency = 'nan'
    data = []

    try:
        for value in list_value:
            query = f"SELECT {value} FROM POWER_METER_4 ORDER BY timestamp DESC LIMIT 1"
            cursor.execute(query)
            data1 = cursor.fetchone()
            data.append(data1)
        # Retrieve the most recent row from table_1


    except mysql.connector.Error as err:
        print("Error: ", err)
        recent_data = None
    finally:
        cursor.close()
        connection.close()

    # current, voltage, active, frequency = data
    print(data)
    current, voltage, active, frequency = data

    return render_template("home.html", total_energy_usage=current, total_voltage=voltage, total_load=active,
                           total_power_factor=frequency)

@app.route('/campus')
def redirect_to_campus():
    return render_template("campus.html" )


#''' <   building   > '''

@app.route('/building')
def redirect_to_building():
    return render_template("building.html" )

@app.route('/building-lines')
def redirect_one_line():
    return render_template("one_line.html" )

@app.route('/floor-plan.html')
def redirect_floor_plan():
    return render_template("floor-plan.html" )


#''' <Industry Page> '''

@app.route('/industry')
def redirect_to_industry():
    return render_template("industry.html" )

@app.route('/demand')
def redirect_industry_demand():
    kw_peaks = ['POWER_METER_4', 'POWER_METER_5', 'POWER_METER_6', 'POWER_METER_7', 'POWER_METER_8', 'POWER_METER_9']

    def get_power_meter_data(peak, value):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            query = f"SELECT {value} FROM {peak} ORDER BY timestamp DESC LIMIT 1"
            cursor.execute(query)
            data = cursor.fetchone()
        except mysql.connector.Error as err:
            print("Error: ", err)
            data = None
        finally:
            cursor.close()
            connection.close()
        return data

    dataX = []

    for peak in kw_peaks:
        data = []
        for value in ['`Present Demand`', '`Peak Demand`']:
            data.append(get_power_meter_data(peak, value))
        dataX.append(data)

    print(dataX)

    return render_template(
        "industry_demand.html",
        meter11=dataX[0][0], meter12=dataX[0][1],
        meter21=dataX[1][0], meter22=dataX[1][1],
        meter31=dataX[2][0], meter32=dataX[2][1],
        meter41=dataX[3][0], meter42=dataX[3][1],
        meter51=dataX[4][0], meter52=dataX[4][1],
        meter61=dataX[5][0], meter62=dataX[5][1]
    )

@app.route('/energy')
def redirect_industry_energy():
    kw_peaks = ['POWER_METER_4', 'POWER_METER_5', 'POWER_METER_6', 'POWER_METER_7', 'POWER_METER_8', 'POWER_METER_9']

    def get_power_meter_data(peak, value):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            query = f"SELECT {value} FROM {peak} ORDER BY timestamp DESC LIMIT 1"
            cursor.execute(query)
            data = cursor.fetchone()
        except mysql.connector.Error as err:
            print("Error: ", err)
            data = None
        finally:
            cursor.close()
            connection.close()
        return data

    dataX = []

    for peak in kw_peaks:
        data = []
        for value in ['`Active Energy Delivered (Into Load)`']:
            data.append(get_power_meter_data(peak, value))
        dataX.append(data)

    print(dataX)

    return render_template(
        "industry_energy.html",
        meter11=dataX[0][0],
        meter21=dataX[1][0],
        meter31=dataX[2][0],
        meter41=dataX[3][0],
        meter51=dataX[4][0],
        meter61=dataX[5][0],
    )



@app.route('/quality')
def redirect_industry_quality():
    kw_peaks = ['POWER_METER_4', 'POWER_METER_5', 'POWER_METER_6', 'POWER_METER_7', 'POWER_METER_8', 'POWER_METER_9']

    def get_power_meter_data(peak, value):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            query = f"SELECT {value} FROM {peak} ORDER BY timestamp DESC LIMIT 1"
            cursor.execute(query)
            data = cursor.fetchone()
        except mysql.connector.Error as err:
            print("Error: ", err)
            data = None
        finally:
            cursor.close()
            connection.close()
        return data

    dataX = []

    for peak in kw_peaks:
        data = []
        for value in ['`Reactive Power Total`', '`Power Factor Total IEC`']:
            data.append(get_power_meter_data(peak, value))
        dataX.append(data)

    print(dataX)

    return render_template(
        "industry_quality.html",
        meter11=dataX[0][0], meter12=dataX[0][1],
        meter21=dataX[1][0], meter22=dataX[1][1],
        meter31=dataX[2][0], meter32=dataX[2][1],
        meter41=dataX[3][0], meter42=dataX[3][1],
        meter51=dataX[4][0], meter52=dataX[4][1],
        meter61=dataX[5][0], meter62=dataX[5][1]
    )

''' <Advance Power Meter Setting Page> '''

@app.route('/volts-amps/<int:meter_number>')
def redirect_volts_amps(meter_number):
    # Map meter numbers to corresponding power meter names
    meter_names = {
        1: 'POWER_METER_5',
        2: 'POWER_METER_6',
        3: 'POWER_METER_7',
        4: 'POWER_METER_8',
        5: 'POWER_METER_9'
    }

    # Get the power meter name based on the meter_number
    meter_name = meter_names.get(meter_number)

    if meter_name is None:
        return "Invalid meter number"

    def get_power_meter_data(peak, value):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            query = f"SELECT {value} FROM {peak} ORDER BY timestamp DESC LIMIT 1"
            cursor.execute(query)
            data = cursor.fetchone()
        except mysql.connector.Error as err:
            print("Error: ", err)
            data = None
        finally:
            cursor.close()
            connection.close()
        return data


    data = []
    values = [
        '`Voltage C-A`',

        '`Voltage B-C`',
        '`Voltage A-B`',
        '`Voltage Unbalance L-N Worst`',
        '`Voltage L-N Avg`',
        '`Current A`',
        '`Current B`',
        '`Current C`',
        '`Current Avg`',
        '`Active Power A`',
        '`Active Power B`',
        '`Active Power C`',
        '`Active Power Total`',
        '`Reactive Power Total`',
        '`Apparent Power Total`',
        '`Voltage A-N`',
        '`Voltage B-N`',
        '`Voltage C-N`',
        '`Voltage L-N Avg`',
        '`Frequency`',
        '`Power Factor Total IEC`'
              ]
    for value in values:
        data.append(get_power_meter_data(meter_name, value))

    # Dynamically generate template variables using globals()
    template_vars = {}
    for i, value in enumerate(values):
        template_vars[value.lower().replace(' ', '_').replace('`', '').replace('-', '')] = data[i]
    print(template_vars)


    return render_template("volts-amps.html", **template_vars)


@app.route('/power-quality')
def redirect_power_quality():
    return render_template("power-quality.html" )

@app.route('/energy-dmd')
def redirect_energy_dmd():
    return render_template("energy-dmd.html" )

@app.route('/inputs-outputs')
def redirect_inputs_outputs():
    return render_template("inputs-outputs.html" )

@app.route('/setpoints')
def redirect_setpoints():
    return render_template("setpoints.html" )

@app.route('/setup-diagnostic')
def redirect_setup_diagnostic():
    return render_template("setup-diagnostic.html" )



''' </Industry Page> '''

#   '''   </Diagram Page >  '''



if __name__ == '__main__':
    app.run()
    connection = create_connection()
    db_name = "power_meter"
    cursor = connection.cursor()
    cursor.execute(f"USE power_meter")
