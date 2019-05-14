mat <- matrix(c(-3,3, 5,-5), nrow = 2, ncol = 2, byrow = TRUE)
prec = 0.01

valx <- c()
val1 <- c()
val2 <- c()
val3 <- c()
val4 <- c()

for (i in (0:100))
{
    temp <- Matrix::expm(mat*i*prec)
    val1 <- c(val1, temp[1,1])
    val2 <- c(val2, temp[1,2])
    val3 <- c(val3, temp[2,1])
    val4 <- c(val4, temp[2,2])
    valx <- c(valx, i*prec)
}

jpeg("Rplot.jpg")
#Create the graph
plot(valx, val1, "l", main = "Exponential of a matrix", col = 'blue', xlab = "X values", ylab = "Y values", ylim = c(0,1))
lines(valx, val2, col = 'blue')
lines(valx, val3, col = 'red')
lines(valx, val4, col = 'red')

#Add the grid
abline(v = 0:173,  lty = 2, col = "grey")
abline(h = 0:5,  lty = 2, col = "grey")

#Resize the graph
options(repr.plot.width=15, repr.plot.height=8)

