from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from tplink_smartplug import plug
import json, time

app = Flask(__name__)

@app.route('/device/<ip>')
def plugdata(ip=None):
    pluginfo = json.loads(plug( ip, 'info'))
    data = pluginfo['system']['get_sysinfo']
    return render_template('details.html', data=data)

@app.route('/og')
def devicelist():
    with open('devices.txt') as f:
        data = f.read().splitlines()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST', 'GET'])
def adddevice():
    if request.method == 'POST':
        devicequery = json.loads(plug( request.form['deviceip'], 'info'))
        data = devicequery['system']['get_sysinfo']
        devicename = data['alias']
        deviceip = request.form['deviceip']
        devicetype = data['dev_name']
        devicemodel = data['model']
        deviceid = int(time.time())
        with open('devices.json') as f:
            savedata = json.loads(f.read())
        
        savedata[deviceid] = {
            "ip": deviceip,
            "type": devicetype,
            "model": devicemodel,
            "name": devicename
        }
        with open('devices.json', 'w') as f:
            json.dump(savedata, f, sort_keys=True, indent=4)
        return redirect('/devices')
    else:    
        return redirect('/devices')


@app.route('/remove/<id>', methods=['GET'])
def removedevice(id):
    with open('devices.json') as f:
        currentdata = json.loads(f.read())
    del currentdata[id]
    with open('devices.json', 'w') as f:
        json.dump(currentdata, f, sort_keys=True, indent=4)
    return redirect('/devices')
    #return render_template('debug.html', data=currentdata)

@app.route('/ison/<ip>')
def ison(ip=None):
    pluginfo = json.loads(plug( ip, 'info'))
    relay_state = pluginfo['system']['get_sysinfo']['relay_state']
    if relay_state == 1:
        return json.dumps(True)
    elif relay_state == 0:
        return json.dumps(False)

@app.route('/devices')
def devices():
    with open('devices.json') as f:
        data = json.loads(f.read())
    return render_template('devices.html', data=data)

@app.route('/')
def index():
    #with open('devices.json') as f:
        #data = json.loads(f.read())
    return render_template('index.html')

@app.route('/togglepower/<ip>')
def poweron(ip=None):
    pluginfo = json.loads(plug( ip, 'info'))
    relay_state = pluginfo['system']['get_sysinfo']['relay_state']
    if relay_state == 1:
        plug(ip, "off")
        return redirect('/devices')
    elif relay_state == 0:
        plug(ip, "on")
        return redirect('/devices')