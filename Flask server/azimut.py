from Credencials.Credentials import Access

print(Access['FORECAST']['API'])
def get_azimut(degree):
    if 0 <= degree <= 22.5:
        return "S"
    elif 22.5 < degree <= 67.5:
        return "SV"
    elif 67.5 < degree <= 112.5:
        return "V"
    elif 112.5 < degree <= 157.5:
        return "JV"
    elif 157.5 < degree <= 202.5:
        return "J"
    elif 202.5 < degree <= 247.5:
        return "JZ"
    elif 247.5 < degree <= 292.5:
        return "Z"
    elif 292.5 < degree <= 337.5:
        return "SZ"
    elif 337.5 < degree <= 360:
        return "S"


if __name__ == "__main__":
    for i in range(0, 360, 1):
        print(i ,"\t" ,get_azimut(i))