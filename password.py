import datetime
import random
import string
import psutil
import win32gui
import win32process
import win32api
from skyfield.api import load, Topos
import hashlib
import time
import requests
import uuid
import os

def get_connection_type():
    connections = psutil.net_if_addrs()
    if 'eth0' in connections:  # check for wired connection
        return 'wired'
    elif 'wlan0' in connections:  # check for wireless connection
        return 'wireless'
    else:
        return 'unknown'

def get_active_process_count():
    return len(psutil.pids())

def get_total_traffic():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent + net_io.bytes_recv

def get_keyboard_layout():
    hwnd = win32gui.GetForegroundWindow()
    thread_id, _ = win32process.GetWindowThreadProcessId(hwnd)
    layout_id = win32api.GetKeyboardLayout(thread_id)
    layout_id_hex = hex(layout_id & (2**16 - 1))  # extract the lower word
    return layout_id_hex

def get_uranus_data():
    ts = load.timescale()
    t = ts.now()
    planets = load('de421.bsp')
    earth, uranus_barycenter = planets['earth'], planets['URANUS BARYCENTER']

    astrometric = earth.at(t).observe(uranus_barycenter)
    ra, dec, distance = astrometric.radec()

    return ra.hours, dec.degrees, distance.au

def get_random_api_data():
    try:
        response = requests.get('https://www.random.org/integers/?num=10&min=1&max=100&col=1&base=10&format=plain&rnd=new')
        if response.status_code == 200:
            return response.text.strip().replace("\n", "")
        else:
            return "defaultapi12345"
    except requests.RequestException:
        return "defaultapi12345"

def get_cpu_temperature():
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            core_temps = temps.get('coretemp', [])
            if core_temps:
                return core_temps[0].current
    except AttributeError:
        pass
    return 0

def get_mac_addresses():
    macs = []
    for iface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                macs.append(addr.address)
    return ''.join(macs)

def get_battery_info():
    try:
        battery = psutil.sensors_battery()
        if battery:
            return battery.percent
    except AttributeError:
        pass
    return 0

def get_disk_usage():
    usage = psutil.disk_usage('/')
    return usage.percent

def initialize_seed_data():
    date_time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    connection_type = get_connection_type()
    active_process_count = get_active_process_count()
    total_traffic = get_total_traffic()
    keyboard_layout = get_keyboard_layout()
    uranus_ra, uranus_dec, uranus_distance = get_uranus_data()
    cpu_temp = get_cpu_temperature()
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    api_data = get_random_api_data()
    mac_addresses = get_mac_addresses()
    battery_percent = get_battery_info()
    disk_usage = get_disk_usage()

    seed_data = (date_time_str + connection_type + str(active_process_count) +
                 str(total_traffic) + keyboard_layout +
                 f"{uranus_ra:.2f}{uranus_dec:.2f}{uranus_distance:.2f}" +
                 f"{cpu_temp}{uptime.total_seconds()}" + api_data +
                 mac_addresses + str(battery_percent) + str(disk_usage))

    for _ in range(1000):
        seed_data = hashlib.sha256(seed_data.encode()).hexdigest()
    
    return seed_data, {
        "date_time_str": date_time_str,
        "connection_type": connection_type,
        "active_process_count": active_process_count,
        "total_traffic": total_traffic,
        "keyboard_layout": keyboard_layout,
        "uranus_ra": uranus_ra,
        "uranus_dec": uranus_dec,
        "uranus_distance": uranus_distance,
        "cpu_temp": cpu_temp,
        "uptime_seconds": uptime.total_seconds(),
        "api_data": api_data,
        "mac_addresses": mac_addresses,
        "battery_percent": battery_percent,
        "disk_usage": disk_usage
    }

def generate_password(length=12, use_special_chars=True, use_uppercase=True):
    start_time = time.time()

    seed_data, seed_info = initialize_seed_data()
    random.seed(seed_data)

    # Introduce random delay
    time.sleep(random.uniform(0.001, 0.01))

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_special_chars:
        characters += string.punctuation
    characters += string.digits

    # Procedural generation of password
    password = ''.join(random.choice(characters) for _ in range(length))

    end_time = time.time()
    elapsed_time = end_time - start_time

    return password, elapsed_time, seed_info

# Example usage
length = int(input("Enter password length: "))
use_special_chars = input("Use special characters? (yes/no): ").lower() == 'yes'
use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == 'yes'

password, elapsed_time, seed_info = generate_password(length, use_special_chars, use_uppercase)
print("Generated password:", password)
print(f"Password generation took {elapsed_time:.6f} seconds\n\n\n")
print("PLEASE SAVE THIS DATA. IT MAY HELP YOU RESTORE THE PASSWORD (MAYBE ONE DAY LOL):")
print("Seed data used for generation:")
for key, value in seed_info.items():
    print(f"{key}: {value}")
print("v3.0")
