orderTeams=function (teams) factor(teams,levels=c("Red Bull Racing-Renault","McLaren-Mercedes","Ferrari","Mercedes","Lotus-Renault","Force India-Mercedes","Sauber-Ferrari","STR-Ferrari","Williams-Renault","Caterham-Renault","HRT-Cosworth","Marussia-Cosworth"),ordered=T)
tlid=data.frame(driverName=c("Sebastian Vettel","Mark Webber","Jenson Button", "Lewis Hamilton", "Fernando Alonso","Felipe Massa","Michael Schumacher","Nico Rosberg", "Kimi Räikkönen","Romain Grosjean","Jerome D'Ambrosio", "Paul di Resta", "Nico Hulkenberg","Kamui Kobayashi","Sergio Perez","Daniel Ricciardo","Jean-Eric Vergne","Pastor Maldonado","Bruno Senna","Heikki Kovalainen","Vitaly Petrov", "Pedro de la Rosa","Narain Karthikeyan","Timo Glock" ,"Charles Pic" ),TLID= c('VET','WEB','BUT','HAM','ALO','MAS','MSC','ROS','RAI','GRO','DAM','DIR','HUL','KOB','PER','RIC','VER','MAL','SEN','KOV','PET','DEL','KAR','GLO','PIC'))

floader=function(table){
  temporaryFile <- tempfile()
  fn=paste("https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=csv&name=f1comscraper&query=select+*+from+`",table,"`&apikey=",sep='')
  download.file(fn,destfile=temporaryFile, method="curl")
  read.csv(temporaryFile)
}

teamDriver=function(d) if (d>13) return(d %% 2) else return((1+d) %% 2)