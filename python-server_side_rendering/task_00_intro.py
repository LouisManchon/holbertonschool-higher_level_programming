import os

def get_value(attendee, key):
    value = attendee.get(key, None)
    return value if value not in [None, ""] else "N/A"

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):
        output = template
        output = output.replace("{name}", get_value(attendee, "name"))
        output = output.replace("{event_title}", get_value(attendee, "event_title"))
        output = output.replace("{event_date}", get_value(attendee, "event_date"))
        output = output.replace("{event_location}", get_value(attendee, "event_location"))

        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(output)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
