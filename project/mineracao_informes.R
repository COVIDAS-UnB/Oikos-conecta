
#Os arquivos devem estar na pesta pasta
arquivos.aux <- choose.files(default=getwd(), 
                             caption="Selecione os arquivos com os informes de congonhas:")

tabelao<-list()
for(k in 1: length(arquivos.aux)){
  arquivo <- pdf_text(arquivos.aux[k])%>%  #Ler o i-esimo arquivo do conjunto escolhido
    readr::read_lines()
  

  
  #Retorna as linhas de interesse
  linhas<-grep("CONFIRMADOS",arquivo)
  
  

  
  #Número de confirmados e de recuperados
  casos<- str_trim(arquivo[linhas])
  b<-str_locate(casos, "[0-9]")  #coleta onde começar o número
  cr<-str_sub(casos, start = b[1], end=b[1]+1) %>% as.numeric()
     
  
  
  #data do informe
  teste<-str_sub(arquivos.aux, start=-15)
  c<-str_locate(teste, "[0-9]")
  dias<-str_sub(teste, start=c[1], end=(c[1]+4)) 
  
  
  caso<-c("casos confirmados", "casos recuperados" )
  inf<-data.frame(caso,cr, dias= rep(dias[k],2) )
  
  tabelao[[k]]<-inf  #lista que vai coletando os pdfs
  
  
}
minerado <- do.call(rbind, tabelao) #junta as informações mineradas de todos os pdf baixados em uma tabela só

casos_confirmados<- minerado %>% filter(caso=="casos confirmados")
casos_recuperados<- minerado %>% filter(caso=="casos recuperados")


#Exportar

write.xlsx(d,file="dados.xlsx")















