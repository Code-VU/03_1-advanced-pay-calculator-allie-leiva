def calculatePay():
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    hrs = float(hrs)

    hourly_rate = input("Enter Rate: ")
    hourly_rate = float(hourly_rate)

    if hrs  > 40:
        #logic that adds overtime
        overtime_hours = hrs - 40
        normal_hours = 40

        overtime_pay = overtime_hours * hourly_rate * 1.5
        normal_pay = normal_hours * hourly_rate

        gross_pay = normal_pay + overtime_pay
            #the usual
    else:
        gross_pay = hourly_rate * hrs
    
    print(f"Pay: {gross_pay}")
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
