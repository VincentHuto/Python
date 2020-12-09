import csv

# Part 1
with open('electricalBilling.csv', newline='') as csvfile:
    # Total Charge Calculation Function
    def calculateCharge(hours):
        runningTotal = 0
        if 300 >= hours > 0:
            runningTotal += hours * 0.12
            return runningTotal
        elif 600 >= hours > 300:
            runningTotal += 300 * 0.12
            runningTotal += (hours - 300) * 0.10
            return runningTotal
        elif 1000 >= hours > 600:
            runningTotal += 300 * 0.12
            runningTotal += 300 * 0.10
            runningTotal += (hours - 600) * 0.09
            return runningTotal
        elif hours > 1000:
            runningTotal += 300 * 0.12
            runningTotal += 300 * 0.10
            runningTotal += 300 * 0.09
            runningTotal += (hours - 1000) * 0.08
            return runningTotal


    custIds = []
    kWhs = []
    charges = []
    electricalReader = csv.reader(csvfile, delimiter=',')
    print("Customer ID\t\tkWsUsed\t\tCharge")
    print("--------------------------------------")
    for row in electricalReader:
        custId = int(row[0])
        kWh = int(row[1])
        print(str(custId) + '\t\t\t\t' + str(kWh) + "\t\t\t" + str(calculateCharge(kWh)))
        custIds.append(int(custId))
        kWhs.append(int(kWh))
        charges.append(calculateCharge(kWh))
print("======================================")
print("Total Customers", len(custIds))
print("Total Power Usage", sum(kWhs))
print("Total Charges", sum(charges))




