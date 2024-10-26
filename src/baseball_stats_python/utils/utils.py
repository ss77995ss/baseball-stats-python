from datetime import datetime


def validate_date_range(start_dt, end_dt):
    date_format = "%Y-%m-%d"
    
    try:
        start_date = datetime.strptime(start_dt, date_format)
        end_date = datetime.strptime(end_dt, date_format)

        if end_date < start_date:
            raise ValueError("end_dt cannot be earlier than start_dt.")
            
    except ValueError as e:
        raise ValueError(f"Invalid date format or range: {e}")