# Module 4 Project

## _Finding the Best Real Estate Cities for Tech Professionals_

### Abstract
This project utilized the ARIMA model from statsmodels. The data set used was sourced from Zillow and it included all housing prices from every zipcode between mid-1996 to mid-2018. Considering this, we chose to begin the modeling on timestamp `1997-01-01`. In addition, the model was trained on data between timestamps `1997 : 2013` and the predictive power of the model was used to predict the rest of the in sample data points. In terms of an iterative model fitting process, the function `arima_search()` was used to search for the best combination of (AR, differencing, MA) orders. This process was semi-autonomous, where if there was an error during fitting one of the parameters the user would have to manually diagnose which parameter was breaking the fit. This can be improved to be more streamlined. Parameters were chosen based on the lowest AIC and RMSE scores for the prediction of the remaining in sample data. In some cases the parameters for minimizing AIC aligned with RMSE, but in other cases there were some discrepancies. The ultimate decision was based on minimizing RMSE. Overall, we found that the *2008 Housing Crisis*, caused by the increased lending to otherwise ineligible borrowers, severely shrunk the market everywhere, but showed signs of rebound afterwards. Our predictions show that most of the emerging tech hubs have or are in the process of returning to pre-recession numbers with the exception of Baltimore, and more severely, Raleigh with a projected stagnant growth.

### Introduction
According to the US Bureau of Labor Statistics:  
          "*Employment of computer and information technology occupations is projected to grow 12 percent from 2018 to 2028, much faster than the average for all occupations. These occupations are projected to add about 546,200 new jobs. Demand for these workers will stem from greater emphasis on cloud computing, the collection and storage of big data, and information security.  
          The median annual wage for computer and information technology occupations was $88,240 in May 2019, which was higher than the median annual wage for all occupations of $39,810.*"(https://www.bls.gov/ooh/computer-and-information-technology/home.htm)
  
With this in mind we feel that it is important for those entering this lucrative field do not get blinded by high salaries and big bonuses, and want to create a deck for tech professionals to consult with so they can invest their well deserved cash into profitable and affordable real estate. 

To get a better understanding of what counts as a *tech city* we consulted with **CompTIA** and **Learn to Code With Me**. The *COMPTIA TECH TOWN INDEX 2019* article was helpful in coordinating a balanced list of regions to research. In addition, *THE 12 BEST CITIES TO START YOUR TECH CAREER IN THE U.S.* article on Learn to Code With Me (will be abbreviated as **LTCWM**) was used in order to fill some informational gaps. The LTCWM article provided a list of six emerging tech cities, and so we felt that this information was useful for our business case. 
 
We chose the top eight emerging tech hubs (metro areas):  
1. Atlanta, GA
2. Phoenix, AZ
3. Raleigh, NC
4. Huntsville, AL
5. Miami, FL
6. Austin, TX
7. Philadelphia, PA
8. Baltimore, MD

These cities were chosen based on the aforementioned article's rating them as emerging tech hubs. We believe that tech talent is necessary throughout the country, and we also believe America is a beautiful country; any place in America can be home if you make it. Tech companies have the immense power to literally change landscapes, build skyscrapers, and form communities. It goes without saying, the metro areas we chose have some considerable growth happening. In addition, property values are low but increasing, making it an excellent and reachable goal for any tech professional to purchase real estate within these metro areas.

### Procedure
First, we analyzed the Zillow data set. It came stock in what is called *Pandas Wide Format*. This format is not friendly to time series modeling and would warrant the use of `pd.melt()` to aid in transforming it to *Pandas Long Format*. 
