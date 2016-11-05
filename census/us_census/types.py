

def CenusDatum(
    latitude, longditude, jobs_total,
    age_0_29, age_30_54, age_55_plus,
    monthly_wage_0_1250, monthly_wage_1251_3333, monthly_wage_3333_plus,
    goods_producing,
    trade_transportation_utilities,
    other_sectors,
    date
):

    return {
        "latitude": latitude,
        "longditude": longditude,
        "jobsTotal": jobs_total,
        "age0to29": age_0_29,
        "age30to54": age_30_54,
        "age55plus": age_55_plus,
        "monthlyWage0to1250": monthly_wage_0_1250,
        "monthlyWage1251to3333": monthly_wage_1251_3333,
        "monthlyWage3333plus": monthly_wage_3333_plus,
        "goodsProducing": goods_producing,
        "tradeTransportationUtilities": trade_transportation_utilities,
        "otherSectors": other_sectors,
        "date": date
    }
