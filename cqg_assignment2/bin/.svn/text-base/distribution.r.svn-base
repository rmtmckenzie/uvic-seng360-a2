# args[1]: input file
# args[2]: data column
# args[3]: output file
# args[4]: max mark
# args[5]: graph title
# args[6]: x lable
args <- commandArgs(trailingOnly = TRUE)


data<-read.csv(file=args[1],sep=",",head=FALSE)
postscript(file=args[3])
d <- data[,as.integer(args[2])]
d <- as.numeric(d)
hist(d,col="red",
 main = args[5],
 xlab = args[6],
 breaks = as.integer(args[4]))
axis(1,at=1:as.integer(args[4]))
