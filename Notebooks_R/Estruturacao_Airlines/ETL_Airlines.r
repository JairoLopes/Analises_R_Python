library(tidyverse)
library(nycflights13) 

voos <- flights[1:10000,]
aeronaves <- planes[1:10000,]
clima <- weather[1:10000,]

voos[1:2,]

aeronaves[1:2,]

clima[1:2,]

df <- select(voos, c(flight,tailnum,carrier,origin,dest,distance,time_hour))
df[1:3,]

df <- df %>% left_join(y= aeronaves[,c(1,7)] , by = "tailnum" )
df[1:3,]

clima <- clima %>% select(c(time_hour,visib,humid,temp))
clima[1:2,]

df <- df %>% inner_join(y = clima, by = "time_hour")
names(df) <- c("n.voo","id_Aeronave","linha_aerea","origem","destino","distancia","data_e_hora","assentos_aeronave","visibilidade","umidade","temperatura")
head(df)


