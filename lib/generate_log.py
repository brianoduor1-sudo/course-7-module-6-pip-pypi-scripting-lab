from datetime import datetime


def generate_log(log_data):
    """Generates a log file from the provided log_data list.

    Raises:
        ValueError: If log_data is not a list.
    """
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list of log entries")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    default_log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
    ]
    generate_log(default_log_data)