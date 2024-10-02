import win32evtlog

def get_event_logs(log_type='System', num_records=10):
    server = 'localhost'  # Name of the target computer to get logs
    log_handle = win32evtlog.OpenEventLog(server, log_type)
    
    try:
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        total_records = win32evtlog.GetNumberOfEventLogRecords(log_handle)
        print(f"Total records in {log_type} log: {total_records}")
        
        events = []
        while True:
            records = win32evtlog.ReadEventLog(log_handle, flags, 0)
            if not records:
                break
            for record in records:
                events.append(record)
                if len(events) >= num_records:
                    return events
    finally:
        win32evtlog.CloseEventLog(log_handle)
    return events

def print_event_logs(events,file_path):
    with open(file_path ,'w') as file:
        for event in events:
            file.write(f"Event ID: {event.EventID}\n")
            file.write(f"Time Generated: {event.TimeGenerated}\n")
            file.write(f"Source Name: {event.SourceName}\n")
            file.write(f"Event Type: {event.EventType}\n")
            file.write(f"Event Category: {event.EventCategory}\n")
            if event.StringInserts:
                file.write("Event Message: " + ", ".join(event.StringInserts) + "\n")
            else:
                file.write("Event Message: None\n")
            file.write("-" * 50 + "\n")


def main():
    num_records_to_fetch = 10
    event_logs = get_event_logs('System', num_records_to_fetch)
    file_path= "C:\\Users\\f3l1x\\OneDrive\\Desktop\\Automation\\event_log.txt"
    print_event_logs(event_logs,file_path)

if __name__ == "__main__":
    main()
