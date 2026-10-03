# Project Findings

## Executive findings

Historical sales total **$2,261,536.78** across **4,922 orders** and **793 customers**.

### Annual trend

 Year       Sales
 2015 479856.2081
 2016 459436.0054
 2017 600192.5500
 2018 722052.0192

2016 declined relative to 2015, followed by stronger growth in 2017 and 2018.

### Category mix

       Category       Sales
     Technology 827455.8730
      Furniture 728658.5757
Office Supplies 705422.3340

### Regional mix

 Region       Sales
   West 710219.6845
   East 669518.7260
Central 492646.9132
  South 389151.4590

### Customer concentration

The top 229 customers account for approximately 60% of historical sales, or 28.9% of the 793-customer base. The top 393 customers account for approximately 80%, or 49.6% of the base.

This is a historical concentration finding, not evidence of causality.

### RFM

                  Customers  Historical_Sales
Segment                                      
Loyal/High Value        255         967698.28
Champions               122         640225.72
Needs Attention         262         398615.80
At Risk                  87         185077.66
New/Promising            67          69919.32

### Cohort retention

Average retention at month 2 among cohorts with an observable month-2 value is approximately 16.0%. Month-12 retention averages approximately 18.4% among cohorts with an observable month-12 value. Later cohorts have fewer observable months, so these should not be treated as directly comparable to mature cohorts without context.

### Shipping

Average shipping duration is 3.96 days; median is 4 days.

### Statistics

          Test                                         Question    Statistic  p_value  Interpretation
Mann–Whitney U Shipping duration: Standard Class vs First Class 8.792881e+06  0.00000     Significant
Kruskal–Wallis                 Shipping duration across regions 1.192625e+01  0.00764     Significant
Kruskal–Wallis             Order value across customer segments 1.472276e+00  0.47896 Not significant

A statistically significant result indicates a distributional difference under the stated test; it does not establish causality.

### Market basket

Top association by lift in the sub-category analysis is **Fasteners + Machines**, with lift **1.66** and 8 orders together. The association is a candidate for investigation, not proof that one product causes purchase of another.

### Forecasting

The fixed 12-month holdout comparison selected **ETS Additive Damped** with MAPE **18.10%**. The model was then refit to the full historical monthly series to produce the 2019 forecast.

### Anomalies

The IQR screen flags **2018-11-01** as an unusually high/low monthly sales observation.

## Business recommendations

1. Use RFM to differentiate retention and reactivation actions.
2. Monitor customer concentration and protect high-value relationships.
3. Investigate high-lift sub-category associations as cross-sell hypotheses.
4. Track shipping duration by service mode and region.
5. Use the forecast as a planning baseline, not a guarantee.
6. Investigate anomalous periods with operational context.

## Limitations

No profit, cost, quantity, discount, inventory, returns or CAC fields are available.
