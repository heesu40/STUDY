# 과금 매상 알아보자

```R
##############################################
게임 매상 감소 원인 분석
##############################################
 
 
# CSV 파일을 읽어들이기
dau <- read.csv("./data/dau.csv", header = T, stringsAsFactors = F)
head(dau)
dpu <- read.csv("./data/dpu.csv", header = T, stringsAsFactors = F)
head(dpu)
install <- read.csv("./data/install.csv", header = T, stringsAsFactors= F)
head(install)


# DAU 데이터에 Install 데이터를 결합시키기 (merge함수)
# 기준변수 ("user_id", "app_name")
dau.install <- merge(dau, install, by = c("user_id", "app_name"))
head(dau.install)

# 1차결합된 데이터에 DPU 데이터를 결합시키기 (merge함수)
# 기준변수 (("log_date", "app_name", "user_id") 
dau.install.payment <- merge(dau.install, dpu, 
                       by = c("log_date","app_name", "user_id"), 
                       all.x = T)
head(dau.install.payment, 20)
head(na.omit(dau.install.payment))

# 비과금 유저의 과금액에 0을 넣기 ( data[row,col]<-0)
#데이터객체[is.na(데이터객체$컬럼명)] <- 0
dau.install.payment$payment[is.na(dau.install.payment$payment)] <- 0
head(dau.install.payment, 20)

# 월 항목 추가   (data.frame객체$새컬럼변수 <- 추가될 데이터, mutate, cbind 등 이용)
dau.install.payment$log_month <-substr(dau.install.payment$log_date, 1, 7)
dau.install.payment$install_month <- substr(dau.install.payment$install_date, 1, 7)
head(dau.install.payment, 20)


# 추가된 월 항목으로 그룹핑후 과금액 집계 (ddply, aggregate, dplyr::group_by등 이용)
mau.payment <- ddply(dau.install.payment,
                     .(log_month, user_id, install_month), # 그룹화
                     summarize, # 집계 명령
                     payment = sum(payment) # payment 합계
                     )

head(mau.payment, 10)


# 신규 유저인지 기존 유저인지 구분하는 항목의 새 컬럼변수 추가
mau.payment$user.type <-  ifelse(mau.payment$install_month == mau.payment$log_month, "new", "old")

# 그래프로 데이터 시각화 
```

