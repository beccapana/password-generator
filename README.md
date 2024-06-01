# Password Generator

This Python script generates a random password based on various system and astronomical data. It utilizes several functions to gather system information and then uses this data to generate a password.

## Functions

1. **get_connection_type()**: Determines the type of network connection (wired, wireless, or unknown).

2. **get_active_process_count()**: Retrieves the number of active processes on the system.

3. **get_total_traffic()**: Calculates the total network traffic (bytes sent and received).

4. **get_keyboard_layout()**: Determines the current keyboard layout.

5. **get_uranus_data()**: Retrieves astronomical data about the planet Uranus (right ascension, declination, and distance from Earth).

6. **generate_password()**: Combines system and astronomical data to generate a random password.

## Example Usage

1. Enter the desired password length when prompted.
2. Specify whether to use special characters (yes/no).
3. Specify whether to use uppercase letters (yes/no).
4. The script then generates a password based on the provided inputs and displays it.

## Dependencies

- `psutil`: A cross-platform library for retrieving information on running processes and system utilization.
- `win32gui`, `win32process`, `win32api`: Windows-specific modules for accessing GUI, process, and keyboard layout information.
- `skyfield`: A Python library for astronomical computations.

## Notes

- Ensure that all necessary dependencies are installed before running the script.
- This script is designed to run on Windows operating systems due to its use of Windows-specific modules.
- The generated password is influenced by various system and astronomical factors, making it unique and potentially more secure.
