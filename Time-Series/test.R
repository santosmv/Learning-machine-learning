## R
require(zoo) ## zoo provides time series functionality
require(data.table) ## data.table is a high performance data frame
unemp <- fread("data/monthly_unemployment.csv")
unemp[, DATE := as.Date(DATE)]
setkey(unemp, DATE)
## generate a data set where data is randomly missing
rand.unemp.idx <- sample(1:nrow(unemp), .1*nrow(unemp))
rand.unemp <- unemp[-rand.unemp.idx]
## generate a data set where data is more likely
## to be missing when unemployment is high
high.unemp.idx <- which(unemp$UNRATE 8)
num.to.select <- .2 * length(high.unemp.idx)
high.unemp.idx <- sample(high.unemp.idx,)
bias.unemp <- unemp[-high.unemp.idx]