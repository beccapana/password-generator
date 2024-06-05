# Password Generator

This Python script generates a random password based on various system and astronomical data. It utilizes several functions to gather system information and then uses this data to generate a password.

## Functions

1. **get_connection_type()**: Determines the type of network connection (wired, wireless, or unknown).

2. **get_active_process_count()**: Retrieves the number of active processes on the system.

3. **get_total_traffic()**: Calculates the total network traffic (bytes sent and received).

4. **get_keyboard_layout()**: Determines the current keyboard layout.

5. **get_uranus_data()**: Retrieves astronomical data about the planet Uranus (right ascension, declination, and distance from Earth).

6. **generate_password()**: Combines system and astronomical data to generate a random password.

7. **get_random_api_data()**: Fetches random data from an external API (`random.org`).

8. **get_cpu_temperature()**: Returns the current CPU temperature.

9. **get_mac_addresses()**: Returns MAC addresses of all network interfaces.

10. **get_battery_info()**: Returns the battery charge percentage.

11. **get_disk_usage()**: Returns the disk usage percentage.

12. **initialize_seed_data()**: Collects a broader range of data for seed generation, including system and astronomical data, random API data, CPU temperature, system uptime, MAC addresses, battery info, and disk usage.

## Example Usage

1. Enter the desired password length when prompted.
2. Specify whether to use special characters (yes/no).
3. Specify whether to use uppercase letters (yes/no).
4. The script then generates a password based on the provided inputs and displays it.

## Dependencies

- `psutil`: A cross-platform library for retrieving information on running processes and system utilization.
- `win32gui`, `win32process`, `win32api`: Windows-specific modules for accessing GUI, process, and keyboard layout information.
- `skyfield`: A Python library for astronomical computations.
- `hashlib`: For hashing data.
- `time`: For measuring execution time and introducing delays.
- `requests`: For accessing external APIs.

## Notes

- Ensure that all necessary dependencies are installed before running the script.
- This script is designed to run on Windows operating systems due to its use of Windows-specific modules.
- The generated password is influenced by various system and astronomical factors, making it unique and potentially more secure.


## Password Generation Code Update: Description of Changes

#### 1. New Module Imports
In the updated version, the following modules have been added:
- `hashlib` for hashing data.
- `time` for measuring execution time and introducing delays.
- `requests` for accessing external APIs.
- `uuid` and `os`, although they are not used in the code.

#### 2. New Functions
The updated code includes new functions for gathering additional data:
- `get_random_api_data()`: Fetches random data from an external API (`random.org`).
- `get_cpu_temperature()`: Returns the current CPU temperature.
- `get_mac_addresses()`: Returns MAC addresses of all network interfaces.
- `get_battery_info()`: Returns the battery charge percentage.
- `get_disk_usage()`: Returns the disk usage percentage.

#### 3. Enhanced Seed Data Initialization
In the updated version, the `initialize_seed_data()` function has been added, which collects a broader range of data for seed generation, including:
- Current date and time with milliseconds.
- Connection type.
- Active process count.
- Total network traffic.
- Keyboard layout.
- Uranus positional data.
- CPU temperature.
- System uptime since boot.
- Random data from an external API.
- MAC addresses.
- Battery charge level.
- Disk usage.

After collecting all the data, it is hashed 1000 times using the SHA-256 algorithm to increase the complexity of the seed.

#### 4. Introduction of Random Delay
The updated code introduces a random delay between 0.001 and 0.01 seconds before generating the password to enhance entropy.

#### 5. Execution Time Measurement
The updated version measures and outputs the time taken to generate the password, providing this information to the user.

#### 6. Additional Information Output
After generating the password, the updated code not only outputs the password but also the time taken for generation and all the data used for seed formation. This allows the user to recover the password if needed.

#### 7. Enhanced Output Formatting
The updated version includes separating text and instructions for the user to save the seed data, helping with password recovery in the future.

### Summary
The updated code significantly expands the data used for seed generation, improves randomness through hashing and external APIs, adds execution time measurement, and provides the user with the ability to recover the password by saving the utilized data.
