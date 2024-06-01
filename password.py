import datetime
import random
import string
import psutil
import win32gui
import win32process
import win32api
from skyfield.api import load, Topos

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

def generate_password(length=12, use_special_chars=True, use_uppercase=True):
    date_time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    connection_type = get_connection_type()
    active_process_count = get_active_process_count()
    total_traffic = get_total_traffic()
    keyboard_layout = get_keyboard_layout()
    uranus_ra, uranus_dec, uranus_distance = get_uranus_data()

    # Character set
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_special_chars:
        characters += string.punctuation
    characters += string.digits

    # Initialize random seed
    seed_data = (date_time_str + connection_type + str(active_process_count) + 
                 str(total_traffic) + keyboard_layout + 
                 f"{uranus_ra:.2f}{uranus_dec:.2f}{uranus_distance:.2f}")
    random.seed(seed_data)

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example usage
length = int(input("Enter password length: "))
use_special_chars = input("Use special characters? (yes/no): ").lower() == 'yes'
use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == 'yes'

password = generate_password(length, use_special_chars, use_uppercase)
print("Generated password:", password)
