## A dictionary consists of Key:Value pairs, any Key cannot be duplicated.
WeekdayConversion = { "Sat": "Saturday",
                      "Sun": "Sunday",
                      "Mon": "Monday",
                      "Tue": "Tuesday",
                      "Wed": "Wednesday",
                      "Thu": "Thursday",
                      "Fri": "Friday"}

print(WeekdayConversion["Sat"])     ## Saturday

print(WeekdayConversion.get("Sun")) ## Saturday

print(WeekdayConversion.get("Rov")) ## None

print(WeekdayConversion.get("Mov", "Not a valid key!" )) ## Not a valid key!
